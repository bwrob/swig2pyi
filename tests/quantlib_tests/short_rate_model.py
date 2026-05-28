from collections import namedtuple
from typing import List, cast
import QuantLib as ql

# Define the CalibrationData named tuple type
CalibrationData = namedtuple("CalibrationData", "start length volatility")

def create_swaption_helpers(
    data: List[CalibrationData],
    index: ql.IborIndex,
    term_structure: ql.YieldTermStructureHandle,
    engine: ql.PricingEngine,
) -> List[ql.BlackCalibrationHelper]:
    swaptions: List[ql.BlackCalibrationHelper] = []
    fixed_leg_tenor = ql.Period(1, ql.Years)
    fixed_leg_daycounter = ql.Actual360()
    floating_leg_daycounter = ql.Actual360()
    for d in data:
        vol_handle = ql.QuoteHandle(ql.SimpleQuote(d.volatility))
        # Note: SwaptionHelper inherits from CalibrationHelper
        helper = ql.SwaptionHelper(
            ql.Period(d.start, ql.Years),
            ql.Period(d.length, ql.Years),
            vol_handle,
            index,
            fixed_leg_tenor,
            fixed_leg_daycounter,
            floating_leg_daycounter,
            term_structure
        )
        helper.setPricingEngine(engine)
        swaptions.append(helper)
    return swaptions

def print_calibration_report(
    swaptions: List[ql.BlackCalibrationHelper],
    data: List[CalibrationData]
) -> None:
    print("-" * 80)
    print(f"{'Model Price':>15} {'Market Price':>15} {'Implied Vol':>15} {'Market Vol':>15} {'Rel Error':>15}")
    print("-" * 80)
    cumulative_error = 0.0
    for helper, d in zip(swaptions, data):
        model_price = helper.modelValue()
        market_price = helper.marketValue()
        # Calibrate implied volatility from the model price
        implied_vol = helper.impliedVolatility(model_price, 1e-4, 1000, 0.05, 0.50)
        rel_error = (model_price - market_price) / market_price
        cumulative_error += abs(rel_error)
        print(f"{model_price:15.5f} {market_price:15.5f} {implied_vol:15.5f} {d.volatility:15.5f} {rel_error:15.5%}")
    print("-" * 80)
    print(f"Average absolute relative error: {cumulative_error / len(data):.5%}")

def run_calibration() -> None:
    today = ql.Date(15, ql.February, 2002)
    settlement = ql.Date(19, ql.February, 2002)
    ql.Settings.instance().evaluationDate = today

    term_structure = ql.YieldTermStructureHandle(
        ql.FlatForward(settlement, 0.04875825, ql.Actual365Fixed())
    )
    index = ql.Euribor1Y(term_structure)

    data = [
        CalibrationData(1, 5, 0.1148),
        CalibrationData(2, 4, 0.1108),
        CalibrationData(3, 3, 0.1070),
        CalibrationData(4, 2, 0.1021),
        CalibrationData(5, 1, 0.1000)
    ]

    # --- 1. Hull-White Calibration ---
    print("Calibrating Hull-White model...")
    hw_model = ql.HullWhite(term_structure)
    hw_engine = ql.JamshidianSwaptionEngine(hw_model)
    hw_swaptions = create_swaption_helpers(data, index, term_structure, hw_engine)

    optimization_method = ql.LevenbergMarquardt(1.0e-8, 1.0e-8, 1.0e-8)
    end_criteria = ql.EndCriteria(10000, 100, 1e-6, 1e-8, 1e-8)

    # Run calibration
    hw_model.calibrate(hw_swaptions, optimization_method, end_criteria)
    hw_params = hw_model.params()
    a_hw, sigma_hw = hw_params[0], hw_params[1]
    print(f"Hull-White: a = {a_hw:.5f}, sigma = {sigma_hw:.5f}")
    print_calibration_report(hw_swaptions, data)

    # Check expectations
    assert abs(a_hw - 0.04642) < 2e-3
    assert abs(sigma_hw - 0.00580) < 2e-4

    # --- 2. Black-Karasinski Calibration ---
    print("\nCalibrating Black-Karasinski model...")
    bk_model = ql.BlackKarasinski(term_structure)
    bk_engine = ql.TreeSwaptionEngine(bk_model, 100)
    bk_swaptions = create_swaption_helpers(data, index, term_structure, bk_engine)

    bk_model.calibrate(bk_swaptions, optimization_method, end_criteria)
    bk_params = bk_model.params()
    a_bk, sigma_bk = bk_params[0], bk_params[1]
    print(f"Black-Karasinski: a = {a_bk:.5f}, sigma = {sigma_bk:.5f}")
    print_calibration_report(bk_swaptions, data)

    assert abs(a_bk - 0.0395) < 1e-3
    assert abs(sigma_bk - 0.11678) < 1e-3

    # --- 3. G2 Calibration ---
    print("\nCalibrating G2 model...")
    g2_model = ql.G2(term_structure)
    g2_engine = ql.TreeSwaptionEngine(g2_model, 25)
    g2_swaptions = create_swaption_helpers(data, index, term_structure, g2_engine)

    g2_model.calibrate(g2_swaptions, optimization_method, end_criteria)
    g2_params = g2_model.params()
    a_g2, sigma_g2 = g2_params[0], g2_params[1]
    b_g2, eta_g2 = g2_params[2], g2_params[3]
    rho_g2 = g2_params[4]
    print(f"G2: a = {a_g2:.5f}, sigma = {sigma_g2:.5f}, b = {b_g2:.5f}, eta = {eta_g2:.5f}, rho = {rho_g2:.5f}")
    print_calibration_report(g2_swaptions, data)

    assert abs(a_g2 - 0.04050) < 1e-2
    assert abs(sigma_g2 - 0.00474) < 1e-3

def test_calibration() -> None:
    run_calibration()
