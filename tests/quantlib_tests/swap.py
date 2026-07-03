import QuantLib as ql

def run_swap_pricing() -> None:
    calculation_date = ql.Date(20, 10, 2015)
    ql.Settings.instance().evaluationDate = calculation_date

    # construct discount curve and libor curve
    risk_free_rate = 0.01
    libor_rate = 0.02
    day_count = ql.Actual365Fixed()

    discount_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(calculation_date, risk_free_rate, day_count)
    )

    libor_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(calculation_date, libor_rate, day_count)
    )

    libor3M_index = ql.USDLibor(ql.Period(3, ql.Months), libor_curve)

    calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
    settle_date = calendar.advance(calculation_date, 5, ql.Days)
    maturity_date = calendar.advance(settle_date, 10, ql.Years)

    fixed_leg_tenor = ql.Period(6, ql.Months)
    fixed_schedule = ql.Schedule(
        settle_date,
        maturity_date,
        fixed_leg_tenor,
        calendar,
        ql.ModifiedFollowing,
        ql.ModifiedFollowing,
        ql.DateGeneration.Forward,
        False
    )

    float_leg_tenor = ql.Period(3, ql.Months)
    float_schedule = ql.Schedule(
        settle_date,
        maturity_date,
        float_leg_tenor,
        calendar,
        ql.ModifiedFollowing,
        ql.ModifiedFollowing,
        ql.DateGeneration.Forward,
        False
    )

    notional = 10000000.0
    fixed_rate = 0.025
    fixed_leg_daycount = ql.Actual360()
    float_spread = 0.004
    float_leg_daycount = ql.Actual360()

    ir_swap = ql.VanillaSwap(
        ql.VanillaSwap.Payer,
        notional,
        fixed_schedule,
        fixed_rate,
        fixed_leg_daycount,
        float_schedule,
        libor3M_index,
        float_spread,
        float_leg_daycount
    )

    swap_engine = ql.DiscountingSwapEngine(discount_curve)
    ir_swap.setPricingEngine(swap_engine)

    # Check legs iteration and properties
    leg0 = ir_swap.leg(0)
    for i, cf in enumerate(leg0):
        print(f"{i+1:2d}    {str(cf.date()):<18}  {cf.amount():10.2f}")

    leg1 = ir_swap.leg(1)
    for i, cf in enumerate(leg1):
        print(f"{i+1:2d}    {str(cf.date()):<18}  {cf.amount():10.2f}")

    npv = ir_swap.NPV()
    fair_spread = ir_swap.fairSpread()
    fair_rate = ir_swap.fairRate()
    fixed_bps = ir_swap.fixedLegBPS()
    floating_bps = ir_swap.floatingLegBPS()

    print(f"Net Present Value   : {npv:20.3f}")
    print(f"Fair Spread         : {fair_spread:20.3f}")
    print(f"Fair Rate           : {fair_rate:20.3f}")
    print(f"Fixed Leg BPS       : {fixed_bps:20.3f}")
    print(f"Floating Leg BPS    : {floating_bps:20.3f}")

    assert abs(npv - (-115054.034)) < 1.0

def test_swap_pricing() -> None:
    run_swap_pricing()
