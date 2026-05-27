from typing import List, cast
import QuantLib as ql

def print_curve(xlist: List[ql.Period], ylist: List[float], precision: int = 3) -> None:
    """
    Method to print curve in a nice format
    """
    print("----------------------")
    print("Maturities\tCurve")
    print("----------------------")
    for x, y in zip(xlist, ylist):
        print(f"{x}\t\t{round(y, precision)}")
    print("----------------------")

def run_term_structure() -> None:
    # Deposit rates
    depo_maturities: List[ql.Period] = [ql.Period(6, ql.Months), ql.Period(12, ql.Months)]
    depo_rates: List[float] = [5.25, 5.5]

    # Bond rates
    bond_maturities: List[ql.Period] = [ql.Period(6 * i, ql.Months) for i in range(3, 21)]
    bond_rates: List[float] = [5.75, 6.0, 6.25, 6.5, 6.75, 6.80, 7.00, 7.1, 7.15,
                              7.2, 7.3, 7.35, 7.4, 7.5, 7.6, 7.6, 7.7, 7.8]

    print_curve(depo_maturities + bond_maturities, depo_rates + bond_rates)

    # some constants and conventions
    calc_date = ql.Date(15, 1, 2015)
    ql.Settings.instance().evaluationDate = calc_date

    calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
    bussiness_convention = ql.Unadjusted
    day_count = ql.Thirty360(ql.Thirty360.BondBasis)
    end_of_month = True
    settlement_days = 0
    face_amount = 100.0
    coupon_frequency = ql.Period(ql.Semiannual)

    # create deposit rate helpers from depo_rates
    depo_helpers: List[ql.DepositRateHelper] = [
        ql.DepositRateHelper(
            ql.QuoteHandle(ql.SimpleQuote(r / 100.0)),
            m,
            settlement_days,
            calendar,
            bussiness_convention,
            end_of_month,
            day_count
        )
        for r, m in zip(depo_rates, depo_maturities)
    ]

    # create fixed rate bond helpers from fixed rate bonds
    bond_helpers: List[ql.FixedRateBondHelper] = []
    for r, m in zip(bond_rates, bond_maturities):
        termination_date = calc_date + m
        schedule = ql.Schedule(
            calc_date,
            termination_date,
            coupon_frequency,
            calendar,
            bussiness_convention,
            bussiness_convention,
            ql.DateGeneration.Backward,
            end_of_month
        )

        helper = ql.FixedRateBondHelper(
            ql.QuoteHandle(ql.SimpleQuote(face_amount)),
            settlement_days,
            face_amount,
            schedule,
            [r / 100.0],
            day_count,
            bussiness_convention,
        )
        bond_helpers.append(helper)

    # Combine helpers using casting or manual list of base type
    rate_helpers: List[ql.RateHelper] = cast(List[ql.RateHelper], depo_helpers) + cast(List[ql.RateHelper], bond_helpers)
    
    yieldcurve = ql.PiecewiseLogCubicDiscount(
        calc_date,
        rate_helpers,
        day_count
    )

    # get spot rates
    spots: List[float] = []
    tenors: List[float] = []
    for d in yieldcurve.dates():
        yrs = day_count.yearFraction(calc_date, d)
        compounding = ql.Compounded
        freq = ql.Semiannual
        # Handle 0 yrs division / limit case if yrs is 0
        if yrs == 0.0:
            zero_rate = yieldcurve.zeroRate(0.0001, compounding, freq)
        else:
            zero_rate = yieldcurve.zeroRate(yrs, compounding, freq)
        tenors.append(yrs)
        eq_rate = zero_rate.equivalentRate(
            day_count,
            compounding,
            freq,
            calc_date,
            d
        ).rate()
        spots.append(100 * eq_rate)

def test_term_structure() -> None:
    run_term_structure()
