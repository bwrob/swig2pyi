import typing
from typing import Any, Optional, overload, Generic, TypeVar
import collections.abc

_T = TypeVar('_T')

class Handle(Generic[_T]):
    def __init__(self, p: Optional[_T] = ...) -> None: ...
    def currentLink(self) -> _T: ...
    def empty(self) -> bool: ...
    def __deref__(self) -> _T: ...
class RelinkableHandle(Handle[_T]):
    def linkTo(self, h: _T, registerAsObserver: bool = True) -> None: ...
class TimeSeries(Generic[_T]):
    def __init__(self) -> None: ...

class Weekday(IntEnum):
    Sunday = 1
    Monday = 2
    Tuesday = 3
    Wednesday = 4
    Thursday = 5
    Friday = 6
    Saturday = 7

class Month(IntEnum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12

class TimeUnit(IntEnum):
    Days
    Weeks
    Months
    Years
    Hours
    Minutes
    Seconds
    Milliseconds
    Microseconds

class Frequency(IntEnum):
    NoFrequency = -1
    Once = 0
    Annual = 1
    Semiannual = 2
    EveryFourthMonth = 3
    Quarterly = 4
    Bimonthly = 6
    Monthly = 12
    EveryFourthWeek = 13
    Biweekly = 26
    Weekly = 52
    Daily = 365
    OtherFrequency = 999

class BusinessDayConvention(IntEnum):
    Following
    ModifiedFollowing
    Preceding
    ModifiedPreceding
    Unadjusted
    HalfMonthModifiedFollowing
    Nearest

class JointCalendarRule(IntEnum):
    JoinHolidays
    JoinBusinessDays

class Compounding(IntEnum):
    Simple
    Compounded
    Continuous
    SimpleThenCompounded
    CompoundedThenSimple

class VolatilityType(IntEnum):
    ShiftedLognormal
    Normal

def reset() -> None: ...
def daysBetween(
    arg0: Date,
    arg1: Date,
) -> float: ...
def nullInt() -> int: ...
def nullDouble() -> float: ...
def yearFractionToDate(
    dayCounter: DayCounter,
    referenceDate: Date,
    t: float,
) -> Date: ...
def inverse(
    m: Matrix,
) -> Matrix: ...
def transpose(
    m: Matrix,
) -> Matrix: ...
def outerProduct(
    v1: Array,
    v2: Array,
) -> Matrix: ...
def pseudoSqrt(
    m: Matrix,
    a: SalvagingAlgorithm.Type,
) -> Matrix: ...
@overload
def CholeskyDecomposition(
    m: Matrix,
) -> Matrix: ...
@overload
def CholeskyDecomposition(
    m: Matrix,
    flexible: bool,
) -> Matrix: ...
def CholeskySolveFor(
    L: Matrix,
    b: Array,
) -> Array: ...
@overload
def close(
    x: float,
    y: float,
) -> bool: ...
@overload
def close(
    x: float,
    y: float,
    n: int,
) -> bool: ...
@overload
def close_enough(
    x: float,
    y: float,
) -> bool: ...
@overload
def close_enough(
    x: float,
    y: float,
    n: int,
) -> bool: ...
def makeQuoteHandle(
    value: float,
) -> RelinkableHandle[Quote]: ...
def dates() -> list[Date]: ...
def firstDate() -> Date: ...
def lastDate() -> Date: ...
def size() -> int: ...
def as_iborindex(
    index: InterestRateIndex,
) -> IborIndex: ...
def as_swap_index(
    index: InterestRateIndex,
) -> SwapIndex: ...
@overload
def sabrVolatility(
    strike: float,
    forward: float,
    expiryTime: float,
    alpha: float,
    beta: float,
    nu: float,
    rho: float,
) -> float: ...
@overload
def sabrVolatility(
    strike: float,
    forward: float,
    expiryTime: float,
    alpha: float,
    beta: float,
    nu: float,
    rho: float,
    volatilityType: VolatilityType,
) -> float: ...
@overload
def shiftedSabrVolatility(
    strike: float,
    forward: float,
    expiryTime: float,
    alpha: float,
    beta: float,
    nu: float,
    rho: float,
    shift: float,
) -> float: ...
@overload
def shiftedSabrVolatility(
    strike: float,
    forward: float,
    expiryTime: float,
    alpha: float,
    beta: float,
    nu: float,
    rho: float,
    shift: float,
    volatilityType: VolatilityType,
) -> float: ...
def sabrFlochKennedyVolatility(
    strike: float,
    forward: float,
    expiryTime: float,
    alpha: float,
    beta: float,
    nu: float,
    rho: float,
) -> float: ...
def _sabrGuess(
    k_m: float,
    vol_m: float,
    k_0: float,
    vol_0: float,
    k_p: float,
    vol_p: float,
    forward: float,
    expiryTime: float,
    beta: float,
    shift: float,
    volatilityType: VolatilityType,
) -> list[float]: ...
def alpha() -> float: ...
def beta() -> float: ...
def nu() -> float: ...
def rho() -> float: ...
def rmsError() -> float: ...
def maxError() -> float: ...
def endCriteria() -> EndCriteria.Type: ...
def as_indexed_cashflow(
    cf: CashFlow,
) -> IndexedCashFlow: ...
def as_coupon(
    cf: CashFlow,
) -> Coupon: ...
def as_fixed_rate_coupon(
    cf: CashFlow,
) -> FixedRateCoupon: ...
@overload
def setCouponPricer(
    arg0: Leg,
    arg1: EquityCashFlowPricer,
) -> None: ...
@overload
def setCouponPricer(
    arg0: Leg,
    arg1: FloatingRateCouponPricer,
) -> None: ...
@overload
def setCouponPricer(
    arg0: Leg,
    arg1: YoYInflationCouponPricer,
) -> None: ...
def as_floating_rate_coupon(
    cf: CashFlow,
) -> FloatingRateCoupon: ...
def as_overnight_indexed_coupon(
    cf: CashFlow,
) -> OvernightIndexedCoupon: ...
def as_multiple_resets_coupon(
    cf: CashFlow,
) -> SubPeriodsCoupon: ...
def as_sub_periods_coupon(
    cf: CashFlow,
) -> SubPeriodsCoupon: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
    exCouponPeriod: Period,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
    paymentLag: int,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
    paymentLag: int,
    compounding: Compounding,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
    paymentLag: int,
    compounding: Compounding,
    compoundingFrequency: Frequency,
) -> Leg: ...
@overload
def _FixedRateLeg(
    schedule: Schedule,
    dayCount: DayCounter,
    nominals: list[float],
    couponRates: list[float],
    paymentAdjustment: BusinessDayConvention,
    firstPeriodDayCount: DayCounter,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
    paymentLag: int,
    compounding: Compounding,
    compoundingFrequency: Frequency,
    interestRates: list[InterestRate],
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
    paymentLag: int,
) -> Leg: ...
@overload
def _IborLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
    paymentLag: int,
    withIndexedCoupons: Optional[bool],
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    gearings: list[float],
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    gearings: list[float],
    spreads: list[float],
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    gearings: list[float],
    spreads: list[float],
    telescopicValueDates: bool,
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    gearings: list[float],
    spreads: list[float],
    telescopicValueDates: bool,
    averagingMethod: RateAveraging.Type,
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    gearings: list[float],
    spreads: list[float],
    telescopicValueDates: bool,
    averagingMethod: RateAveraging.Type,
    paymentCalendar: Calendar,
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    gearings: list[float],
    spreads: list[float],
    telescopicValueDates: bool,
    averagingMethod: RateAveraging.Type,
    paymentCalendar: Calendar,
    paymentLag: int,
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    gearings: list[float],
    spreads: list[float],
    telescopicValueDates: bool,
    averagingMethod: RateAveraging.Type,
    paymentCalendar: Calendar,
    paymentLag: int,
    lookbackDays: int,
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    gearings: list[float],
    spreads: list[float],
    telescopicValueDates: bool,
    averagingMethod: RateAveraging.Type,
    paymentCalendar: Calendar,
    paymentLag: int,
    lookbackDays: int,
    lockoutDays: int,
) -> Leg: ...
@overload
def _OvernightLeg(
    nominals: list[float],
    schedule: Schedule,
    index: OvernightIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    gearings: list[float],
    spreads: list[float],
    telescopicValueDates: bool,
    averagingMethod: RateAveraging.Type,
    paymentCalendar: Calendar,
    paymentLag: int,
    lookbackDays: int,
    lockoutDays: int,
    applyObservationShift: bool,
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _CmsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _CmsZeroLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
) -> Leg: ...
@overload
def _CmsSpreadLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapSpreadIndex,
) -> Leg: ...
@overload
def _CmsSpreadLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapSpreadIndex,
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _CmsSpreadLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapSpreadIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _CmsSpreadLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapSpreadIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
) -> Leg: ...
@overload
def _CmsSpreadLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapSpreadIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
) -> Leg: ...
@overload
def _CmsSpreadLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapSpreadIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
) -> Leg: ...
@overload
def _CmsSpreadLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapSpreadIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
) -> Leg: ...
@overload
def _CmsSpreadLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapSpreadIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
) -> Leg: ...
@overload
def _CmsSpreadLeg(
    nominals: list[float],
    schedule: Schedule,
    index: SwapSpreadIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
    isInArrears: bool,
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
) -> Leg: ...
@overload
def _MultipleResetsLeg(
    fullResetSchedule: Schedule,
    index: IborIndex,
    resetsPerCoupon: int,
    nominals: list[float],
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    averagingMethod: RateAveraging.Type,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
) -> Leg: ...
@overload
def _SubPeriodsLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    paymentCalendar: Calendar,
    paymentLag: int,
    fixingDays: list[int],
    gearings: list[float],
    couponSpreads: list[float],
    rateSpreads: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    averagingMethod: RateAveraging.Type,
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    lowerTriggers: list[float],
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    lowerTriggers: list[float],
    upperTriggers: list[float],
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    lowerTriggers: list[float],
    upperTriggers: list[float],
    observationTenor: Period,
) -> Leg: ...
@overload
def _RangeAccrualLeg(
    nominals: list[float],
    schedule: Schedule,
    index: IborIndex,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixingDays: list[int],
    gearings: list[float],
    spreads: list[float],
    lowerTriggers: list[float],
    upperTriggers: list[float],
    observationTenor: Period,
    observationConvention: BusinessDayConvention,
) -> Leg: ...
def DividendVector(
    dividendDates: list[Date],
    dividends: list[float],
) -> list[Dividend]: ...
def as_gsr_process(
    proc: StochasticProcess,
) -> GsrProcess: ...
def as_plain_vanilla_payoff(
    payoff: Payoff,
) -> PlainVanillaPayoff: ...
@overload
def blackFormula(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
) -> float: ...
@overload
def blackFormula(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
    discount: float,
) -> float: ...
@overload
def blackFormula(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
    discount: float,
    displacement: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDev(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDev(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDev(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDev(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDev(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
    accuracy: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDev(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
    accuracy: float,
    maxIterations: int,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
    omega: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
    omega: float,
    accuracy: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    optionType: Option.Type,
    strike: float,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
    omega: float,
    accuracy: float,
    maxIterations: int,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    payoff: PlainVanillaPayoff,
    forward: float,
    blackPrice: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    payoff: PlainVanillaPayoff,
    forward: float,
    blackPrice: float,
    discount: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    payoff: PlainVanillaPayoff,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    payoff: PlainVanillaPayoff,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    payoff: PlainVanillaPayoff,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
    omega: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    payoff: PlainVanillaPayoff,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
    omega: float,
    accuracy: float,
) -> float: ...
@overload
def blackFormulaImpliedStdDevLiRS(
    payoff: PlainVanillaPayoff,
    forward: float,
    blackPrice: float,
    discount: float,
    displacement: float,
    guess: float,
    omega: float,
    accuracy: float,
    maxIterations: int,
) -> float: ...
@overload
def blackFormulaCashItmProbability(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
) -> float: ...
@overload
def blackFormulaCashItmProbability(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
    displacement: float,
) -> float: ...
@overload
def blackFormulaCashItmProbability(
    payoff: PlainVanillaPayoff,
    forward: float,
    stdDev: float,
) -> float: ...
@overload
def blackFormulaCashItmProbability(
    payoff: PlainVanillaPayoff,
    forward: float,
    stdDev: float,
    displacement: float,
) -> float: ...
@overload
def blackFormulaAssetItmProbability(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
) -> float: ...
@overload
def blackFormulaAssetItmProbability(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
    displacement: float,
) -> float: ...
@overload
def blackFormulaAssetItmProbability(
    payoff: PlainVanillaPayoff,
    forward: float,
    stdDev: float,
) -> float: ...
@overload
def blackFormulaAssetItmProbability(
    payoff: PlainVanillaPayoff,
    forward: float,
    stdDev: float,
    displacement: float,
) -> float: ...
@overload
def bachelierBlackFormula(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
) -> float: ...
@overload
def bachelierBlackFormula(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
    discount: float,
) -> float: ...
@overload
def bachelierBlackFormulaImpliedVol(
    optionType: Option.Type,
    strike: float,
    forward: float,
    tte: float,
    bachelierPrice: float,
) -> float: ...
@overload
def bachelierBlackFormulaImpliedVol(
    optionType: Option.Type,
    strike: float,
    forward: float,
    tte: float,
    bachelierPrice: float,
    discount: float,
) -> float: ...
@overload
def bachelierBlackFormulaImpliedVolChoi(
    optionType: Option.Type,
    strike: float,
    forward: float,
    tte: float,
    bachelierPrice: float,
) -> float: ...
@overload
def bachelierBlackFormulaImpliedVolChoi(
    optionType: Option.Type,
    strike: float,
    forward: float,
    tte: float,
    bachelierPrice: float,
    discount: float,
) -> float: ...
@overload
def bachelierBlackFormulaAssetItmProbability(
    optionType: Option.Type,
    strike: float,
    forward: float,
    stdDev: float,
) -> float: ...
@overload
def bachelierBlackFormulaAssetItmProbability(
    payoff: PlainVanillaPayoff,
    forward: float,
    stdDev: float,
) -> float: ...
@overload
def simplifyNotificationGraph(
    bond: Bond,
) -> None: ...
@overload
def simplifyNotificationGraph(
    bond: Bond,
    unregisterCoupons: bool,
) -> None: ...
@overload
def simplifyNotificationGraph(
    swap: Swap,
) -> None: ...
@overload
def simplifyNotificationGraph(
    swap: Swap,
    unregisterCoupons: bool,
) -> None: ...
def as_overnight_swap_index(
    index: InterestRateIndex,
) -> OvernightIndexedSwap: ...
def as_multiplicative_price_seasonality(
    seasonality: Seasonality,
) -> MultiplicativePriceSeasonality: ...
def as_zero_inflation_index(
    i: Index,
) -> ZeroInflationIndex: ...
def as_inflation_coupon(
    cf: CashFlow,
) -> InflationCoupon: ...
def as_cpi_coupon(
    cf: CashFlow,
) -> CPICoupon: ...
def as_cpi_cashflow(
    cf: CashFlow,
) -> CPICashFlow: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
    caps: list[float],
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
    caps: list[float],
    floors: list[float],
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
    growthOnly: bool,
) -> Leg: ...
@overload
def _CPILeg(
    nominals: list[float],
    schedule: Schedule,
    index: ZeroInflationIndex,
    baseCPI: float,
    observationLag: Period,
    paymentDayCounter: DayCounter,
    paymentConvention: BusinessDayConvention,
    fixedRates: list[float],
    caps: list[float],
    floors: list[float],
    exCouponPeriod: Period,
    exCouponCalendar: Calendar,
    exCouponConvention: BusinessDayConvention,
    exCouponEndOfMonth: bool,
    paymentCalendar: Calendar,
    growthOnly: bool,
    observationInterpolation: CPI.InterpolationType,
) -> Leg: ...
def as_zero_inflation_cash_flow(
    cf: CashFlow,
) -> ZeroInflationCashFlow: ...
def quote() -> Handle[Quote]: ...
def latestDate() -> Date: ...
def earliestDate() -> Date: ...
def maturityDate() -> Date: ...
def latestRelevantDate() -> Date: ...
def pillarDate() -> Date: ...
def impliedQuote() -> float: ...
def quoteError() -> float: ...
def times() -> list[float]: ...
def data() -> list[float]: ...
@overload
def nodes() -> list[tuple[Date,DiscountFactor]]: ...
@overload
def nodes() -> list[tuple[Date,Rate]]: ...
@overload
def nodes() -> list[tuple[Date,Real]]: ...
def inflationPeriod(
    d: Date,
    f: Frequency,
) -> tuple[Date,Date]: ...
def inflationYearFraction(
    f: Frequency,
    indexIsInterpolated: bool,
    dayCount: DayCounter,
    d1: Date,
    d2: Date,
) -> float: ...
def inflationBaseDate(
    referenceDate: Date,
    observationLag: Period,
    frequency: Frequency,
    indexIsInterpolated: bool,
) -> Date: ...
def as_yoy_inflation_coupon(
    cf: CashFlow,
) -> YoYInflationCoupon: ...
def as_capped_floored_yoy_inflation_coupon(
    cf: CashFlow,
) -> CappedFlooredYoYInflationCoupon: ...
@overload
def _yoyInflationLeg(
    schedule: Schedule,
    calendar: Calendar,
    index: YoYInflationIndex,
    observationLag: Period,
    interpolation: CPI.InterpolationType,
    notionals: list[float],
    paymentDayCounter: DayCounter,
) -> Leg: ...
@overload
def _yoyInflationLeg(
    schedule: Schedule,
    calendar: Calendar,
    index: YoYInflationIndex,
    observationLag: Period,
    interpolation: CPI.InterpolationType,
    notionals: list[float],
    paymentDayCounter: DayCounter,
    paymentAdjustment: BusinessDayConvention,
) -> Leg: ...
@overload
def _yoyInflationLeg(
    schedule: Schedule,
    calendar: Calendar,
    index: YoYInflationIndex,
    observationLag: Period,
    interpolation: CPI.InterpolationType,
    notionals: list[float],
    paymentDayCounter: DayCounter,
    paymentAdjustment: BusinessDayConvention,
    fixingDays: int,
) -> Leg: ...
@overload
def _yoyInflationLeg(
    schedule: Schedule,
    calendar: Calendar,
    index: YoYInflationIndex,
    observationLag: Period,
    interpolation: CPI.InterpolationType,
    notionals: list[float],
    paymentDayCounter: DayCounter,
    paymentAdjustment: BusinessDayConvention,
    fixingDays: int,
    gearings: list[float],
) -> Leg: ...
@overload
def _yoyInflationLeg(
    schedule: Schedule,
    calendar: Calendar,
    index: YoYInflationIndex,
    observationLag: Period,
    interpolation: CPI.InterpolationType,
    notionals: list[float],
    paymentDayCounter: DayCounter,
    paymentAdjustment: BusinessDayConvention,
    fixingDays: int,
    gearings: list[float],
    spreads: list[float],
) -> Leg: ...
@overload
def _yoyInflationLeg(
    schedule: Schedule,
    calendar: Calendar,
    index: YoYInflationIndex,
    observationLag: Period,
    interpolation: CPI.InterpolationType,
    notionals: list[float],
    paymentDayCounter: DayCounter,
    paymentAdjustment: BusinessDayConvention,
    fixingDays: int,
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
) -> Leg: ...
@overload
def _yoyInflationLeg(
    schedule: Schedule,
    calendar: Calendar,
    index: YoYInflationIndex,
    observationLag: Period,
    interpolation: CPI.InterpolationType,
    notionals: list[float],
    paymentDayCounter: DayCounter,
    paymentAdjustment: BusinessDayConvention,
    fixingDays: int,
    gearings: list[float],
    spreads: list[float],
    caps: list[float],
    floors: list[float],
) -> Leg: ...
def rates() -> list[float]: ...
def Dslice(
    d: Date,
) -> tuple[std.vector[Rate)>,std.vector<(Volatility]]: ...
@overload
def cleanPriceFromZSpread(
    bond: Bond,
    discountCurve: YieldTermStructure,
    zSpread: float,
    dc: DayCounter,
    compounding: Compounding,
    freq: Frequency,
) -> float: ...
@overload
def cleanPriceFromZSpread(
    bond: Bond,
    discountCurve: YieldTermStructure,
    zSpread: float,
    dc: DayCounter,
    compounding: Compounding,
    freq: Frequency,
    settlementDate: Date,
) -> float: ...
def sinkingSchedule(
    startDate: Date,
    bondLength: Period,
    frequency: Frequency,
    paymentCalendar: Calendar,
) -> Schedule: ...
def sinkingNotionals(
    bondLength: Period,
    frequency: Frequency,
    couponRate: float,
    initialNotional: float,
) -> list[float]: ...
def as_black_helper(
    h: CalibrationHelper,
) -> BlackCalibrationHelper: ...
def as_swaption_helper(
    h: BlackCalibrationHelper,
) -> SwaptionHelper: ...
def as_depositratehelper(
    helper: RateHelper,
) -> DepositRateHelper: ...
def as_fraratehelper(
    helper: RateHelper,
) -> FraRateHelper: ...
def as_swapratehelper(
    helper: RateHelper,
) -> SwapRateHelper: ...
def as_oisratehelper(
    helper: RateHelper,
) -> OISRateHelper: ...
def as_constnotionalcrosscurrencybasisswapratehelper(
    helper: RateHelper,
) -> ConstNotionalCrossCurrencyBasisSwapRateHelper: ...
def as_mtmcrosscurrencybasisswapratehelper(
    helper: RateHelper,
) -> MtMCrossCurrencyBasisSwapRateHelper: ...
def hazardRates() -> list[float]: ...
def defaultDensities() -> list[float]: ...
def survivalProbabilities() -> list[Probability]: ...
def cdsMaturity(
    tradeDate: Date,
    tenor: Period,
    rule: DateGeneration.Rule,
) -> Date: ...
def discounts() -> list[float]: ...
def applyTo(
    a: array_type,
    t: float,
) -> None: ...
def interpolateAt(
    x: list[float],
) -> float: ...
def thetaAt(
    x: list[float],
) -> float: ...
def forwards() -> list[float]: ...
def numberOfEvaluations() -> int: ...
@overload
def next() -> Sample[float]: ...
@overload
def next() -> sample_type: ...
def nextSequence() -> Sample[list[float]]: ...
def dimension() -> int: ...
def _checkCompatibility(
    evolution: EvolutionDescription,
    numeraires: list[int],
) -> None: ...
def _isInTerminalMeasure(
    evolution: EvolutionDescription,
    numeraires: list[int],
) -> bool: ...
@overload
def _isInMoneyMarketPlusMeasure(
    evolution: EvolutionDescription,
    numeraires: list[int],
) -> bool: ...
@overload
def _isInMoneyMarketPlusMeasure(
    evolution: EvolutionDescription,
    numeraires: list[int],
    offset: int,
) -> bool: ...
def _isInMoneyMarketMeasure(
    evolution: EvolutionDescription,
    numeraires: list[int],
) -> bool: ...
def _terminalMeasure(
    evolution: EvolutionDescription,
) -> list[int]: ...
@overload
def _moneyMarketPlusMeasure(
    evolution: EvolutionDescription,
) -> list[int]: ...
@overload
def _moneyMarketPlusMeasure(
    evolution: EvolutionDescription,
    offset: int,
) -> list[int]: ...
def _moneyMarketMeasure(
    evolution: EvolutionDescription,
) -> list[int]: ...
def getCovariance(
    volatilities: Array,
    correlations: Matrix,
) -> Matrix: ...
def antithetic() -> sample_type: ...
def timeGrid() -> TimeGrid: ...
def baseCurve() -> Handle[YieldTermStructure]: ...
def samples() -> int: ...
def weightSum() -> float: ...
def mean() -> list[float]: ...
def variance() -> list[float]: ...
def standardDeviation() -> list[float]: ...
def errorEstimate() -> list[float]: ...
def skewness() -> list[float]: ...
def kurtosis() -> list[float]: ...
def min() -> list[float]: ...
def max() -> list[float]: ...
def covariance() -> Matrix: ...
def correlation() -> Matrix: ...
@overload
def add(
    value: Array,
) -> None: ...
@overload
def add(
    value: Array,
    weight: float,
) -> None: ...
@overload
def add(
    value: list[float],
) -> None: ...
@overload
def add(
    value: list[float],
    weight: float,
) -> None: ...
def enableTracing() -> None: ...
def disableTracing() -> None: ...
def zeroRates() -> list[float]: ...
class Period:
    @overload
    def __init__(
        self,
        arg0: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        units: TimeUnit,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def length(self) -> int: ...
    def units(self) -> TimeUnit: ...
    def frequency(self) -> Frequency: ...
    def normalized(self) -> Period: ...

class Date:
    @overload
    def __init__(
        self,
        d: int,
        m: Month,
        y: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        serialNumber: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def weekday(self) -> Weekday: ...
    def dayOfMonth(self) -> int: ...
    def dayOfYear(self) -> int: ...
    def month(self) -> Month: ...
    def year(self) -> int: ...
    def serialNumber(self) -> int: ...
    def isLeap(
        self,
        y: int,
    ) -> bool: ...
    def minDate(self) -> Date: ...
    def maxDate(self) -> Date: ...
    def todaysDate(self) -> Date: ...
    def startOfMonth(
        self,
        arg0: Date,
    ) -> Date: ...
    def endOfMonth(
        self,
        arg0: Date,
    ) -> Date: ...
    def isStartOfMonth(
        self,
        arg0: Date,
    ) -> bool: ...
    def isEndOfMonth(
        self,
        arg0: Date,
    ) -> bool: ...
    def nextWeekday(
        self,
        arg0: Date,
        arg1: Weekday,
    ) -> Date: ...
    def nthWeekday(
        self,
        n: int,
        arg1: Weekday,
        m: Month,
        y: int,
    ) -> Date: ...
    @overload
    def __add__(
        self,
        arg0: Period,
    ) -> Date: ...
    @overload
    def __add__(
        self,
        days: int,
    ) -> Date: ...
    @overload
    def __sub__(
        self,
        arg0: Period,
    ) -> Date: ...
    @overload
    def __sub__(
        self,
        days: int,
    ) -> Date: ...

class DateParser:
    def __init__(self) -> None: ...
    def parseFormatted(
        self,
        str_: str,
        fmt: str,
    ) -> Date: ...
    def parseISO(
        self,
        str_: str,
    ) -> Date: ...

class PeriodParser:
    def __init__(self) -> None: ...
    def parse(
        self,
        str_: str,
    ) -> Period: ...

class IMM:
    class Month(IntEnum):
        F = 1
        G = 2
        H = 3
        J = 4
        K = 5
        M = 6
        N = 7
        Q = 8
        U = 9
        V = 10
        X = 11
        Z = 12

    def __init__(self) -> None: ...
    @overload
    def isIMMdate(
        self,
        d: Date,
    ) -> bool: ...
    @overload
    def isIMMdate(
        self,
        d: Date,
        mainCycle: bool,
    ) -> bool: ...
    @overload
    def isIMMcode(
        self,
        code: str,
    ) -> bool: ...
    @overload
    def isIMMcode(
        self,
        code: str,
        mainCycle: bool,
    ) -> bool: ...
    def code(
        self,
        immDate: Date,
    ) -> str: ...
    @overload
    def date(
        self,
        immCode: str,
    ) -> Date: ...
    @overload
    def date(
        self,
        immCode: str,
        referenceDate: Date,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        d: Date,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        d: Date,
        mainCycle: bool,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        immCode: str,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        immCode: str,
        mainCycle: bool,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        immCode: str,
        mainCycle: bool,
        referenceDate: Date,
    ) -> Date: ...
    @overload
    def nextDate(self) -> Date: ...
    @overload
    def nextCode(
        self,
        d: Date,
    ) -> str: ...
    @overload
    def nextCode(
        self,
        d: Date,
        mainCycle: bool,
    ) -> str: ...
    @overload
    def nextCode(
        self,
        immCode: str,
    ) -> str: ...
    @overload
    def nextCode(
        self,
        immCode: str,
        mainCycle: bool,
    ) -> str: ...
    @overload
    def nextCode(
        self,
        immCode: str,
        mainCycle: bool,
        referenceDate: Date,
    ) -> str: ...
    @overload
    def nextCode(self) -> str: ...

class ASX:
    class Month(IntEnum):
        F = 1
        G = 2
        H = 3
        J = 4
        K = 5
        M = 6
        N = 7
        Q = 8
        U = 9
        V = 10
        X = 11
        Z = 12

    def __init__(self) -> None: ...
    @overload
    def isASXdate(
        self,
        d: Date,
    ) -> bool: ...
    @overload
    def isASXdate(
        self,
        d: Date,
        mainCycle: bool,
    ) -> bool: ...
    @overload
    def isASXcode(
        self,
        code: str,
    ) -> bool: ...
    @overload
    def isASXcode(
        self,
        code: str,
        mainCycle: bool,
    ) -> bool: ...
    def code(
        self,
        asxDate: Date,
    ) -> str: ...
    @overload
    def date(
        self,
        asxCode: str,
    ) -> Date: ...
    @overload
    def date(
        self,
        asxCode: str,
        referenceDate: Date,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        asxCode: str,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        asxCode: str,
        mainCycle: bool,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        asxCode: str,
        mainCycle: bool,
        referenceDate: Date,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        d: Date,
    ) -> Date: ...
    @overload
    def nextDate(
        self,
        d: Date,
        mainCycle: bool,
    ) -> Date: ...
    @overload
    def nextDate(self) -> Date: ...
    @overload
    def nextCode(
        self,
        asxCode: str,
    ) -> str: ...
    @overload
    def nextCode(
        self,
        asxCode: str,
        mainCycle: bool,
    ) -> str: ...
    @overload
    def nextCode(
        self,
        asxCode: str,
        mainCycle: bool,
        referenceDate: Date,
    ) -> str: ...
    @overload
    def nextCode(
        self,
        d: Date,
    ) -> str: ...
    @overload
    def nextCode(
        self,
        d: Date,
        mainCycle: bool,
    ) -> str: ...
    @overload
    def nextCode(self) -> str: ...

class Calendar:
    def __init__(self) -> None: ...
    def isWeekend(
        self,
        w: Weekday,
    ) -> bool: ...
    def startOfMonth(
        self,
        arg0: Date,
    ) -> Date: ...
    def endOfMonth(
        self,
        arg0: Date,
    ) -> Date: ...
    def isBusinessDay(
        self,
        arg0: Date,
    ) -> bool: ...
    def isHoliday(
        self,
        arg0: Date,
    ) -> bool: ...
    def isEndOfMonth(
        self,
        arg0: Date,
    ) -> bool: ...
    def isStartOfMonth(
        self,
        arg0: Date,
    ) -> bool: ...
    def addHoliday(
        self,
        arg0: Date,
    ) -> None: ...
    def removeHoliday(
        self,
        arg0: Date,
    ) -> None: ...
    def resetAddedAndRemovedHolidays(self) -> None: ...
    @overload
    def adjust(
        self,
        d: Date,
    ) -> Date: ...
    @overload
    def adjust(
        self,
        d: Date,
        convention: BusinessDayConvention,
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        n: int,
        unit: TimeUnit,
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        n: int,
        unit: TimeUnit,
        convention: BusinessDayConvention,
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        n: int,
        unit: TimeUnit,
        convention: BusinessDayConvention,
        endOfMonth: bool,
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        period: Period,
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        period: Period,
        convention: BusinessDayConvention,
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        period: Period,
        convention: BusinessDayConvention,
        endOfMonth: bool,
    ) -> Date: ...
    @overload
    def businessDaysBetween(
        self,
        from_: Date,
        to: Date,
    ) -> int: ...
    @overload
    def businessDaysBetween(
        self,
        from_: Date,
        to: Date,
        includeFirst: bool,
    ) -> int: ...
    @overload
    def businessDaysBetween(
        self,
        from_: Date,
        to: Date,
        includeFirst: bool,
        includeLast: bool,
    ) -> int: ...
    @overload
    def holidayList(
        self,
        from_: Date,
        to: Date,
    ) -> list[Date]: ...
    @overload
    def holidayList(
        self,
        from_: Date,
        to: Date,
        includeWeekEnds: bool,
    ) -> list[Date]: ...
    def businessDayList(
        self,
        from_: Date,
        to: Date,
    ) -> list[Date]: ...
    def name(self) -> str: ...
    def empty(self) -> bool: ...

class Argentina(Calendar):
    class Market(IntEnum):
        Merval

    @overload
    def __init__(
        self,
        m: Argentina.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Australia(Calendar):
    class Market(IntEnum):
        Settlement
        ASX

    @overload
    def __init__(
        self,
        market: Australia.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Austria(Calendar):
    class Market(IntEnum):
        Settlement
        Exchange

    @overload
    def __init__(
        self,
        m: Austria.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Botswana(Calendar):
    def __init__(self) -> None: ...

class Brazil(Calendar):
    class Market(IntEnum):
        Settlement
        Exchange

    @overload
    def __init__(
        self,
        m: Brazil.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Canada(Calendar):
    class Market(IntEnum):
        Settlement
        TSX

    @overload
    def __init__(
        self,
        m: Canada.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Chile(Calendar):
    class Market(IntEnum):
        SSE

    @overload
    def __init__(
        self,
        m: Chile.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class China(Calendar):
    class Market(IntEnum):
        SSE
        IB

    @overload
    def __init__(
        self,
        m: China.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class CzechRepublic(Calendar):
    class Market(IntEnum):
        PSE

    @overload
    def __init__(
        self,
        m: CzechRepublic.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Denmark(Calendar):
    def __init__(self) -> None: ...

class Finland(Calendar):
    def __init__(self) -> None: ...

class France(Calendar):
    class Market(IntEnum):
        Settlement
        Exchange

    @overload
    def __init__(
        self,
        m: France.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Germany(Calendar):
    class Market(IntEnum):
        Settlement
        FrankfurtStockExchange
        Xetra
        Eurex

    @overload
    def __init__(
        self,
        m: Germany.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class HongKong(Calendar):
    class Market(IntEnum):
        HKEx

    @overload
    def __init__(
        self,
        m: HongKong.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Hungary(Calendar):
    def __init__(self) -> None: ...

class Iceland(Calendar):
    class Market(IntEnum):
        ICEX

    @overload
    def __init__(
        self,
        m: Iceland.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class India(Calendar):
    class Market(IntEnum):
        NSE

    @overload
    def __init__(
        self,
        m: India.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Indonesia(Calendar):
    class Market(IntEnum):
        BEJ
        JSX

    @overload
    def __init__(
        self,
        m: Indonesia.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Israel(Calendar):
    class Market(IntEnum):
        Settlement
        TASE
        SHIR

    @overload
    def __init__(
        self,
        m: Israel.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Italy(Calendar):
    class Market(IntEnum):
        Settlement
        Exchange

    @overload
    def __init__(
        self,
        m: Italy.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Japan(Calendar):
    def __init__(self) -> None: ...

class Mexico(Calendar):
    class Market(IntEnum):
        BMV

    @overload
    def __init__(
        self,
        m: Mexico.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class NewZealand(Calendar):
    class Market(IntEnum):
        Wellington
        Auckland

    @overload
    def __init__(
        self,
        m: NewZealand.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Norway(Calendar):
    def __init__(self) -> None: ...

class Poland(Calendar):
    class Market(IntEnum):
        Settlement
        WSE

    @overload
    def __init__(
        self,
        m: Poland.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Romania(Calendar):
    class Market(IntEnum):
        Public
        BVB

    @overload
    def __init__(
        self,
        m: Romania.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Russia(Calendar):
    class Market(IntEnum):
        Settlement
        MOEX

    @overload
    def __init__(
        self,
        m: Russia.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SaudiArabia(Calendar):
    class Market(IntEnum):
        Tadawul

    @overload
    def __init__(
        self,
        m: SaudiArabia.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Singapore(Calendar):
    class Market(IntEnum):
        SGX

    @overload
    def __init__(
        self,
        m: Singapore.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Slovakia(Calendar):
    class Market(IntEnum):
        BSSE

    @overload
    def __init__(
        self,
        m: Slovakia.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SouthAfrica(Calendar):
    def __init__(self) -> None: ...

class SouthKorea(Calendar):
    class Market(IntEnum):
        Settlement
        KRX

    @overload
    def __init__(
        self,
        m: SouthKorea.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Sweden(Calendar):
    def __init__(self) -> None: ...

class Switzerland(Calendar):
    def __init__(self) -> None: ...

class Taiwan(Calendar):
    class Market(IntEnum):
        TSEC

    @overload
    def __init__(
        self,
        m: Taiwan.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class TARGET(Calendar):
    def __init__(self) -> None: ...

class Thailand(Calendar):
    def __init__(self) -> None: ...

class Turkey(Calendar):
    def __init__(self) -> None: ...

class Ukraine(Calendar):
    class Market(IntEnum):
        USE

    @overload
    def __init__(
        self,
        m: Ukraine.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class UnitedKingdom(Calendar):
    class Market(IntEnum):
        Settlement
        Exchange
        Metals

    @overload
    def __init__(
        self,
        m: UnitedKingdom.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class UnitedStates(Calendar):
    class Market(IntEnum):
        Settlement
        NYSE
        GovernmentBond
        NERC
        LiborImpact
        FederalReserve
        SOFR

    def __init__(
        self,
        m: UnitedStates.Market,
    ) -> None: ...

class NullCalendar(Calendar):
    def __init__(self) -> None: ...

class WeekendsOnly(Calendar):
    def __init__(self) -> None: ...

class JointCalendar(Calendar):
    @overload
    def __init__(
        self,
        arg0: Calendar,
        arg1: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Calendar,
        arg1: Calendar,
        arg2: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Calendar,
        arg1: Calendar,
        arg2: Calendar,
        arg3: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Calendar,
        arg1: Calendar,
        arg2: Calendar,
        arg3: Calendar,
        rule: JointCalendarRule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Calendar,
        arg1: Calendar,
        arg2: Calendar,
        rule: JointCalendarRule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Calendar,
        arg1: Calendar,
        rule: JointCalendarRule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: list[Calendar],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: list[Calendar],
        arg1: JointCalendarRule,
    ) -> None: ...

class BespokeCalendar(Calendar):
    def __init__(
        self,
        name: str,
    ) -> None: ...
    def addWeekend(
        self,
        arg0: Weekday,
    ) -> None: ...

class DayCounter:
    def __init__(self) -> None: ...
    def dayCount(
        self,
        d1: Date,
        d2: Date,
    ) -> int: ...
    @overload
    def yearFraction(
        self,
        d1: Date,
        d2: Date,
    ) -> float: ...
    @overload
    def yearFraction(
        self,
        d1: Date,
        d2: Date,
        startRef: Date,
    ) -> float: ...
    @overload
    def yearFraction(
        self,
        d1: Date,
        d2: Date,
        startRef: Date,
        endRef: Date,
    ) -> float: ...
    def name(self) -> str: ...
    def empty(self) -> bool: ...

class Actual360(DayCounter):
    @overload
    def __init__(
        self,
        includeLastDay: bool,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Actual366(DayCounter):
    @overload
    def __init__(
        self,
        includeLastDay: bool,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Actual36525(DayCounter):
    @overload
    def __init__(
        self,
        includeLastDay: bool,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Actual364(DayCounter):
    def __init__(self) -> None: ...

class Actual365Fixed(DayCounter):
    class Convention(IntEnum):
        Standard
        Canadian
        NoLeap

    @overload
    def __init__(
        self,
        c: Actual365Fixed.Convention,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Thirty360(DayCounter):
    class Convention(IntEnum):
        USA
        BondBasis
        European
        EurobondBasis
        Italian
        German
        ISMA
        ISDA
        NASD

    @overload
    def __init__(
        self,
        c: Thirty360.Convention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        c: Thirty360.Convention,
        terminationDate: Date,
    ) -> None: ...

class Thirty365(DayCounter):
    def __init__(self) -> None: ...

class ActualActual(DayCounter):
    class Convention(IntEnum):
        ISMA
        Bond
        ISDA
        Historical
        Actual365
        AFB
        Euro

    @overload
    def __init__(
        self,
        c: ActualActual.Convention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        c: ActualActual.Convention,
        schedule: Schedule,
    ) -> None: ...

class OneDayCounter(DayCounter):
    def __init__(self) -> None: ...

class SimpleDayCounter(DayCounter):
    def __init__(self) -> None: ...

class Business252(DayCounter):
    @overload
    def __init__(
        self,
        c: Calendar,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Rounding:
    def __init__(self) -> None: ...
    def __call__(
        self,
        value: float,
    ) -> float: ...

class UpRounding(Rounding):
    @overload
    def __init__(
        self,
        precision: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        precision: int,
        digit: int,
    ) -> None: ...

class DownRounding(Rounding):
    @overload
    def __init__(
        self,
        precision: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        precision: int,
        digit: int,
    ) -> None: ...

class ClosestRounding(Rounding):
    @overload
    def __init__(
        self,
        precision: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        precision: int,
        digit: int,
    ) -> None: ...

class CeilingTruncation(Rounding):
    @overload
    def __init__(
        self,
        precision: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        precision: int,
        digit: int,
    ) -> None: ...

class FloorTruncation(Rounding):
    @overload
    def __init__(
        self,
        precision: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        precision: int,
        digit: int,
    ) -> None: ...

class Currency:
    @overload
    def __init__(
        self,
        name: str,
        code: str,
        numericCode: int,
        symbol: str,
        fractionSymbol: str,
        fractionsPerUnit: int,
        rounding: Rounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        code: str,
        numericCode: int,
        symbol: str,
        fractionSymbol: str,
        fractionsPerUnit: int,
        rounding: Rounding,
        triangulationCurrency: Currency,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def name(self) -> str: ...
    def code(self) -> str: ...
    def numericCode(self) -> int: ...
    def symbol(self) -> str: ...
    def fractionSymbol(self) -> str: ...
    def fractionsPerUnit(self) -> int: ...
    def rounding(self) -> Rounding: ...
    def empty(self) -> bool: ...
    def triangulationCurrency(self) -> Currency: ...

class AEDCurrency(Currency):
    def __init__(self) -> None: ...

class AOACurrency(Currency):
    def __init__(self) -> None: ...

class ARSCurrency(Currency):
    def __init__(self) -> None: ...

class ATSCurrency(Currency):
    def __init__(self) -> None: ...

class AUDCurrency(Currency):
    def __init__(self) -> None: ...

class BDTCurrency(Currency):
    def __init__(self) -> None: ...

class BEFCurrency(Currency):
    def __init__(self) -> None: ...

class BHDCurrency(Currency):
    def __init__(self) -> None: ...

class BGLCurrency(Currency):
    def __init__(self) -> None: ...

class BGNCurrency(Currency):
    def __init__(self) -> None: ...

class BRLCurrency(Currency):
    def __init__(self) -> None: ...

class BWPCurrency(Currency):
    def __init__(self) -> None: ...

class BYRCurrency(Currency):
    def __init__(self) -> None: ...

class CADCurrency(Currency):
    def __init__(self) -> None: ...

class CHFCurrency(Currency):
    def __init__(self) -> None: ...

class CLFCurrency(Currency):
    def __init__(self) -> None: ...

class CLPCurrency(Currency):
    def __init__(self) -> None: ...

class CNHCurrency(Currency):
    def __init__(self) -> None: ...

class CNYCurrency(Currency):
    def __init__(self) -> None: ...

class COPCurrency(Currency):
    def __init__(self) -> None: ...

class COUCurrency(Currency):
    def __init__(self) -> None: ...

class CYPCurrency(Currency):
    def __init__(self) -> None: ...

class CZKCurrency(Currency):
    def __init__(self) -> None: ...

class DEMCurrency(Currency):
    def __init__(self) -> None: ...

class DKKCurrency(Currency):
    def __init__(self) -> None: ...

class EEKCurrency(Currency):
    def __init__(self) -> None: ...

class EGPCurrency(Currency):
    def __init__(self) -> None: ...

class ESPCurrency(Currency):
    def __init__(self) -> None: ...

class ETBCurrency(Currency):
    def __init__(self) -> None: ...

class EURCurrency(Currency):
    def __init__(self) -> None: ...

class FIMCurrency(Currency):
    def __init__(self) -> None: ...

class FRFCurrency(Currency):
    def __init__(self) -> None: ...

class GELCurrency(Currency):
    def __init__(self) -> None: ...

class GBPCurrency(Currency):
    def __init__(self) -> None: ...

class GHSCurrency(Currency):
    def __init__(self) -> None: ...

class GRDCurrency(Currency):
    def __init__(self) -> None: ...

class HKDCurrency(Currency):
    def __init__(self) -> None: ...

class HRKCurrency(Currency):
    def __init__(self) -> None: ...

class HUFCurrency(Currency):
    def __init__(self) -> None: ...

class IDRCurrency(Currency):
    def __init__(self) -> None: ...

class IEPCurrency(Currency):
    def __init__(self) -> None: ...

class ILSCurrency(Currency):
    def __init__(self) -> None: ...

class INRCurrency(Currency):
    def __init__(self) -> None: ...

class IQDCurrency(Currency):
    def __init__(self) -> None: ...

class IRRCurrency(Currency):
    def __init__(self) -> None: ...

class ISKCurrency(Currency):
    def __init__(self) -> None: ...

class ITLCurrency(Currency):
    def __init__(self) -> None: ...

class JODCurrency(Currency):
    def __init__(self) -> None: ...

class JPYCurrency(Currency):
    def __init__(self) -> None: ...

class KESCurrency(Currency):
    def __init__(self) -> None: ...

class KRWCurrency(Currency):
    def __init__(self) -> None: ...

class KWDCurrency(Currency):
    def __init__(self) -> None: ...

class KZTCurrency(Currency):
    def __init__(self) -> None: ...

class LKRCurrency(Currency):
    def __init__(self) -> None: ...

class LTLCurrency(Currency):
    def __init__(self) -> None: ...

class LUFCurrency(Currency):
    def __init__(self) -> None: ...

class LVLCurrency(Currency):
    def __init__(self) -> None: ...

class MADCurrency(Currency):
    def __init__(self) -> None: ...

class MTLCurrency(Currency):
    def __init__(self) -> None: ...

class MURCurrency(Currency):
    def __init__(self) -> None: ...

class MXNCurrency(Currency):
    def __init__(self) -> None: ...

class MXVCurrency(Currency):
    def __init__(self) -> None: ...

class MYRCurrency(Currency):
    def __init__(self) -> None: ...

class NGNCurrency(Currency):
    def __init__(self) -> None: ...

class NLGCurrency(Currency):
    def __init__(self) -> None: ...

class NOKCurrency(Currency):
    def __init__(self) -> None: ...

class NPRCurrency(Currency):
    def __init__(self) -> None: ...

class NZDCurrency(Currency):
    def __init__(self) -> None: ...

class OMRCurrency(Currency):
    def __init__(self) -> None: ...

class PEHCurrency(Currency):
    def __init__(self) -> None: ...

class PEICurrency(Currency):
    def __init__(self) -> None: ...

class PENCurrency(Currency):
    def __init__(self) -> None: ...

class PHPCurrency(Currency):
    def __init__(self) -> None: ...

class PKRCurrency(Currency):
    def __init__(self) -> None: ...

class PLNCurrency(Currency):
    def __init__(self) -> None: ...

class PTECurrency(Currency):
    def __init__(self) -> None: ...

class QARCurrency(Currency):
    def __init__(self) -> None: ...

class ROLCurrency(Currency):
    def __init__(self) -> None: ...

class RONCurrency(Currency):
    def __init__(self) -> None: ...

class RSDCurrency(Currency):
    def __init__(self) -> None: ...

class RUBCurrency(Currency):
    def __init__(self) -> None: ...

class SARCurrency(Currency):
    def __init__(self) -> None: ...

class SEKCurrency(Currency):
    def __init__(self) -> None: ...

class SGDCurrency(Currency):
    def __init__(self) -> None: ...

class SITCurrency(Currency):
    def __init__(self) -> None: ...

class SKKCurrency(Currency):
    def __init__(self) -> None: ...

class THBCurrency(Currency):
    def __init__(self) -> None: ...

class TNDCurrency(Currency):
    def __init__(self) -> None: ...

class TRLCurrency(Currency):
    def __init__(self) -> None: ...

class TRYCurrency(Currency):
    def __init__(self) -> None: ...

class TTDCurrency(Currency):
    def __init__(self) -> None: ...

class TWDCurrency(Currency):
    def __init__(self) -> None: ...

class UAHCurrency(Currency):
    def __init__(self) -> None: ...

class UGXCurrency(Currency):
    def __init__(self) -> None: ...

class USDCurrency(Currency):
    def __init__(self) -> None: ...

class UYUCurrency(Currency):
    def __init__(self) -> None: ...

class VEBCurrency(Currency):
    def __init__(self) -> None: ...

class VNDCurrency(Currency):
    def __init__(self) -> None: ...

class XOFCurrency(Currency):
    def __init__(self) -> None: ...

class ZARCurrency(Currency):
    def __init__(self) -> None: ...

class ZMWCurrency(Currency):
    def __init__(self) -> None: ...

class BCHCurrency(Currency):
    def __init__(self) -> None: ...

class BTCCurrency(Currency):
    def __init__(self) -> None: ...

class DASHCurrency(Currency):
    def __init__(self) -> None: ...

class ETCCurrency(Currency):
    def __init__(self) -> None: ...

class ETHCurrency(Currency):
    def __init__(self) -> None: ...

class LTCCurrency(Currency):
    def __init__(self) -> None: ...

class XRPCurrency(Currency):
    def __init__(self) -> None: ...

class ZECCurrency(Currency):
    def __init__(self) -> None: ...

class InterestRate:
    @overload
    def __init__(
        self,
        r: float,
        dc: DayCounter,
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def rate(self) -> float: ...
    def dayCounter(self) -> DayCounter: ...
    def compounding(self) -> Compounding: ...
    def frequency(self) -> Frequency: ...
    @overload
    def discountFactor(
        self,
        d1: Date,
        d2: Date,
    ) -> float: ...
    @overload
    def discountFactor(
        self,
        d1: Date,
        d2: Date,
        refStart: Date,
    ) -> float: ...
    @overload
    def discountFactor(
        self,
        d1: Date,
        d2: Date,
        refStart: Date,
        refEnd: Date,
    ) -> float: ...
    @overload
    def discountFactor(
        self,
        t: float,
    ) -> float: ...
    @overload
    def compoundFactor(
        self,
        d1: Date,
        d2: Date,
    ) -> float: ...
    @overload
    def compoundFactor(
        self,
        d1: Date,
        d2: Date,
        refStart: Date,
    ) -> float: ...
    @overload
    def compoundFactor(
        self,
        d1: Date,
        d2: Date,
        refStart: Date,
        refEnd: Date,
    ) -> float: ...
    @overload
    def compoundFactor(
        self,
        t: float,
    ) -> float: ...
    @overload
    def impliedRate(
        self,
        compound: float,
        resultDC: DayCounter,
        comp: Compounding,
        freq: Frequency,
        d1: Date,
        d2: Date,
    ) -> InterestRate: ...
    @overload
    def impliedRate(
        self,
        compound: float,
        resultDC: DayCounter,
        comp: Compounding,
        freq: Frequency,
        d1: Date,
        d2: Date,
        refStart: Date,
    ) -> InterestRate: ...
    @overload
    def impliedRate(
        self,
        compound: float,
        resultDC: DayCounter,
        comp: Compounding,
        freq: Frequency,
        d1: Date,
        d2: Date,
        refStart: Date,
        refEnd: Date,
    ) -> InterestRate: ...
    @overload
    def impliedRate(
        self,
        compound: float,
        resultDC: DayCounter,
        comp: Compounding,
        freq: Frequency,
        t: float,
    ) -> InterestRate: ...
    @overload
    def equivalentRate(
        self,
        comp: Compounding,
        freq: Frequency,
        t: float,
    ) -> InterestRate: ...
    @overload
    def equivalentRate(
        self,
        resultDayCounter: DayCounter,
        comp: Compounding,
        freq: Frequency,
        d1: Date,
        d2: Date,
    ) -> InterestRate: ...
    @overload
    def equivalentRate(
        self,
        resultDayCounter: DayCounter,
        comp: Compounding,
        freq: Frequency,
        d1: Date,
        d2: Date,
        refStart: Date,
    ) -> InterestRate: ...
    @overload
    def equivalentRate(
        self,
        resultDayCounter: DayCounter,
        comp: Compounding,
        freq: Frequency,
        d1: Date,
        d2: Date,
        refStart: Date,
        refEnd: Date,
    ) -> InterestRate: ...

class Observable:
    def __init__(self) -> None: ...

class Array:
    @overload
    def __init__(
        self,
        arg0: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        fill: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def size(self) -> int: ...

class Matrix:
    @overload
    def __init__(
        self,
        arg0: Matrix,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rows: int,
        columns: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rows: int,
        columns: int,
        fill: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def rows(self) -> int: ...
    def columns(self) -> int: ...

class SalvagingAlgorithm:
    class Type(IntEnum):
        None_
        Spectral
        Hypersphere
        LowerDiagonal
        Higham
        Principal

    def __init__(self) -> None: ...

class SVD:
    def __init__(
        self,
        arg0: Matrix,
    ) -> None: ...
    def U(self) -> Matrix: ...
    def V(self) -> Matrix: ...
    def S(self) -> Matrix: ...
    def singularValues(self) -> Array: ...

class SymmetricSchurDecomposition:
    def __init__(
        self,
        s: Matrix,
    ) -> None: ...
    def eigenvalues(self) -> Array: ...
    def eigenvectors(self) -> Matrix: ...

class Quote(Observable):
    def __init__(self) -> None: ...
    def value(self) -> float: ...
    def isValid(self) -> bool: ...

class SimpleQuote(Quote):
    @overload
    def __init__(
        self,
        value: Optional[float],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def setValue(
        self,
        value: Optional[float],
    ) -> None: ...
    @overload
    def setValue(self) -> None: ...
    def reset(self) -> None: ...

class LastFixingQuote(Quote):
    def __init__(
        self,
        index: Index,
    ) -> None: ...
    def index(self) -> Index: ...
    def referenceDate(self) -> Date: ...

class FuturesConvAdjustmentQuote(Quote):
    @overload
    def __init__(
        self,
        index: IborIndex,
        futuresDate: Date,
        futuresQuote: Handle[Quote],
        volatility: Handle[Quote],
        meanReversion: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        index: IborIndex,
        immCode: str,
        futuresQuote: Handle[Quote],
        volatility: Handle[Quote],
        meanReversion: Handle[Quote],
    ) -> None: ...
    def futuresValue(self) -> float: ...
    def volatility(self) -> float: ...
    def meanReversion(self) -> float: ...
    def immDate(self) -> Date: ...

class Brent:
    def __init__(self) -> None: ...
    def setMaxEvaluations(
        self,
        evaluations: int,
    ) -> None: ...
    def setLowerBound(
        self,
        lowerBound: float,
    ) -> None: ...
    def setUpperBound(
        self,
        upperBound: float,
    ) -> None: ...

class Bisection:
    def __init__(self) -> None: ...
    def setMaxEvaluations(
        self,
        evaluations: int,
    ) -> None: ...
    def setLowerBound(
        self,
        lowerBound: float,
    ) -> None: ...
    def setUpperBound(
        self,
        upperBound: float,
    ) -> None: ...

class FalsePosition:
    def __init__(self) -> None: ...
    def setMaxEvaluations(
        self,
        evaluations: int,
    ) -> None: ...
    def setLowerBound(
        self,
        lowerBound: float,
    ) -> None: ...
    def setUpperBound(
        self,
        upperBound: float,
    ) -> None: ...

class Ridder:
    def __init__(self) -> None: ...
    def setMaxEvaluations(
        self,
        evaluations: int,
    ) -> None: ...
    def setLowerBound(
        self,
        lowerBound: float,
    ) -> None: ...
    def setUpperBound(
        self,
        upperBound: float,
    ) -> None: ...

class Secant:
    def __init__(self) -> None: ...
    def setMaxEvaluations(
        self,
        evaluations: int,
    ) -> None: ...
    def setLowerBound(
        self,
        lowerBound: float,
    ) -> None: ...
    def setUpperBound(
        self,
        upperBound: float,
    ) -> None: ...

class Constraint:
    def __init__(self) -> None: ...

class BoundaryConstraint(Constraint):
    def __init__(
        self,
        lower: float,
        upper: float,
    ) -> None: ...

class NoConstraint(Constraint):
    def __init__(self) -> None: ...

class PositiveConstraint(Constraint):
    def __init__(self) -> None: ...

class CompositeConstraint(Constraint):
    def __init__(
        self,
        c1: Constraint,
        c2: Constraint,
    ) -> None: ...

class NonhomogeneousBoundaryConstraint(Constraint):
    def __init__(
        self,
        l: Array,
        u: Array,
    ) -> None: ...

class EndCriteria:
    class Type(IntEnum):
        None_
        MaxIterations
        StationaryPoint
        StationaryFunctionValue
        StationaryFunctionAccuracy
        ZeroGradientNorm
        FunctionEpsilonTooSmall
        Unknown

    def __init__(
        self,
        maxIteration: int,
        maxStationaryStateIterations: int,
        rootEpsilon: float,
        functionEpsilon: float,
        gradientNormEpsilon: float,
    ) -> None: ...
    def succeeded(
        self,
        ecType: EndCriteria.Type,
    ) -> bool: ...

class OptimizationMethod:
    def __init__(self) -> None: ...

class ConjugateGradient(OptimizationMethod):
    def __init__(self) -> None: ...

class Simplex(OptimizationMethod):
    def __init__(
        self,
        lambda_: float,
    ) -> None: ...
    def lambda_(self) -> float: ...

class SteepestDescent(OptimizationMethod):
    def __init__(self) -> None: ...

class BFGS(OptimizationMethod):
    def __init__(self) -> None: ...

class LevenbergMarquardt(OptimizationMethod):
    @overload
    def __init__(
        self,
        epsfcn: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        epsfcn: float,
        xtol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        epsfcn: float,
        xtol: float,
        gtol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        epsfcn: float,
        xtol: float,
        gtol: float,
        useCostFunctionsJacobian: bool,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class DifferentialEvolution(OptimizationMethod):
    def __init__(self) -> None: ...

class SamplerGaussian:
    @overload
    def __init__(
        self,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SamplerLogNormal:
    @overload
    def __init__(
        self,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SamplerMirrorGaussian:
    @overload
    def __init__(
        self,
        lower: Array,
        upper: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        lower: Array,
        upper: Array,
        seed: int,
    ) -> None: ...

class ProbabilityBoltzmannDownhill:
    @overload
    def __init__(
        self,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class TemperatureExponential:
    @overload
    def __init__(
        self,
        initialTemp: float,
        dimension: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        initialTemp: float,
        dimension: int,
        power: float,
    ) -> None: ...

class ReannealingTrivial:
    def __init__(self) -> None: ...

class GaussianSimulatedAnnealing(OptimizationMethod):
    class ResetScheme(IntEnum):
        NoResetScheme
        ResetToBestPoint
        ResetToOrigin

    @overload
    def __init__(
        self,
        sampler: SamplerGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
        reAnnealSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
        reAnnealSteps: int,
        resetScheme: GaussianSimulatedAnnealing.ResetScheme,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
        reAnnealSteps: int,
        resetScheme: GaussianSimulatedAnnealing.ResetScheme,
        resetSteps: int,
    ) -> None: ...

class MirrorGaussianSimulatedAnnealing(OptimizationMethod):
    class ResetScheme(IntEnum):
        NoResetScheme
        ResetToBestPoint
        ResetToOrigin

    @overload
    def __init__(
        self,
        sampler: SamplerMirrorGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerMirrorGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerMirrorGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerMirrorGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerMirrorGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
        reAnnealSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerMirrorGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
        reAnnealSteps: int,
        resetScheme: MirrorGaussianSimulatedAnnealing.ResetScheme,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerMirrorGaussian,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
        reAnnealSteps: int,
        resetScheme: MirrorGaussianSimulatedAnnealing.ResetScheme,
        resetSteps: int,
    ) -> None: ...

class LogNormalSimulatedAnnealing(OptimizationMethod):
    class ResetScheme(IntEnum):
        NoResetScheme
        ResetToBestPoint
        ResetToOrigin

    @overload
    def __init__(
        self,
        sampler: SamplerLogNormal,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerLogNormal,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerLogNormal,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerLogNormal,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerLogNormal,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
        reAnnealSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerLogNormal,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
        reAnnealSteps: int,
        resetScheme: LogNormalSimulatedAnnealing.ResetScheme,
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampler: SamplerLogNormal,
        probability: ProbabilityBoltzmannDownhill,
        temperature: TemperatureExponential,
        reannealing: ReannealingTrivial,
        startTemperature: float,
        endTemperature: float,
        reAnnealSteps: int,
        resetScheme: LogNormalSimulatedAnnealing.ResetScheme,
        resetSteps: int,
    ) -> None: ...

class Optimizer:
    def __init__(self) -> None: ...

class SafeLinearInterpolation:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeLogLinearInterpolation:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeBackwardFlatInterpolation:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeForwardFlatInterpolation:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeCubicNaturalSpline:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeLogCubicNaturalSpline:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeMonotonicCubicNaturalSpline:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeMonotonicLogCubicNaturalSpline:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeKrugerCubic:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeKrugerLogCubic:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeFritschButlandCubic:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeFritschButlandLogCubic:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeParabolic:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeLogParabolic:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeMonotonicParabolic:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeMonotonicLogParabolic:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeLagrangeInterpolation:
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeBilinearInterpolation:
    def __init__(
        self,
        x: Array,
        y: Array,
        m: Matrix,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
        y: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        y: float,
        allowExtrapolation: bool,
    ) -> float: ...

class SafeBicubicSpline:
    def __init__(
        self,
        x: Array,
        y: Array,
        m: Matrix,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
        y: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        y: float,
        allowExtrapolation: bool,
    ) -> float: ...

class CubicInterpolation:
    class DerivativeApprox(IntEnum):
        Spline
        SplineOM1
        SplineOM2
        FourthOrder
        Parabolic
        FritschButland
        Akima
        Kruger
        Harmonic


class MixedInterpolation:
    class Behavior(IntEnum):
        ShareRanges
        SplitRanges


class BackwardFlat:
    def __init__(self) -> None: ...

class ForwardFlat:
    def __init__(self) -> None: ...

class Linear:
    def __init__(self) -> None: ...

class LogLinear:
    def __init__(self) -> None: ...

class Cubic:
    def __init__(self) -> None: ...

class Bicubic:
    def __init__(self) -> None: ...

class MonotonicCubic:
    def __init__(self) -> None: ...

class DefaultLogCubic:
    def __init__(self) -> None: ...

class MonotonicLogCubic:
    def __init__(self) -> None: ...

class SplineCubic:
    def __init__(self) -> None: ...

class SplineLogCubic:
    def __init__(self) -> None: ...

class Kruger:
    def __init__(self) -> None: ...

class KrugerLog:
    def __init__(self) -> None: ...

class ConvexMonotone:
    @overload
    def __init__(
        self,
        quadraticity: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        quadraticity: float,
        monotonicity: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        quadraticity: float,
        monotonicity: float,
        forcePositive: bool,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class ParabolicCubic:
    def __init__(self) -> None: ...

class MonotonicParabolicCubic:
    def __init__(self) -> None: ...

class LogParabolicCubic:
    def __init__(self) -> None: ...

class MonotonicLogParabolicCubic:
    def __init__(self) -> None: ...

class LogMixedLinearCubic:
    @overload
    def __init__(
        self,
        n: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        behavior: MixedInterpolation.Behavior,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        behavior: MixedInterpolation.Behavior,
        da: CubicInterpolation.DerivativeApprox,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        behavior: MixedInterpolation.Behavior,
        da: CubicInterpolation.DerivativeApprox,
        monotonic: bool,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class RichardsonExtrapolation:
    def __init__(self) -> None: ...
    @overload
    def __call__(
        self,
        t: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        t: float,
        s: float,
    ) -> float: ...
    @overload
    def __call__(self) -> float: ...

class ChebyshevInterpolation:
    class PointsType(IntEnum):
        FirstKind
        SecondKind

    @overload
    def __init__(
        self,
        f: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f: Array,
        pointsType: ChebyshevInterpolation.PointsType,
    ) -> None: ...
    @overload
    def __call__(
        self,
        z: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        z: float,
        allowExtrapolation: bool,
    ) -> float: ...
    def nodes(
        self,
        n: int,
        pointsType: ChebyshevInterpolation.PointsType,
    ) -> Array: ...

class SafeConvexMonotoneInterpolation:
    @overload
    def __init__(
        self,
        x: Array,
        y: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        x: Array,
        y: Array,
        quadraticity: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        x: Array,
        y: Array,
        quadraticity: float,
        monotonicity: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        x: Array,
        y: Array,
        quadraticity: float,
        monotonicity: float,
        forcePositive: bool,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...

class TermStructure(Observable):
    def __init__(self) -> None: ...
    def dayCounter(self) -> DayCounter: ...
    def timeFromReference(
        self,
        date: Date,
    ) -> float: ...
    def calendar(self) -> Calendar: ...
    def referenceDate(self) -> Date: ...
    def maxDate(self) -> Date: ...
    def maxTime(self) -> float: ...
    @overload
    def enableExtrapolation(
        self,
        b: bool,
    ) -> None: ...
    @overload
    def enableExtrapolation(self) -> None: ...
    @overload
    def disableExtrapolation(
        self,
        b: bool,
    ) -> None: ...
    @overload
    def disableExtrapolation(self) -> None: ...
    def allowsExtrapolation(self) -> bool: ...

class YieldTermStructure(TermStructure):
    def __init__(self) -> None: ...
    @overload
    def discount(
        self,
        arg0: Date,
    ) -> float: ...
    @overload
    def discount(
        self,
        arg0: Date,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def discount(
        self,
        arg0: float,
    ) -> float: ...
    @overload
    def discount(
        self,
        arg0: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def zeroRate(
        self,
        d: Date,
        arg1: DayCounter,
        arg2: Compounding,
    ) -> InterestRate: ...
    @overload
    def zeroRate(
        self,
        d: Date,
        arg1: DayCounter,
        arg2: Compounding,
        f: Frequency,
    ) -> InterestRate: ...
    @overload
    def zeroRate(
        self,
        d: Date,
        arg1: DayCounter,
        arg2: Compounding,
        f: Frequency,
        extrapolate: bool,
    ) -> InterestRate: ...
    @overload
    def zeroRate(
        self,
        t: float,
        arg1: Compounding,
    ) -> InterestRate: ...
    @overload
    def zeroRate(
        self,
        t: float,
        arg1: Compounding,
        f: Frequency,
    ) -> InterestRate: ...
    @overload
    def zeroRate(
        self,
        t: float,
        arg1: Compounding,
        f: Frequency,
        extrapolate: bool,
    ) -> InterestRate: ...
    @overload
    def forwardRate(
        self,
        d1: Date,
        d2: Date,
        arg2: DayCounter,
        arg3: Compounding,
    ) -> InterestRate: ...
    @overload
    def forwardRate(
        self,
        d1: Date,
        d2: Date,
        arg2: DayCounter,
        arg3: Compounding,
        f: Frequency,
    ) -> InterestRate: ...
    @overload
    def forwardRate(
        self,
        d1: Date,
        d2: Date,
        arg2: DayCounter,
        arg3: Compounding,
        f: Frequency,
        extrapolate: bool,
    ) -> InterestRate: ...
    @overload
    def forwardRate(
        self,
        t1: float,
        t2: float,
        arg2: Compounding,
    ) -> InterestRate: ...
    @overload
    def forwardRate(
        self,
        t1: float,
        t2: float,
        arg2: Compounding,
        f: Frequency,
    ) -> InterestRate: ...
    @overload
    def forwardRate(
        self,
        t1: float,
        t2: float,
        arg2: Compounding,
        f: Frequency,
        extrapolate: bool,
    ) -> InterestRate: ...

class ImpliedTermStructure(YieldTermStructure):
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        referenceDate: Date,
    ) -> None: ...

class ZeroSpreadedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        spreadHandle: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        spreadHandle: Handle[Quote],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        spreadHandle: Handle[Quote],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        spreadHandle: Handle[Quote],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...

class ForwardSpreadedTermStructure(YieldTermStructure):
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        spreadHandle: Handle[Quote],
    ) -> None: ...

class PiecewiseZeroSpreadedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
        factory: Linear,
    ) -> None: ...

class SpreadedLinearZeroInterpolatedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
        factory: Linear,
    ) -> None: ...

class SpreadedBackwardFlatZeroInterpolatedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
        factory: BackwardFlat,
    ) -> None: ...

class SpreadedCubicZeroInterpolatedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
        factory: Cubic,
    ) -> None: ...

class SpreadedKrugerZeroInterpolatedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
        factory: Kruger,
    ) -> None: ...

class SpreadedSplineCubicZeroInterpolatedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
        factory: SplineCubic,
    ) -> None: ...

class SpreadedParabolicCubicZeroInterpolatedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
        factory: ParabolicCubic,
    ) -> None: ...

class SpreadedMonotonicParabolicCubicZeroInterpolatedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
        factory: MonotonicParabolicCubic,
    ) -> None: ...

class PiecewiseForwardSpreadedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        dc: DayCounter,
        factory: BackwardFlat,
    ) -> None: ...

class PiecewiseLinearForwardSpreadedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: list[Handle[Quote]],
        dates: list[Date],
        dc: DayCounter,
        factory: Linear,
    ) -> None: ...

class FlatForward(YieldTermStructure):
    @overload
    def __init__(
        self,
        referenceDate: Date,
        forward: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        forward: Handle[Quote],
        dayCounter: DayCounter,
        compounding: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        forward: Handle[Quote],
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        forward: float,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        forward: float,
        dayCounter: DayCounter,
        compounding: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        forward: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        forward: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        forward: Handle[Quote],
        dayCounter: DayCounter,
        compounding: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        forward: Handle[Quote],
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        forward: float,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        forward: float,
        dayCounter: DayCounter,
        compounding: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        forward: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> None: ...

class UltimateForwardTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        lastLiquidForwardRate: Handle[Quote],
        ultimateForwardRate: Handle[Quote],
        firstSmoothingPoint: Period,
        alpha: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        lastLiquidForwardRate: Handle[Quote],
        ultimateForwardRate: Handle[Quote],
        firstSmoothingPoint: Period,
        alpha: float,
        roundingDigits: Optional[int],
    ) -> None: ...
    @overload
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        lastLiquidForwardRate: Handle[Quote],
        ultimateForwardRate: Handle[Quote],
        firstSmoothingPoint: Period,
        alpha: float,
        roundingDigits: Optional[int],
        compounding: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        lastLiquidForwardRate: Handle[Quote],
        ultimateForwardRate: Handle[Quote],
        firstSmoothingPoint: Period,
        alpha: float,
        roundingDigits: Optional[int],
        compounding: Compounding,
        frequency: Frequency,
    ) -> None: ...

class QuantoTermStructure(YieldTermStructure):
    def __init__(
        self,
        underlyingDividendTS: Handle[YieldTermStructure],
        riskFreeTS: Handle[YieldTermStructure],
        foreignRiskFreeTS: Handle[YieldTermStructure],
        underlyingBlackVolTS: Handle[Any],
        strike: float,
        exchRateBlackVolTS: Handle[Any],
        exchRateATMlevel: float,
        underlyingExchRateCorrelation: float,
    ) -> None: ...

class IntervalPrice:
    class Type(IntEnum):
        Open
        Close
        High
        Low

    def __init__(
        self,
        arg0: float,
        arg1: float,
        arg2: float,
        arg3: float,
    ) -> None: ...
    def setValue(
        self,
        arg0: float,
        arg1: IntervalPrice.Type,
    ) -> None: ...
    def setValues(
        self,
        arg0: float,
        arg1: float,
        arg2: float,
        arg3: float,
    ) -> None: ...
    def value(
        self,
        t: IntervalPrice.Type,
    ) -> float: ...
    def open_(self) -> float: ...
    def close(self) -> float: ...
    def high(self) -> float: ...
    def low(self) -> float: ...
    def makeSeries(
        self,
        d: list[Date],
        open_: list[float],
        close: list[float],
        high: list[float],
        low: list[float],
    ) -> TimeSeries[IntervalPrice]: ...
    def extractValues(
        self,
        arg0: TimeSeries[IntervalPrice],
        t: IntervalPrice.Type,
    ) -> list[float]: ...
    def extractComponent(
        self,
        arg0: TimeSeries[IntervalPrice],
        t: IntervalPrice.Type,
    ) -> TimeSeries[float]: ...

class IndexManager:
    def __init__(self) -> None: ...
    def instance(self) -> IndexManager: ...
    def setHistory(
        self,
        name: str,
        fixings: TimeSeries[float],
    ) -> None: ...
    def getHistory(
        self,
        name: str,
    ) -> TimeSeries[float]: ...
    def hasHistory(
        self,
        name: str,
    ) -> bool: ...
    def histories(self) -> list[str]: ...
    def clearHistory(
        self,
        name: str,
    ) -> None: ...
    def clearHistories(self) -> None: ...
    def hasHistoricalFixing(
        self,
        name: str,
        fixingDate: Date,
    ) -> bool: ...

class Index(Observable):
    def __init__(self) -> None: ...
    def name(self) -> str: ...
    def fixingCalendar(self) -> Calendar: ...
    def isValidFixingDate(
        self,
        fixingDate: Date,
    ) -> bool: ...
    def hasHistoricalFixing(
        self,
        fixingDate: Date,
    ) -> bool: ...
    @overload
    def fixing(
        self,
        fixingDate: Date,
    ) -> float: ...
    @overload
    def fixing(
        self,
        fixingDate: Date,
        forecastTodaysFixing: bool,
    ) -> float: ...
    def pastFixing(
        self,
        fixingDate: Date,
    ) -> float: ...
    @overload
    def addFixing(
        self,
        fixingDate: Date,
        fixing: float,
    ) -> None: ...
    @overload
    def addFixing(
        self,
        fixingDate: Date,
        fixing: float,
        forceOverwrite: bool,
    ) -> None: ...
    def timeSeries(self) -> TimeSeries[float]: ...
    def clearFixings(self) -> None: ...

class InterestRateIndex(Index):
    def __init__(self) -> None: ...
    def familyName(self) -> str: ...
    def tenor(self) -> Period: ...
    def fixingDays(self) -> int: ...
    def fixingDate(
        self,
        valueDate: Date,
    ) -> Date: ...
    def currency(self) -> Currency: ...
    def dayCounter(self) -> DayCounter: ...
    def maturityDate(
        self,
        valueDate: Date,
    ) -> Date: ...
    def valueDate(
        self,
        fixingDate: Date,
    ) -> Date: ...

class IborIndex(InterestRateIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    def businessDayConvention(self) -> BusinessDayConvention: ...
    def endOfMonth(self) -> bool: ...
    def forwardingTermStructure(self) -> Handle[YieldTermStructure]: ...
    def clone(
        self,
        arg0: Handle[YieldTermStructure],
    ) -> IborIndex: ...

class OvernightIndex(IborIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        settlementDays: int,
        currency: Currency,
        calendar: Calendar,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        settlementDays: int,
        currency: Currency,
        calendar: Calendar,
        dayCounter: DayCounter,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Libor(IborIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        financialCenterCalendar: Calendar,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        financialCenterCalendar: Calendar,
        dayCounter: DayCounter,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    def jointCalendar(self) -> Calendar: ...

class DailyTenorLibor(IborIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        settlementDays: int,
        currency: Currency,
        financialCenterCalendar: Calendar,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        settlementDays: int,
        currency: Currency,
        financialCenterCalendar: Calendar,
        dayCounter: DayCounter,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class CustomIborIndex(IborIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        fixingCalendar: Calendar,
        valueCalendar: Calendar,
        maturityCalendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        fixingCalendar: Calendar,
        valueCalendar: Calendar,
        maturityCalendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    def valueCalendar(self) -> Calendar: ...
    def maturityCalendar(self) -> Calendar: ...

class SwapIndex(InterestRateIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        calendar: Calendar,
        fixedLegTenor: Period,
        fixedLegConvention: BusinessDayConvention,
        fixedLegDayCounter: DayCounter,
        iborIndex: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        calendar: Calendar,
        fixedLegTenor: Period,
        fixedLegConvention: BusinessDayConvention,
        fixedLegDayCounter: DayCounter,
        iborIndex: IborIndex,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    def fixedLegTenor(self) -> Period: ...
    def fixedLegConvention(self) -> BusinessDayConvention: ...
    def iborIndex(self) -> IborIndex: ...
    def forwardingTermStructure(self) -> Handle[YieldTermStructure]: ...
    def discountingTermStructure(self) -> Handle[YieldTermStructure]: ...
    @overload
    def clone(
        self,
        forwarding: Handle[YieldTermStructure],
        discounting: Handle[YieldTermStructure],
    ) -> SwapIndex: ...
    @overload
    def clone(
        self,
        h: Handle[YieldTermStructure],
    ) -> SwapIndex: ...
    @overload
    def clone(
        self,
        tenor: Period,
    ) -> SwapIndex: ...

class SwapSpreadIndex(InterestRateIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        swapIndex1: SwapIndex,
        swapIndex2: SwapIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        swapIndex1: SwapIndex,
        swapIndex2: SwapIndex,
        gearing1: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        swapIndex1: SwapIndex,
        swapIndex2: SwapIndex,
        gearing1: float,
        gearing2: float,
    ) -> None: ...
    def forecastFixing(
        self,
        fixingDate: Date,
    ) -> float: ...
    def swapIndex1(self) -> SwapIndex: ...
    def swapIndex2(self) -> SwapIndex: ...
    def gearing1(self) -> float: ...
    def gearing2(self) -> float: ...

class EquityIndex(Index):
    @overload
    def __init__(
        self,
        name: str,
        fixingCalendar: Calendar,
        currency: Currency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        fixingCalendar: Calendar,
        currency: Currency,
        interest: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        fixingCalendar: Calendar,
        currency: Currency,
        interest: Handle[YieldTermStructure],
        dividend: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        fixingCalendar: Calendar,
        currency: Currency,
        interest: Handle[YieldTermStructure],
        dividend: Handle[YieldTermStructure],
        spot: Handle[Quote],
    ) -> None: ...
    def currency(self) -> Currency: ...
    def equityInterestRateCurve(self) -> Handle[YieldTermStructure]: ...
    def equityDividendCurve(self) -> Handle[YieldTermStructure]: ...
    def spot(self) -> Handle[Quote]: ...
    def clone(
        self,
        interest: Handle[YieldTermStructure],
        dividend: Handle[YieldTermStructure],
        spot: Handle[Quote],
    ) -> EquityIndex: ...

class AUDLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class CADLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class CADLiborON(DailyTenorLibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Cdor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class CHFLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class DKKLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Bbsw(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Bbsw1M(Bbsw):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bbsw2M(Bbsw):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bbsw3M(Bbsw):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bbsw4M(Bbsw):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bbsw5M(Bbsw):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bbsw6M(Bbsw):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bkbm(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Bkbm1M(Bkbm):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bkbm2M(Bkbm):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bkbm3M(Bkbm):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bkbm4M(Bkbm):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bkbm5M(Bkbm):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bkbm6M(Bkbm):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Euribor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Euribor1W(Euribor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Euribor1M(Euribor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Euribor3M(Euribor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Euribor6M(Euribor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Euribor1Y(Euribor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Euribor365(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class EURLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class EURLibor1M(EURLibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class EURLibor3M(EURLibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class EURLibor6M(EURLibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class EURLibor1Y(EURLibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class GBPLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class GBPLiborON(DailyTenorLibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Jibar(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class JPYLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Mosprime(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class NZDLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Pribor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Robor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class SEKLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Shibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Tibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class THBFIX(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class TRLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class USDLibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class USDLiborON(DailyTenorLibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Wibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Zibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Aonia(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Cdi(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Corra(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Destr(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Eonia(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Estr(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class FedFunds(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Kofr(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Nzocr(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Saron(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Sofr(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Sonia(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Swestr(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Tonar(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Tona(OvernightIndex):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class EuriborSwapIsdaFixA(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class EuriborSwapIsdaFixB(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class EuriborSwapIfrFix(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class EurLiborSwapIsdaFixA(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class EurLiborSwapIsdaFixB(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class EurLiborSwapIfrFix(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class ChfLiborSwapIsdaFix(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class GbpLiborSwapIsdaFix(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class JpyLiborSwapIsdaFixAm(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class JpyLiborSwapIsdaFixPm(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class UsdLiborSwapIsdaFixAm(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class UsdLiborSwapIsdaFixPm(SwapIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h1: Handle[YieldTermStructure],
        h2: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class Bibor(IborIndex):
    @overload
    def __init__(
        self,
        tenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tenor: Period,
        h: Handle[YieldTermStructure],
    ) -> None: ...

class BiborSW(Bibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bibor1M(Bibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bibor2M(Bibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bibor3M(Bibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bibor6M(Bibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Bibor1Y(Bibor):
    @overload
    def __init__(
        self,
        h: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class DateGeneration:
    class Rule(IntEnum):
        Backward
        Forward
        Zero
        ThirdWednesday
        ThirdWednesdayInclusive
        Twentieth
        TwentiethIMM
        OldCDS
        CDS
        CDS2015

    def __init__(self) -> None: ...

class Schedule:
    @overload
    def __init__(
        self,
        arg0: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: list[Date],
        calendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: list[Date],
        calendar: Calendar,
        convention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        effectiveDate: Date,
        terminationDate: Date,
        tenor: Period,
        calendar: Calendar,
        convention: BusinessDayConvention,
        terminationDateConvention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        endOfMonth: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        effectiveDate: Date,
        terminationDate: Date,
        tenor: Period,
        calendar: Calendar,
        convention: BusinessDayConvention,
        terminationDateConvention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        endOfMonth: bool,
        firstDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        effectiveDate: Date,
        terminationDate: Date,
        tenor: Period,
        calendar: Calendar,
        convention: BusinessDayConvention,
        terminationDateConvention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        endOfMonth: bool,
        firstDate: Date,
        nextToLastDate: Date,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def size(self) -> int: ...
    def date(
        self,
        i: int,
    ) -> Date: ...
    def previousDate(
        self,
        refDate: Date,
    ) -> Date: ...
    def nextDate(
        self,
        refDate: Date,
    ) -> Date: ...
    def dates(self) -> list[Date]: ...
    def hasIsRegular(self) -> bool: ...
    @overload
    def isRegular(
        self,
        i: int,
    ) -> bool: ...
    @overload
    def isRegular(self) -> list[bool]: ...
    def calendar(self) -> Calendar: ...
    def startDate(self) -> Date: ...
    def endDate(self) -> Date: ...
    def hasTenor(self) -> bool: ...
    def tenor(self) -> Period: ...
    def businessDayConvention(self) -> BusinessDayConvention: ...
    def hasTerminationDateBusinessDayConvention(self) -> bool: ...
    def terminationDateBusinessDayConvention(self) -> BusinessDayConvention: ...
    def hasRule(self) -> bool: ...
    def rule(self) -> DateGeneration.Rule: ...
    def hasEndOfMonth(self) -> bool: ...
    def endOfMonth(self) -> bool: ...
    def after(
        self,
        truncationDate: Date,
    ) -> Schedule: ...
    def until(
        self,
        truncationDate: Date,
    ) -> Schedule: ...

class MakeSchedule:
    def __init__(self) -> None: ...
    def from_(
        self,
        effectiveDate: Date,
    ) -> MakeSchedule: ...
    def to(
        self,
        terminationDate: Date,
    ) -> MakeSchedule: ...
    def withTenor(
        self,
        arg0: Period,
    ) -> MakeSchedule: ...
    def withFrequency(
        self,
        arg0: Frequency,
    ) -> MakeSchedule: ...
    def withCalendar(
        self,
        arg0: Calendar,
    ) -> MakeSchedule: ...
    def withConvention(
        self,
        arg0: BusinessDayConvention,
    ) -> MakeSchedule: ...
    def withTerminationDateConvention(
        self,
        arg0: BusinessDayConvention,
    ) -> MakeSchedule: ...
    def withRule(
        self,
        arg0: DateGeneration.Rule,
    ) -> MakeSchedule: ...
    def forwards(self) -> MakeSchedule: ...
    def backwards(self) -> MakeSchedule: ...
    @overload
    def endOfMonth(
        self,
        flag: bool,
    ) -> MakeSchedule: ...
    @overload
    def endOfMonth(self) -> MakeSchedule: ...
    def withFirstDate(
        self,
        d: Date,
    ) -> MakeSchedule: ...
    def withNextToLastDate(
        self,
        d: Date,
    ) -> MakeSchedule: ...

class VolatilityTermStructure(TermStructure):
    def __init__(self) -> None: ...
    def minStrike(self) -> float: ...
    def maxStrike(self) -> float: ...

class BlackVolTermStructure(VolatilityTermStructure):
    def __init__(self) -> None: ...
    @overload
    def blackVol(
        self,
        arg0: Date,
        strike: float,
    ) -> float: ...
    @overload
    def blackVol(
        self,
        arg0: Date,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackVol(
        self,
        arg0: float,
        strike: float,
    ) -> float: ...
    @overload
    def blackVol(
        self,
        arg0: float,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        arg0: Date,
        strike: float,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        arg0: Date,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        arg0: float,
        strike: float,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        arg0: float,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackForwardVol(
        self,
        arg0: Date,
        arg1: Date,
        strike: float,
    ) -> float: ...
    @overload
    def blackForwardVol(
        self,
        arg0: Date,
        arg1: Date,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackForwardVol(
        self,
        arg0: float,
        arg1: float,
        strike: float,
    ) -> float: ...
    @overload
    def blackForwardVol(
        self,
        arg0: float,
        arg1: float,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackForwardVariance(
        self,
        arg0: Date,
        arg1: Date,
        strike: float,
    ) -> float: ...
    @overload
    def blackForwardVariance(
        self,
        arg0: Date,
        arg1: Date,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackForwardVariance(
        self,
        arg0: float,
        arg1: float,
        strike: float,
    ) -> float: ...
    @overload
    def blackForwardVariance(
        self,
        arg0: float,
        arg1: float,
        strike: float,
        extrapolate: bool,
    ) -> float: ...

class LocalVolTermStructure(VolatilityTermStructure):
    def __init__(self) -> None: ...
    @overload
    def localVol(
        self,
        arg0: Date,
        u: float,
    ) -> float: ...
    @overload
    def localVol(
        self,
        arg0: Date,
        u: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def localVol(
        self,
        arg0: float,
        u: float,
    ) -> float: ...
    @overload
    def localVol(
        self,
        arg0: float,
        u: float,
        extrapolate: bool,
    ) -> float: ...

class OptionletVolatilityStructure(VolatilityTermStructure):
    def __init__(self) -> None: ...
    @overload
    def volatility(
        self,
        arg0: Date,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        arg0: Date,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def volatility(
        self,
        arg0: float,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        arg0: float,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        arg0: Date,
        strike: float,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        arg0: Date,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        arg0: float,
        strike: float,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        arg0: float,
        strike: float,
        extrapolate: bool,
    ) -> float: ...

class YoYOptionletVolatilitySurface(VolatilityTermStructure):
    def __init__(self) -> None: ...
    def observationLag(self) -> Period: ...
    def frequency(self) -> float: ...
    def indexIsInterpolated(self) -> bool: ...
    def baseDate(self) -> Date: ...
    @overload
    def timeFromBase(
        self,
        date: Date,
    ) -> float: ...
    @overload
    def timeFromBase(
        self,
        date: Date,
        obsLag: Period,
    ) -> float: ...
    def minStrike(self) -> float: ...
    def maxStrike(self) -> float: ...
    def baseLevel(self) -> float: ...
    @overload
    def volatility(
        self,
        maturityDate: Date,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        maturityDate: Date,
        strike: float,
        obsLag: Period,
    ) -> float: ...
    @overload
    def volatility(
        self,
        maturityDate: Date,
        strike: float,
        obsLag: Period,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def volatility(
        self,
        optionTenor: Period,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        optionTenor: Period,
        strike: float,
        obsLag: Period,
    ) -> float: ...
    @overload
    def volatility(
        self,
        optionTenor: Period,
        strike: float,
        obsLag: Period,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def totalVariance(
        self,
        exerciseDate: Date,
        strike: float,
    ) -> float: ...
    @overload
    def totalVariance(
        self,
        exerciseDate: Date,
        strike: float,
        obsLag: Period,
    ) -> float: ...
    @overload
    def totalVariance(
        self,
        exerciseDate: Date,
        strike: float,
        obsLag: Period,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def totalVariance(
        self,
        optionTenor: Period,
        strike: float,
    ) -> float: ...
    @overload
    def totalVariance(
        self,
        optionTenor: Period,
        strike: float,
        obsLag: Period,
    ) -> float: ...
    @overload
    def totalVariance(
        self,
        optionTenor: Period,
        strike: float,
        obsLag: Period,
        extrapolate: bool,
    ) -> float: ...

class SmileSection(Observable):
    def __init__(self) -> None: ...
    def minStrike(self) -> float: ...
    def maxStrike(self) -> float: ...
    def atmLevel(self) -> float: ...
    def variance(
        self,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        strike: float,
        type: VolatilityType,
    ) -> float: ...
    @overload
    def volatility(
        self,
        strike: float,
        type: VolatilityType,
        shift: float,
    ) -> float: ...
    def exerciseDate(self) -> Date: ...
    def volatilityType(self) -> VolatilityType: ...
    def shift(self) -> float: ...
    def referenceDate(self) -> Date: ...
    def exerciseTime(self) -> float: ...
    def dayCounter(self) -> DayCounter: ...
    @overload
    def optionPrice(
        self,
        strike: float,
    ) -> float: ...
    @overload
    def optionPrice(
        self,
        strike: float,
        type: Option.Type,
    ) -> float: ...
    @overload
    def optionPrice(
        self,
        strike: float,
        type: Option.Type,
        discount: float,
    ) -> float: ...
    @overload
    def digitalOptionPrice(
        self,
        strike: float,
    ) -> float: ...
    @overload
    def digitalOptionPrice(
        self,
        strike: float,
        type: Option.Type,
    ) -> float: ...
    @overload
    def digitalOptionPrice(
        self,
        strike: float,
        type: Option.Type,
        discount: float,
    ) -> float: ...
    @overload
    def digitalOptionPrice(
        self,
        strike: float,
        type: Option.Type,
        discount: float,
        gap: float,
    ) -> float: ...
    @overload
    def vega(
        self,
        strike: float,
    ) -> float: ...
    @overload
    def vega(
        self,
        strike: float,
        discount: float,
    ) -> float: ...
    @overload
    def density(
        self,
        strike: float,
    ) -> float: ...
    @overload
    def density(
        self,
        strike: float,
        discount: float,
    ) -> float: ...
    @overload
    def density(
        self,
        strike: float,
        discount: float,
        gap: float,
    ) -> float: ...

class SwaptionVolatilityStructure(VolatilityTermStructure):
    def __init__(self) -> None: ...
    @overload
    def volatility(
        self,
        start: Date,
        length: Period,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        start: Date,
        length: Period,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def volatility(
        self,
        start: float,
        length: float,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        start: float,
        length: float,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        start: Date,
        length: Period,
        strike: float,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        start: Date,
        length: Period,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        start: float,
        length: float,
        strike: float,
    ) -> float: ...
    @overload
    def blackVariance(
        self,
        start: float,
        length: float,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    def optionDateFromTenor(
        self,
        p: Period,
    ) -> Date: ...
    @overload
    def shift(
        self,
        optionDate: Date,
        swapLength: float,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionDate: Date,
        swapLength: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionDate: Date,
        swapTenor: Period,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionDate: Date,
        swapTenor: Period,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionTenor: Period,
        swapLength: float,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionTenor: Period,
        swapLength: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionTenor: Period,
        swapTenor: Period,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionTenor: Period,
        swapTenor: Period,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionTime: float,
        swapLength: float,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionTime: float,
        swapLength: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionTime: float,
        swapTenor: Period,
    ) -> float: ...
    @overload
    def shift(
        self,
        optionTime: float,
        swapTenor: Period,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def smileSection(
        self,
        optionDate: Date,
        swapLength: float,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionDate: Date,
        swapLength: float,
        extr: bool,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionDate: Date,
        swapTenor: Period,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionDate: Date,
        swapTenor: Period,
        extr: bool,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionTenor: Period,
        swapLength: float,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionTenor: Period,
        swapLength: float,
        extr: bool,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionTenor: Period,
        swapTenor: Period,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionTenor: Period,
        swapTenor: Period,
        extr: bool,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionTime: float,
        swapLength: float,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionTime: float,
        swapLength: float,
        extr: bool,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionTime: float,
        swapTenor: Period,
    ) -> SmileSection: ...
    @overload
    def smileSection(
        self,
        optionTime: float,
        swapTenor: Period,
        extr: bool,
    ) -> SmileSection: ...

class SafeSABRInterpolation:
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
        rhoIsFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
        rhoIsFixed: bool,
        vegaWeighted: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
        rhoIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
        rhoIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        optMethod: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
        rhoIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        optMethod: OptimizationMethod,
        errorAccept: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
        rhoIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        optMethod: OptimizationMethod,
        errorAccept: float,
        useMaxError: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
        rhoIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        optMethod: OptimizationMethod,
        errorAccept: float,
        useMaxError: bool,
        maxGuesses: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
        rhoIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        optMethod: OptimizationMethod,
        errorAccept: float,
        useMaxError: bool,
        maxGuesses: int,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        strikes: Array,
        volatilities: Array,
        expiryTime: float,
        forward: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        alphaIsFixed: bool,
        betaIsFixed: bool,
        nuIsFixed: bool,
        rhoIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        optMethod: OptimizationMethod,
        errorAccept: float,
        useMaxError: bool,
        maxGuesses: int,
        shift: float,
        volatilityType: VolatilityType,
    ) -> None: ...
    @overload
    def __call__(
        self,
        x: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        x: float,
        allowExtrapolation: bool,
    ) -> float: ...
    def alpha(self) -> float: ...
    def beta(self) -> float: ...
    def rho(self) -> float: ...
    def nu(self) -> float: ...

class BlackConstantVol(Any):
    @overload
    def __init__(
        self,
        referenceDate: Date,
        c: Calendar,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        c: Calendar,
        volatility: float,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        volatility: float,
        dayCounter: DayCounter,
    ) -> None: ...

class BlackVarianceCurve(Any):
    @overload
    def __init__(
        self,
        referenceDate: Date,
        dates: list[Date],
        volatilities: list[float],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        dates: list[Date],
        volatilities: list[float],
        dayCounter: DayCounter,
        forceMonotoneVariance: bool,
    ) -> None: ...

class BlackVarianceSurface(Any):
    class Extrapolation(IntEnum):
        ConstantExtrapolation
        InterpolatorDefaultExtrapolation


class ConstantOptionletVolatility(OptionletVolatilityStructure):
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dayCounter: DayCounter,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dayCounter: DayCounter,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dayCounter: DayCounter,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dayCounter: DayCounter,
        type: VolatilityType,
        shift: float,
    ) -> None: ...

class ConstantSwaptionVolatility(SwaptionVolatilityStructure):
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dc: DayCounter,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dc: DayCounter,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dc: DayCounter,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dc: DayCounter,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dc: DayCounter,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: Handle[Quote],
        dc: DayCounter,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dc: DayCounter,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        volatility: float,
        dc: DayCounter,
        type: VolatilityType,
        shift: float,
    ) -> None: ...

class SwaptionVolatilityDiscrete(SwaptionVolatilityStructure):
    def __init__(self) -> None: ...
    def optionTenors(self) -> list[Period]: ...
    def optionDates(self) -> list[Date]: ...
    def optionTimes(self) -> list[float]: ...
    def swapTenors(self) -> list[Period]: ...
    def swapLengths(self) -> list[float]: ...
    def optionDateFromTime(
        self,
        optionTime: float,
    ) -> Date: ...

class SwaptionVolatilityMatrix(SwaptionVolatilityDiscrete):
    @overload
    def __init__(
        self,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        swapTenors: list[Period],
        vols: Matrix,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        swapTenors: list[Period],
        vols: Matrix,
        dayCounter: DayCounter,
        flatExtrapolation: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        swapTenors: list[Period],
        vols: Matrix,
        dayCounter: DayCounter,
        flatExtrapolation: bool,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        swapTenors: list[Period],
        vols: Matrix,
        dayCounter: DayCounter,
        flatExtrapolation: bool,
        type: VolatilityType,
        shifts: Matrix,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        swapTenors: list[Period],
        vols: list[list[Handle[Quote]]],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        swapTenors: list[Period],
        vols: list[list[Handle[Quote]]],
        dayCounter: DayCounter,
        flatExtrapolation: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        swapTenors: list[Period],
        vols: list[list[Handle[Quote]]],
        dayCounter: DayCounter,
        flatExtrapolation: bool,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        swapTenors: list[Period],
        vols: list[list[Handle[Quote]]],
        dayCounter: DayCounter,
        flatExtrapolation: bool,
        type: VolatilityType,
        shifts: list[list[float]],
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        dates: list[Date],
        lengths: list[Period],
        vols: Matrix,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        dates: list[Date],
        lengths: list[Period],
        vols: Matrix,
        dayCounter: DayCounter,
        flatExtrapolation: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        dates: list[Date],
        lengths: list[Period],
        vols: Matrix,
        dayCounter: DayCounter,
        flatExtrapolation: bool,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        dates: list[Date],
        lengths: list[Period],
        vols: Matrix,
        dayCounter: DayCounter,
        flatExtrapolation: bool,
        type: VolatilityType,
        shifts: Matrix,
    ) -> None: ...
    def volatilityType(self) -> VolatilityType: ...

class SabrSmileSection(SmileSection):
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sabrParameters: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sabrParameters: list[float],
        referenceDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sabrParameters: list[float],
        referenceDate: Date,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sabrParameters: list[float],
        referenceDate: Date,
        dc: DayCounter,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sabrParameters: list[float],
        referenceDate: Date,
        dc: DayCounter,
        shift: float,
        volatilityType: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeToExpiry: float,
        forward: float,
        sabrParameters: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeToExpiry: float,
        forward: float,
        sabrParameters: list[float],
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeToExpiry: float,
        forward: float,
        sabrParameters: list[float],
        shift: float,
        volatilityType: VolatilityType,
    ) -> None: ...
    def alpha(self) -> float: ...
    def beta(self) -> float: ...
    def nu(self) -> float: ...
    def rho(self) -> float: ...

class SviSmileSection(SmileSection):
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sviParameters: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sviParameters: list[float],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeToExpiry: float,
        forward: float,
        sviParameters: list[float],
    ) -> None: ...

class SviInterpolatedSmileSection(SmileSection):
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        aIsFixed: bool,
        bIsFixed: bool,
        sigmaIsFixed: bool,
        rhoIsFixed: bool,
        mIsFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        aIsFixed: bool,
        bIsFixed: bool,
        sigmaIsFixed: bool,
        rhoIsFixed: bool,
        mIsFixed: bool,
        vegaWeighted: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        aIsFixed: bool,
        bIsFixed: bool,
        sigmaIsFixed: bool,
        rhoIsFixed: bool,
        mIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        aIsFixed: bool,
        bIsFixed: bool,
        sigmaIsFixed: bool,
        rhoIsFixed: bool,
        mIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        aIsFixed: bool,
        bIsFixed: bool,
        sigmaIsFixed: bool,
        rhoIsFixed: bool,
        mIsFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        isAFixed: bool,
        isBFixed: bool,
        isSigmaFixed: bool,
        isRhoFixed: bool,
        isMFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        isAFixed: bool,
        isBFixed: bool,
        isSigmaFixed: bool,
        isRhoFixed: bool,
        isMFixed: bool,
        vegaWeighted: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        isAFixed: bool,
        isBFixed: bool,
        isSigmaFixed: bool,
        isRhoFixed: bool,
        isMFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        isAFixed: bool,
        isBFixed: bool,
        isSigmaFixed: bool,
        isRhoFixed: bool,
        isMFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        a: float,
        b: float,
        sigma: float,
        rho: float,
        m: float,
        isAFixed: bool,
        isBFixed: bool,
        isSigmaFixed: bool,
        isRhoFixed: bool,
        isMFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
        dc: DayCounter,
    ) -> None: ...
    def a(self) -> float: ...
    def b(self) -> float: ...
    def sigma(self) -> float: ...
    def rho(self) -> float: ...
    def m(self) -> float: ...
    def rmsError(self) -> float: ...
    def maxError(self) -> float: ...
    def endCriteria(self) -> EndCriteria.Type: ...

class SwaptionVolatilityCube(SwaptionVolatilityDiscrete):
    def __init__(self) -> None: ...
    def atmStrike(
        self,
        optionDate: Date,
        swapTenor: Period,
    ) -> float: ...

class SabrSwaptionVolatilityCube(SwaptionVolatilityCube):
    @overload
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
        parametersGuess: list[list[Handle[Quote]]],
        isParameterFixed: list[bool],
        isAtmCalibrated: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
        parametersGuess: list[list[Handle[Quote]]],
        isParameterFixed: list[bool],
        isAtmCalibrated: bool,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
        parametersGuess: list[list[Handle[Quote]]],
        isParameterFixed: list[bool],
        isAtmCalibrated: bool,
        endCriteria: EndCriteria,
        maxErrorTolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
        parametersGuess: list[list[Handle[Quote]]],
        isParameterFixed: list[bool],
        isAtmCalibrated: bool,
        endCriteria: EndCriteria,
        maxErrorTolerance: float,
        optMethod: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
        parametersGuess: list[list[Handle[Quote]]],
        isParameterFixed: list[bool],
        isAtmCalibrated: bool,
        endCriteria: EndCriteria,
        maxErrorTolerance: float,
        optMethod: OptimizationMethod,
        errorAccept: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
        parametersGuess: list[list[Handle[Quote]]],
        isParameterFixed: list[bool],
        isAtmCalibrated: bool,
        endCriteria: EndCriteria,
        maxErrorTolerance: float,
        optMethod: OptimizationMethod,
        errorAccept: float,
        useMaxError: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
        parametersGuess: list[list[Handle[Quote]]],
        isParameterFixed: list[bool],
        isAtmCalibrated: bool,
        endCriteria: EndCriteria,
        maxErrorTolerance: float,
        optMethod: OptimizationMethod,
        errorAccept: float,
        useMaxError: bool,
        maxGuesses: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
        parametersGuess: list[list[Handle[Quote]]],
        isParameterFixed: list[bool],
        isAtmCalibrated: bool,
        endCriteria: EndCriteria,
        maxErrorTolerance: float,
        optMethod: OptimizationMethod,
        errorAccept: float,
        useMaxError: bool,
        maxGuesses: int,
        backwardFlat: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
        parametersGuess: list[list[Handle[Quote]]],
        isParameterFixed: list[bool],
        isAtmCalibrated: bool,
        endCriteria: EndCriteria,
        maxErrorTolerance: float,
        optMethod: OptimizationMethod,
        errorAccept: float,
        useMaxError: bool,
        maxGuesses: int,
        backwardFlat: bool,
        cutoffStrike: float,
    ) -> None: ...
    def sparseSabrParameters(self) -> Matrix: ...
    def denseSabrParameters(self) -> Matrix: ...
    def marketVolCube(self) -> Matrix: ...
    def volCubeAtmCalibrated(self) -> Matrix: ...

class InterpolatedSwaptionVolatilityCube(SwaptionVolatilityCube):
    def __init__(
        self,
        atmVolStructure: Handle[SwaptionVolatilityStructure],
        optionTenors: list[Period],
        swapTenors: list[Period],
        strikeSpreads: list[float],
        volSpreads: list[list[Handle[Quote]]],
        swapIndex: SwapIndex,
        shortSwapIndex: SwapIndex,
        vegaWeightedSmileFit: bool,
    ) -> None: ...

class SpreadedSwaptionVolatility(SwaptionVolatilityStructure):
    def __init__(
        self,
        arg0: Handle[SwaptionVolatilityStructure],
        spread: Handle[Quote],
    ) -> None: ...

class ConstantYoYOptionletVolatility(YoYOptionletVolatilitySurface):
    @overload
    def __init__(
        self,
        volatility: float,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        dc: DayCounter,
        observationLag: Period,
        frequency: Frequency,
        indexIsInterpolated: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        volatility: float,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        dc: DayCounter,
        observationLag: Period,
        frequency: Frequency,
        indexIsInterpolated: bool,
        minStrike: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        volatility: float,
        settlementDays: int,
        cal: Calendar,
        bdc: BusinessDayConvention,
        dc: DayCounter,
        observationLag: Period,
        frequency: Frequency,
        indexIsInterpolated: bool,
        minStrike: float,
        maxStrike: float,
    ) -> None: ...

class FlatSmileSection(SmileSection):
    @overload
    def __init__(
        self,
        d: Date,
        vol: float,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        vol: float,
        dc: DayCounter,
        referenceDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        vol: float,
        dc: DayCounter,
        referenceDate: Date,
        atmLevel: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        vol: float,
        dc: DayCounter,
        referenceDate: Date,
        atmLevel: float,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        vol: float,
        dc: DayCounter,
        referenceDate: Date,
        atmLevel: float,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseTime: float,
        vol: float,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseTime: float,
        vol: float,
        dc: DayCounter,
        atmLevel: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseTime: float,
        vol: float,
        dc: DayCounter,
        atmLevel: float,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseTime: float,
        vol: float,
        dc: DayCounter,
        atmLevel: float,
        type: VolatilityType,
        shift: float,
    ) -> None: ...

class KahaleSmileSection(SmileSection):
    @overload
    def __init__(
        self,
        source: SmileSection,
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: SmileSection,
        atm: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: SmileSection,
        atm: float,
        interpolate: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: SmileSection,
        atm: float,
        interpolate: bool,
        exponentialExtrapolation: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: SmileSection,
        atm: float,
        interpolate: bool,
        exponentialExtrapolation: bool,
        deleteArbitragePoints: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: SmileSection,
        atm: float,
        interpolate: bool,
        exponentialExtrapolation: bool,
        deleteArbitragePoints: bool,
        moneynessGrid: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: SmileSection,
        atm: float,
        interpolate: bool,
        exponentialExtrapolation: bool,
        deleteArbitragePoints: bool,
        moneynessGrid: list[float],
        gap: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: SmileSection,
        atm: float,
        interpolate: bool,
        exponentialExtrapolation: bool,
        deleteArbitragePoints: bool,
        moneynessGrid: list[float],
        gap: float,
        forcedLeftIndex: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: SmileSection,
        atm: float,
        interpolate: bool,
        exponentialExtrapolation: bool,
        deleteArbitragePoints: bool,
        moneynessGrid: list[float],
        gap: float,
        forcedLeftIndex: int,
        forcedRightIndex: int,
    ) -> None: ...

class ZabrShortMaturityLognormal:
    def __init__(self) -> None: ...

class ZabrShortMaturityNormal:
    def __init__(self) -> None: ...

class ZabrLocalVolatility:
    def __init__(self) -> None: ...

class ZabrFullFd:
    def __init__(self) -> None: ...

class NoArbSabrSmileSection(SmileSection):
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sabrParameters: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sabrParameters: list[float],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sabrParameters: list[float],
        dc: DayCounter,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: Date,
        forward: float,
        sabrParameters: list[float],
        dc: DayCounter,
        shift: float,
        volatilityType: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeToExpiry: float,
        forward: float,
        sabrParameters: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeToExpiry: float,
        forward: float,
        sabrParameters: list[float],
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeToExpiry: float,
        forward: float,
        sabrParameters: list[float],
        shift: float,
        volatilityType: VolatilityType,
    ) -> None: ...

class NoArbSabrInterpolatedSmileSection(SmileSection):
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
        vegaWeighted: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: Handle[Quote],
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: Handle[Quote],
        volHandles: list[Handle[Quote]],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
        vegaWeighted: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        optionDate: Date,
        forward: float,
        strikes: list[float],
        hasFloatingStrikes: bool,
        atmVolatility: float,
        vols: list[float],
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        isAlphaFixed: bool,
        isBetaFixed: bool,
        isNuFixed: bool,
        isRhoFixed: bool,
        vegaWeighted: bool,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
        dc: DayCounter,
    ) -> None: ...
    def alpha(self) -> float: ...
    def beta(self) -> float: ...
    def nu(self) -> float: ...
    def rho(self) -> float: ...
    def rmsError(self) -> float: ...
    def maxError(self) -> float: ...
    def endCriteria(self) -> EndCriteria.Type: ...

class AndreasenHugeVolatilityInterpl(Observable):
    class InterpolationType(IntEnum):
        PiecewiseConstant
        Linear
        CubicSpline

    class CalibrationType(IntEnum):
        Call = 1
        Put = -1
        CallPut

    @overload
    def __init__(
        self,
        calibrationSet: AndreasenHugeVolatilityInterpl.CalibrationSet,
        spot: Handle[Quote],
        rTS: Handle[YieldTermStructure],
        qTS: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        calibrationSet: AndreasenHugeVolatilityInterpl.CalibrationSet,
        spot: Handle[Quote],
        rTS: Handle[YieldTermStructure],
        qTS: Handle[YieldTermStructure],
        interpolationType: AndreasenHugeVolatilityInterpl.InterpolationType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calibrationSet: AndreasenHugeVolatilityInterpl.CalibrationSet,
        spot: Handle[Quote],
        rTS: Handle[YieldTermStructure],
        qTS: Handle[YieldTermStructure],
        interpolationType: AndreasenHugeVolatilityInterpl.InterpolationType,
        calibrationType: AndreasenHugeVolatilityInterpl.CalibrationType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calibrationSet: AndreasenHugeVolatilityInterpl.CalibrationSet,
        spot: Handle[Quote],
        rTS: Handle[YieldTermStructure],
        qTS: Handle[YieldTermStructure],
        interpolationType: AndreasenHugeVolatilityInterpl.InterpolationType,
        calibrationType: AndreasenHugeVolatilityInterpl.CalibrationType,
        nGridPoints: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calibrationSet: AndreasenHugeVolatilityInterpl.CalibrationSet,
        spot: Handle[Quote],
        rTS: Handle[YieldTermStructure],
        qTS: Handle[YieldTermStructure],
        interpolationType: AndreasenHugeVolatilityInterpl.InterpolationType,
        calibrationType: AndreasenHugeVolatilityInterpl.CalibrationType,
        nGridPoints: int,
        minStrike: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calibrationSet: AndreasenHugeVolatilityInterpl.CalibrationSet,
        spot: Handle[Quote],
        rTS: Handle[YieldTermStructure],
        qTS: Handle[YieldTermStructure],
        interpolationType: AndreasenHugeVolatilityInterpl.InterpolationType,
        calibrationType: AndreasenHugeVolatilityInterpl.CalibrationType,
        nGridPoints: int,
        minStrike: float,
        maxStrike: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calibrationSet: AndreasenHugeVolatilityInterpl.CalibrationSet,
        spot: Handle[Quote],
        rTS: Handle[YieldTermStructure],
        qTS: Handle[YieldTermStructure],
        interpolationType: AndreasenHugeVolatilityInterpl.InterpolationType,
        calibrationType: AndreasenHugeVolatilityInterpl.CalibrationType,
        nGridPoints: int,
        minStrike: float,
        maxStrike: float,
        optimizationMethod: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        calibrationSet: AndreasenHugeVolatilityInterpl.CalibrationSet,
        spot: Handle[Quote],
        rTS: Handle[YieldTermStructure],
        qTS: Handle[YieldTermStructure],
        interpolationType: AndreasenHugeVolatilityInterpl.InterpolationType,
        calibrationType: AndreasenHugeVolatilityInterpl.CalibrationType,
        nGridPoints: int,
        minStrike: float,
        maxStrike: float,
        optimizationMethod: OptimizationMethod,
        endCriteria: EndCriteria,
    ) -> None: ...
    def maxDate(self) -> Date: ...
    def minStrike(self) -> float: ...
    def maxStrike(self) -> float: ...
    def fwd(
        self,
        t: float,
    ) -> float: ...
    def riskFreeRate(self) -> Handle[YieldTermStructure]: ...
    def calibrationError(self) -> std.tuple[Real,Real,Real]: ...
    def optionPrice(
        self,
        t: float,
        strike: float,
        optionType: Option.Type,
    ) -> float: ...
    def localVol(
        self,
        t: float,
        strike: float,
    ) -> float: ...

class AndreasenHugeVolatilityAdapter(Any):
    @overload
    def __init__(
        self,
        volInterpl: AndreasenHugeVolatilityInterpl,
    ) -> None: ...
    @overload
    def __init__(
        self,
        volInterpl: AndreasenHugeVolatilityInterpl,
        eps: float,
    ) -> None: ...

class AndreasenHugeLocalVolAdapter(LocalVolTermStructure):
    def __init__(
        self,
        localVol: AndreasenHugeVolatilityInterpl,
    ) -> None: ...

class HestonBlackVolSurface(Any):
    @overload
    def __init__(
        self,
        hestonModel: Handle[HestonModel],
    ) -> None: ...
    @overload
    def __init__(
        self,
        hestonModel: Handle[HestonModel],
        cpxLogFormula: AnalyticHestonEngine.ComplexLogFormula,
    ) -> None: ...
    @overload
    def __init__(
        self,
        hestonModel: Handle[HestonModel],
        cpxLogFormula: AnalyticHestonEngine.ComplexLogFormula,
        integration: AnalyticHestonEngine.Integration,
    ) -> None: ...

class CmsMarket:
    def __init__(
        self,
        swapLengths: list[Period],
        swapIndexes: list[SwapIndex],
        iborIndex: IborIndex,
        bidAskSpreads: list[list[Handle[Quote]]],
        pricers: list[CmsCouponPricer],
        discountingTS: Handle[YieldTermStructure],
    ) -> None: ...
    def reprice(
        self,
        volStructure: Handle[SwaptionVolatilityStructure],
        meanReversion: float,
    ) -> None: ...
    def swapTenors(self) -> list[Period]: ...
    def swapLengths(self) -> list[Period]: ...
    def impliedCmsSpreads(self) -> Matrix: ...
    def spreadErrors(self) -> Matrix: ...
    def browse(self) -> Matrix: ...
    def weightedSpreadError(
        self,
        weights: Matrix,
    ) -> float: ...
    def weightedSpotNpvError(
        self,
        weights: Matrix,
    ) -> float: ...
    def weightedFwdNpvError(
        self,
        weights: Matrix,
    ) -> float: ...
    def weightedSpreadErrors(
        self,
        weights: Matrix,
    ) -> Array: ...
    def weightedSpotNpvErrors(
        self,
        weights: Matrix,
    ) -> Array: ...
    def weightedFwdNpvErrors(
        self,
        weights: Matrix,
    ) -> Array: ...

class CmsMarketCalibration:
    class CalibrationType(IntEnum):
        OnSpread
        OnPrice
        OnForwardCmsPrice

    def __init__(
        self,
        volCube: Handle[SwaptionVolatilityStructure],
        cmsMarket: CmsMarket,
        weights: Matrix,
        calibrationType: CmsMarketCalibration.CalibrationType,
    ) -> None: ...
    @overload
    def compute(
        self,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
        guess: Array,
        isMeanReversionFixed: bool,
    ) -> Array: ...
    @overload
    def compute(
        self,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
        guess: Matrix,
        isMeanReversionFixed: bool,
    ) -> Matrix: ...
    @overload
    def compute(
        self,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
        guess: Matrix,
        isMeanReversionFixed: bool,
        meanReversionGuess: float,
    ) -> Matrix: ...
    @overload
    def computeParametric(
        self,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
        guess: Matrix,
        isMeanReversionFixed: bool,
    ) -> Matrix: ...
    @overload
    def computeParametric(
        self,
        endCriteria: EndCriteria,
        method: OptimizationMethod,
        guess: Matrix,
        isMeanReversionFixed: bool,
        meanReversionGuess: float,
    ) -> Matrix: ...
    def error(self) -> float: ...
    def endCriteria(self) -> EndCriteria.Type: ...

class CashFlow(Observable):
    def __init__(self) -> None: ...
    def amount(self) -> float: ...
    def date(self) -> Date: ...
    @overload
    def hasOccurred(
        self,
        refDate: Date,
    ) -> bool: ...
    @overload
    def hasOccurred(self) -> bool: ...

class SimpleCashFlow(CashFlow):
    def __init__(
        self,
        amount: float,
        date: Date,
    ) -> None: ...

class Redemption(CashFlow):
    def __init__(
        self,
        amount: float,
        date: Date,
    ) -> None: ...

class AmortizingPayment(CashFlow):
    def __init__(
        self,
        amount: float,
        date: Date,
    ) -> None: ...

class IndexedCashFlow(CashFlow):
    @overload
    def __init__(
        self,
        notional: float,
        index: Index,
        baseDate: Date,
        fixingDate: Date,
        paymentDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        notional: float,
        index: Index,
        baseDate: Date,
        fixingDate: Date,
        paymentDate: Date,
        growthOnly: bool,
    ) -> None: ...
    def notional(self) -> float: ...
    def baseDate(self) -> Date: ...
    def fixingDate(self) -> Date: ...
    def baseFixing(self) -> float: ...
    def indexFixing(self) -> float: ...
    def index(self) -> Index: ...
    def growthOnly(self) -> bool: ...

class Coupon(CashFlow):
    def __init__(self) -> None: ...
    def nominal(self) -> float: ...
    def accrualStartDate(self) -> Date: ...
    def accrualEndDate(self) -> Date: ...
    def referencePeriodStart(self) -> Date: ...
    def referencePeriodEnd(self) -> Date: ...
    def exCouponDate(self) -> Date: ...
    def rate(self) -> float: ...
    def accrualPeriod(self) -> float: ...
    def accrualDays(self) -> int: ...
    def dayCounter(self) -> DayCounter: ...
    def accruedAmount(
        self,
        date: Date,
    ) -> float: ...

class FixedRateCoupon(Coupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        rate: float,
        dayCounter: DayCounter,
        startDate: Date,
        endDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        rate: float,
        dayCounter: DayCounter,
        startDate: Date,
        endDate: Date,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        rate: float,
        dayCounter: DayCounter,
        startDate: Date,
        endDate: Date,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        rate: float,
        dayCounter: DayCounter,
        startDate: Date,
        endDate: Date,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        exCouponDate: Date,
    ) -> None: ...
    def interestRate(self) -> InterestRate: ...

class FloatingRateCouponPricer:
    def __init__(self) -> None: ...
    def swapletPrice(self) -> float: ...
    def swapletRate(self) -> float: ...
    def capletPrice(
        self,
        effectiveCap: float,
    ) -> float: ...
    def capletRate(
        self,
        effectiveCap: float,
    ) -> float: ...
    def floorletPrice(
        self,
        effectiveFloor: float,
    ) -> float: ...
    def floorletRate(
        self,
        effectiveFloor: float,
    ) -> float: ...

class FloatingRateCoupon(Coupon):
    def __init__(self) -> None: ...
    def fixingDate(self) -> Date: ...
    def fixingDays(self) -> int: ...
    def isInArrears(self) -> bool: ...
    def gearing(self) -> float: ...
    def spread(self) -> float: ...
    def indexFixing(self) -> float: ...
    def adjustedFixing(self) -> float: ...
    def convexityAdjustment(self) -> float: ...
    def price(
        self,
        discountCurve: Handle[YieldTermStructure],
    ) -> float: ...
    def index(self) -> InterestRateIndex: ...
    def setPricer(
        self,
        p: FloatingRateCouponPricer,
    ) -> None: ...

class RateAveraging:
    class Type(IntEnum):
        Simple
        Compound

    def __init__(self) -> None: ...

class OvernightIndexedCoupon(FloatingRateCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        telescopicValueDates: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
        lockoutDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        overnightIndex: OvernightIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
    ) -> None: ...
    def fixingDates(self) -> list[Date]: ...
    def interestDates(self) -> list[Date]: ...
    def dt(self) -> list[float]: ...
    def indexFixings(self) -> list[float]: ...
    def valueDates(self) -> list[Date]: ...
    def averagingMethod(self) -> RateAveraging.Type: ...
    def lockoutDays(self) -> int: ...
    def applyObservationShift(self) -> bool: ...
    def canApplyTelescopicFormula(self) -> bool: ...

class CappedFlooredCoupon(FloatingRateCoupon):
    @overload
    def __init__(
        self,
        underlying: FloatingRateCoupon,
    ) -> None: ...
    @overload
    def __init__(
        self,
        underlying: FloatingRateCoupon,
        cap: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        underlying: FloatingRateCoupon,
        cap: float,
        floor: float,
    ) -> None: ...
    def cap(self) -> float: ...
    def floor(self) -> float: ...
    def effectiveCap(self) -> float: ...
    def effectiveFloor(self) -> float: ...
    def isCapped(self) -> bool: ...
    def isFloored(self) -> bool: ...
    def setPricer(
        self,
        p: FloatingRateCouponPricer,
    ) -> None: ...

class IborCoupon(FloatingRateCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
        exCouponDate: Date,
    ) -> None: ...
    def hasFixed(self) -> bool: ...

class CappedFlooredIborCoupon(CappedFlooredCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        cap: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
        exCouponDate: Date,
    ) -> None: ...

class MultipleResetsCoupon(FloatingRateCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        resetSchedule: Schedule,
        fixingDays: int,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        resetSchedule: Schedule,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        resetSchedule: Schedule,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        resetSchedule: Schedule,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        resetSchedule: Schedule,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        resetSchedule: Schedule,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        resetSchedule: Schedule,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        resetSchedule: Schedule,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        exCouponDate: Date,
    ) -> None: ...
    def fixingDates(self) -> list[Date]: ...
    def dt(self) -> list[float]: ...
    def valueDates(self) -> list[Date]: ...
    def rateSpread(self) -> float: ...

class SubPeriodsCoupon(FloatingRateCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: IborIndex,
        gearing: float,
        couponSpread: float,
        rateSpread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        exCouponDate: Date,
    ) -> None: ...
    def fixingDates(self) -> list[Date]: ...
    def dt(self) -> list[float]: ...
    def valueDates(self) -> list[Date]: ...
    def rateSpread(self) -> float: ...

class IborCouponPricer(FloatingRateCouponPricer):
    def __init__(self) -> None: ...
    def capletVolatility(self) -> Handle[OptionletVolatilityStructure]: ...
    @overload
    def setCapletVolatility(
        self,
        v: Handle[OptionletVolatilityStructure],
    ) -> None: ...
    @overload
    def setCapletVolatility(self) -> None: ...

class BlackIborCouponPricer(IborCouponPricer):
    class TimingAdjustment(IntEnum):
        Black76
        BivariateLognormal

    @overload
    def __init__(
        self,
        v: Handle[OptionletVolatilityStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        v: Handle[OptionletVolatilityStructure],
        timingAdjustment: BlackIborCouponPricer.TimingAdjustment,
    ) -> None: ...
    @overload
    def __init__(
        self,
        v: Handle[OptionletVolatilityStructure],
        timingAdjustment: BlackIborCouponPricer.TimingAdjustment,
        correlation: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        v: Handle[OptionletVolatilityStructure],
        timingAdjustment: BlackIborCouponPricer.TimingAdjustment,
        correlation: Handle[Quote],
        useIndexedCoupon: Optional[bool],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SubPeriodsPricer(FloatingRateCouponPricer):
    def __init__(self) -> None: ...

class CompoundingOvernightIndexedCouponPricer(FloatingRateCouponPricer):
    def __init__(self) -> None: ...

class ArithmeticAveragedOvernightIndexedCouponPricer(FloatingRateCouponPricer):
    @overload
    def __init__(
        self,
        meanReversion: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        meanReversion: float,
        volatility: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        meanReversion: float,
        volatility: float,
        byApprox: bool,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class CompoundingMultipleResetsPricer(FloatingRateCouponPricer):
    pass

class AveragingMultipleResetsPricer(FloatingRateCouponPricer):
    pass

class CompoundingRatePricer(SubPeriodsPricer):
    def __init__(self) -> None: ...

class AveragingRatePricer(SubPeriodsPricer):
    def __init__(self) -> None: ...

class CmsCoupon(FloatingRateCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
        exCouponDate: Date,
    ) -> None: ...

class CmsSpreadCoupon(FloatingRateCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
        exCouponDate: Date,
    ) -> None: ...

class CmsCouponPricer(FloatingRateCouponPricer):
    def __init__(self) -> None: ...
    def swaptionVolatility(self) -> Handle[SwaptionVolatilityStructure]: ...
    @overload
    def setSwaptionVolatility(
        self,
        v: Handle[SwaptionVolatilityStructure],
    ) -> None: ...
    @overload
    def setSwaptionVolatility(self) -> None: ...

class GFunctionFactory:
    class YieldCurveModel(IntEnum):
        Standard
        ExactYield
        ParallelShifts
        NonParallelShifts

    def __init__(self) -> None: ...

class AnalyticHaganPricer(CmsCouponPricer):
    def __init__(
        self,
        v: Handle[SwaptionVolatilityStructure],
        model: GFunctionFactory.YieldCurveModel,
        meanReversion: Handle[Quote],
    ) -> None: ...

class NumericHaganPricer(CmsCouponPricer):
    @overload
    def __init__(
        self,
        v: Handle[SwaptionVolatilityStructure],
        model: GFunctionFactory.YieldCurveModel,
        meanReversion: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        v: Handle[SwaptionVolatilityStructure],
        model: GFunctionFactory.YieldCurveModel,
        meanReversion: Handle[Quote],
        lowerLimit: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        v: Handle[SwaptionVolatilityStructure],
        model: GFunctionFactory.YieldCurveModel,
        meanReversion: Handle[Quote],
        lowerLimit: float,
        upperLimit: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        v: Handle[SwaptionVolatilityStructure],
        model: GFunctionFactory.YieldCurveModel,
        meanReversion: Handle[Quote],
        lowerLimit: float,
        upperLimit: float,
        precision: float,
    ) -> None: ...

class CappedFlooredCmsCoupon(CappedFlooredCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        cap: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
        exCouponDate: Date,
    ) -> None: ...

class CappedFlooredCmsSpreadCoupon(CappedFlooredCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        cap: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: SwapSpreadIndex,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        dayCounter: DayCounter,
        isInArrears: bool,
        exCouponDate: Date,
    ) -> None: ...

class LinearTsrPricer(CmsCouponPricer):
    @overload
    def __init__(
        self,
        swaptionVol: Handle[SwaptionVolatilityStructure],
        meanReversion: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        swaptionVol: Handle[SwaptionVolatilityStructure],
        meanReversion: Handle[Quote],
        couponDiscountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        swaptionVol: Handle[SwaptionVolatilityStructure],
        meanReversion: Handle[Quote],
        couponDiscountCurve: Handle[YieldTermStructure],
        settings: LinearTsrPricer.Settings,
    ) -> None: ...

class Settings:
    class Strategy(IntEnum):
        RateBound
        VegaRatio
        PriceThreshold
        BSStdDevs

    def __init__(self) -> None: ...
    @overload
    def withRateBound(
        self,
        lowerRateBound: float,
    ) -> LinearTsrPricer.Settings: ...
    @overload
    def withRateBound(
        self,
        lowerRateBound: float,
        upperRateBound: float,
    ) -> LinearTsrPricer.Settings: ...
    @overload
    def withRateBound(self) -> LinearTsrPricer.Settings: ...
    @overload
    def withVegaRatio(
        self,
        vegaRatio: float,
    ) -> LinearTsrPricer.Settings: ...
    @overload
    def withVegaRatio(
        self,
        vegaRatio: float,
        lowerRateBound: float,
        upperRateBound: float,
    ) -> LinearTsrPricer.Settings: ...
    @overload
    def withVegaRatio(self) -> LinearTsrPricer.Settings: ...
    @overload
    def withPriceThreshold(
        self,
        priceThreshold: float,
    ) -> LinearTsrPricer.Settings: ...
    @overload
    def withPriceThreshold(
        self,
        priceThreshold: float,
        lowerRateBound: float,
        upperRateBound: float,
    ) -> LinearTsrPricer.Settings: ...
    @overload
    def withPriceThreshold(self) -> LinearTsrPricer.Settings: ...
    @overload
    def withBSStdDevs(
        self,
        stdDevs: float,
    ) -> LinearTsrPricer.Settings: ...
    @overload
    def withBSStdDevs(
        self,
        stdDevs: float,
        lowerRateBound: float,
        upperRateBound: float,
    ) -> LinearTsrPricer.Settings: ...
    @overload
    def withBSStdDevs(self) -> LinearTsrPricer.Settings: ...

class CmsSpreadCouponPricer(FloatingRateCouponPricer):
    def __init__(self) -> None: ...
    def correlation(self) -> Handle[Quote]: ...
    @overload
    def setCorrelation(
        self,
        correlation: Handle[Quote],
    ) -> None: ...
    @overload
    def setCorrelation(self) -> None: ...

class LognormalCmsSpreadPricer(CmsSpreadCouponPricer):
    @overload
    def __init__(
        self,
        cmsPricer: CmsCouponPricer,
        correlation: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        cmsPricer: CmsCouponPricer,
        correlation: Handle[Quote],
        couponDiscountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        cmsPricer: CmsCouponPricer,
        correlation: Handle[Quote],
        couponDiscountCurve: Handle[YieldTermStructure],
        IntegrationPoints: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cmsPricer: CmsCouponPricer,
        correlation: Handle[Quote],
        couponDiscountCurve: Handle[YieldTermStructure],
        IntegrationPoints: int,
        volatilityType: Optional[VolatilityType],
    ) -> None: ...
    @overload
    def __init__(
        self,
        cmsPricer: CmsCouponPricer,
        correlation: Handle[Quote],
        couponDiscountCurve: Handle[YieldTermStructure],
        IntegrationPoints: int,
        volatilityType: Optional[VolatilityType],
        shift1: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cmsPricer: CmsCouponPricer,
        correlation: Handle[Quote],
        couponDiscountCurve: Handle[YieldTermStructure],
        IntegrationPoints: int,
        volatilityType: Optional[VolatilityType],
        shift1: float,
        shift2: float,
    ) -> None: ...
    def swapletPrice(self) -> float: ...
    def swapletRate(self) -> float: ...
    def capletPrice(
        self,
        effectiveCap: float,
    ) -> float: ...
    def capletRate(
        self,
        effectiveCap: float,
    ) -> float: ...
    def floorletPrice(
        self,
        effectiveFloor: float,
    ) -> float: ...
    def floorletRate(
        self,
        effectiveFloor: float,
    ) -> float: ...

class EquityCashFlowPricer:
    def __init__(self) -> None: ...

class EquityCashFlow(IndexedCashFlow):
    @overload
    def __init__(
        self,
        notional: float,
        index: EquityIndex,
        baseDate: Date,
        fixingDate: Date,
        paymentDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        notional: float,
        index: EquityIndex,
        baseDate: Date,
        fixingDate: Date,
        paymentDate: Date,
        growthOnly: bool,
    ) -> None: ...
    def setPricer(
        self,
        arg0: EquityCashFlowPricer,
    ) -> None: ...

class EquityQuantoCashFlowPricer(EquityCashFlowPricer):
    def __init__(
        self,
        quantoCurrencyTermStructure: Handle[YieldTermStructure],
        equityVolatility: Handle[Any],
        fxVolatility: Handle[Any],
        correlation: Handle[Quote],
    ) -> None: ...

class RangeAccrualFloatersCoupon(FloatingRateCoupon):
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        index: IborIndex,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        dayCounter: DayCounter,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        observationsSchedule: Schedule,
        lowerTrigger: float,
        upperTrigger: float,
    ) -> None: ...

class RangeAccrualPricer(FloatingRateCouponPricer):
    pass

class RangeAccrualPricerByBgm(RangeAccrualPricer):
    def __init__(
        self,
        correlation: float,
        smilesOnExpiry: SmileSection,
        smilesOnPayment: SmileSection,
        withSmile: bool,
        byCallSpread: bool,
    ) -> None: ...

class Duration:
    class Type(IntEnum):
        Simple
        Macaulay
        Modified

    def __init__(self) -> None: ...

class CashFlows:
    @overload
    def __init__(
        self,
        arg0: CashFlows,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def startDate(
        self,
        arg0: Leg,
    ) -> Date: ...
    def maturityDate(
        self,
        arg0: Leg,
    ) -> Date: ...
    @overload
    def previousCashFlowDate(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
    ) -> Date: ...
    @overload
    def previousCashFlowDate(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> Date: ...
    @overload
    def nextCashFlowDate(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
    ) -> Date: ...
    @overload
    def nextCashFlowDate(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> Date: ...
    @overload
    def previousCashFlowAmount(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def previousCashFlowAmount(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def nextCashFlowAmount(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def nextCashFlowAmount(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def accrualPeriod(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def accrualPeriod(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def accrualDays(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
    ) -> int: ...
    @overload
    def accrualDays(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> int: ...
    @overload
    def accruedPeriod(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def accruedPeriod(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def accruedDays(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
    ) -> int: ...
    @overload
    def accruedDays(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> int: ...
    @overload
    def accruedAmount(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def accruedAmount(
        self,
        leg: Leg,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def npv(
        self,
        arg0: Leg,
        arg1: InterestRate,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def npv(
        self,
        arg0: Leg,
        arg1: InterestRate,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def npv(
        self,
        arg0: Leg,
        arg1: InterestRate,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def npv(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def npv(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def npv(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def bps(
        self,
        arg0: Leg,
        arg1: InterestRate,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def bps(
        self,
        arg0: Leg,
        arg1: InterestRate,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def bps(
        self,
        arg0: Leg,
        arg1: InterestRate,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def bps(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def bps(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def bps(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def yield_(
        self,
        arg0: Leg,
        npv: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def yield_(
        self,
        arg0: Leg,
        npv: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def yield_(
        self,
        arg0: Leg,
        npv: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def yield_(
        self,
        arg0: Leg,
        npv: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
        accuracy: float,
    ) -> float: ...
    @overload
    def yield_(
        self,
        arg0: Leg,
        npv: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
        accuracy: float,
        maxIterations: int,
    ) -> float: ...
    @overload
    def yield_(
        self,
        arg0: Leg,
        npv: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
        accuracy: float,
        maxIterations: int,
        guess: float,
    ) -> float: ...
    @overload
    def duration(
        self,
        arg0: Leg,
        arg1: InterestRate,
        type: Duration.Type,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def duration(
        self,
        arg0: Leg,
        arg1: InterestRate,
        type: Duration.Type,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def duration(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        type: Duration.Type,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def duration(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        type: Duration.Type,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def duration(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        type: Duration.Type,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def convexity(
        self,
        arg0: Leg,
        arg1: InterestRate,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def convexity(
        self,
        arg0: Leg,
        arg1: InterestRate,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def convexity(
        self,
        arg0: Leg,
        arg1: InterestRate,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def convexity(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def convexity(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def convexity(
        self,
        arg0: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        leg: Leg,
        yield_: InterestRate,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        leg: Leg,
        yield_: InterestRate,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        leg: Leg,
        yield_: InterestRate,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        leg: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        leg: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        leg: Leg,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        leg: Leg,
        npv: float,
        arg2: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        leg: Leg,
        npv: float,
        arg2: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        leg: Leg,
        npv: float,
        arg2: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        leg: Leg,
        npv: float,
        arg2: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
        accuracy: float,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        leg: Leg,
        npv: float,
        arg2: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
        accuracy: float,
        maxIterations: int,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        leg: Leg,
        npv: float,
        arg2: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
        accuracy: float,
        maxIterations: int,
        guess: float,
    ) -> float: ...

class Dividend(CashFlow):
    def __init__(self) -> None: ...

class FixedDividend(Dividend):
    def __init__(
        self,
        amount: float,
        date: Date,
    ) -> None: ...

class FractionalDividend(Dividend):
    def __init__(
        self,
        rate: float,
        date: Date,
    ) -> None: ...

class Exercise:
    class Type(IntEnum):
        American
        Bermudan
        European

    def __init__(
        self,
        type: Exercise.Type,
    ) -> None: ...
    def type(self) -> Exercise.Type: ...
    def date(
        self,
        index: int,
    ) -> Date: ...
    def dateAt(
        self,
        index: int,
    ) -> Date: ...
    def dates(self) -> list[Date]: ...
    def lastDate(self) -> Date: ...

class EuropeanExercise(Exercise):
    def __init__(
        self,
        date: Date,
    ) -> None: ...

class AmericanExercise(Exercise):
    @overload
    def __init__(
        self,
        earliestDate: Date,
        latestDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        earliestDate: Date,
        latestDate: Date,
        payoffAtExpiry: bool,
    ) -> None: ...

class BermudanExercise(Exercise):
    @overload
    def __init__(
        self,
        dates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        dates: list[Date],
        payoffAtExpiry: bool,
    ) -> None: ...

class RebatedExercise(Exercise):
    @overload
    def __init__(
        self,
        exercise: Exercise,
        rebates: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        rebates: list[float],
        rebateSettlementDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        rebates: list[float],
        rebateSettlementDays: int,
        rebatePaymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        rebates: list[float],
        rebateSettlementDays: int,
        rebatePaymentCalendar: Calendar,
        rebatePaymentConvention: BusinessDayConvention,
    ) -> None: ...

class SwingExercise(Exercise):
    def __init__(
        self,
        dates: list[Date],
    ) -> None: ...

class TimeGrid:
    @overload
    def __init__(
        self,
        end: float,
        steps: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def size(self) -> int: ...

class StochasticProcess(Observable):
    def __init__(self) -> None: ...
    def size(self) -> int: ...
    def factors(self) -> int: ...
    def initialValues(self) -> Array: ...
    def drift(
        self,
        t: float,
        x: Array,
    ) -> Array: ...
    def diffusion(
        self,
        t: float,
        x: Array,
    ) -> Matrix: ...
    def expectation(
        self,
        t0: float,
        x0: Array,
        dt: float,
    ) -> Array: ...
    def stdDeviation(
        self,
        t0: float,
        x0: Array,
        dt: float,
    ) -> Matrix: ...
    def covariance(
        self,
        t0: float,
        x0: Array,
        dt: float,
    ) -> Matrix: ...
    def evolve(
        self,
        t0: float,
        x0: Array,
        dt: float,
        dw: Array,
    ) -> Array: ...

class StochasticProcess1D(StochasticProcess):
    def x0(self) -> float: ...
    def drift(
        self,
        t: float,
        x: float,
    ) -> float: ...
    def diffusion(
        self,
        t: float,
        x: float,
    ) -> float: ...
    def expectation(
        self,
        t0: float,
        x0: float,
        dt: float,
    ) -> float: ...
    def stdDeviation(
        self,
        t0: float,
        x0: float,
        dt: float,
    ) -> float: ...
    def variance(
        self,
        t0: float,
        x0: float,
        dt: float,
    ) -> float: ...
    def evolve(
        self,
        t0: float,
        x0: float,
        dt: float,
        dw: float,
    ) -> float: ...
    def apply(
        self,
        x0: float,
        dx: float,
    ) -> float: ...

class GeneralizedBlackScholesProcess(StochasticProcess1D):
    @overload
    def __init__(
        self,
        s0: Handle[Quote],
        dividendTS: Handle[YieldTermStructure],
        riskFreeTS: Handle[YieldTermStructure],
        volTS: Handle[Any],
    ) -> None: ...
    @overload
    def __init__(
        self,
        x0: Handle[Quote],
        dividendTS: Handle[YieldTermStructure],
        riskFreeTS: Handle[YieldTermStructure],
        blackVolTS: Handle[Any],
        localVolTS: Handle[LocalVolTermStructure],
    ) -> None: ...
    def stateVariable(self) -> Handle[Quote]: ...
    def dividendYield(self) -> Handle[YieldTermStructure]: ...
    def riskFreeRate(self) -> Handle[YieldTermStructure]: ...
    def blackVolatility(self) -> Handle[Any]: ...
    def localVolatility(self) -> Handle[LocalVolTermStructure]: ...

class BlackScholesProcess(GeneralizedBlackScholesProcess):
    def __init__(
        self,
        s0: Handle[Quote],
        riskFreeTS: Handle[YieldTermStructure],
        volTS: Handle[Any],
    ) -> None: ...

class BlackScholesMertonProcess(GeneralizedBlackScholesProcess):
    def __init__(
        self,
        s0: Handle[Quote],
        dividendTS: Handle[YieldTermStructure],
        riskFreeTS: Handle[YieldTermStructure],
        volTS: Handle[Any],
    ) -> None: ...

class BlackProcess(GeneralizedBlackScholesProcess):
    def __init__(
        self,
        s0: Handle[Quote],
        riskFreeTS: Handle[YieldTermStructure],
        volTS: Handle[Any],
    ) -> None: ...

class GarmanKohlagenProcess(GeneralizedBlackScholesProcess):
    def __init__(
        self,
        s0: Handle[Quote],
        foreignRiskFreeTS: Handle[YieldTermStructure],
        domesticRiskFreeTS: Handle[YieldTermStructure],
        volTS: Handle[Any],
    ) -> None: ...

class Merton76Process(StochasticProcess1D):
    def __init__(
        self,
        stateVariable: Handle[Quote],
        dividendTS: Handle[YieldTermStructure],
        riskFreeTS: Handle[YieldTermStructure],
        volTS: Handle[Any],
        jumpIntensity: Handle[Quote],
        meanLogJump: Handle[Quote],
        jumpVolatility: Handle[Quote],
    ) -> None: ...

class StochasticProcessArray(StochasticProcess):
    def __init__(
        self,
        array: list[StochasticProcess1D],
        correlation: Matrix,
    ) -> None: ...

class GeometricBrownianMotionProcess(StochasticProcess1D):
    def __init__(
        self,
        initialValue: float,
        mu: float,
        sigma: float,
    ) -> None: ...

class VarianceGammaProcess(StochasticProcess1D):
    def __init__(
        self,
        s0: Handle[Quote],
        dividendYield: Handle[YieldTermStructure],
        riskFreeRate: Handle[YieldTermStructure],
        sigma: float,
        nu: float,
        theta: float,
    ) -> None: ...

class HestonProcess(StochasticProcess):
    class Discretization(IntEnum):
        PartialTruncation
        FullTruncation
        Reflection
        NonCentralChiSquareVariance
        QuadraticExponential
        QuadraticExponentialMartingale
        BroadieKayaExactSchemeLobatto
        BroadieKayaExactSchemeLaguerre
        BroadieKayaExactSchemeTrapezoidal

    @overload
    def __init__(
        self,
        riskFreeTS: Handle[YieldTermStructure],
        dividendTS: Handle[YieldTermStructure],
        s0: Handle[Quote],
        v0: float,
        kappa: float,
        theta: float,
        sigma: float,
        rho: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        riskFreeTS: Handle[YieldTermStructure],
        dividendTS: Handle[YieldTermStructure],
        s0: Handle[Quote],
        v0: float,
        kappa: float,
        theta: float,
        sigma: float,
        rho: float,
        d: HestonProcess.Discretization,
    ) -> None: ...
    def s0(self) -> Handle[Quote]: ...
    def dividendYield(self) -> Handle[YieldTermStructure]: ...
    def riskFreeRate(self) -> Handle[YieldTermStructure]: ...

class BatesProcess(HestonProcess):
    def __init__(
        self,
        riskFreeRate: Handle[YieldTermStructure],
        dividendYield: Handle[YieldTermStructure],
        s0: Handle[Quote],
        v0: float,
        kappa: float,
        theta: float,
        sigma: float,
        rho: float,
        lambda_: float,
        nu: float,
        delta: float,
    ) -> None: ...

class HullWhiteProcess(StochasticProcess1D):
    def __init__(
        self,
        riskFreeTS: Handle[YieldTermStructure],
        a: float,
        sigma: float,
    ) -> None: ...

class HullWhiteForwardProcess(StochasticProcess1D):
    def __init__(
        self,
        riskFreeTS: Handle[YieldTermStructure],
        a: float,
        sigma: float,
    ) -> None: ...
    def alpha(
        self,
        t: float,
    ) -> float: ...
    def M_T(
        self,
        s: float,
        t: float,
        T: float,
    ) -> float: ...
    def B(
        self,
        t: float,
        T: float,
    ) -> float: ...
    def setForwardMeasureTime(
        self,
        t: float,
    ) -> None: ...

class G2Process(StochasticProcess):
    def __init__(
        self,
        a: float,
        sigma: float,
        b: float,
        eta: float,
        rho: float,
    ) -> None: ...

class G2ForwardProcess(StochasticProcess):
    def __init__(
        self,
        a: float,
        sigma: float,
        b: float,
        eta: float,
        rho: float,
    ) -> None: ...
    def setForwardMeasureTime(
        self,
        t: float,
    ) -> None: ...

class GsrProcess(StochasticProcess1D):
    @overload
    def __init__(
        self,
        times: Array,
        vols: Array,
        reversions: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        times: Array,
        vols: Array,
        reversions: Array,
        T: float,
    ) -> None: ...
    def sigma(
        self,
        t: float,
    ) -> float: ...
    def reversion(
        self,
        t: float,
    ) -> float: ...
    def y(
        self,
        t: float,
    ) -> float: ...
    def G(
        self,
        t: float,
        T: float,
        x: float,
    ) -> float: ...
    def setForwardMeasureTime(
        self,
        t: float,
    ) -> None: ...

class OrnsteinUhlenbeckProcess(StochasticProcess1D):
    @overload
    def __init__(
        self,
        speed: float,
        vol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        speed: float,
        vol: float,
        x0: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        speed: float,
        vol: float,
        x0: float,
        level: float,
    ) -> None: ...
    def speed(self) -> float: ...
    def volatility(self) -> float: ...
    def level(self) -> float: ...

class ExtendedOrnsteinUhlenbeckProcess(StochasticProcess1D):
    class Discretization(IntEnum):
        MidPoint
        Trapezodial
        GaussLobatto


class ExtOUWithJumpsProcess(StochasticProcess):
    def __init__(
        self,
        process: ExtendedOrnsteinUhlenbeckProcess,
        Y0: float,
        beta: float,
        jumpIntensity: float,
        eta: float,
    ) -> None: ...

class KlugeExtOUProcess(StochasticProcess):
    def __init__(
        self,
        rho: float,
        kluge: ExtOUWithJumpsProcess,
        extOU: ExtendedOrnsteinUhlenbeckProcess,
    ) -> None: ...

class GJRGARCHProcess(StochasticProcess):
    class Discretization(IntEnum):
        PartialTruncation
        FullTruncation
        Reflection

    @overload
    def __init__(
        self,
        riskFreeRate: Handle[YieldTermStructure],
        dividendYield: Handle[YieldTermStructure],
        s0: Handle[Quote],
        v0: float,
        omega: float,
        alpha: float,
        beta: float,
        gamma: float,
        lambda_: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        riskFreeRate: Handle[YieldTermStructure],
        dividendYield: Handle[YieldTermStructure],
        s0: Handle[Quote],
        v0: float,
        omega: float,
        alpha: float,
        beta: float,
        gamma: float,
        lambda_: float,
        daysPerYear: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        riskFreeRate: Handle[YieldTermStructure],
        dividendYield: Handle[YieldTermStructure],
        s0: Handle[Quote],
        v0: float,
        omega: float,
        alpha: float,
        beta: float,
        gamma: float,
        lambda_: float,
        daysPerYear: float,
        d: GJRGARCHProcess.Discretization,
    ) -> None: ...
    def s0(self) -> Handle[Quote]: ...
    def dividendYield(self) -> Handle[YieldTermStructure]: ...
    def riskFreeRate(self) -> Handle[YieldTermStructure]: ...

class LazyObject(Observable):
    def __init__(self) -> None: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PricingEngine(Observable):
    def __init__(self) -> None: ...

class Instrument(LazyObject):
    def __init__(self) -> None: ...
    def NPV(self) -> float: ...
    def errorEstimate(self) -> float: ...
    def isExpired(self) -> bool: ...
    def setPricingEngine(
        self,
        arg0: PricingEngine,
    ) -> None: ...

class Stock(Instrument):
    def __init__(
        self,
        quote: Handle[Quote],
    ) -> None: ...

class CompositeInstrument(Instrument):
    def __init__(self) -> None: ...
    @overload
    def add(
        self,
        instrument: Instrument,
    ) -> None: ...
    @overload
    def add(
        self,
        instrument: Instrument,
        multiplier: float,
    ) -> None: ...
    @overload
    def subtract(
        self,
        instrument: Instrument,
    ) -> None: ...
    @overload
    def subtract(
        self,
        instrument: Instrument,
        multiplier: float,
    ) -> None: ...

class CalibrationHelper:
    def __init__(self) -> None: ...
    def calibrationError(self) -> float: ...

class CalibratedModel(Observable):
    def __init__(self) -> None: ...
    def params(self) -> Array: ...
    @overload
    def calibrate(
        self,
        arg0: list[CalibrationHelper],
        arg1: OptimizationMethod,
        arg2: EndCriteria,
    ) -> None: ...
    @overload
    def calibrate(
        self,
        arg0: list[CalibrationHelper],
        arg1: OptimizationMethod,
        arg2: EndCriteria,
        constraint: Constraint,
    ) -> None: ...
    @overload
    def calibrate(
        self,
        arg0: list[CalibrationHelper],
        arg1: OptimizationMethod,
        arg2: EndCriteria,
        constraint: Constraint,
        weights: list[float],
    ) -> None: ...
    @overload
    def calibrate(
        self,
        arg0: list[CalibrationHelper],
        arg1: OptimizationMethod,
        arg2: EndCriteria,
        constraint: Constraint,
        weights: list[float],
        fixParameters: list[bool],
    ) -> None: ...
    def setParams(
        self,
        params: Array,
    ) -> None: ...
    def value(
        self,
        params: Array,
        arg1: list[CalibrationHelper],
    ) -> float: ...
    def constraint(self) -> Constraint: ...
    def endCriteria(self) -> EndCriteria.Type: ...
    def problemValues(self) -> Array: ...
    def functionEvaluation(self) -> int: ...

class TermStructureConsistentModel(Observable):
    def __init__(self) -> None: ...
    def termStructure(self) -> Handle[YieldTermStructure]: ...

class Parameter:
    def __init__(self) -> None: ...
    def params(self) -> Array: ...
    def setParam(
        self,
        i: int,
        x: float,
    ) -> None: ...
    def testParams(
        self,
        params: Array,
    ) -> bool: ...
    def size(self) -> int: ...
    def __call__(
        self,
        t: float,
    ) -> float: ...
    def constraint(self) -> Constraint: ...

class ConstantParameter(Parameter):
    @overload
    def __init__(
        self,
        constraint: Constraint,
    ) -> None: ...
    @overload
    def __init__(
        self,
        value: float,
        constraint: Constraint,
    ) -> None: ...

class NullParameter(Parameter):
    def __init__(self) -> None: ...

class PiecewiseConstantParameter(Parameter):
    @overload
    def __init__(
        self,
        times: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        times: list[float],
        constraint: Constraint,
    ) -> None: ...

class Payoff:
    def __init__(self) -> None: ...
    def __call__(
        self,
        price: float,
    ) -> float: ...

class Option(Instrument):
    class Type(IntEnum):
        Put = -1
        Call = 1

    def __init__(self) -> None: ...
    def payoff(self) -> Payoff: ...
    def exercise(self) -> Exercise: ...

class TypePayoff(Payoff):
    def __init__(self) -> None: ...
    def optionType(self) -> Option.Type: ...

class FloatingTypePayoff(TypePayoff):
    def __init__(
        self,
        type: Option.Type,
    ) -> None: ...
    @overload
    def __call__(
        self,
        price: float,
    ) -> float: ...
    @overload
    def __call__(
        self,
        price: float,
        strike: float,
    ) -> float: ...

class StrikedTypePayoff(TypePayoff):
    def __init__(self) -> None: ...
    def strike(self) -> float: ...

class DeltaVolQuote(Quote):
    class DeltaType(IntEnum):
        Spot
        Fwd
        PaSpot
        PaFwd

    class AtmType(IntEnum):
        AtmNull
        AtmSpot
        AtmFwd
        AtmDeltaNeutral
        AtmVegaMax
        AtmGammaMax
        AtmPutCall50

    @overload
    def __init__(
        self,
        delta: float,
        vol: Handle[Quote],
        maturity: float,
        deltaType: DeltaVolQuote.DeltaType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        vol: Handle[Quote],
        deltaType: DeltaVolQuote.DeltaType,
        maturity: float,
        atmType: DeltaVolQuote.AtmType,
    ) -> None: ...
    def delta(self) -> float: ...
    def maturity(self) -> float: ...
    def atmType(self) -> DeltaVolQuote.AtmType: ...
    def deltaType(self) -> DeltaVolQuote.DeltaType: ...

class OneAssetOption(Option):
    def __init__(self) -> None: ...
    def delta(self) -> float: ...
    def deltaForward(self) -> float: ...
    def elasticity(self) -> float: ...
    def gamma(self) -> float: ...
    def theta(self) -> float: ...
    def thetaPerDay(self) -> float: ...
    def vega(self) -> float: ...
    def rho(self) -> float: ...
    def dividendRho(self) -> float: ...
    def strikeSensitivity(self) -> float: ...
    def itmCashProbability(self) -> float: ...

class VanillaOption(OneAssetOption):
    def __init__(
        self,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...

class EuropeanOption(VanillaOption):
    def __init__(
        self,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class ForwardVanillaOption(OneAssetOption):
    def __init__(
        self,
        moneyness: float,
        resetDate: Date,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class QuantoVanillaOption(OneAssetOption):
    def __init__(
        self,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...
    def qvega(self) -> float: ...
    def qrho(self) -> float: ...
    def qlambda(self) -> float: ...

class QuantoForwardVanillaOption(ForwardVanillaOption):
    def __init__(
        self,
        moneyness: float,
        resetDate: Date,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class MultiAssetOption(Option):
    def delta(self) -> float: ...
    def gamma(self) -> float: ...
    def theta(self) -> float: ...
    def vega(self) -> float: ...
    def rho(self) -> float: ...
    def dividendRho(self) -> float: ...

class AnalyticEuropeanEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...

class HestonModel(CalibratedModel):
    def __init__(
        self,
        process: HestonProcess,
    ) -> None: ...
    def theta(self) -> float: ...
    def kappa(self) -> float: ...
    def sigma(self) -> float: ...
    def rho(self) -> float: ...
    def v0(self) -> float: ...
    def process(self) -> HestonProcess: ...

class PiecewiseTimeDependentHestonModel(CalibratedModel):
    def __init__(
        self,
        riskFreeRate: Handle[YieldTermStructure],
        dividendYield: Handle[YieldTermStructure],
        s0: Handle[Quote],
        v0: float,
        theta: Parameter,
        kappa: Parameter,
        sigma: Parameter,
        rho: Parameter,
        timeGrid: TimeGrid,
    ) -> None: ...
    def theta(
        self,
        t: float,
    ) -> float: ...
    def kappa(
        self,
        t: float,
    ) -> float: ...
    def sigma(
        self,
        t: float,
    ) -> float: ...
    def rho(
        self,
        t: float,
    ) -> float: ...
    def v0(self) -> float: ...
    def s0(self) -> float: ...
    def timeGrid(self) -> TimeGrid: ...
    def dividendYield(self) -> Handle[YieldTermStructure]: ...
    def riskFreeRate(self) -> Handle[YieldTermStructure]: ...

class AnalyticHestonEngine(PricingEngine):
    class ComplexLogFormula(IntEnum):
        Gatheral
        BranchCorrection
        AndersenPiterbarg
        AndersenPiterbargOptCV
        AsymptoticChF
        AngledContour
        AngledContourNoCV
        OptimalCV

    @overload
    def __init__(
        self,
        model: HestonModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        cpxLog: AnalyticHestonEngine.ComplexLogFormula,
        itg: AnalyticHestonEngine.Integration,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        cpxLog: AnalyticHestonEngine.ComplexLogFormula,
        itg: AnalyticHestonEngine.Integration,
        andersenPiterbargEpsilon: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        integrationOrder: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        relTolerance: float,
        maxEvaluations: int,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...

class Integration:
    def __init__(self) -> None: ...
    @overload
    def gaussLaguerre(
        self,
        integrationOrder: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussLaguerre(self) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussLegendre(
        self,
        integrationOrder: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussLegendre(self) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussChebyshev(
        self,
        integrationOrder: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussChebyshev(self) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussChebyshev2nd(
        self,
        integrationOrder: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussChebyshev2nd(self) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussLobatto(
        self,
        relTolerance: float,
        absTolerance: float,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussLobatto(
        self,
        relTolerance: float,
        absTolerance: float,
        maxEvaluations: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussLobatto(
        self,
        relTolerance: float,
        absTolerance: float,
        maxEvaluations: int,
        useConvergenceEstimate: bool,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussKronrod(
        self,
        absTolerance: float,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def gaussKronrod(
        self,
        absTolerance: float,
        maxEvaluations: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def simpson(
        self,
        absTolerance: float,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def simpson(
        self,
        absTolerance: float,
        maxEvaluations: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def trapezoid(
        self,
        absTolerance: float,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def trapezoid(
        self,
        absTolerance: float,
        maxEvaluations: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def discreteSimpson(
        self,
        evaluation: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def discreteSimpson(self) -> AnalyticHestonEngine.Integration: ...
    @overload
    def discreteTrapezoid(
        self,
        evaluation: int,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def discreteTrapezoid(self) -> AnalyticHestonEngine.Integration: ...
    @overload
    def expSinh(
        self,
        relTolerance: float,
    ) -> AnalyticHestonEngine.Integration: ...
    @overload
    def expSinh(self) -> AnalyticHestonEngine.Integration: ...
    def andersenPiterbargIntegrationLimit(
        self,
        c_inf: float,
        epsilon: float,
        v0: float,
        t: float,
    ) -> float: ...
    def numberOfEvaluations(self) -> int: ...
    def isAdaptiveIntegration(self) -> bool: ...

class OptimalAlpha:
    def __call__(
        self,
        strike: float,
    ) -> float: ...
    def alphaGreaterZero(
        self,
        strike: float,
    ) -> tuple[Real,Real]: ...
    def alphaSmallerMinusOne(
        self,
        strike: float,
    ) -> tuple[Real,Real]: ...
    def numberOfEvaluations(self) -> int: ...
    def M(
        self,
        k: float,
    ) -> float: ...
    def k(
        self,
        x: float,
        sgn: int,
    ) -> float: ...
    def alphaMin(
        self,
        strike: float,
    ) -> float: ...
    def alphaMax(
        self,
        strike: float,
    ) -> float: ...

class COSHestonEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: HestonModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        L: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        L: float,
        N: int,
    ) -> None: ...

class ExponentialFittingHestonEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: HestonModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        cv: ExponentialFittingHestonEngine.ControlVariate,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        cv: ExponentialFittingHestonEngine.ControlVariate,
        scaling: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        cv: ExponentialFittingHestonEngine.ControlVariate,
        scaling: Optional[float],
        alpha: float,
    ) -> None: ...

class AnalyticPTDHestonEngine(PricingEngine):
    class ComplexLogFormula(IntEnum):
        Gatheral
        AndersenPiterbarg

    @overload
    def __init__(
        self,
        model: PiecewiseTimeDependentHestonModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: PiecewiseTimeDependentHestonModel,
        cpxLog: AnalyticPTDHestonEngine.ComplexLogFormula,
        itg: AnalyticPTDHestonEngine.Integration,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: PiecewiseTimeDependentHestonModel,
        cpxLog: AnalyticPTDHestonEngine.ComplexLogFormula,
        itg: AnalyticPTDHestonEngine.Integration,
        andersenPiterbargEpsilon: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: PiecewiseTimeDependentHestonModel,
        integrationOrder: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: PiecewiseTimeDependentHestonModel,
        relTolerance: float,
        maxEvaluations: int,
    ) -> None: ...

class AnalyticPDFHestonEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: HestonModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        gaussLobattoEps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        gaussLobattoEps: float,
        gaussLobattoIntegrationOrder: int,
    ) -> None: ...

class BatesModel(HestonModel):
    def __init__(
        self,
        process: BatesProcess,
    ) -> None: ...
    def nu(self) -> float: ...
    def delta(self) -> float: ...
    def lambda_(self) -> float: ...

class BatesEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: BatesModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        integrationOrder: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        relTolerance: float,
        maxEvaluations: int,
    ) -> None: ...

class IntegralEngine(PricingEngine):
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
    ) -> None: ...

class LsmBasisSystem:
    class PolynomialType(IntEnum):
        Monomial
        Laguerre
        Hermite
        Hyperbolic
        Legendre
        Chebyshev
        Chebyshev2nd

    def __init__(self) -> None: ...

class BaroneAdesiWhaleyApproximationEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class BjerksundStenslandApproximationEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class JuQuadraticApproximationEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticDigitalAmericanEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticDigitalAmericanKOEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticDividendEuropeanEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
    ) -> None: ...

class QdPlusAmericanEngine(PricingEngine):
    class SolverType(IntEnum):
        Brent
        Newton
        Ridder
        Halley
        SuperHalley

    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        interpolationPoints: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        interpolationPoints: int,
        solverType: QdPlusAmericanEngine.SolverType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        interpolationPoints: int,
        solverType: QdPlusAmericanEngine.SolverType,
        eps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        interpolationPoints: int,
        solverType: QdPlusAmericanEngine.SolverType,
        eps: float,
        maxIter: int,
    ) -> None: ...

class QdFpIterationScheme:
    def __init__(self) -> None: ...

class QdFpLegendreScheme(QdFpIterationScheme):
    def __init__(
        self,
        l: int,
        m: int,
        n: int,
        p: int,
    ) -> None: ...

class QdFpLegendreTanhSinhScheme(QdFpLegendreScheme):
    def __init__(
        self,
        l: int,
        m: int,
        n: int,
        eps: float,
    ) -> None: ...

class QdFpTanhSinhIterationScheme(QdFpIterationScheme):
    def __init__(
        self,
        m: int,
        n: int,
        eps: float,
    ) -> None: ...

class QdFpAmericanEngine(PricingEngine):
    class FixedPointEquation(IntEnum):
        FP_A
        FP_B
        Auto

    @overload
    def __init__(
        self,
        bsProcess: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        bsProcess: GeneralizedBlackScholesProcess,
        iterationScheme: QdFpIterationScheme,
    ) -> None: ...
    @overload
    def __init__(
        self,
        bsProcess: GeneralizedBlackScholesProcess,
        iterationScheme: QdFpIterationScheme,
        fpEquation: QdFpAmericanEngine.FixedPointEquation,
    ) -> None: ...
    def fastScheme(self) -> QdFpIterationScheme: ...
    def accurateScheme(self) -> QdFpIterationScheme: ...
    def highPrecisionScheme(self) -> QdFpIterationScheme: ...

class FdmSchemeDesc:
    class FdmSchemeType(IntEnum):
        HundsdorferType
        DouglasType
        CraigSneydType
        ModifiedCraigSneydType
        ImplicitEulerType
        ExplicitEulerType
        MethodOfLinesType
        TrBDF2Type
        CrankNicolsonType

    def __init__(
        self,
        type: FdmSchemeDesc.FdmSchemeType,
        theta: float,
        mu: float,
    ) -> None: ...
    def Douglas(self) -> FdmSchemeDesc: ...
    def CrankNicolson(self) -> FdmSchemeDesc: ...
    def ImplicitEuler(self) -> FdmSchemeDesc: ...
    def ExplicitEuler(self) -> FdmSchemeDesc: ...
    def CraigSneyd(self) -> FdmSchemeDesc: ...
    def ModifiedCraigSneyd(self) -> FdmSchemeDesc: ...
    def Hundsdorfer(self) -> FdmSchemeDesc: ...
    def ModifiedHundsdorfer(self) -> FdmSchemeDesc: ...
    @overload
    def MethodOfLines(
        self,
        eps: float,
    ) -> FdmSchemeDesc: ...
    @overload
    def MethodOfLines(
        self,
        eps: float,
        relInitStepSize: float,
    ) -> FdmSchemeDesc: ...
    @overload
    def MethodOfLines(self) -> FdmSchemeDesc: ...
    def TrBDF2(self) -> FdmSchemeDesc: ...

class FdmQuantoHelper:
    def __init__(
        self,
        rTS: YieldTermStructure,
        fTS: YieldTermStructure,
        fxVolTS: Any,
        equityFxCorrelation: float,
        exchRateATMlevel: float,
    ) -> None: ...

class FdBlackScholesVanillaEngine(PricingEngine):
    class CashDividendModel(IntEnum):
        Spot
        Escrowed

    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
        cashDividendModel: FdBlackScholesVanillaEngine.CashDividendModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        quantoHelper: FdmQuantoHelper,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
        cashDividendModel: FdBlackScholesVanillaEngine.CashDividendModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
        cashDividendModel: FdBlackScholesVanillaEngine.CashDividendModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
        cashDividendModel: FdBlackScholesVanillaEngine.CashDividendModel,
    ) -> None: ...

class FdBlackScholesShoutEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class FdOrnsteinUhlenbeckVanillaEngine(PricingEngine):
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        dividends: DividendSchedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        dividends: DividendSchedule,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        epsilon: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        epsilon: float,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        epsilon: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        epsilon: float,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class FdBatesVanillaEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: BatesModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        dividends: DividendSchedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        dividends: DividendSchedule,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: BatesModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class FdHestonVanillaEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: HestonModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        quantoHelper: FdmQuantoHelper,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        quantoHelper: FdmQuantoHelper,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...

class AnalyticCEVEngine(PricingEngine):
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        rTS: Handle[YieldTermStructure],
    ) -> None: ...

class FdCEVVanillaEngine(PricingEngine):
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        rTS: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        scalingFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        scalingFactor: float,
        eps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        scalingFactor: float,
        eps: float,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class FdSabrVanillaEngine(PricingEngine):
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        rTS: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        fGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        fGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        fGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        fGrid: int,
        xGrid: int,
        dampingSteps: int,
        scalingFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        fGrid: int,
        xGrid: int,
        dampingSteps: int,
        scalingFactor: float,
        eps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
        rTS: Handle[YieldTermStructure],
        tGrid: int,
        fGrid: int,
        xGrid: int,
        dampingSteps: int,
        scalingFactor: float,
        eps: float,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class FdHestonHullWhiteVanillaEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        corrEquityShortRate: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        corrEquityShortRate: float,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        rGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        rGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        rGrid: int,
        dampingSteps: int,
        controlVariate: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        rGrid: int,
        dampingSteps: int,
        controlVariate: bool,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        dividends: DividendSchedule,
        corrEquityShortRate: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        dividends: DividendSchedule,
        corrEquityShortRate: float,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        dividends: DividendSchedule,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        dividends: DividendSchedule,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        dividends: DividendSchedule,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        rGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        dividends: DividendSchedule,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        rGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        dividends: DividendSchedule,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        rGrid: int,
        dampingSteps: int,
        controlVariate: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hwProcess: HullWhiteProcess,
        dividends: DividendSchedule,
        corrEquityShortRate: float,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        rGrid: int,
        dampingSteps: int,
        controlVariate: bool,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class AnalyticHestonHullWhiteEngine(PricingEngine):
    @overload
    def __init__(
        self,
        hestonModel: HestonModel,
        hullWhiteModel: HullWhite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        hestonModel: HestonModel,
        hullWhiteModel: HullWhite,
        integrationOrder: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hullWhiteModel: HullWhite,
        relTolerance: float,
        maxEvaluations: int,
    ) -> None: ...

class AnalyticH1HWEngine(PricingEngine):
    @overload
    def __init__(
        self,
        hestonModel: HestonModel,
        hullWhiteModel: HullWhite,
        rhoSr: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        hestonModel: HestonModel,
        hullWhiteModel: HullWhite,
        rhoSr: float,
        integrationOrder: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        hullWhiteModel: HullWhite,
        rhoSr: float,
        relTolerance: float,
        maxEvaluations: int,
    ) -> None: ...

class ForwardEuropeanEngine(PricingEngine):
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
    ) -> None: ...

class QuantoEuropeanEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        foreignRiskFreeRate: Handle[YieldTermStructure],
        exchangeRateVolatility: Handle[Any],
        correlation: Handle[Quote],
    ) -> None: ...

class QuantoForwardEuropeanEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        foreignRiskFreeRate: Handle[YieldTermStructure],
        exchangeRateVolatility: Handle[Any],
        correlation: Handle[Quote],
    ) -> None: ...

class AnalyticHestonForwardEuropeanEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: HestonProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: HestonProcess,
        integrationOrder: int,
    ) -> None: ...

class BlackCalculator:
    @overload
    def __init__(
        self,
        payoff: StrikedTypePayoff,
        forward: float,
        stdDev: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payoff: StrikedTypePayoff,
        forward: float,
        stdDev: float,
        discount: float,
    ) -> None: ...
    def value(self) -> float: ...
    def deltaForward(self) -> float: ...
    def delta(
        self,
        spot: float,
    ) -> float: ...
    def elasticityForward(self) -> float: ...
    def elasticity(
        self,
        spot: float,
    ) -> float: ...
    def gammaForward(self) -> float: ...
    def gamma(
        self,
        spot: float,
    ) -> float: ...
    def theta(
        self,
        spot: float,
        maturity: float,
    ) -> float: ...
    def thetaPerDay(
        self,
        spot: float,
        maturity: float,
    ) -> float: ...
    def vega(
        self,
        maturity: float,
    ) -> float: ...
    def rho(
        self,
        maturity: float,
    ) -> float: ...
    def dividendRho(
        self,
        maturity: float,
    ) -> float: ...
    def itmCashProbability(self) -> float: ...
    def itmAssetProbability(self) -> float: ...
    def strikeSensitivity(self) -> float: ...
    def strikeGamma(self) -> float: ...
    def vanna(
        self,
        spot: float,
        maturity: float,
    ) -> float: ...
    def volga(
        self,
        maturity: float,
    ) -> float: ...
    def alpha(self) -> float: ...
    def beta(self) -> float: ...

class BachelierCalculator:
    @overload
    def __init__(
        self,
        payoff: StrikedTypePayoff,
        forward: float,
        stdDev: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payoff: StrikedTypePayoff,
        forward: float,
        stdDev: float,
        discount: float,
    ) -> None: ...
    def value(self) -> float: ...
    def deltaForward(self) -> float: ...
    def delta(
        self,
        spot: float,
    ) -> float: ...
    def elasticityForward(self) -> float: ...
    def elasticity(
        self,
        spot: float,
    ) -> float: ...
    def gammaForward(self) -> float: ...
    def gamma(
        self,
        spot: float,
    ) -> float: ...
    def theta(
        self,
        spot: float,
        maturity: float,
    ) -> float: ...
    def thetaPerDay(
        self,
        spot: float,
        maturity: float,
    ) -> float: ...
    def vega(
        self,
        maturity: float,
    ) -> float: ...
    def rho(
        self,
        maturity: float,
    ) -> float: ...
    def dividendRho(
        self,
        maturity: float,
    ) -> float: ...
    def itmCashProbability(self) -> float: ...
    def itmAssetProbability(self) -> float: ...
    def strikeSensitivity(self) -> float: ...
    def strikeGamma(self) -> float: ...
    def vanna(
        self,
        maturity: float,
    ) -> float: ...
    def volga(
        self,
        maturity: float,
    ) -> float: ...
    def alpha(self) -> float: ...
    def beta(self) -> float: ...

class VarianceGammaEngine(PricingEngine):
    def __init__(
        self,
        process: VarianceGammaProcess,
    ) -> None: ...

class FFTVarianceGammaEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: VarianceGammaProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: VarianceGammaProcess,
        logStrikeSpacing: float,
    ) -> None: ...
    def precalculate(
        self,
        optionList: list[Instrument],
    ) -> None: ...

class GJRGARCHModel(CalibratedModel):
    def __init__(
        self,
        process: GJRGARCHProcess,
    ) -> None: ...
    def omega(self) -> float: ...
    def alpha(self) -> float: ...
    def beta(self) -> float: ...
    def gamma(self) -> float: ...
    def lambda_(self) -> float: ...
    def v0(self) -> float: ...
    def process(self) -> GJRGARCHProcess: ...

class AnalyticGJRGARCHEngine(PricingEngine):
    def __init__(
        self,
        process: GJRGARCHModel,
    ) -> None: ...

class MargrabeOption(MultiAssetOption):
    def __init__(
        self,
        Q1: int,
        Q2: int,
        arg2: Exercise,
    ) -> None: ...
    def delta1(self) -> float: ...
    def delta2(self) -> float: ...
    def gamma1(self) -> float: ...
    def gamma2(self) -> float: ...

class AnalyticEuropeanMargrabeEngine(PricingEngine):
    def __init__(
        self,
        process1: GeneralizedBlackScholesProcess,
        process2: GeneralizedBlackScholesProcess,
        correlation: float,
    ) -> None: ...

class AnalyticAmericanMargrabeEngine(PricingEngine):
    def __init__(
        self,
        process1: GeneralizedBlackScholesProcess,
        process2: GeneralizedBlackScholesProcess,
        correlation: float,
    ) -> None: ...

class CompoundOption(OneAssetOption):
    def __init__(
        self,
        motherPayoff: StrikedTypePayoff,
        motherExercise: Exercise,
        daughterPayoff: StrikedTypePayoff,
        daughterExercise: Exercise,
    ) -> None: ...

class AnalyticCompoundOptionEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class SimpleChooserOption(OneAssetOption):
    def __init__(
        self,
        choosingDate: Date,
        strike: float,
        exercise: Exercise,
    ) -> None: ...

class AnalyticSimpleChooserEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class ComplexChooserOption(OneAssetOption):
    def __init__(
        self,
        choosingDate: Date,
        strikeCall: float,
        strikePut: float,
        exerciseCall: Exercise,
        exercisePut: Exercise,
    ) -> None: ...

class AnalyticComplexChooserEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class HolderExtensibleOption(OneAssetOption):
    def __init__(
        self,
        type: Option.Type,
        premium: float,
        secondExpiryDate: Date,
        secondStrike: float,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class AnalyticHolderExtensibleOptionEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class WriterExtensibleOption(OneAssetOption):
    def __init__(
        self,
        payoff1: PlainVanillaPayoff,
        exercise1: Exercise,
        payoff2: PlainVanillaPayoff,
        exercise2: Exercise,
    ) -> None: ...
    def payoff2(self) -> Payoff: ...
    def exercise2(self) -> Exercise: ...

class AnalyticWriterExtensibleOptionEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class TwoAssetCorrelationOption(MultiAssetOption):
    def __init__(
        self,
        type: Option.Type,
        strike1: float,
        strike2: float,
        arg3: Exercise,
    ) -> None: ...

class AnalyticTwoAssetCorrelationEngine(PricingEngine):
    def __init__(
        self,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: Handle[Quote],
    ) -> None: ...

class Average:
    class Type(IntEnum):
        Arithmetic
        Geometric

    def __init__(self) -> None: ...

class ContinuousAveragingAsianOption(OneAssetOption):
    def __init__(
        self,
        averageType: Average.Type,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class DiscreteAveragingAsianOption(OneAssetOption):
    @overload
    def __init__(
        self,
        averageType: Average.Type,
        fixingDates: list[Date],
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...
    @overload
    def __init__(
        self,
        averageType: Average.Type,
        fixingDates: list[Date],
        payoff: StrikedTypePayoff,
        exercise: Exercise,
        allPastFixings: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        averageType: Average.Type,
        runningAccumulator: float,
        pastFixings: int,
        fixingDates: list[Date],
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class AnalyticContinuousGeometricAveragePriceAsianEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticContinuousGeometricAveragePriceAsianHestonEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: HestonProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: HestonProcess,
        summationCutoff: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: HestonProcess,
        summationCutoff: int,
        xiRightLimit: float,
    ) -> None: ...

class AnalyticDiscreteGeometricAveragePriceAsianEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticDiscreteGeometricAveragePriceAsianHestonEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: HestonProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: HestonProcess,
        xiRightLimit: float,
    ) -> None: ...

class AnalyticDiscreteGeometricAverageStrikeAsianEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class ContinuousArithmeticAsianLevyEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        runningAverage: Handle[Quote],
        startDate: Date,
    ) -> None: ...

class FdBlackScholesAsianEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        aGrid: int,
    ) -> None: ...

class ChoiAsianEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        lambda_: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        lambda_: float,
        maxNrIntegrationSteps: int,
    ) -> None: ...

class TurnbullWakemanAsianEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class Barrier:
    class Type(IntEnum):
        DownIn
        UpIn
        DownOut
        UpOut

    def __init__(self) -> None: ...

class BarrierOption(OneAssetOption):
    def __init__(
        self,
        barrierType: Barrier.Type,
        barrier: float,
        rebate: float,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        targetValue: float,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...

class QuantoBarrierOption(BarrierOption):
    def __init__(
        self,
        barrierType: Barrier.Type,
        barrier: float,
        rebate: float,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class PartialBarrier:
    class Range(IntEnum):
        Start = 0
        EndB1 = 2
        EndB2 = 3

    def __init__(self) -> None: ...

class PartialTimeBarrierOption(OneAssetOption):
    def __init__(
        self,
        barrierType: Barrier.Type,
        barrierRange: PartialBarrier.Range,
        barrier: float,
        rebate: float,
        coverEventDate: Date,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class AnalyticPartialTimeBarrierOptionEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticBarrierEngine(PricingEngine):
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
    ) -> None: ...

class QuantoBarrierEngine(PricingEngine):
    def __init__(
        self,
        arg0: GeneralizedBlackScholesProcess,
        foreignRiskFreeRate: Handle[YieldTermStructure],
        exchangeRateVolatility: Handle[Any],
        correlation: Handle[Quote],
    ) -> None: ...

class FdBlackScholesBarrierEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...

class FdBlackScholesRebateEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...

class FdHestonBarrierEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: HestonModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...

class FdHestonRebateEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: HestonModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        dividends: DividendSchedule,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...

class AnalyticBinaryBarrierEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class VannaVolgaBarrierEngine(PricingEngine):
    @overload
    def __init__(
        self,
        atmVol: Handle[DeltaVolQuote],
        vol25Put: Handle[DeltaVolQuote],
        vol25Call: Handle[DeltaVolQuote],
        spotFX: Handle[Quote],
        domesticTS: Handle[YieldTermStructure],
        foreignTS: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVol: Handle[DeltaVolQuote],
        vol25Put: Handle[DeltaVolQuote],
        vol25Call: Handle[DeltaVolQuote],
        spotFX: Handle[Quote],
        domesticTS: Handle[YieldTermStructure],
        foreignTS: Handle[YieldTermStructure],
        adaptVanDelta: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        atmVol: Handle[DeltaVolQuote],
        vol25Put: Handle[DeltaVolQuote],
        vol25Call: Handle[DeltaVolQuote],
        spotFX: Handle[Quote],
        domesticTS: Handle[YieldTermStructure],
        foreignTS: Handle[YieldTermStructure],
        adaptVanDelta: bool,
        bsPriceWithSmile: float,
    ) -> None: ...

class DoubleBarrier:
    class Type(IntEnum):
        KnockIn
        KnockOut
        KIKO
        KOKI

    def __init__(self) -> None: ...

class DoubleBarrierOption(OneAssetOption):
    def __init__(
        self,
        barrierType: DoubleBarrier.Type,
        barrier_lo: float,
        barrier_hi: float,
        rebate: float,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class QuantoDoubleBarrierOption(DoubleBarrierOption):
    def __init__(
        self,
        barrierType: DoubleBarrier.Type,
        barrier_lo: float,
        barrier_hi: float,
        rebate: float,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...
    def qvega(self) -> float: ...
    def qrho(self) -> float: ...
    def qlambda(self) -> float: ...

class AnalyticDoubleBarrierEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        series: int,
    ) -> None: ...

class FdHestonDoubleBarrierEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: HestonModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HestonModel,
        tGrid: int,
        xGrid: int,
        vGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...

class SuoWangDoubleBarrierEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        series: int,
    ) -> None: ...

class AnalyticDoubleBarrierBinaryEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class TwoAssetBarrierOption(Option):
    def __init__(
        self,
        barrierType: Barrier.Type,
        barrier: float,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class AnalyticTwoAssetBarrierEngine(PricingEngine):
    def __init__(
        self,
        process1: GeneralizedBlackScholesProcess,
        process2: GeneralizedBlackScholesProcess,
        rho: Handle[Quote],
    ) -> None: ...

class SoftBarrierOption(OneAssetOption):
    def __init__(
        self,
        barrierType: Barrier.Type,
        barrier_lo: float,
        barrier_hi: float,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        process: GeneralizedBlackScholesProcess,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        process: GeneralizedBlackScholesProcess,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...

class AnalyticSoftBarrierEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class PlainVanillaPayoff(StrikedTypePayoff):
    def __init__(
        self,
        type: Option.Type,
        strike: float,
    ) -> None: ...

class PercentageStrikePayoff(StrikedTypePayoff):
    def __init__(
        self,
        type: Option.Type,
        moneyness: float,
    ) -> None: ...

class CashOrNothingPayoff(StrikedTypePayoff):
    def __init__(
        self,
        type: Option.Type,
        strike: float,
        payoff: float,
    ) -> None: ...

class AssetOrNothingPayoff(StrikedTypePayoff):
    def __init__(
        self,
        type: Option.Type,
        strike: float,
    ) -> None: ...

class SuperSharePayoff(StrikedTypePayoff):
    def __init__(
        self,
        type: Option.Type,
        strike: float,
        increment: float,
    ) -> None: ...

class GapPayoff(StrikedTypePayoff):
    def __init__(
        self,
        type: Option.Type,
        strike: float,
        strikePayoff: float,
    ) -> None: ...

class VanillaForwardPayoff(StrikedTypePayoff):
    def __init__(
        self,
        type: Option.Type,
        strike: float,
    ) -> None: ...

class BasketPayoff(Payoff):
    def __init__(self) -> None: ...

class MinBasketPayoff(BasketPayoff):
    def __init__(
        self,
        p: Payoff,
    ) -> None: ...

class MaxBasketPayoff(BasketPayoff):
    def __init__(
        self,
        p: Payoff,
    ) -> None: ...

class AverageBasketPayoff(BasketPayoff):
    @overload
    def __init__(
        self,
        p: Payoff,
        a: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        p: Payoff,
        n: int,
    ) -> None: ...

class SpreadBasketPayoff(BasketPayoff):
    def __init__(
        self,
        p: Payoff,
    ) -> None: ...

class BasketOption(MultiAssetOption):
    def __init__(
        self,
        payoff: BasketPayoff,
        exercise: Exercise,
    ) -> None: ...

class StulzEngine(PricingEngine):
    def __init__(
        self,
        process1: GeneralizedBlackScholesProcess,
        process2: GeneralizedBlackScholesProcess,
        correlation: float,
    ) -> None: ...

class KirkEngine(PricingEngine):
    def __init__(
        self,
        process1: GeneralizedBlackScholesProcess,
        process2: GeneralizedBlackScholesProcess,
        correlation: float,
    ) -> None: ...

class BjerksundStenslandSpreadEngine(PricingEngine):
    def __init__(
        self,
        process1: GeneralizedBlackScholesProcess,
        process2: GeneralizedBlackScholesProcess,
        correlation: float,
    ) -> None: ...

class OperatorSplittingSpreadEngine(PricingEngine):
    class Order(IntEnum):
        First
        Second

    @overload
    def __init__(
        self,
        process1: GeneralizedBlackScholesProcess,
        process2: GeneralizedBlackScholesProcess,
        correlation: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process1: GeneralizedBlackScholesProcess,
        process2: GeneralizedBlackScholesProcess,
        correlation: float,
        order: OperatorSplittingSpreadEngine.Order,
    ) -> None: ...

class Fd2dBlackScholesVanillaEngine(PricingEngine):
    @overload
    def __init__(
        self,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        xGrid: int,
        yGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        xGrid: int,
        yGrid: int,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        xGrid: int,
        yGrid: int,
        tGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        xGrid: int,
        yGrid: int,
        tGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        xGrid: int,
        yGrid: int,
        tGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        xGrid: int,
        yGrid: int,
        tGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...

class ChoiBasketEngine(PricingEngine):
    @overload
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
    ) -> None: ...
    @overload
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
        lambda_: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
        lambda_: float,
        maxNrIntegrationSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
        lambda_: float,
        maxNrIntegrationSteps: int,
        calcfwdDelta: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
        lambda_: float,
        maxNrIntegrationSteps: int,
        calcfwdDelta: bool,
        controlVariate: bool,
    ) -> None: ...

class DengLiZhouBasketEngine(PricingEngine):
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
    ) -> None: ...

class FdndimBlackScholesVanillaEngine(PricingEngine):
    @overload
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
        xGrid: int,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
        xGrid: int,
        tGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        processes: list[GeneralizedBlackScholesProcess],
        rho: Matrix,
        xGrid: int,
        tGrid: int,
        dampingSteps: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class EverestOption(MultiAssetOption):
    def __init__(
        self,
        notional: float,
        guarantee: float,
        exercise: Exercise,
    ) -> None: ...

class HimalayaOption(MultiAssetOption):
    def __init__(
        self,
        fixingDates: list[Date],
        strike: float,
    ) -> None: ...

class BlackDeltaCalculator:
    def __init__(
        self,
        ot: Option.Type,
        dt: DeltaVolQuote.DeltaType,
        spot: float,
        dDiscount: float,
        fDiscount: float,
        stDev: float,
    ) -> None: ...
    def deltaFromStrike(
        self,
        strike: float,
    ) -> float: ...
    def strikeFromDelta(
        self,
        delta: float,
    ) -> float: ...
    def atmStrike(
        self,
        atmT: DeltaVolQuote.AtmType,
    ) -> float: ...

class TimeBasket:
    @overload
    def __init__(
        self,
        arg0: list[Date],
        arg1: list[float],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def size(self) -> int: ...
    def rebin(
        self,
        arg0: list[Date],
    ) -> TimeBasket: ...

class Swap(Instrument):
    class Type(IntEnum):
        Receiver = -1
        Payer = 1

    @overload
    def __init__(
        self,
        firstLeg: list[CashFlow],
        secondLeg: list[CashFlow],
    ) -> None: ...
    @overload
    def __init__(
        self,
        legs: list[Leg],
        payer: list[bool],
    ) -> None: ...
    def numberOfLegs(self) -> int: ...
    def startDate(self) -> Date: ...
    def maturityDate(self) -> Date: ...
    def leg(
        self,
        i: int,
    ) -> Leg: ...
    def legNPV(
        self,
        j: int,
    ) -> float: ...
    def legBPS(
        self,
        k: int,
    ) -> float: ...
    def startDiscounts(
        self,
        j: int,
    ) -> float: ...
    def endDiscounts(
        self,
        j: int,
    ) -> float: ...
    def npvDateDiscount(self) -> float: ...
    def payer(
        self,
        j: int,
    ) -> bool: ...

class FixedVsFloatingSwap(Swap):
    def __init__(self) -> None: ...
    def type(self) -> Swap.Type: ...
    def nominal(self) -> float: ...
    def nominals(self) -> list[float]: ...
    def fixedNominals(self) -> list[float]: ...
    def fixedSchedule(self) -> Schedule: ...
    def fixedRate(self) -> float: ...
    def fixedDayCount(self) -> DayCounter: ...
    def floatingNominals(self) -> list[float]: ...
    def floatingSchedule(self) -> Schedule: ...
    def iborIndex(self) -> IborIndex: ...
    def spread(self) -> float: ...
    def floatingDayCount(self) -> DayCounter: ...
    def paymentConvention(self) -> BusinessDayConvention: ...
    def fixedLeg(self) -> Leg: ...
    def floatingLeg(self) -> Leg: ...
    def fixedLegBPS(self) -> float: ...
    def fixedLegNPV(self) -> float: ...
    def fairRate(self) -> float: ...
    def floatingLegBPS(self) -> float: ...
    def floatingLegNPV(self) -> float: ...
    def fairSpread(self) -> float: ...

class VanillaSwap(FixedVsFloatingSwap):
    pass

class MakeVanillaSwap:
    @overload
    def __init__(
        self,
        swapTenor: Period,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swapTenor: Period,
        index: IborIndex,
        fixedRate: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        swapTenor: Period,
        index: IborIndex,
        fixedRate: Optional[float],
        forwardStart: Period,
    ) -> None: ...
    @overload
    def receiveFixed(
        self,
        flag: bool,
    ) -> MakeVanillaSwap: ...
    @overload
    def receiveFixed(self) -> MakeVanillaSwap: ...
    def withType(
        self,
        type: Swap.Type,
    ) -> MakeVanillaSwap: ...
    def withNominal(
        self,
        n: float,
    ) -> MakeVanillaSwap: ...
    def withSettlementDays(
        self,
        settlementDays: int,
    ) -> MakeVanillaSwap: ...
    def withEffectiveDate(
        self,
        arg0: Date,
    ) -> MakeVanillaSwap: ...
    def withTerminationDate(
        self,
        arg0: Date,
    ) -> MakeVanillaSwap: ...
    def withRule(
        self,
        r: DateGeneration.Rule,
    ) -> MakeVanillaSwap: ...
    def withPaymentConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeVanillaSwap: ...
    def withFixedLegTenor(
        self,
        t: Period,
    ) -> MakeVanillaSwap: ...
    def withFixedLegCalendar(
        self,
        cal: Calendar,
    ) -> MakeVanillaSwap: ...
    def withFixedLegConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeVanillaSwap: ...
    def withFixedLegTerminationDateConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeVanillaSwap: ...
    def withFixedLegRule(
        self,
        r: DateGeneration.Rule,
    ) -> MakeVanillaSwap: ...
    @overload
    def withFixedLegEndOfMonth(
        self,
        flag: bool,
    ) -> MakeVanillaSwap: ...
    @overload
    def withFixedLegEndOfMonth(self) -> MakeVanillaSwap: ...
    def withFixedLegFirstDate(
        self,
        d: Date,
    ) -> MakeVanillaSwap: ...
    def withFixedLegNextToLastDate(
        self,
        d: Date,
    ) -> MakeVanillaSwap: ...
    def withFixedLegDayCount(
        self,
        dc: DayCounter,
    ) -> MakeVanillaSwap: ...
    def withFloatingLegTenor(
        self,
        t: Period,
    ) -> MakeVanillaSwap: ...
    def withFloatingLegCalendar(
        self,
        cal: Calendar,
    ) -> MakeVanillaSwap: ...
    def withFloatingLegConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeVanillaSwap: ...
    def withFloatingLegTerminationDateConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeVanillaSwap: ...
    def withFloatingLegRule(
        self,
        r: DateGeneration.Rule,
    ) -> MakeVanillaSwap: ...
    @overload
    def withFloatingLegEndOfMonth(
        self,
        flag: bool,
    ) -> MakeVanillaSwap: ...
    @overload
    def withFloatingLegEndOfMonth(self) -> MakeVanillaSwap: ...
    def withFloatingLegFirstDate(
        self,
        d: Date,
    ) -> MakeVanillaSwap: ...
    def withFloatingLegNextToLastDate(
        self,
        d: Date,
    ) -> MakeVanillaSwap: ...
    def withFloatingLegDayCount(
        self,
        dc: DayCounter,
    ) -> MakeVanillaSwap: ...
    def withFloatingLegSpread(
        self,
        sp: float,
    ) -> MakeVanillaSwap: ...
    def withDiscountingTermStructure(
        self,
        discountCurve: Handle[YieldTermStructure],
    ) -> MakeVanillaSwap: ...
    def withPricingEngine(
        self,
        engine: PricingEngine,
    ) -> MakeVanillaSwap: ...
    @overload
    def withIndexedCoupons(
        self,
        flag: bool,
    ) -> MakeVanillaSwap: ...
    @overload
    def withIndexedCoupons(self) -> MakeVanillaSwap: ...
    @overload
    def withAtParCoupons(
        self,
        flag: bool,
    ) -> MakeVanillaSwap: ...
    @overload
    def withAtParCoupons(self) -> MakeVanillaSwap: ...

class NonstandardSwap(Swap):
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominal: list[float],
        floatingNominal: list[float],
        fixedSchedule: Schedule,
        fixedRate: list[float],
        fixedDayCount: DayCounter,
        floatSchedule: Schedule,
        index: IborIndex,
        gearing: list[float],
        spread: list[float],
        floatDayCount: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominal: list[float],
        floatingNominal: list[float],
        fixedSchedule: Schedule,
        fixedRate: list[float],
        fixedDayCount: DayCounter,
        floatSchedule: Schedule,
        index: IborIndex,
        gearing: list[float],
        spread: list[float],
        floatDayCount: DayCounter,
        intermediateCapitalExchange: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominal: list[float],
        floatingNominal: list[float],
        fixedSchedule: Schedule,
        fixedRate: list[float],
        fixedDayCount: DayCounter,
        floatSchedule: Schedule,
        index: IborIndex,
        gearing: list[float],
        spread: list[float],
        floatDayCount: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominal: list[float],
        floatingNominal: list[float],
        fixedSchedule: Schedule,
        fixedRate: list[float],
        fixedDayCount: DayCounter,
        floatSchedule: Schedule,
        index: IborIndex,
        gearing: list[float],
        spread: list[float],
        floatDayCount: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    def type(self) -> Swap.Type: ...
    def fixedNominal(self) -> list[float]: ...
    def floatingNominal(self) -> list[float]: ...
    def fixedSchedule(self) -> Schedule: ...
    def fixedRate(self) -> list[float]: ...
    def fixedDayCount(self) -> DayCounter: ...
    def floatingSchedule(self) -> Schedule: ...
    def iborIndex(self) -> IborIndex: ...
    def spread(self) -> float: ...
    def gearing(self) -> float: ...
    def spreads(self) -> list[float]: ...
    def gearings(self) -> list[float]: ...
    def floatingDayCount(self) -> DayCounter: ...
    def paymentConvention(self) -> BusinessDayConvention: ...
    def fixedLeg(self) -> Leg: ...
    def floatingLeg(self) -> Leg: ...

class DiscountingSwapEngine(PricingEngine):
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        includeSettlementDateFlows: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        includeSettlementDateFlows: bool,
        settlementDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        includeSettlementDateFlows: bool,
        settlementDate: Date,
        npvDate: Date,
    ) -> None: ...

class AssetSwap(Swap):
    @overload
    def __init__(
        self,
        payFixedRate: bool,
        bond: Bond,
        bondCleanPrice: float,
        index: IborIndex,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payFixedRate: bool,
        bond: Bond,
        bondCleanPrice: float,
        index: IborIndex,
        spread: float,
        floatSchedule: Schedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payFixedRate: bool,
        bond: Bond,
        bondCleanPrice: float,
        index: IborIndex,
        spread: float,
        floatSchedule: Schedule,
        floatingDayCount: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payFixedRate: bool,
        bond: Bond,
        bondCleanPrice: float,
        index: IborIndex,
        spread: float,
        floatSchedule: Schedule,
        floatingDayCount: DayCounter,
        parAssetSwap: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payFixedRate: bool,
        bond: Bond,
        bondCleanPrice: float,
        index: IborIndex,
        spread: float,
        floatSchedule: Schedule,
        floatingDayCount: DayCounter,
        parAssetSwap: bool,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payFixedRate: bool,
        bond: Bond,
        bondCleanPrice: float,
        index: IborIndex,
        spread: float,
        floatSchedule: Schedule,
        floatingDayCount: DayCounter,
        parAssetSwap: bool,
        gearing: float,
        nonParRepayment: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payFixedRate: bool,
        bond: Bond,
        bondCleanPrice: float,
        index: IborIndex,
        spread: float,
        floatSchedule: Schedule,
        floatingDayCount: DayCounter,
        parAssetSwap: bool,
        gearing: float,
        nonParRepayment: float,
        dealMaturity: Date,
    ) -> None: ...
    def fairCleanPrice(self) -> float: ...
    def fairSpread(self) -> float: ...

class FloatFloatSwap(Swap):
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
        spread1: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
        spread1: list[float],
        cappedRate1: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
        spread1: list[float],
        cappedRate1: list[float],
        flooredRate1: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
        spread1: list[float],
        cappedRate1: list[float],
        flooredRate1: list[float],
        gearing2: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
        spread1: list[float],
        cappedRate1: list[float],
        flooredRate1: list[float],
        gearing2: list[float],
        spread2: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
        spread1: list[float],
        cappedRate1: list[float],
        flooredRate1: list[float],
        gearing2: list[float],
        spread2: list[float],
        cappedRate2: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
        spread1: list[float],
        cappedRate1: list[float],
        flooredRate1: list[float],
        gearing2: list[float],
        spread2: list[float],
        cappedRate2: list[float],
        flooredRate2: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
        spread1: list[float],
        cappedRate1: list[float],
        flooredRate1: list[float],
        gearing2: list[float],
        spread2: list[float],
        cappedRate2: list[float],
        flooredRate2: list[float],
        paymentConvention1: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal1: list[float],
        nominal2: list[float],
        schedule1: Schedule,
        index1: InterestRateIndex,
        dayCount1: DayCounter,
        schedule2: Schedule,
        index2: InterestRateIndex,
        dayCount2: DayCounter,
        intermediateCapitalExchange: bool,
        finalCapitalExchange: bool,
        gearing1: list[float],
        spread1: list[float],
        cappedRate1: list[float],
        flooredRate1: list[float],
        gearing2: list[float],
        spread2: list[float],
        cappedRate2: list[float],
        flooredRate2: list[float],
        paymentConvention1: BusinessDayConvention,
        paymentConvention2: BusinessDayConvention,
    ) -> None: ...

class OvernightIndexedSwap(FixedVsFloatingSwap):
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
        spread: float,
        paymentLag: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
        lockoutDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        fixedNominals: list[float],
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        overnightNominals: list[float],
        overnightSchedule: Schedule,
        overnightIndex: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
        lockoutDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
        lockoutDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominals: list[float],
        schedule: Schedule,
        fixedRate: float,
        fixedDC: DayCounter,
        index: OvernightIndex,
        spread: float,
        paymentLag: int,
        paymentAdjustment: BusinessDayConvention,
        paymentCalendar: Calendar,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
    ) -> None: ...
    def overnightLegBPS(self) -> float: ...
    def overnightLegNPV(self) -> float: ...
    def paymentFrequency(self) -> Frequency: ...
    def overnightIndex(self) -> OvernightIndex: ...
    def overnightLeg(self) -> Leg: ...
    def averagingMethod(self) -> RateAveraging.Type: ...
    def lookbackDays(self) -> int: ...
    def lockoutDays(self) -> int: ...
    def applyObservationShift(self) -> bool: ...

class MakeOIS:
    @overload
    def __init__(
        self,
        swapTenor: Period,
        overnightIndex: OvernightIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swapTenor: Period,
        overnightIndex: OvernightIndex,
        fixedRate: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        swapTenor: Period,
        overnightIndex: OvernightIndex,
        fixedRate: Optional[float],
        fwdStart: Period,
    ) -> None: ...
    @overload
    def receiveFixed(
        self,
        flag: bool,
    ) -> MakeOIS: ...
    @overload
    def receiveFixed(self) -> MakeOIS: ...
    def withType(
        self,
        type: Swap.Type,
    ) -> MakeOIS: ...
    def withNominal(
        self,
        n: float,
    ) -> MakeOIS: ...
    def withSettlementDays(
        self,
        settlementDays: int,
    ) -> MakeOIS: ...
    def withEffectiveDate(
        self,
        arg0: Date,
    ) -> MakeOIS: ...
    def withTerminationDate(
        self,
        arg0: Date,
    ) -> MakeOIS: ...
    def withRule(
        self,
        r: DateGeneration.Rule,
    ) -> MakeOIS: ...
    def withFixedLegRule(
        self,
        r: DateGeneration.Rule,
    ) -> MakeOIS: ...
    def withOvernightLegRule(
        self,
        r: DateGeneration.Rule,
    ) -> MakeOIS: ...
    def withPaymentFrequency(
        self,
        f: Frequency,
    ) -> MakeOIS: ...
    def withFixedLegPaymentFrequency(
        self,
        f: Frequency,
    ) -> MakeOIS: ...
    def withOvernightLegPaymentFrequency(
        self,
        f: Frequency,
    ) -> MakeOIS: ...
    def withPaymentAdjustment(
        self,
        convention: BusinessDayConvention,
    ) -> MakeOIS: ...
    def withPaymentLag(
        self,
        lag: int,
    ) -> MakeOIS: ...
    def withPaymentCalendar(
        self,
        cal: Calendar,
    ) -> MakeOIS: ...
    def withCalendar(
        self,
        cal: Calendar,
    ) -> MakeOIS: ...
    def withFixedLegCalendar(
        self,
        cal: Calendar,
    ) -> MakeOIS: ...
    def withOvernightLegCalendar(
        self,
        cal: Calendar,
    ) -> MakeOIS: ...
    def withConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeOIS: ...
    def withFixedLegConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeOIS: ...
    def withOvernightLegConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeOIS: ...
    def withTerminationDateConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeOIS: ...
    def withFixedLegTerminationDateConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeOIS: ...
    def withOvernightLegTerminationDateConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeOIS: ...
    @overload
    def withEndOfMonth(
        self,
        flag: bool,
    ) -> MakeOIS: ...
    @overload
    def withEndOfMonth(self) -> MakeOIS: ...
    @overload
    def withFixedLegEndOfMonth(
        self,
        flag: bool,
    ) -> MakeOIS: ...
    @overload
    def withFixedLegEndOfMonth(self) -> MakeOIS: ...
    @overload
    def withOvernightLegEndOfMonth(
        self,
        flag: bool,
    ) -> MakeOIS: ...
    @overload
    def withOvernightLegEndOfMonth(self) -> MakeOIS: ...
    def withFixedLegDayCount(
        self,
        dc: DayCounter,
    ) -> MakeOIS: ...
    def withOvernightLegSpread(
        self,
        sp: float,
    ) -> MakeOIS: ...
    def withDiscountingTermStructure(
        self,
        discountingTermStructure: Handle[YieldTermStructure],
    ) -> MakeOIS: ...
    def withTelescopicValueDates(
        self,
        telescopicValueDates: bool,
    ) -> MakeOIS: ...
    def withAveragingMethod(
        self,
        averagingMethod: RateAveraging.Type,
    ) -> MakeOIS: ...
    def withLookbackDays(
        self,
        lookbackDays: int,
    ) -> MakeOIS: ...
    def withLockoutDays(
        self,
        lockoutDays: int,
    ) -> MakeOIS: ...
    @overload
    def withObservationShift(
        self,
        applyObservationShift: bool,
    ) -> MakeOIS: ...
    @overload
    def withObservationShift(self) -> MakeOIS: ...
    def withPricingEngine(
        self,
        engine: PricingEngine,
    ) -> MakeOIS: ...

class OvernightIndexedSwapIndex(SwapIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        overnightIndex: OvernightIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        overnightIndex: OvernightIndex,
        telescopicValueDates: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        tenor: Period,
        settlementDays: int,
        currency: Currency,
        overnightIndex: OvernightIndex,
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    def overnightIndex(self) -> OvernightIndex: ...
    def underlyingSwap(
        self,
        fixingDate: Date,
    ) -> OvernightIndexedSwap: ...

class ZeroCouponSwap(Swap):
    @overload
    def __init__(
        self,
        type: Swap.Type,
        baseNominal: float,
        startDate: Date,
        maturityDate: Date,
        fixedPayment: float,
        iborIndex: IborIndex,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        baseNominal: float,
        startDate: Date,
        maturityDate: Date,
        fixedPayment: float,
        iborIndex: IborIndex,
        paymentCalendar: Calendar,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        baseNominal: float,
        startDate: Date,
        maturityDate: Date,
        fixedPayment: float,
        iborIndex: IborIndex,
        paymentCalendar: Calendar,
        paymentConvention: BusinessDayConvention,
        paymentDelay: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        baseNominal: float,
        startDate: Date,
        maturityDate: Date,
        fixedRate: float,
        fixedDayCounter: DayCounter,
        iborIndex: IborIndex,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        baseNominal: float,
        startDate: Date,
        maturityDate: Date,
        fixedRate: float,
        fixedDayCounter: DayCounter,
        iborIndex: IborIndex,
        paymentCalendar: Calendar,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        baseNominal: float,
        startDate: Date,
        maturityDate: Date,
        fixedRate: float,
        fixedDayCounter: DayCounter,
        iborIndex: IborIndex,
        paymentCalendar: Calendar,
        paymentConvention: BusinessDayConvention,
        paymentDelay: int,
    ) -> None: ...
    def type(self) -> Swap.Type: ...
    def baseNominal(self) -> float: ...
    def iborIndex(self) -> IborIndex: ...
    def fixedLeg(self) -> Leg: ...
    def floatingLeg(self) -> Leg: ...
    def fixedPayment(self) -> float: ...
    def fixedLegNPV(self) -> float: ...
    def floatingLegNPV(self) -> float: ...
    def fairFixedPayment(self) -> float: ...
    def fairFixedRate(
        self,
        dayCounter: DayCounter,
    ) -> float: ...

class EquityTotalReturnSwap(Swap):
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: IborIndex,
        dayCounter: DayCounter,
        margin: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: IborIndex,
        dayCounter: DayCounter,
        margin: float,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: IborIndex,
        dayCounter: DayCounter,
        margin: float,
        gearing: float,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: IborIndex,
        dayCounter: DayCounter,
        margin: float,
        gearing: float,
        paymentCalendar: Calendar,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: IborIndex,
        dayCounter: DayCounter,
        margin: float,
        gearing: float,
        paymentCalendar: Calendar,
        paymentConvention: BusinessDayConvention,
        paymentDelay: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: OvernightIndex,
        dayCounter: DayCounter,
        margin: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: OvernightIndex,
        dayCounter: DayCounter,
        margin: float,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: OvernightIndex,
        dayCounter: DayCounter,
        margin: float,
        gearing: float,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: OvernightIndex,
        dayCounter: DayCounter,
        margin: float,
        gearing: float,
        paymentCalendar: Calendar,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        schedule: Schedule,
        equityIndex: EquityIndex,
        interestRateIndex: OvernightIndex,
        dayCounter: DayCounter,
        margin: float,
        gearing: float,
        paymentCalendar: Calendar,
        paymentConvention: BusinessDayConvention,
        paymentDelay: int,
    ) -> None: ...
    def type(self) -> Swap.Type: ...
    def nominal(self) -> float: ...
    def equityIndex(self) -> EquityIndex: ...
    def interestRateIndex(self) -> InterestRateIndex: ...
    def schedule(self) -> Schedule: ...
    def dayCounter(self) -> DayCounter: ...
    def margin(self) -> float: ...
    def gearing(self) -> float: ...
    def paymentCalendar(self) -> Calendar: ...
    def paymentConvention(self) -> BusinessDayConvention: ...
    def paymentDelay(self) -> int: ...
    def equityLeg(self) -> Leg: ...
    def interestRateLeg(self) -> Leg: ...
    def equityLegNPV(self) -> float: ...
    def interestRateLegNPV(self) -> float: ...
    def fairMargin(self) -> float: ...

class Seasonality:
    def __init__(self) -> None: ...
    def correctZeroRate(
        self,
        d: Date,
        r: float,
        iTS: InflationTermStructure,
    ) -> float: ...
    def correctYoYRate(
        self,
        d: Date,
        r: float,
        iTS: InflationTermStructure,
    ) -> float: ...
    def isConsistent(
        self,
        iTS: InflationTermStructure,
    ) -> bool: ...

class MultiplicativePriceSeasonality(Seasonality):
    def __init__(
        self,
        seasonalityBaseDate: Date,
        frequency: Frequency,
        seasonalityFactors: list[float],
    ) -> None: ...
    def seasonalityBaseDate(self) -> Date: ...
    def frequency(self) -> Frequency: ...
    def seasonalityFactors(self) -> list[float]: ...
    def seasonalityFactor(
        self,
        d: Date,
    ) -> float: ...

class KerkhofSeasonality(MultiplicativePriceSeasonality):
    def __init__(
        self,
        seasonalityBaseDate: Date,
        seasonalityFactors: list[float],
    ) -> None: ...

class InflationTermStructure(TermStructure):
    def __init__(self) -> None: ...
    def observationLag(self) -> Period: ...
    def frequency(self) -> Frequency: ...
    def baseRate(self) -> float: ...
    def baseDate(self) -> Date: ...
    def hasExplicitBaseDate(self) -> bool: ...
    def setSeasonality(
        self,
        seasonality: Seasonality,
    ) -> None: ...
    def seasonality(self) -> Seasonality: ...
    def hasSeasonality(self) -> bool: ...

class YoYInflationTermStructure(InflationTermStructure):
    def __init__(self) -> None: ...
    @overload
    def yoyRate(
        self,
        d: Date,
    ) -> float: ...
    @overload
    def yoyRate(
        self,
        d: Date,
        instObsLag: Period,
    ) -> float: ...
    @overload
    def yoyRate(
        self,
        d: Date,
        instObsLag: Period,
        forceLinearInterpolation: bool,
    ) -> float: ...
    @overload
    def yoyRate(
        self,
        d: Date,
        instObsLag: Period,
        forceLinearInterpolation: bool,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def yoyRate(
        self,
        t: float,
    ) -> float: ...
    @overload
    def yoyRate(
        self,
        t: float,
        extrapolate: bool,
    ) -> float: ...
    def indexIsInterpolated(self) -> bool: ...

class ZeroInflationTermStructure(InflationTermStructure):
    def __init__(self) -> None: ...
    @overload
    def zeroRate(
        self,
        d: Date,
    ) -> float: ...
    @overload
    def zeroRate(
        self,
        d: Date,
        instObsLag: Period,
    ) -> float: ...
    @overload
    def zeroRate(
        self,
        d: Date,
        instObsLag: Period,
        forceLinearInterpolation: bool,
    ) -> float: ...
    @overload
    def zeroRate(
        self,
        d: Date,
        instObsLag: Period,
        forceLinearInterpolation: bool,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def zeroRate(
        self,
        t: float,
    ) -> float: ...
    @overload
    def zeroRate(
        self,
        t: float,
        extrapolate: bool,
    ) -> float: ...

class Region:
    def __init__(self) -> None: ...
    def name(self) -> str: ...
    def code(self) -> str: ...

class CustomRegion(Region):
    def __init__(
        self,
        name: str,
        code: str,
    ) -> None: ...

class InflationIndex(Index):
    def __init__(self) -> None: ...
    def familyName(self) -> str: ...
    def region(self) -> Region: ...
    def revised(self) -> bool: ...
    def frequency(self) -> Frequency: ...
    def availabilityLag(self) -> Period: ...
    def currency(self) -> Currency: ...

class ZeroInflationIndex(InflationIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        region: Region,
        revised: bool,
        frequency: Frequency,
        availabilityLag: Period,
        currency: Currency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        region: Region,
        revised: bool,
        frequency: Frequency,
        availabilityLag: Period,
        currency: Currency,
        h: Handle[ZeroInflationTermStructure],
    ) -> None: ...
    def lastFixingDate(self) -> Date: ...
    def zeroInflationTermStructure(self) -> Handle[ZeroInflationTermStructure]: ...
    def clone(
        self,
        h: Handle[ZeroInflationTermStructure],
    ) -> ZeroInflationIndex: ...
    def needsForecast(
        self,
        fixingDate: Date,
    ) -> bool: ...

class YoYInflationIndex(InflationIndex):
    @overload
    def __init__(
        self,
        familyName: str,
        region: Region,
        revised: bool,
        frequency: Frequency,
        availabilityLag: Period,
        currency: Currency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        region: Region,
        revised: bool,
        frequency: Frequency,
        availabilityLag: Period,
        currency: Currency,
        ts: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        region: Region,
        revised: bool,
        interpolated: bool,
        frequency: Frequency,
        availabilityLag: Period,
        currency: Currency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        familyName: str,
        region: Region,
        revised: bool,
        interpolated: bool,
        frequency: Frequency,
        availabilityLag: Period,
        currency: Currency,
        ts: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        underlyingIndex: ZeroInflationIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        underlyingIndex: ZeroInflationIndex,
        interpolated: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        underlyingIndex: ZeroInflationIndex,
        interpolated: bool,
        ts: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        underlyingIndex: ZeroInflationIndex,
        ts: Handle[YoYInflationTermStructure],
    ) -> None: ...
    def lastFixingDate(self) -> Date: ...
    def ratio(self) -> bool: ...
    def interpolated(self) -> bool: ...
    def underlyingIndex(self) -> ZeroInflationIndex: ...
    def yoyInflationTermStructure(self) -> Handle[YoYInflationTermStructure]: ...
    def clone(
        self,
        h: Handle[YoYInflationTermStructure],
    ) -> YoYInflationIndex: ...
    def needsForecast(
        self,
        fixingDate: Date,
    ) -> bool: ...

class EUHICP(ZeroInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[ZeroInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class EUHICPXT(ZeroInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[ZeroInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class FRHICP(ZeroInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[ZeroInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class UKRPI(ZeroInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[ZeroInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class UKHICP(ZeroInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[ZeroInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class USCPI(ZeroInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[ZeroInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class ZACPI(ZeroInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[ZeroInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class AUCPI(ZeroInflationIndex):
    @overload
    def __init__(
        self,
        frequency: Frequency,
        revised: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        frequency: Frequency,
        revised: bool,
        h: Handle[ZeroInflationTermStructure],
    ) -> None: ...

class YYEUHICP(YoYInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class YYEUHICPXT(YoYInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class YYFRHICP(YoYInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class YYUKRPI(YoYInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class YYUSCPI(YoYInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class YYZACPI(YoYInflationIndex):
    @overload
    def __init__(
        self,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        interpolated: bool,
        h: Handle[YoYInflationTermStructure],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class CPI:
    class InterpolationType(IntEnum):
        AsIndex
        Flat
        Linear

    def __init__(self) -> None: ...
    def laggedFixing(
        self,
        index: ZeroInflationIndex,
        date: Date,
        observationLag: Period,
        interpolationType: CPI.InterpolationType,
    ) -> float: ...
    def laggedYoYRate(
        self,
        index: YoYInflationIndex,
        date: Date,
        observationLag: Period,
        interpolationType: CPI.InterpolationType,
    ) -> float: ...

class InflationCoupon(Coupon):
    def __init__(self) -> None: ...
    def fixingDate(self) -> Date: ...
    def fixingDays(self) -> int: ...
    def observationLag(self) -> Period: ...
    def indexFixing(self) -> float: ...
    def index(self) -> InflationIndex: ...

class CPICouponPricer:
    def __init__(self) -> None: ...

class CPICoupon(InflationCoupon):
    @overload
    def __init__(
        self,
        baseCPI: float,
        baseDate: Date,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCPI: float,
        baseDate: Date,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCPI: float,
        baseDate: Date,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCPI: float,
        baseDate: Date,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        exCouponDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCPI: float,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCPI: float,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCPI: float,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCPI: float,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        exCouponDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseDate: Date,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseDate: Date,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseDate: Date,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseDate: Date,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        index: ZeroInflationIndex,
        observationLag: Period,
        observationInterpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        fixedRate: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
        exCouponDate: Date,
    ) -> None: ...
    def fixedRate(self) -> float: ...
    def adjustedIndexGrowth(self) -> float: ...
    def indexFixing(self) -> float: ...
    def indexRatio(
        self,
        d: Date,
    ) -> float: ...
    def baseCPI(self) -> float: ...
    def baseDate(self) -> Date: ...
    def observationInterpolation(self) -> CPI.InterpolationType: ...
    def cpiIndex(self) -> ZeroInflationIndex: ...
    def setPricer(
        self,
        arg0: CPICouponPricer,
    ) -> None: ...

class CPICashFlow(IndexedCashFlow):
    @overload
    def __init__(
        self,
        notional: float,
        index: ZeroInflationIndex,
        baseDate: Date,
        baseFixing: float,
        observationDate: Date,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        paymentDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        notional: float,
        index: ZeroInflationIndex,
        baseDate: Date,
        baseFixing: float,
        observationDate: Date,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        paymentDate: Date,
        growthOnly: bool,
    ) -> None: ...
    def interpolation(self) -> CPI.InterpolationType: ...
    def frequency(self) -> Frequency: ...

class ZeroInflationCashFlow(CashFlow):
    @overload
    def __init__(
        self,
        notional: float,
        index: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        startDate: Date,
        endDate: Date,
        observationLag: Period,
        paymentDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        notional: float,
        index: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        startDate: Date,
        endDate: Date,
        observationLag: Period,
        paymentDate: Date,
        growthOnly: bool,
    ) -> None: ...
    def notional(self) -> float: ...
    def baseDate(self) -> Date: ...
    def fixingDate(self) -> Date: ...
    def growthOnly(self) -> bool: ...
    def observationInterpolation(self) -> CPI.InterpolationType: ...
    def zeroInflationIndex(self) -> ZeroInflationIndex: ...

class ZeroCouponInflationSwapHelper(BootstrapHelper[ZeroInflationTermStructure]):
    @overload
    def __init__(
        self,
        quote: Handle[Quote],
        lag: Period,
        maturity: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        dayCounter: DayCounter,
        index: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        quote: Handle[Quote],
        lag: Period,
        maturity: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        dayCounter: DayCounter,
        index: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        nominalTS: Handle[YieldTermStructure],
    ) -> None: ...
    def swap(self) -> ZeroCouponInflationSwap: ...

class YearOnYearInflationSwapHelper(BootstrapHelper[YoYInflationTermStructure]):
    def __init__(
        self,
        quote: Handle[Quote],
        lag: Period,
        maturity: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        dayCounter: DayCounter,
        index: YoYInflationIndex,
        interpolation: CPI.InterpolationType,
        nominalTS: Handle[YieldTermStructure],
    ) -> None: ...
    def swap(self) -> YearOnYearInflationSwap: ...

class YoYInflationCouponPricer:
    def __init__(self) -> None: ...

class YoYInflationCoupon(InflationCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
        spread: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    def gearing(self) -> float: ...
    def spread(self) -> float: ...
    def adjustedFixing(self) -> float: ...
    def yoyIndex(self) -> YoYInflationIndex: ...
    def interpolation(self) -> CPI.InterpolationType: ...

class CappedFlooredYoYInflationCoupon(YoYInflationCoupon):
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
        spread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
        spread: float,
        cap: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        paymentDate: Date,
        nominal: float,
        startDate: Date,
        endDate: Date,
        fixingDays: int,
        index: YoYInflationIndex,
        observationLag: Period,
        interpolation: CPI.InterpolationType,
        dayCounter: DayCounter,
        gearing: float,
        spread: float,
        cap: float,
        floor: float,
        refPeriodStart: Date,
        refPeriodEnd: Date,
    ) -> None: ...
    def rate(self) -> float: ...
    def cap(self) -> float: ...
    def floor(self) -> float: ...
    def effectiveCap(self) -> float: ...
    def effectiveFloor(self) -> float: ...
    def underlyingRate(self) -> float: ...
    def isCapped(self) -> bool: ...
    def isFloored(self) -> bool: ...

class BlackYoYInflationCouponPricer(YoYInflationCouponPricer):
    def __init__(
        self,
        capletVol: Handle[YoYOptionletVolatilitySurface],
        nominalTermStructure: Handle[YieldTermStructure],
    ) -> None: ...

class UnitDisplacedBlackYoYInflationCouponPricer(YoYInflationCouponPricer):
    def __init__(
        self,
        capletVol: Handle[YoYOptionletVolatilitySurface],
        nominalTermStructure: Handle[YieldTermStructure],
    ) -> None: ...

class BachelierYoYInflationCouponPricer(YoYInflationCouponPricer):
    def __init__(
        self,
        capletVol: Handle[YoYOptionletVolatilitySurface],
        nominalTermStructure: Handle[YieldTermStructure],
    ) -> None: ...

class ZeroCouponInflationSwap(Swap):
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        start: Date,
        maturity: Date,
        calendar: Calendar,
        convention: BusinessDayConvention,
        dayCounter: DayCounter,
        fixedRate: float,
        index: ZeroInflationIndex,
        lag: Period,
        observationInterpolation: CPI.InterpolationType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        start: Date,
        maturity: Date,
        calendar: Calendar,
        convention: BusinessDayConvention,
        dayCounter: DayCounter,
        fixedRate: float,
        index: ZeroInflationIndex,
        lag: Period,
        observationInterpolation: CPI.InterpolationType,
        adjustInfObsDates: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        start: Date,
        maturity: Date,
        calendar: Calendar,
        convention: BusinessDayConvention,
        dayCounter: DayCounter,
        fixedRate: float,
        index: ZeroInflationIndex,
        lag: Period,
        observationInterpolation: CPI.InterpolationType,
        adjustInfObsDates: bool,
        infCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        start: Date,
        maturity: Date,
        calendar: Calendar,
        convention: BusinessDayConvention,
        dayCounter: DayCounter,
        fixedRate: float,
        index: ZeroInflationIndex,
        lag: Period,
        observationInterpolation: CPI.InterpolationType,
        adjustInfObsDates: bool,
        infCalendar: Calendar,
        infConvention: BusinessDayConvention,
    ) -> None: ...
    def fairRate(self) -> float: ...
    def fixedLegNPV(self) -> float: ...
    def fixedLegBPS(self) -> float: ...
    def inflationLegNPV(self) -> float: ...
    def fixedLeg(self) -> list[CashFlow]: ...
    def inflationLeg(self) -> list[CashFlow]: ...
    def type(self) -> Swap.Type: ...

class YearOnYearInflationSwap(Swap):
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDayCounter: DayCounter,
        yoySchedule: Schedule,
        index: YoYInflationIndex,
        lag: Period,
        interpolation: CPI.InterpolationType,
        spread: float,
        yoyDayCounter: DayCounter,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        fixedSchedule: Schedule,
        fixedRate: float,
        fixedDayCounter: DayCounter,
        yoySchedule: Schedule,
        index: YoYInflationIndex,
        lag: Period,
        interpolation: CPI.InterpolationType,
        spread: float,
        yoyDayCounter: DayCounter,
        paymentCalendar: Calendar,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    def fairRate(self) -> float: ...
    def fixedLegNPV(self) -> float: ...
    def yoyLegNPV(self) -> float: ...
    def fairSpread(self) -> float: ...
    def fixedLeg(self) -> Leg: ...
    def yoyLeg(self) -> Leg: ...

class CPISwap(Swap):
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        subtractInflationNominal: bool,
        spread: float,
        floatDayCount: DayCounter,
        floatSchedule: Schedule,
        floatRoll: BusinessDayConvention,
        fixingDays: int,
        floatIndex: IborIndex,
        fixedRate: float,
        baseCPI: float,
        fixedDayCount: DayCounter,
        fixedSchedule: Schedule,
        fixedRoll: BusinessDayConvention,
        observationLag: Period,
        fixedIndex: ZeroInflationIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        subtractInflationNominal: bool,
        spread: float,
        floatDayCount: DayCounter,
        floatSchedule: Schedule,
        floatRoll: BusinessDayConvention,
        fixingDays: int,
        floatIndex: IborIndex,
        fixedRate: float,
        baseCPI: float,
        fixedDayCount: DayCounter,
        fixedSchedule: Schedule,
        fixedRoll: BusinessDayConvention,
        observationLag: Period,
        fixedIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: Swap.Type,
        nominal: float,
        subtractInflationNominal: bool,
        spread: float,
        floatDayCount: DayCounter,
        floatSchedule: Schedule,
        floatRoll: BusinessDayConvention,
        fixingDays: int,
        floatIndex: IborIndex,
        fixedRate: float,
        baseCPI: float,
        fixedDayCount: DayCounter,
        fixedSchedule: Schedule,
        fixedRoll: BusinessDayConvention,
        observationLag: Period,
        fixedIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        inflationNominal: float,
    ) -> None: ...
    def fairRate(self) -> float: ...
    def floatLegNPV(self) -> float: ...
    def fairSpread(self) -> float: ...
    def fixedLegNPV(self) -> float: ...
    def cpiLeg(self) -> Leg: ...
    def floatLeg(self) -> Leg: ...

class YoYInflationCapFloor(Instrument):
    class Type(IntEnum):
        Cap
        Floor
        Collar

    def __init__(
        self,
        type: YoYInflationCapFloor.Type,
        yoyLeg: Leg,
        strikes: list[float],
    ) -> None: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        curve: Handle[YoYInflationTermStructure],
        guess: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        curve: Handle[YoYInflationTermStructure],
        guess: float,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        curve: Handle[YoYInflationTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        curve: Handle[YoYInflationTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        curve: Handle[YoYInflationTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...

class YoYInflationCap(YoYInflationCapFloor):
    def __init__(
        self,
        leg: list[CashFlow],
        capRates: list[float],
    ) -> None: ...

class YoYInflationFloor(YoYInflationCapFloor):
    def __init__(
        self,
        leg: list[CashFlow],
        floorRates: list[float],
    ) -> None: ...

class YoYInflationCollar(YoYInflationCapFloor):
    def __init__(
        self,
        leg: list[CashFlow],
        capRates: list[float],
        floorRates: list[float],
    ) -> None: ...

class YoYCapFloorTermPriceSurface(TermStructure):
    def __init__(self) -> None: ...
    def atmYoYSwapTimeRates(self) -> tuple[std.vector[Time)>,std.vector<(Rate]]: ...
    def atmYoYSwapDateRates(self) -> tuple[std.vector[Date)>,std.vector<(Rate]]: ...
    def YoYTS(self) -> YoYInflationTermStructure: ...
    def yoyIndex(self) -> YoYInflationIndex: ...
    def businessDayConvention(self) -> BusinessDayConvention: ...
    def observationLag(self) -> Period: ...
    def frequency(self) -> Frequency: ...
    def fixingDays(self) -> int: ...
    @overload
    def price(
        self,
        d: Date,
        k: float,
    ) -> float: ...
    @overload
    def price(
        self,
        d: Period,
        k: float,
    ) -> float: ...
    @overload
    def capPrice(
        self,
        d: Date,
        k: float,
    ) -> float: ...
    @overload
    def capPrice(
        self,
        d: Period,
        k: float,
    ) -> float: ...
    @overload
    def floorPrice(
        self,
        d: Date,
        k: float,
    ) -> float: ...
    @overload
    def floorPrice(
        self,
        d: Period,
        k: float,
    ) -> float: ...
    @overload
    def atmYoYSwapRate(
        self,
        d: Date,
    ) -> float: ...
    @overload
    def atmYoYSwapRate(
        self,
        d: Date,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def atmYoYSwapRate(
        self,
        d: Period,
    ) -> float: ...
    @overload
    def atmYoYSwapRate(
        self,
        d: Period,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def atmYoYRate(
        self,
        d: Date,
    ) -> float: ...
    @overload
    def atmYoYRate(
        self,
        d: Date,
        obsLag: Period,
    ) -> float: ...
    @overload
    def atmYoYRate(
        self,
        d: Date,
        obsLag: Period,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def atmYoYRate(
        self,
        d: Period,
    ) -> float: ...
    @overload
    def atmYoYRate(
        self,
        d: Period,
        obsLag: Period,
    ) -> float: ...
    @overload
    def atmYoYRate(
        self,
        d: Period,
        obsLag: Period,
        extrapolate: bool,
    ) -> float: ...
    def baseDate(self) -> Date: ...
    def strikes(self) -> list[float]: ...
    def capStrikes(self) -> list[float]: ...
    def floorStrikes(self) -> list[float]: ...
    def maturities(self) -> list[Period]: ...
    def minStrike(self) -> float: ...
    def maxStrike(self) -> float: ...
    def minMaturity(self) -> Date: ...
    def maxMaturity(self) -> Date: ...
    def yoyOptionDateFromTenor(
        self,
        p: Period,
    ) -> Date: ...

class YoYInflationCapFloorTermPriceSurface(YoYCapFloorTermPriceSurface):
    @overload
    def __init__(
        self,
        fixingDays: int,
        yyLag: Period,
        yii: YoYInflationIndex,
        interpolation: CPI.InterpolationType,
        nominal: Handle[YieldTermStructure],
        dc: DayCounter,
        cal: Calendar,
        bdc: BusinessDayConvention,
        cStrikes: list[float],
        fStrikes: list[float],
        cfMaturities: list[Period],
        cPrice: Matrix,
        fPrice: Matrix,
    ) -> None: ...
    @overload
    def __init__(
        self,
        fixingDays: int,
        yyLag: Period,
        yii: YoYInflationIndex,
        interpolation: CPI.InterpolationType,
        nominal: Handle[YieldTermStructure],
        dc: DayCounter,
        cal: Calendar,
        bdc: BusinessDayConvention,
        cStrikes: list[float],
        fStrikes: list[float],
        cfMaturities: list[Period],
        cPrice: Matrix,
        fPrice: Matrix,
        interpolator2d: Bicubic,
    ) -> None: ...
    @overload
    def __init__(
        self,
        fixingDays: int,
        yyLag: Period,
        yii: YoYInflationIndex,
        interpolation: CPI.InterpolationType,
        nominal: Handle[YieldTermStructure],
        dc: DayCounter,
        cal: Calendar,
        bdc: BusinessDayConvention,
        cStrikes: list[float],
        fStrikes: list[float],
        cfMaturities: list[Period],
        cPrice: Matrix,
        fPrice: Matrix,
        interpolator2d: Bicubic,
        interpolator1d: Cubic,
    ) -> None: ...

class YoYInflationBlackCapFloorEngine(PricingEngine):
    def __init__(
        self,
        arg0: YoYInflationIndex,
        vol: Handle[YoYOptionletVolatilitySurface],
        nominalTermStructure: Handle[YieldTermStructure],
    ) -> None: ...

class YoYInflationUnitDisplacedBlackCapFloorEngine(PricingEngine):
    def __init__(
        self,
        arg0: YoYInflationIndex,
        vol: Handle[YoYOptionletVolatilitySurface],
        nominalTermStructure: Handle[YieldTermStructure],
    ) -> None: ...

class YoYInflationBachelierCapFloorEngine(PricingEngine):
    def __init__(
        self,
        arg0: YoYInflationIndex,
        vol: Handle[YoYOptionletVolatilitySurface],
        nominalTermStructure: Handle[YieldTermStructure],
    ) -> None: ...

class YoYOptionletHelper(BootstrapHelper[YoYOptionletVolatilitySurface]):
    pass

class YoYOptionletStripper:
    def __init__(self) -> None: ...
    def maxStrike(self) -> float: ...
    def strikes(self) -> list[float]: ...
    def slice(
        self,
        d: Date,
    ) -> tuple[std.vector[Rate)>,std.vector<(Volatility]]: ...

class ShortRateModel(CalibratedModel):
    def __init__(self) -> None: ...

class OneFactorAffineModel(ShortRateModel):
    def __init__(self) -> None: ...
    def discount(
        self,
        t: float,
    ) -> float: ...
    @overload
    def discountBond(
        self,
        now: float,
        maturity: float,
        factors: Array,
    ) -> float: ...
    @overload
    def discountBond(
        self,
        now: float,
        maturity: float,
        rate: float,
    ) -> float: ...
    def discountBondOption(
        self,
        type: Option.Type,
        strike: float,
        maturity: float,
        bondMaturity: float,
    ) -> float: ...

class Vasicek(OneFactorAffineModel):
    @overload
    def __init__(
        self,
        r0: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        r0: float,
        a: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        r0: float,
        a: float,
        b: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        r0: float,
        a: float,
        b: float,
        sigma: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        r0: float,
        a: float,
        b: float,
        sigma: float,
        lambda_: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class HullWhite(Vasicek):
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        a: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        a: float,
        sigma: float,
    ) -> None: ...
    def convexityBias(
        self,
        futurePrice: float,
        t: float,
        T: float,
        sigma: float,
        a: float,
    ) -> float: ...
    def termStructure(self) -> Handle[YieldTermStructure]: ...

class BlackKarasinski(ShortRateModel):
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        a: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        a: float,
        sigma: float,
    ) -> None: ...
    def termStructure(self) -> Handle[YieldTermStructure]: ...

class CoxIngersollRoss(OneFactorAffineModel):
    @overload
    def __init__(
        self,
        r0: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        r0: float,
        theta: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        r0: float,
        theta: float,
        k: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        r0: float,
        theta: float,
        k: float,
        sigma: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class ExtendedCoxIngersollRoss(CoxIngersollRoss):
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        theta: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        theta: float,
        k: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        theta: float,
        k: float,
        sigma: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        theta: float,
        k: float,
        sigma: float,
        x0: float,
    ) -> None: ...
    def termStructure(self) -> Handle[YieldTermStructure]: ...

class G2(ShortRateModel):
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        a: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        a: float,
        sigma: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        a: float,
        sigma: float,
        b: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        a: float,
        sigma: float,
        b: float,
        eta: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        a: float,
        sigma: float,
        b: float,
        eta: float,
        rho: float,
    ) -> None: ...
    def termStructure(self) -> Handle[YieldTermStructure]: ...
    def discount(
        self,
        t: float,
    ) -> float: ...
    def discountBond(
        self,
        now: float,
        maturity: float,
        factors: Array,
    ) -> float: ...
    def discountBondOption(
        self,
        type: Option.Type,
        strike: float,
        maturity: float,
        bondMaturity: float,
    ) -> float: ...

class JamshidianSwaptionEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: OneFactorAffineModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: OneFactorAffineModel,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...

class TreeSwaptionEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: Handle[ShortRateModel],
        timeSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Handle[ShortRateModel],
        timeSteps: int,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        grid: TimeGrid,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        grid: TimeGrid,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        timeSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        timeSteps: int,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...

class AnalyticCapFloorEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: OneFactorAffineModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: OneFactorAffineModel,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...

class TreeCapFloorEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        grid: TimeGrid,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        grid: TimeGrid,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        timeSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        timeSteps: int,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...

class G2SwaptionEngine(PricingEngine):
    def __init__(
        self,
        model: G2,
        range: float,
        intervals: int,
    ) -> None: ...

class FdG2SwaptionEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: G2,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: G2,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: G2,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: G2,
        tGrid: int,
        xGrid: int,
        yGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: G2,
        tGrid: int,
        xGrid: int,
        yGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: G2,
        tGrid: int,
        xGrid: int,
        yGrid: int,
        dampingSteps: int,
        invEps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: G2,
        tGrid: int,
        xGrid: int,
        yGrid: int,
        dampingSteps: int,
        invEps: float,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class FdHullWhiteSwaptionEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: HullWhite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HullWhite,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HullWhite,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HullWhite,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HullWhite,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        invEps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: HullWhite,
        tGrid: int,
        xGrid: int,
        dampingSteps: int,
        invEps: float,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class AnalyticBSMHullWhiteEngine(PricingEngine):
    def __init__(
        self,
        equityShortRateCorrelation: float,
        arg1: GeneralizedBlackScholesProcess,
        arg2: HullWhite,
    ) -> None: ...

class BondPrice:
    class Type(IntEnum):
        Dirty
        Clean

    def __init__(
        self,
        amount: float,
        type: BondPrice.Type,
    ) -> None: ...
    def amount(self) -> float: ...
    def type(self) -> BondPrice.Type: ...
    def isValid(self) -> bool: ...

class Bond(Instrument):
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        faceAmount: float,
        maturityDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        faceAmount: float,
        maturityDate: Date,
        issueDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        faceAmount: float,
        maturityDate: Date,
        issueDate: Date,
        cashflows: Leg,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        issueDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        issueDate: Date,
        coupons: Leg,
    ) -> None: ...
    @overload
    def nextCouponRate(
        self,
        d: Date,
    ) -> float: ...
    @overload
    def nextCouponRate(self) -> float: ...
    @overload
    def previousCouponRate(
        self,
        d: Date,
    ) -> float: ...
    @overload
    def previousCouponRate(self) -> float: ...
    @overload
    def nextCashFlowDate(
        self,
        d: Date,
    ) -> Date: ...
    @overload
    def nextCashFlowDate(self) -> Date: ...
    @overload
    def previousCashFlowDate(
        self,
        d: Date,
    ) -> Date: ...
    @overload
    def previousCashFlowDate(self) -> Date: ...
    def settlementDays(self) -> int: ...
    @overload
    def settlementDate(
        self,
        d: Date,
    ) -> Date: ...
    @overload
    def settlementDate(self) -> Date: ...
    @overload
    def isTradable(
        self,
        d: Date,
    ) -> bool: ...
    @overload
    def isTradable(self) -> bool: ...
    def startDate(self) -> Date: ...
    def maturityDate(self) -> Date: ...
    def issueDate(self) -> Date: ...
    def cashflows(self) -> list[CashFlow]: ...
    def redemptions(self) -> list[CashFlow]: ...
    def redemption(self) -> CashFlow: ...
    def calendar(self) -> Calendar: ...
    def notionals(self) -> list[float]: ...
    @overload
    def notional(
        self,
        d: Date,
    ) -> float: ...
    @overload
    def notional(self) -> float: ...
    @overload
    def cleanPrice(
        self,
        yield_: float,
        dc: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def cleanPrice(
        self,
        yield_: float,
        dc: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlement: Date,
    ) -> float: ...
    @overload
    def cleanPrice(self) -> float: ...
    @overload
    def dirtyPrice(
        self,
        yield_: float,
        dc: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def dirtyPrice(
        self,
        yield_: float,
        dc: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlement: Date,
    ) -> float: ...
    @overload
    def dirtyPrice(self) -> float: ...
    @overload
    def yield_(
        self,
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
    ) -> float: ...
    @overload
    def yield_(
        self,
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        accuracy: float,
    ) -> float: ...
    @overload
    def yield_(
        self,
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def yield_(
        self,
        price: BondPrice,
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
    ) -> float: ...
    @overload
    def yield_(
        self,
        price: BondPrice,
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        settlement: Date,
    ) -> float: ...
    @overload
    def yield_(
        self,
        price: BondPrice,
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        settlement: Date,
        accuracy: float,
    ) -> float: ...
    @overload
    def yield_(
        self,
        price: BondPrice,
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        settlement: Date,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def yield_(
        self,
        price: BondPrice,
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        settlement: Date,
        accuracy: float,
        maxEvaluations: int,
        guess: float,
    ) -> float: ...
    @overload
    def accruedAmount(
        self,
        settlement: Date,
    ) -> float: ...
    @overload
    def accruedAmount(self) -> float: ...
    @overload
    def settlementValue(
        self,
        cleanPrice: float,
    ) -> float: ...
    @overload
    def settlementValue(self) -> float: ...

class ZeroCouponBond(Bond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        faceAmount: float,
        maturityDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        faceAmount: float,
        maturityDate: Date,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        faceAmount: float,
        maturityDate: Date,
        paymentConvention: BusinessDayConvention,
        redemption: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        faceAmount: float,
        maturityDate: Date,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
    ) -> None: ...

class FixedRateBond(Bond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
    ) -> None: ...
    def frequency(self) -> Frequency: ...
    def dayCounter(self) -> DayCounter: ...

class AmortizingFixedRateBond(Bond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        exCouponPeriod: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
        redemptions: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
        redemptions: list[float],
        paymentLag: int,
    ) -> None: ...
    def frequency(self) -> Frequency: ...
    def dayCounter(self) -> DayCounter: ...

class AmortizingFloatingRateBond(Bond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        issueDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        issueDate: Date,
        exCouponPeriod: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
        redemptions: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notional: list[float],
        schedule: Schedule,
        index: IborIndex,
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
        redemptions: list[float],
        paymentLag: int,
    ) -> None: ...

class FloatingRateBond(Bond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        redemption: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        redemption: float,
        issueDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        redemption: float,
        issueDate: Date,
        exCouponPeriod: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        redemption: float,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        redemption: float,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: IborIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        redemption: float,
        issueDate: Date,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
    ) -> None: ...

class CmsRateBond(Bond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        redemption: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        redemption: float,
        issueDate: Date,
    ) -> None: ...

class AmortizingCmsRateBond(Bond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        notionals: list[float],
        schedule: Schedule,
        index: SwapIndex,
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        fixingDays: int,
        gearings: list[float],
        spreads: list[float],
        caps: list[float],
        floors: list[float],
        inArrears: bool,
        issueDate: Date,
    ) -> None: ...

class DiscountingBondEngine(PricingEngine):
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...

class Callability:
    class Type(IntEnum):
        Call
        Put

    def __init__(
        self,
        price: BondPrice,
        type: Callability.Type,
        date: Date,
    ) -> None: ...
    def price(self) -> BondPrice: ...
    def type(self) -> Callability.Type: ...
    def date(self) -> Date: ...

class SoftCallability(Callability):
    def __init__(
        self,
        price: BondPrice,
        date: Date,
        trigger: float,
    ) -> None: ...

class CallableBond(Bond):
    def __init__(self) -> None: ...
    def callability(self) -> list[Callability]: ...
    def impliedVolatility(
        self,
        targetPrice: BondPrice,
        discountCurve: Handle[YieldTermStructure],
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...
    @overload
    def OAS(
        self,
        cleanPrice: float,
        engineTS: Handle[YieldTermStructure],
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
    ) -> float: ...
    @overload
    def OAS(
        self,
        cleanPrice: float,
        engineTS: Handle[YieldTermStructure],
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def OAS(
        self,
        cleanPrice: float,
        engineTS: Handle[YieldTermStructure],
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        settlementDate: Date,
        accuracy: float,
    ) -> float: ...
    @overload
    def OAS(
        self,
        cleanPrice: float,
        engineTS: Handle[YieldTermStructure],
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        settlementDate: Date,
        accuracy: float,
        maxIterations: int,
    ) -> float: ...
    @overload
    def OAS(
        self,
        cleanPrice: float,
        engineTS: Handle[YieldTermStructure],
        dc: DayCounter,
        compounding: Compounding,
        freq: Frequency,
        settlementDate: Date,
        accuracy: float,
        maxIterations: int,
        guess: float,
    ) -> float: ...
    @overload
    def cleanPriceOAS(
        self,
        oas: float,
        engineTS: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def cleanPriceOAS(
        self,
        oas: float,
        engineTS: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def effectiveDuration(
        self,
        oas: float,
        engineTS: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def effectiveDuration(
        self,
        oas: float,
        engineTS: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        bump: float,
    ) -> float: ...
    @overload
    def effectiveConvexity(
        self,
        oas: float,
        engineTS: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def effectiveConvexity(
        self,
        oas: float,
        engineTS: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        bump: float,
    ) -> float: ...

class CallableFixedRateBond(CallableBond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        putCallSchedule: list[Callability],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        putCallSchedule: list[Callability],
        exCouponPeriod: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        putCallSchedule: list[Callability],
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        putCallSchedule: list[Callability],
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        putCallSchedule: list[Callability],
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
    ) -> None: ...

class CallableZeroCouponBond(CallableBond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        calendar: Calendar,
        maturityDate: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        calendar: Calendar,
        maturityDate: Date,
        dayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        calendar: Calendar,
        maturityDate: Date,
        dayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        calendar: Calendar,
        maturityDate: Date,
        dayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        calendar: Calendar,
        maturityDate: Date,
        dayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        putCallSchedule: list[Callability],
    ) -> None: ...

class TreeCallableFixedRateBondEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        grid: TimeGrid,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        grid: TimeGrid,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        timeSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: ShortRateModel,
        timeSteps: int,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...

class BlackCallableFixedRateBondEngine(PricingEngine):
    def __init__(
        self,
        fwdYieldVol: Handle[Quote],
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...

class CPIBond(Bond):
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        growthOnly: bool,
        baseCPI: float,
        observationLag: Period,
        cpiIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        growthOnly: bool,
        baseCPI: float,
        observationLag: Period,
        cpiIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        growthOnly: bool,
        baseCPI: float,
        observationLag: Period,
        cpiIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        growthOnly: bool,
        baseCPI: float,
        observationLag: Period,
        cpiIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        growthOnly: bool,
        baseCPI: float,
        observationLag: Period,
        cpiIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        growthOnly: bool,
        baseCPI: float,
        observationLag: Period,
        cpiIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        growthOnly: bool,
        baseCPI: float,
        observationLag: Period,
        cpiIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        faceAmount: float,
        growthOnly: bool,
        baseCPI: float,
        observationLag: Period,
        cpiIndex: ZeroInflationIndex,
        observationInterpolation: CPI.InterpolationType,
        schedule: Schedule,
        coupons: list[float],
        accrualDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
    ) -> None: ...

class BondFunctions:
    def __init__(self) -> None: ...
    def startDate(
        self,
        bond: Bond,
    ) -> Date: ...
    def maturityDate(
        self,
        bond: Bond,
    ) -> Date: ...
    @overload
    def isTradable(
        self,
        bond: Bond,
    ) -> bool: ...
    @overload
    def isTradable(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> bool: ...
    @overload
    def previousCashFlowDate(
        self,
        bond: Bond,
    ) -> Date: ...
    @overload
    def previousCashFlowDate(
        self,
        bond: Bond,
        refDate: Date,
    ) -> Date: ...
    @overload
    def nextCashFlowDate(
        self,
        bond: Bond,
    ) -> Date: ...
    @overload
    def nextCashFlowDate(
        self,
        bond: Bond,
        refDate: Date,
    ) -> Date: ...
    @overload
    def previousCashFlowAmount(
        self,
        bond: Bond,
    ) -> float: ...
    @overload
    def previousCashFlowAmount(
        self,
        bond: Bond,
        refDate: Date,
    ) -> float: ...
    @overload
    def nextCashFlowAmount(
        self,
        bond: Bond,
    ) -> float: ...
    @overload
    def nextCashFlowAmount(
        self,
        bond: Bond,
        refDate: Date,
    ) -> float: ...
    @overload
    def previousCouponRate(
        self,
        bond: Bond,
    ) -> float: ...
    @overload
    def previousCouponRate(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def nextCouponRate(
        self,
        bond: Bond,
    ) -> float: ...
    @overload
    def nextCouponRate(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def accrualStartDate(
        self,
        bond: Bond,
    ) -> Date: ...
    @overload
    def accrualStartDate(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> Date: ...
    @overload
    def accrualEndDate(
        self,
        bond: Bond,
    ) -> Date: ...
    @overload
    def accrualEndDate(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> Date: ...
    @overload
    def accrualPeriod(
        self,
        bond: Bond,
    ) -> float: ...
    @overload
    def accrualPeriod(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def accrualDays(
        self,
        bond: Bond,
    ) -> int: ...
    @overload
    def accrualDays(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> int: ...
    @overload
    def accruedPeriod(
        self,
        bond: Bond,
    ) -> float: ...
    @overload
    def accruedPeriod(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def accruedDays(
        self,
        bond: Bond,
    ) -> int: ...
    @overload
    def accruedDays(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> int: ...
    @overload
    def accruedAmount(
        self,
        bond: Bond,
    ) -> float: ...
    @overload
    def accruedAmount(
        self,
        bond: Bond,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def cleanPrice(
        self,
        bond: Bond,
        discount: YieldTermStructure,
        zSpread: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def cleanPrice(
        self,
        bond: Bond,
        discount: YieldTermStructure,
        zSpread: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def cleanPrice(
        self,
        bond: Bond,
        discountCurve: YieldTermStructure,
    ) -> float: ...
    @overload
    def cleanPrice(
        self,
        bond: Bond,
        discountCurve: YieldTermStructure,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def cleanPrice(
        self,
        bond: Bond,
        yield_: InterestRate,
    ) -> float: ...
    @overload
    def cleanPrice(
        self,
        bond: Bond,
        yield_: InterestRate,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def cleanPrice(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def cleanPrice(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def dirtyPrice(
        self,
        bond: Bond,
        discount: YieldTermStructure,
        zSpread: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def dirtyPrice(
        self,
        bond: Bond,
        discount: YieldTermStructure,
        zSpread: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def dirtyPrice(
        self,
        bond: Bond,
        discountCurve: YieldTermStructure,
    ) -> float: ...
    @overload
    def dirtyPrice(
        self,
        bond: Bond,
        discountCurve: YieldTermStructure,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def bps(
        self,
        bond: Bond,
        discountCurve: YieldTermStructure,
    ) -> float: ...
    @overload
    def bps(
        self,
        bond: Bond,
        discountCurve: YieldTermStructure,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def bps(
        self,
        bond: Bond,
        yield_: InterestRate,
    ) -> float: ...
    @overload
    def bps(
        self,
        bond: Bond,
        yield_: InterestRate,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def bps(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def bps(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def atmRate(
        self,
        bond: Bond,
        discountCurve: YieldTermStructure,
    ) -> float: ...
    @overload
    def atmRate(
        self,
        bond: Bond,
        discountCurve: YieldTermStructure,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def atmRate(
        self,
        bond: Bond,
        discountCurve: YieldTermStructure,
        settlementDate: Date,
        price: BondPrice,
    ) -> float: ...
    @overload
    def yield_(
        self,
        bond: Bond,
        price: BondPrice,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def yield_(
        self,
        bond: Bond,
        price: BondPrice,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def yield_(
        self,
        bond: Bond,
        price: BondPrice,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
        accuracy: float,
    ) -> float: ...
    @overload
    def yield_(
        self,
        bond: Bond,
        price: BondPrice,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
        accuracy: float,
        maxIterations: int,
    ) -> float: ...
    @overload
    def yield_(
        self,
        bond: Bond,
        price: BondPrice,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
        accuracy: float,
        maxIterations: int,
        guess: float,
    ) -> float: ...
    @overload
    def duration(
        self,
        bond: Bond,
        yield_: InterestRate,
    ) -> float: ...
    @overload
    def duration(
        self,
        bond: Bond,
        yield_: InterestRate,
        type: Duration.Type,
    ) -> float: ...
    @overload
    def duration(
        self,
        bond: Bond,
        yield_: InterestRate,
        type: Duration.Type,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def duration(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def duration(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        type: Duration.Type,
    ) -> float: ...
    @overload
    def duration(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        type: Duration.Type,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def convexity(
        self,
        bond: Bond,
        yield_: InterestRate,
    ) -> float: ...
    @overload
    def convexity(
        self,
        bond: Bond,
        yield_: InterestRate,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def convexity(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def convexity(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        bond: Bond,
        yield_: InterestRate,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        bond: Bond,
        yield_: InterestRate,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def basisPointValue(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def yieldValueBasisPoint(
        self,
        bond: Bond,
        yield_: InterestRate,
    ) -> float: ...
    @overload
    def yieldValueBasisPoint(
        self,
        bond: Bond,
        yield_: InterestRate,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def yieldValueBasisPoint(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def yieldValueBasisPoint(
        self,
        bond: Bond,
        yield_: float,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        bond: Bond,
        price: BondPrice,
        discountCurve: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        bond: Bond,
        price: BondPrice,
        discountCurve: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        bond: Bond,
        price: BondPrice,
        discountCurve: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
        accuracy: float,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        bond: Bond,
        price: BondPrice,
        discountCurve: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
        accuracy: float,
        maxIterations: int,
    ) -> float: ...
    @overload
    def zSpread(
        self,
        bond: Bond,
        price: BondPrice,
        discountCurve: YieldTermStructure,
        dayCounter: DayCounter,
        compounding: Compounding,
        frequency: Frequency,
        settlementDate: Date,
        accuracy: float,
        maxIterations: int,
        guess: float,
    ) -> float: ...

class BlackCalibrationHelper(CalibrationHelper):
    class CalibrationErrorType(IntEnum):
        RelativePriceError
        PriceError
        ImpliedVolError

    def __init__(self) -> None: ...
    def setPricingEngine(
        self,
        engine: PricingEngine,
    ) -> None: ...
    def marketValue(self) -> float: ...
    def modelValue(self) -> float: ...
    def impliedVolatility(
        self,
        targetValue: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...
    def blackPrice(
        self,
        volatility: float,
    ) -> float: ...
    def volatility(self) -> Handle[Quote]: ...
    def volatilityType(self) -> VolatilityType: ...
    def calibrationError(self) -> float: ...

class SwaptionHelper(BlackCalibrationHelper):
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        endDate: Date,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        endDate: Date,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        endDate: Date,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        endDate: Date,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        endDate: Date,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        endDate: Date,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        endDate: Date,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
        shift: float,
        settlementDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        endDate: Date,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
        shift: float,
        settlementDays: int,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
        shift: float,
        settlementDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseDate: Date,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
        shift: float,
        settlementDays: int,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maturity: Period,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        maturity: Period,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maturity: Period,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maturity: Period,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maturity: Period,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maturity: Period,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
        shift: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maturity: Period,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
        shift: float,
        settlementDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maturity: Period,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegTenor: Period,
        fixedLegDayCounter: DayCounter,
        floatingLegDayCounter: DayCounter,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        strike: float,
        nominal: float,
        type: VolatilityType,
        shift: float,
        settlementDays: int,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    def underlying(self) -> FixedVsFloatingSwap: ...
    def swaption(self) -> Swaption: ...

class CapHelper(BlackCalibrationHelper):
    @overload
    def __init__(
        self,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegFrequency: Frequency,
        fixedLegDayCounter: DayCounter,
        includeFirstSwaplet: bool,
        termStructure: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegFrequency: Frequency,
        fixedLegDayCounter: DayCounter,
        includeFirstSwaplet: bool,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegFrequency: Frequency,
        fixedLegDayCounter: DayCounter,
        includeFirstSwaplet: bool,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        length: Period,
        volatility: Handle[Quote],
        index: IborIndex,
        fixedLegFrequency: Frequency,
        fixedLegDayCounter: DayCounter,
        includeFirstSwaplet: bool,
        termStructure: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
        type: VolatilityType,
        shift: float,
    ) -> None: ...

class HestonModelHelper(BlackCalibrationHelper):
    @overload
    def __init__(
        self,
        maturity: Period,
        calendar: Calendar,
        s0: float,
        strikePrice: float,
        volatility: Handle[Quote],
        riskFreeRate: Handle[YieldTermStructure],
        dividendYield: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        maturity: Period,
        calendar: Calendar,
        s0: float,
        strikePrice: float,
        volatility: Handle[Quote],
        riskFreeRate: Handle[YieldTermStructure],
        dividendYield: Handle[YieldTermStructure],
        errorType: BlackCalibrationHelper.CalibrationErrorType,
    ) -> None: ...

class CapFloor(Instrument):
    class Type(IntEnum):
        Cap
        Floor
        Collar

    @overload
    def impliedVolatility(
        self,
        price: float,
        disc: Handle[YieldTermStructure],
        guess: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        disc: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        disc: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        disc: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        disc: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        disc: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
        type: VolatilityType,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        disc: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
        type: VolatilityType,
        displacement: float,
    ) -> float: ...
    def floatingLeg(self) -> Leg: ...
    def capRates(self) -> list[float]: ...
    def floorRates(self) -> list[float]: ...
    def startDate(self) -> Date: ...
    def maturityDate(self) -> Date: ...
    def type(self) -> CapFloor.Type: ...
    def atmRate(
        self,
        discountCurve: YieldTermStructure,
    ) -> float: ...

class Cap(CapFloor):
    def __init__(
        self,
        leg: list[CashFlow],
        capRates: list[float],
    ) -> None: ...

class Floor(CapFloor):
    def __init__(
        self,
        leg: list[CashFlow],
        floorRates: list[float],
    ) -> None: ...

class Collar(CapFloor):
    def __init__(
        self,
        leg: list[CashFlow],
        capRates: list[float],
        floorRates: list[float],
    ) -> None: ...

class BlackCapFloorEngine(PricingEngine):
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        vol: Handle[OptionletVolatilityStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        vol: Handle[OptionletVolatilityStructure],
        displacement: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        vol: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        vol: Handle[Quote],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        vol: Handle[Quote],
        dc: DayCounter,
        displacement: float,
    ) -> None: ...

class BachelierCapFloorEngine(PricingEngine):
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        vol: Handle[OptionletVolatilityStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        vol: Handle[Quote],
    ) -> None: ...

class MakeCapFloor:
    @overload
    def __init__(
        self,
        capFloorType: CapFloor.Type,
        capFloorTenor: Period,
        iborIndex: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        capFloorType: CapFloor.Type,
        capFloorTenor: Period,
        iborIndex: IborIndex,
        strike: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        capFloorType: CapFloor.Type,
        capFloorTenor: Period,
        iborIndex: IborIndex,
        strike: Optional[float],
        forwardStart: Period,
    ) -> None: ...
    def withNominal(
        self,
        n: float,
    ) -> MakeCapFloor: ...
    def withEffectiveDate(
        self,
        arg0: Date,
        firstCapletExcluded: bool,
    ) -> MakeCapFloor: ...
    def withTenor(
        self,
        arg0: Period,
    ) -> MakeCapFloor: ...
    def withCalendar(
        self,
        arg0: Calendar,
    ) -> MakeCapFloor: ...
    def withConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeCapFloor: ...
    def withTerminationDateConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeCapFloor: ...
    def withRule(
        self,
        r: DateGeneration.Rule,
    ) -> MakeCapFloor: ...
    @overload
    def withEndOfMonth(
        self,
        flag: bool,
    ) -> MakeCapFloor: ...
    @overload
    def withEndOfMonth(self) -> MakeCapFloor: ...
    def withFirstDate(
        self,
        arg0: Date,
    ) -> MakeCapFloor: ...
    def withNextToLastDate(
        self,
        arg0: Date,
    ) -> MakeCapFloor: ...
    def withDayCount(
        self,
        arg0: DayCounter,
    ) -> MakeCapFloor: ...
    @overload
    def asOptionlet(
        self,
        b: bool,
    ) -> MakeCapFloor: ...
    @overload
    def asOptionlet(self) -> MakeCapFloor: ...
    def withPricingEngine(
        self,
        engine: PricingEngine,
    ) -> MakeCapFloor: ...

class CliquetOption(OneAssetOption):
    def __init__(
        self,
        payoff: PercentageStrikePayoff,
        maturity: EuropeanExercise,
        resetDates: list[Date],
    ) -> None: ...

class AnalyticCliquetEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticPerformanceEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class ConvertibleZeroCouponBond(Bond):
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        dayCounter: DayCounter,
        schedule: Schedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
    ) -> None: ...

class ConvertibleFixedCouponBond(Bond):
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        coupons: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        coupons: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        coupons: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
        exCouponPeriod: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        coupons: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        coupons: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        coupons: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
    ) -> None: ...

class ConvertibleFloatingRateBond(Bond):
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        index: IborIndex,
        fixingDays: int,
        spreads: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        index: IborIndex,
        fixingDays: int,
        spreads: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        index: IborIndex,
        fixingDays: int,
        spreads: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
        exCouponPeriod: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        index: IborIndex,
        fixingDays: int,
        spreads: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        index: IborIndex,
        fixingDays: int,
        spreads: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exercise: Exercise,
        conversionRatio: float,
        callability: list[Callability],
        issueDate: Date,
        settlementDays: int,
        index: IborIndex,
        fixingDays: int,
        spreads: list[float],
        dayCounter: DayCounter,
        schedule: Schedule,
        redemption: float,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
    ) -> None: ...

class Forward(Instrument):
    def __init__(self) -> None: ...
    def settlementDate(self) -> Date: ...
    def isExpired(self) -> bool: ...
    def calendar(self) -> Calendar: ...
    def businessDayConvention(self) -> BusinessDayConvention: ...
    def dayCounter(self) -> DayCounter: ...
    def discountCurve(self) -> Handle[YieldTermStructure]: ...
    def incomeDiscountCurve(self) -> Handle[YieldTermStructure]: ...
    def spotValue(self) -> float: ...
    def spotIncome(
        self,
        incomeDiscountCurve: Handle[YieldTermStructure],
    ) -> float: ...
    def forwardValue(self) -> float: ...
    def impliedYield(
        self,
        underlyingSpotValue: float,
        forwardValue: float,
        settlementDate: Date,
        compoundingConvention: Compounding,
        dayCounter: DayCounter,
    ) -> InterestRate: ...

class BondForward(Forward):
    @overload
    def __init__(
        self,
        valueDate: Date,
        maturityDate: Date,
        type: Position.Type,
        strike: float,
        settlementDays: int,
        dayCounter: DayCounter,
        calendar: Calendar,
        businessDayConvention: BusinessDayConvention,
        bond: Bond,
    ) -> None: ...
    @overload
    def __init__(
        self,
        valueDate: Date,
        maturityDate: Date,
        type: Position.Type,
        strike: float,
        settlementDays: int,
        dayCounter: DayCounter,
        calendar: Calendar,
        businessDayConvention: BusinessDayConvention,
        bond: Bond,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        valueDate: Date,
        maturityDate: Date,
        type: Position.Type,
        strike: float,
        settlementDays: int,
        dayCounter: DayCounter,
        calendar: Calendar,
        businessDayConvention: BusinessDayConvention,
        bond: Bond,
        discountCurve: Handle[YieldTermStructure],
        incomeDiscountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    def forwardPrice(self) -> float: ...
    def cleanForwardPrice(self) -> float: ...

class Futures:
    class Type(IntEnum):
        IMM
        ASX
        Custom

    def __init__(self) -> None: ...

class OvernightIndexFuture(Instrument):
    @overload
    def __init__(
        self,
        overnightIndex: OvernightIndex,
        valueDate: Date,
        maturityDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        overnightIndex: OvernightIndex,
        valueDate: Date,
        maturityDate: Date,
        convexityAdjustment: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        overnightIndex: OvernightIndex,
        valueDate: Date,
        maturityDate: Date,
        convexityAdjustment: Handle[Quote],
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    def convexityAdjustment(self) -> float: ...

class PerpetualFutures(Instrument):
    class PayoffType(IntEnum):
        Linear
        Inverse

    class FundingType(IntEnum):
        FundingWithPreviousSpot
        FundingWithCurrentSpot

    @overload
    def __init__(
        self,
        payoffType: PerpetualFutures.PayoffType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payoffType: PerpetualFutures.PayoffType,
        fundingType: PerpetualFutures.FundingType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payoffType: PerpetualFutures.PayoffType,
        fundingType: PerpetualFutures.FundingType,
        fundingFrequency: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payoffType: PerpetualFutures.PayoffType,
        fundingType: PerpetualFutures.FundingType,
        fundingFrequency: Period,
        cal: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        payoffType: PerpetualFutures.PayoffType,
        fundingType: PerpetualFutures.FundingType,
        fundingFrequency: Period,
        cal: Calendar,
        dc: DayCounter,
    ) -> None: ...

class DiscountingPerpetualFuturesEngine(PricingEngine):
    class InterpolationType(IntEnum):
        PiecewiseConstant
        Linear
        CubicSpline

    @overload
    def __init__(
        self,
        domesticDiscountCurve: Handle[YieldTermStructure],
        foreignDiscountCurve: Handle[YieldTermStructure],
        assetSpot: Handle[Quote],
        fundingTimes: list[float],
        fundingRates: list[float],
        interestRateDiffs: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        domesticDiscountCurve: Handle[YieldTermStructure],
        foreignDiscountCurve: Handle[YieldTermStructure],
        assetSpot: Handle[Quote],
        fundingTimes: list[float],
        fundingRates: list[float],
        interestRateDiffs: list[float],
        fundingInterpType: DiscountingPerpetualFuturesEngine.InterpolationType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        domesticDiscountCurve: Handle[YieldTermStructure],
        foreignDiscountCurve: Handle[YieldTermStructure],
        assetSpot: Handle[Quote],
        fundingTimes: list[float],
        fundingRates: list[float],
        interestRateDiffs: list[float],
        fundingInterpType: DiscountingPerpetualFuturesEngine.InterpolationType,
        maxT: float,
    ) -> None: ...

class Pillar:
    class Choice(IntEnum):
        MaturityDate
        LastRelevantDate
        CustomDate

    def __init__(self) -> None: ...

class RateHelper(Observable):
    def __init__(self) -> None: ...
    def quote(self) -> Handle[Quote]: ...
    def latestDate(self) -> Date: ...
    def earliestDate(self) -> Date: ...
    def maturityDate(self) -> Date: ...
    def latestRelevantDate(self) -> Date: ...
    def pillarDate(self) -> Date: ...
    def impliedQuote(self) -> float: ...
    def quoteError(self) -> float: ...

class DepositRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        fixingDate: Date,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
    ) -> None: ...

class FraRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        immOffsetStart: int,
        immOffsetEnd: int,
        iborIndex: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        immOffsetStart: int,
        immOffsetEnd: int,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        immOffsetStart: int,
        immOffsetEnd: int,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        immOffsetStart: int,
        immOffsetEnd: int,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        useIndexedCoupon: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        monthsToStart: int,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        monthsToStart: int,
        index: IborIndex,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        monthsToStart: int,
        index: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        monthsToStart: int,
        index: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        useIndexedCoupon: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        monthsToStart: int,
        monthsToEnd: int,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        monthsToStart: int,
        monthsToEnd: int,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        monthsToStart: int,
        monthsToEnd: int,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        monthsToStart: int,
        monthsToEnd: int,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        useIndexedCoupon: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        periodToStart: Period,
        iborIndex: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        periodToStart: Period,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        periodToStart: Period,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        periodToStart: Period,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        useIndexedCoupon: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        immOffsetStart: int,
        immOffsetEnd: int,
        iborIndex: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        immOffsetStart: int,
        immOffsetEnd: int,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        immOffsetStart: int,
        immOffsetEnd: int,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        immOffsetStart: int,
        immOffsetEnd: int,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        useIndexedCoupon: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        monthsToStart: int,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        monthsToStart: int,
        index: IborIndex,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        monthsToStart: int,
        index: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        monthsToStart: int,
        index: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        useIndexedCoupon: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        monthsToStart: int,
        monthsToEnd: int,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        monthsToStart: int,
        monthsToEnd: int,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        monthsToStart: int,
        monthsToEnd: int,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        monthsToStart: int,
        monthsToEnd: int,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        useIndexedCoupon: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        periodToStart: Period,
        iborIndex: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        periodToStart: Period,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        periodToStart: Period,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        periodToStart: Period,
        iborIndex: IborIndex,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        useIndexedCoupon: bool,
    ) -> None: ...

class FuturesRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        iborStartDate: Date,
        iborEndDate: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        iborStartDate: Date,
        iborEndDate: Date,
        dayCounter: DayCounter,
        convexityAdjustment: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        iborStartDate: Date,
        iborEndDate: Date,
        dayCounter: DayCounter,
        convexityAdjustment: Handle[Quote],
        type: Futures.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        iborStartDate: Date,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        iborStartDate: Date,
        index: IborIndex,
        convexityAdjustment: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        iborStartDate: Date,
        index: IborIndex,
        convexityAdjustment: Handle[Quote],
        type: Futures.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        iborStartDate: Date,
        nMonths: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        iborStartDate: Date,
        nMonths: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        convexityAdjustment: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        iborStartDate: Date,
        nMonths: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        convexityAdjustment: Handle[Quote],
        type: Futures.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        iborStartDate: Date,
        iborEndDate: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        iborStartDate: Date,
        iborEndDate: Date,
        dayCounter: DayCounter,
        convexityAdjustment: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        iborStartDate: Date,
        iborEndDate: Date,
        dayCounter: DayCounter,
        convexityAdjustment: float,
        type: Futures.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        iborStartDate: Date,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        iborStartDate: Date,
        index: IborIndex,
        convexityAdjustment: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        iborStartDate: Date,
        index: IborIndex,
        convexityAdjustment: float,
        type: Futures.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        iborStartDate: Date,
        nMonths: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        iborStartDate: Date,
        nMonths: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        convexityAdjustment: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        iborStartDate: Date,
        nMonths: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        dayCounter: DayCounter,
        convexityAdjustment: float,
        type: Futures.Type,
    ) -> None: ...
    def convexityAdjustment(self) -> float: ...

class SwapRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        index: SwapIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        index: SwapIndex,
        spread: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        pillar: Pillar.Choice,
        customPillarDate: Date,
        endOfMonth: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        pillar: Pillar.Choice,
        customPillarDate: Date,
        endOfMonth: bool,
        withIndexedCoupons: Optional[bool],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        endOfMonth: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: Handle[Quote],
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        endOfMonth: bool,
        withIndexedCoupons: Optional[bool],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        index: SwapIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        index: SwapIndex,
        spread: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        pillar: Pillar.Choice,
        customPillarDate: Date,
        endOfMonth: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        index: SwapIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        pillar: Pillar.Choice,
        customPillarDate: Date,
        endOfMonth: bool,
        withIndexedCoupons: Optional[bool],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        endOfMonth: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        tenor: Period,
        calendar: Calendar,
        fixedFrequency: Frequency,
        fixedConvention: BusinessDayConvention,
        fixedDayCount: DayCounter,
        index: IborIndex,
        spread: Handle[Quote],
        fwdStart: Period,
        discountingCurve: Handle[YieldTermStructure],
        settlementDays: int,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        endOfMonth: bool,
        withIndexedCoupons: Optional[bool],
    ) -> None: ...
    def spread(self) -> float: ...
    def swap(self) -> VanillaSwap: ...

class BondHelper(RateHelper):
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        bond: Bond,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        bond: Bond,
        priceType: BondPrice.Type,
    ) -> None: ...
    def bond(self) -> Bond: ...

class FixedRateBondHelper(BondHelper):
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cleanPrice: Handle[Quote],
        settlementDays: int,
        faceAmount: float,
        schedule: Schedule,
        coupons: list[float],
        paymentDayCounter: DayCounter,
        paymentConvention: BusinessDayConvention,
        redemption: float,
        issueDate: Date,
        paymentCalendar: Calendar,
        exCouponPeriod: Period,
        exCouponCalendar: Calendar,
        exCouponConvention: BusinessDayConvention,
        exCouponEndOfMonth: bool,
        priceType: BondPrice.Type,
    ) -> None: ...

class OISRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
        lockoutDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
        pricer: FloatingRateCouponPricer,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
        pricer: FloatingRateCouponPricer,
        rule: DateGeneration.Rule,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
        pricer: FloatingRateCouponPricer,
        rule: DateGeneration.Rule,
        overnightCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        tenor: Period,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        forwardStart: Period,
        overnightSpread: float,
        pillar: Pillar.Choice,
        customPillarDate: Date,
        averagingMethod: RateAveraging.Type,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
        pricer: FloatingRateCouponPricer,
        rule: DateGeneration.Rule,
        overnightCalendar: Calendar,
        convention: BusinessDayConvention,
    ) -> None: ...
    def swap(self) -> OvernightIndexedSwap: ...

class DatedOISRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        overnightSpread: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        overnightSpread: float,
        endOfMonth: Optional[bool],
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        overnightSpread: float,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        overnightSpread: float,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        overnightSpread: float,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        overnightSpread: float,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
        lockoutDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        overnightSpread: float,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        startDate: Date,
        endDate: Date,
        rate: Handle[Quote],
        index: OvernightIndex,
        discountingCurve: Handle[YieldTermStructure],
        telescopicValueDates: bool,
        averagingMethod: RateAveraging.Type,
        paymentLag: int,
        paymentConvention: BusinessDayConvention,
        paymentFrequency: Frequency,
        paymentCalendar: Calendar,
        overnightSpread: float,
        endOfMonth: Optional[bool],
        fixedPaymentFrequency: Optional[Frequency],
        fixedCalendar: Calendar,
        lookbackDays: int,
        lockoutDays: int,
        applyObservationShift: bool,
        pricer: FloatingRateCouponPricer,
    ) -> None: ...
    def swap(self) -> OvernightIndexedSwap: ...

class FxSwapRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        fwdPoint: Handle[Quote],
        spotFx: Handle[Quote],
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        isFxBaseCurrencyCollateralCurrency: bool,
        collateralCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        fwdPoint: Handle[Quote],
        spotFx: Handle[Quote],
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        isFxBaseCurrencyCollateralCurrency: bool,
        collateralCurve: Handle[YieldTermStructure],
        tradingCalendar: Calendar,
    ) -> None: ...
    def spot(self) -> float: ...
    def tenor(self) -> Period: ...
    def fixingDays(self) -> int: ...
    def calendar(self) -> Calendar: ...
    def businessDayConvention(self) -> BusinessDayConvention: ...
    def endOfMonth(self) -> bool: ...
    def isFxBaseCurrencyCollateralCurrency(self) -> bool: ...
    def tradingCalendar(self) -> Calendar: ...
    def adjustmentCalendar(self) -> Calendar: ...

class OvernightIndexFutureRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        valueDate: Date,
        maturityDate: Date,
        index: OvernightIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        valueDate: Date,
        maturityDate: Date,
        index: OvernightIndex,
        convexityAdjustment: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        valueDate: Date,
        maturityDate: Date,
        index: OvernightIndex,
        convexityAdjustment: Handle[Quote],
        averagingMethod: RateAveraging.Type,
    ) -> None: ...
    def convexityAdjustment(self) -> float: ...

class SofrFutureRateHelper(OvernightIndexFutureRateHelper):
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        referenceMonth: Month,
        referenceYear: int,
        referenceFreq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: Handle[Quote],
        referenceMonth: Month,
        referenceYear: int,
        referenceFreq: Frequency,
        convexityAdjustment: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        referenceMonth: Month,
        referenceYear: int,
        referenceFreq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        price: float,
        referenceMonth: Month,
        referenceYear: int,
        referenceFreq: Frequency,
        convexityAdjustment: float,
    ) -> None: ...

class ConstNotionalCrossCurrencyBasisSwapRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        basis: Handle[Quote],
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        baseCurrencyIndex: IborIndex,
        quoteCurrencyIndex: IborIndex,
        collateralCurve: Handle[YieldTermStructure],
        isFxBaseCurrencyCollateralCurrency: bool,
        isBasisOnFxBaseCurrencyLeg: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        basis: Handle[Quote],
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        baseCurrencyIndex: IborIndex,
        quoteCurrencyIndex: IborIndex,
        collateralCurve: Handle[YieldTermStructure],
        isFxBaseCurrencyCollateralCurrency: bool,
        isBasisOnFxBaseCurrencyLeg: bool,
        paymentFrequency: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        basis: Handle[Quote],
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        baseCurrencyIndex: IborIndex,
        quoteCurrencyIndex: IborIndex,
        collateralCurve: Handle[YieldTermStructure],
        isFxBaseCurrencyCollateralCurrency: bool,
        isBasisOnFxBaseCurrencyLeg: bool,
        paymentFrequency: Frequency,
        paymentLag: int,
    ) -> None: ...

class MtMCrossCurrencyBasisSwapRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        basis: Handle[Quote],
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        baseCurrencyIndex: IborIndex,
        quoteCurrencyIndex: IborIndex,
        collateralCurve: Handle[YieldTermStructure],
        isFxBaseCurrencyCollateralCurrency: bool,
        isBasisOnFxBaseCurrencyLeg: bool,
        isFxBaseCurrencyLegResettable: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        basis: Handle[Quote],
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        baseCurrencyIndex: IborIndex,
        quoteCurrencyIndex: IborIndex,
        collateralCurve: Handle[YieldTermStructure],
        isFxBaseCurrencyCollateralCurrency: bool,
        isBasisOnFxBaseCurrencyLeg: bool,
        isFxBaseCurrencyLegResettable: bool,
        paymentFrequency: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        basis: Handle[Quote],
        tenor: Period,
        fixingDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        baseCurrencyIndex: IborIndex,
        quoteCurrencyIndex: IborIndex,
        collateralCurve: Handle[YieldTermStructure],
        isFxBaseCurrencyCollateralCurrency: bool,
        isBasisOnFxBaseCurrencyLeg: bool,
        isFxBaseCurrencyLegResettable: bool,
        paymentFrequency: Frequency,
        paymentLag: int,
    ) -> None: ...

class IborIborBasisSwapRateHelper(RateHelper):
    def __init__(
        self,
        basis: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        baseIndex: IborIndex,
        otherIndex: IborIndex,
        discountHandle: Handle[YieldTermStructure],
        bootstrapBaseCurve: bool,
    ) -> None: ...
    def swap(self) -> Swap: ...

class OvernightIborBasisSwapRateHelper(RateHelper):
    @overload
    def __init__(
        self,
        basis: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        baseIndex: OvernightIndex,
        otherIndex: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        basis: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        convention: BusinessDayConvention,
        endOfMonth: bool,
        baseIndex: OvernightIndex,
        otherIndex: IborIndex,
        discountHandle: Handle[YieldTermStructure],
    ) -> None: ...
    def swap(self) -> Swap: ...

class _IterativeBootstrap:
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        minValue: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        minValue: Optional[float],
        maxValue: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        minValue: Optional[float],
        maxValue: Optional[float],
        maxAttempts: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        minValue: Optional[float],
        maxValue: Optional[float],
        maxAttempts: int,
        maxFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        minValue: Optional[float],
        maxValue: Optional[float],
        maxAttempts: int,
        maxFactor: float,
        minFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        minValue: Optional[float],
        maxValue: Optional[float],
        maxAttempts: int,
        maxFactor: float,
        minFactor: float,
        dontThrow: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        minValue: Optional[float],
        maxValue: Optional[float],
        maxAttempts: int,
        maxFactor: float,
        minFactor: float,
        dontThrow: bool,
        dontThrowSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        minValue: Optional[float],
        maxValue: Optional[float],
        maxAttempts: int,
        maxFactor: float,
        minFactor: float,
        dontThrow: bool,
        dontThrowSteps: int,
        maxEvaluations: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class PiecewiseFlatForward(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseLogLinearDiscount(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseLinearForward(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseLinearZero(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseCubicZero(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseLogCubicDiscount(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseSplineCubicDiscount(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseKrugerZero(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseKrugerLogDiscount(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseConvexMonotoneForward(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseConvexMonotoneZero(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseNaturalCubicZero(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseNaturalLogCubicDiscount(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseLogMixedLinearCubicDiscount(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseParabolicCubicZero(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseMonotonicParabolicCubicZero(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseLogParabolicCubicDiscount(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseMonotonicLogParabolicCubicDiscount(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class _GlobalBootstrap:
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        optimizer: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        accuracy: Optional[float],
        optimizer: OptimizationMethod,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def __init__(
        self,
        additionalHelpers: list[RateHelper],
        additionalDates: list[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        additionalHelpers: list[RateHelper],
        additionalDates: list[Date],
        accuracy: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        additionalHelpers: list[RateHelper],
        additionalDates: list[Date],
        accuracy: Optional[float],
        optimizer: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        additionalHelpers: list[RateHelper],
        additionalDates: list[Date],
        accuracy: Optional[float],
        optimizer: OptimizationMethod,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class GlobalLinearSimpleZeroCurve(YieldTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...

class PiecewiseLogLinearSpreadDiscount(YieldTermStructure):
    def baseCurve(self) -> Handle[YieldTermStructure]: ...
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseLogLinearDiscountSpread(YieldTermStructure):
    def baseCurve(self) -> Handle[YieldTermStructure]: ...
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseLogCubicSpreadDiscount(YieldTermStructure):
    def baseCurve(self) -> Handle[YieldTermStructure]: ...
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseNaturalLogCubicSpreadDiscount(YieldTermStructure):
    def baseCurve(self) -> Handle[YieldTermStructure]: ...
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class PiecewiseLogMixedLinearCubicSpreadDiscount(YieldTermStructure):
    def baseCurve(self) -> Handle[YieldTermStructure]: ...
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def data(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class DefaultProbabilityTermStructure(TermStructure):
    def __init__(self) -> None: ...
    @overload
    def defaultProbability(
        self,
        arg0: Date,
    ) -> Probability: ...
    @overload
    def defaultProbability(
        self,
        arg0: Date,
        arg1: Date,
    ) -> Probability: ...
    @overload
    def defaultProbability(
        self,
        arg0: Date,
        arg1: Date,
        extrapolate: bool,
    ) -> Probability: ...
    @overload
    def defaultProbability(
        self,
        arg0: Date,
        extrapolate: bool,
    ) -> Probability: ...
    @overload
    def defaultProbability(
        self,
        arg0: float,
    ) -> Probability: ...
    @overload
    def defaultProbability(
        self,
        arg0: float,
        arg1: float,
    ) -> Probability: ...
    @overload
    def defaultProbability(
        self,
        arg0: float,
        arg1: float,
        extrapolate: bool,
    ) -> Probability: ...
    @overload
    def defaultProbability(
        self,
        arg0: float,
        extrapolate: bool,
    ) -> Probability: ...
    @overload
    def survivalProbability(
        self,
        arg0: Date,
    ) -> Probability: ...
    @overload
    def survivalProbability(
        self,
        arg0: Date,
        extrapolate: bool,
    ) -> Probability: ...
    @overload
    def survivalProbability(
        self,
        arg0: float,
    ) -> Probability: ...
    @overload
    def survivalProbability(
        self,
        arg0: float,
        extrapolate: bool,
    ) -> Probability: ...
    @overload
    def defaultDensity(
        self,
        arg0: Date,
    ) -> float: ...
    @overload
    def defaultDensity(
        self,
        arg0: Date,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def defaultDensity(
        self,
        arg0: float,
    ) -> float: ...
    @overload
    def defaultDensity(
        self,
        arg0: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def hazardRate(
        self,
        arg0: Date,
    ) -> float: ...
    @overload
    def hazardRate(
        self,
        arg0: Date,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def hazardRate(
        self,
        arg0: float,
    ) -> float: ...
    @overload
    def hazardRate(
        self,
        arg0: float,
        extrapolate: bool,
    ) -> float: ...

class FlatHazardRate(DefaultProbabilityTermStructure):
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        hazardRate: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        todaysDate: Date,
        hazardRate: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...

class DefaultProbabilityHelper(Observable):
    def __init__(self) -> None: ...
    def quote(self) -> Handle[Quote]: ...
    def latestDate(self) -> Date: ...
    def earliestDate(self) -> Date: ...
    def maturityDate(self) -> Date: ...
    def latestRelevantDate(self) -> Date: ...
    def pillarDate(self) -> Date: ...
    def impliedQuote(self) -> float: ...
    def quoteError(self) -> float: ...

class SpreadCdsHelper(DefaultProbabilityHelper):
    @overload
    def __init__(
        self,
        spread: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: Handle[Quote],
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
        model: CreditDefaultSwap.PricingModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
        model: CreditDefaultSwap.PricingModel,
    ) -> None: ...

class UpfrontCdsHelper(DefaultProbabilityHelper):
    @overload
    def __init__(
        self,
        upfront: Handle[Quote],
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: Handle[Quote],
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: Handle[Quote],
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: Handle[Quote],
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: Handle[Quote],
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: Handle[Quote],
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: Handle[Quote],
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: Handle[Quote],
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
        model: CreditDefaultSwap.PricingModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: float,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: float,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: float,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: float,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: float,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: float,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: float,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        upfront: float,
        spread: float,
        tenor: Period,
        settlementDays: int,
        calendar: Calendar,
        frequency: Frequency,
        convention: BusinessDayConvention,
        rule: DateGeneration.Rule,
        dayCounter: DayCounter,
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        upfrontSettlementDays: int,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        startDate: Date,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
        model: CreditDefaultSwap.PricingModel,
    ) -> None: ...

class HazardRate:
    def __init__(self) -> None: ...

class DefaultDensity:
    def __init__(self) -> None: ...

class PiecewiseFlatHazardRate(DefaultProbabilityTermStructure):
    def dates(self) -> list[Date]: ...
    def times(self) -> list[float]: ...
    def nodes(self) -> list[tuple[Date,Real]]: ...

class RiskyBondEngine(PricingEngine):
    def __init__(
        self,
        defaultCurve: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        riskFreeCurve: Handle[YieldTermStructure],
    ) -> None: ...

class Protection:
    class Side(IntEnum):
        Buyer
        Seller

    def __init__(self) -> None: ...

class Claim:
    def __init__(self) -> None: ...
    def amount(
        self,
        defaultDate: Date,
        notional: float,
        recoveryRate: float,
    ) -> float: ...

class FaceValueClaim(Claim):
    def __init__(self) -> None: ...

class FaceValueAccrualClaim(Claim):
    def __init__(
        self,
        bond: Bond,
    ) -> None: ...

class CreditDefaultSwap(Instrument):
    class PricingModel(IntEnum):
        Midpoint
        ISDA

    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        claim: Claim,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        claim: Claim,
        lastPeriodDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        claim: Claim,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        claim: Claim,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
        tradeDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        claim: Claim,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
        tradeDate: Date,
        cashSettlementDays: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        upfrontDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        upfrontDate: Date,
        claim: Claim,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        upfrontDate: Date,
        claim: Claim,
        lastPeriodDayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        upfrontDate: Date,
        claim: Claim,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        upfrontDate: Date,
        claim: Claim,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
        tradeDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        side: Protection.Side,
        notional: float,
        upfront: float,
        spread: float,
        schedule: Schedule,
        paymentConvention: BusinessDayConvention,
        dayCounter: DayCounter,
        settlesAccrual: bool,
        paysAtDefaultTime: bool,
        protectionStart: Date,
        upfrontDate: Date,
        claim: Claim,
        lastPeriodDayCounter: DayCounter,
        rebatesAccrual: bool,
        tradeDate: Date,
        cashSettlementDays: int,
    ) -> None: ...
    def side(self) -> Protection.Side: ...
    def notional(self) -> float: ...
    def runningSpread(self) -> float: ...
    def settlesAccrual(self) -> bool: ...
    def paysAtDefaultTime(self) -> bool: ...
    def coupons(self) -> list[CashFlow]: ...
    def protectionStartDate(self) -> Date: ...
    def protectionEndDate(self) -> Date: ...
    def rebatesAccrual(self) -> bool: ...
    def upfrontPayment(self) -> CashFlow: ...
    def accrualRebate(self) -> CashFlow: ...
    def tradeDate(self) -> Date: ...
    def cashSettlementDays(self) -> int: ...
    def fairUpfront(self) -> float: ...
    def fairSpread(self) -> float: ...
    def couponLegBPS(self) -> float: ...
    def upfrontBPS(self) -> float: ...
    def couponLegNPV(self) -> float: ...
    def defaultLegNPV(self) -> float: ...
    def upfrontNPV(self) -> float: ...
    def accrualRebateNPV(self) -> float: ...
    @overload
    def impliedHazardRate(
        self,
        targetNPV: float,
        discountCurve: Handle[YieldTermStructure],
        dayCounter: DayCounter,
    ) -> float: ...
    @overload
    def impliedHazardRate(
        self,
        targetNPV: float,
        discountCurve: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        recoveryRate: float,
    ) -> float: ...
    @overload
    def impliedHazardRate(
        self,
        targetNPV: float,
        discountCurve: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        recoveryRate: float,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedHazardRate(
        self,
        targetNPV: float,
        discountCurve: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        recoveryRate: float,
        accuracy: float,
        model: CreditDefaultSwap.PricingModel,
    ) -> float: ...
    @overload
    def conventionalSpread(
        self,
        conventionalRecovery: float,
        discountCurve: Handle[YieldTermStructure],
        dayCounter: DayCounter,
    ) -> float: ...
    @overload
    def conventionalSpread(
        self,
        conventionalRecovery: float,
        discountCurve: Handle[YieldTermStructure],
        dayCounter: DayCounter,
        model: CreditDefaultSwap.PricingModel,
    ) -> float: ...

class MidPointCdsEngine(PricingEngine):
    def __init__(
        self,
        probability: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...

class IntegralCdsEngine(PricingEngine):
    @overload
    def __init__(
        self,
        integrationStep: Period,
        probability: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        integrationStep: Period,
        probability: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        includeSettlementDateFlows: bool,
    ) -> None: ...

class IsdaCdsEngine(PricingEngine):
    class NumericalFix(IntEnum):
        None_
        Taylor

    class AccrualBias(IntEnum):
        HalfDayBias
        NoBias

    class ForwardsInCouponPeriod(IntEnum):
        Flat
        Piecewise

    @overload
    def __init__(
        self,
        probability: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        probability: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        includeSettlementDateFlows: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        probability: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        includeSettlementDateFlows: bool,
        numericalFix: IsdaCdsEngine.NumericalFix,
    ) -> None: ...
    @overload
    def __init__(
        self,
        probability: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        includeSettlementDateFlows: bool,
        numericalFix: IsdaCdsEngine.NumericalFix,
        accrualBias: IsdaCdsEngine.AccrualBias,
    ) -> None: ...
    @overload
    def __init__(
        self,
        probability: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        discountCurve: Handle[YieldTermStructure],
        includeSettlementDateFlows: bool,
        numericalFix: IsdaCdsEngine.NumericalFix,
        accrualBias: IsdaCdsEngine.AccrualBias,
        forwardsInCouponPeriod: IsdaCdsEngine.ForwardsInCouponPeriod,
    ) -> None: ...

class CdsOption(Option):
    @overload
    def __init__(
        self,
        swap: CreditDefaultSwap,
        exercise: Exercise,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swap: CreditDefaultSwap,
        exercise: Exercise,
        knocksOut: bool,
    ) -> None: ...
    def atmRate(self) -> float: ...
    def riskyAnnuity(self) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        termStructure: Handle[YieldTermStructure],
        arg2: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        termStructure: Handle[YieldTermStructure],
        arg2: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        termStructure: Handle[YieldTermStructure],
        arg2: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        termStructure: Handle[YieldTermStructure],
        arg2: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        termStructure: Handle[YieldTermStructure],
        arg2: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...

class BlackCdsOptionEngine(PricingEngine):
    def __init__(
        self,
        arg0: Handle[DefaultProbabilityTermStructure],
        recoveryRate: float,
        termStructure: Handle[YieldTermStructure],
        vol: Handle[Quote],
    ) -> None: ...
    def termStructure(self) -> Handle[YieldTermStructure]: ...
    def volatility(self) -> Handle[Quote]: ...

class NormalDistribution:
    @overload
    def __init__(
        self,
        average: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        average: float,
        sigma: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...
    def derivative(
        self,
        x: float,
    ) -> float: ...

class CumulativeNormalDistribution:
    @overload
    def __init__(
        self,
        average: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        average: float,
        sigma: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...
    def derivative(
        self,
        x: float,
    ) -> float: ...

class InverseCumulativeNormal:
    @overload
    def __init__(
        self,
        average: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        average: float,
        sigma: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class MoroInverseCumulativeNormal:
    @overload
    def __init__(
        self,
        average: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        average: float,
        sigma: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class BivariateCumulativeNormalDistribution:
    def __init__(
        self,
        rho: float,
    ) -> None: ...
    def __call__(
        self,
        x: float,
        y: float,
    ) -> float: ...

class BinomialDistribution:
    def __init__(
        self,
        p: float,
        n: BigNatural,
    ) -> None: ...
    def __call__(
        self,
        k: BigNatural,
    ) -> float: ...

class CumulativeBinomialDistribution:
    def __init__(
        self,
        p: float,
        n: BigNatural,
    ) -> None: ...
    def __call__(
        self,
        k: BigNatural,
    ) -> float: ...

class BivariateCumulativeNormalDistributionDr78:
    def __init__(
        self,
        rho: float,
    ) -> None: ...
    def __call__(
        self,
        a: float,
        b: float,
    ) -> float: ...

class BivariateCumulativeNormalDistributionWe04DP:
    def __init__(
        self,
        rho: float,
    ) -> None: ...
    def __call__(
        self,
        a: float,
        b: float,
    ) -> float: ...

class CumulativeChiSquareDistribution:
    def __init__(
        self,
        df: float,
    ) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class NonCentralCumulativeChiSquareDistribution:
    def __init__(
        self,
        df: float,
        ncp: float,
    ) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class InverseNonCentralCumulativeChiSquareDistribution:
    @overload
    def __init__(
        self,
        df: float,
        ncp: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        df: float,
        ncp: float,
        maxEvaluations: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        df: float,
        ncp: float,
        maxEvaluations: int,
        accuracy: float,
    ) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class CumulativeGammaDistribution:
    def __init__(
        self,
        a: float,
    ) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class GammaFunction:
    def __init__(self) -> None: ...
    def logValue(
        self,
        x: float,
    ) -> float: ...

class PoissonDistribution:
    def __init__(
        self,
        mu: float,
    ) -> None: ...
    def __call__(
        self,
        k: BigNatural,
    ) -> float: ...

class CumulativePoissonDistribution:
    def __init__(
        self,
        mu: float,
    ) -> None: ...
    def __call__(
        self,
        k: BigNatural,
    ) -> float: ...

class InverseCumulativePoisson:
    def __init__(
        self,
        lambda_: float,
    ) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class StudentDistribution:
    def __init__(
        self,
        n: int,
    ) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class CumulativeStudentDistribution:
    def __init__(
        self,
        n: int,
    ) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class InverseCumulativeStudent:
    @overload
    def __init__(
        self,
        n: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        accuracy: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        accuracy: float,
        maxIterations: int,
    ) -> None: ...
    def __call__(
        self,
        x: float,
    ) -> float: ...

class Money:
    class ConversionType(IntEnum):
        NoConversion
        BaseCurrencyConversion
        AutomatedConversion

    @overload
    def __init__(
        self,
        currency: Currency,
        value: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        value: float,
        currency: Currency,
    ) -> None: ...
    def currency(self) -> Currency: ...
    def value(self) -> float: ...
    def rounded(self) -> Money: ...

class ExchangeRate:
    class Type(IntEnum):
        Direct
        Derived

    def __init__(
        self,
        source: Currency,
        target: Currency,
        rate: float,
    ) -> None: ...
    def source(self) -> Currency: ...
    def target(self) -> Currency: ...
    def type(self) -> ExchangeRate.Type: ...
    def rate(self) -> float: ...
    def exchange(
        self,
        amount: Money,
    ) -> Money: ...
    def chain(
        self,
        r1: ExchangeRate,
        r2: ExchangeRate,
    ) -> ExchangeRate: ...

class ExchangeRateManager:
    def __init__(self) -> None: ...
    def instance(self) -> ExchangeRateManager: ...
    @overload
    def add(
        self,
        arg0: ExchangeRate,
    ) -> None: ...
    @overload
    def add(
        self,
        arg0: ExchangeRate,
        startDate: Date,
    ) -> None: ...
    @overload
    def add(
        self,
        arg0: ExchangeRate,
        startDate: Date,
        endDate: Date,
    ) -> None: ...
    @overload
    def lookup(
        self,
        source: Currency,
        target: Currency,
        date: Date,
    ) -> ExchangeRate: ...
    @overload
    def lookup(
        self,
        source: Currency,
        target: Currency,
        date: Date,
        type: ExchangeRate.Type,
    ) -> ExchangeRate: ...
    def clear(self) -> None: ...

class Settings:
    def __init__(self) -> None: ...
    def instance(self) -> Settings: ...
    def anchorEvaluationDate(self) -> None: ...
    def resetEvaluationDate(self) -> None: ...

class Fdm1dMesher:
    def __init__(
        self,
        size: int,
    ) -> None: ...
    def size(self) -> int: ...
    def dplus(
        self,
        index: int,
    ) -> float: ...
    def dminus(
        self,
        index: int,
    ) -> float: ...
    def location(
        self,
        index: int,
    ) -> float: ...
    def locations(self) -> list[float]: ...

class FdmBlackScholesMesher(Fdm1dMesher):
    @overload
    def __init__(
        self,
        size: int,
        process: GeneralizedBlackScholesProcess,
        maturity: float,
        strike: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: GeneralizedBlackScholesProcess,
        maturity: float,
        strike: float,
        xMinConstraint: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: GeneralizedBlackScholesProcess,
        maturity: float,
        strike: float,
        xMinConstraint: Optional[float],
        xMaxConstraint: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: GeneralizedBlackScholesProcess,
        maturity: float,
        strike: float,
        xMinConstraint: Optional[float],
        xMaxConstraint: Optional[float],
        eps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: GeneralizedBlackScholesProcess,
        maturity: float,
        strike: float,
        xMinConstraint: Optional[float],
        xMaxConstraint: Optional[float],
        eps: float,
        scaleFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: GeneralizedBlackScholesProcess,
        maturity: float,
        strike: float,
        xMinConstraint: Optional[float],
        xMaxConstraint: Optional[float],
        eps: float,
        scaleFactor: float,
        cPoint: tuple[Real,Real],
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: GeneralizedBlackScholesProcess,
        maturity: float,
        strike: float,
        xMinConstraint: Optional[float],
        xMaxConstraint: Optional[float],
        eps: float,
        scaleFactor: float,
        cPoint: tuple[Real,Real],
        dividendSchedule: list[Dividend],
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: GeneralizedBlackScholesProcess,
        maturity: float,
        strike: float,
        xMinConstraint: Optional[float],
        xMaxConstraint: Optional[float],
        eps: float,
        scaleFactor: float,
        cPoint: tuple[Real,Real],
        dividendSchedule: list[Dividend],
        fdmQuantoHelper: FdmQuantoHelper,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: GeneralizedBlackScholesProcess,
        maturity: float,
        strike: float,
        xMinConstraint: Optional[float],
        xMaxConstraint: Optional[float],
        eps: float,
        scaleFactor: float,
        cPoint: tuple[Real,Real],
        dividendSchedule: list[Dividend],
        fdmQuantoHelper: FdmQuantoHelper,
        spotAdjustment: float,
    ) -> None: ...
    def processHelper(
        self,
        s0: Handle[Quote],
        rTS: Handle[YieldTermStructure],
        qTS: Handle[YieldTermStructure],
        vol: float,
    ) -> GeneralizedBlackScholesProcess: ...

class Concentrating1dMesher(Fdm1dMesher):
    @overload
    def __init__(
        self,
        start: float,
        end: float,
        size: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        start: float,
        end: float,
        size: int,
        cPoints: list[std.tuple[Real,Real,bool]],
    ) -> None: ...
    @overload
    def __init__(
        self,
        start: float,
        end: float,
        size: int,
        cPoints: list[std.tuple[Real,Real,bool]],
        tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        start: float,
        end: float,
        size: int,
        cPoints: tuple[Real,Real],
    ) -> None: ...
    @overload
    def __init__(
        self,
        start: float,
        end: float,
        size: int,
        cPoints: tuple[Real,Real],
        requireCPoint: bool,
    ) -> None: ...

class ExponentialJump1dMesher(Fdm1dMesher):
    @overload
    def __init__(
        self,
        steps: int,
        beta: float,
        jumpIntensity: float,
        eta: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        steps: int,
        beta: float,
        jumpIntensity: float,
        eta: float,
        eps: float,
    ) -> None: ...

class FdmCEV1dMesher(Fdm1dMesher):
    @overload
    def __init__(
        self,
        size: int,
        f0: float,
        alpha: float,
        beta: float,
        maturity: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        f0: float,
        alpha: float,
        beta: float,
        maturity: float,
        eps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        f0: float,
        alpha: float,
        beta: float,
        maturity: float,
        eps: float,
        scaleFactor: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        f0: float,
        alpha: float,
        beta: float,
        maturity: float,
        eps: float,
        scaleFactor: float,
        cPoint: tuple[Real,Real],
    ) -> None: ...

class FdmHestonVarianceMesher(Fdm1dMesher):
    @overload
    def __init__(
        self,
        size: int,
        process: HestonProcess,
        maturity: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: HestonProcess,
        maturity: float,
        tAvgSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: HestonProcess,
        maturity: float,
        tAvgSteps: int,
        epsilon: float,
    ) -> None: ...
    def volaEstimate(self) -> float: ...

class FdmHestonLocalVolatilityVarianceMesher(Fdm1dMesher):
    @overload
    def __init__(
        self,
        size: int,
        process: HestonProcess,
        leverageFct: LocalVolTermStructure,
        maturity: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: HestonProcess,
        leverageFct: LocalVolTermStructure,
        maturity: float,
        tAvgSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: HestonProcess,
        leverageFct: LocalVolTermStructure,
        maturity: float,
        tAvgSteps: int,
        epsilon: float,
    ) -> None: ...
    def volaEstimate(self) -> float: ...

class FdmSimpleProcess1dMesher(Fdm1dMesher):
    @overload
    def __init__(
        self,
        size: int,
        process: StochasticProcess1D,
        maturity: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: StochasticProcess1D,
        maturity: float,
        tAvgSteps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: StochasticProcess1D,
        maturity: float,
        tAvgSteps: int,
        epsilon: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: int,
        process: StochasticProcess1D,
        maturity: float,
        tAvgSteps: int,
        epsilon: float,
        mandatoryPoint: Optional[float],
    ) -> None: ...

class Uniform1dMesher(Fdm1dMesher):
    def __init__(
        self,
        start: float,
        end: float,
        size: int,
    ) -> None: ...

class Predefined1dMesher(Fdm1dMesher):
    def __init__(
        self,
        x: list[float],
    ) -> None: ...

class Glued1dMesher(Fdm1dMesher):
    def __init__(
        self,
        leftMesher: Fdm1dMesher,
        rightMesher: Fdm1dMesher,
    ) -> None: ...

class FdmLinearOpIterator:
    def index(self) -> int: ...

class FdmLinearOpLayout:
    def begin(self) -> FdmLinearOpIterator: ...
    def end(self) -> FdmLinearOpIterator: ...
    def size(self) -> int: ...
    @overload
    def neighbourhood(
        self,
        iterator: FdmLinearOpIterator,
        i1: int,
        offset1: int,
        i2: int,
        offset2: int,
    ) -> int: ...
    @overload
    def neighbourhood(
        self,
        iterator: FdmLinearOpIterator,
        i: int,
        offset: int,
    ) -> int: ...
    def iter_neighbourhood(
        self,
        iterator: FdmLinearOpIterator,
        i: int,
        offset: int,
    ) -> FdmLinearOpIterator: ...

class FdmMesher:
    def __init__(self) -> None: ...
    def dplus(
        self,
        iter: FdmLinearOpIterator,
        direction: int,
    ) -> float: ...
    def dminus(
        self,
        iter: FdmLinearOpIterator,
        direction: int,
    ) -> float: ...
    def location(
        self,
        iter: FdmLinearOpIterator,
        direction: int,
    ) -> float: ...
    def locations(
        self,
        direction: int,
    ) -> Array: ...
    def layout(self) -> FdmLinearOpLayout: ...

class FdmMesherComposite(FdmMesher):
    @overload
    def __init__(
        self,
        layout: FdmLinearOpLayout,
        mesher: list[Fdm1dMesher],
    ) -> None: ...
    @overload
    def __init__(
        self,
        m1: Fdm1dMesher,
        m2: Fdm1dMesher,
    ) -> None: ...
    @overload
    def __init__(
        self,
        m1: Fdm1dMesher,
        m2: Fdm1dMesher,
        m3: Fdm1dMesher,
    ) -> None: ...
    @overload
    def __init__(
        self,
        m1: Fdm1dMesher,
        m2: Fdm1dMesher,
        m3: Fdm1dMesher,
        m4: Fdm1dMesher,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: Fdm1dMesher,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: list[Fdm1dMesher],
    ) -> None: ...
    def getFdm1dMeshers(self) -> list[Fdm1dMesher]: ...

class FdmLinearOp:
    def __init__(self) -> None: ...
    def apply(
        self,
        r: Array,
    ) -> Array: ...

class SparseMatrix:
    def __init__(self) -> None: ...

class FdmLinearOpComposite(FdmLinearOp):
    def __init__(self) -> None: ...
    def size(self) -> int: ...
    def setTime(
        self,
        t1: float,
        t2: float,
    ) -> None: ...
    def apply_mixed(
        self,
        r: Array,
    ) -> Array: ...
    def apply_direction(
        self,
        direction: int,
        r: Array,
    ) -> Array: ...
    def solve_splitting(
        self,
        direction: int,
        r: Array,
        s: float,
    ) -> Array: ...
    def preconditioner(
        self,
        r: Array,
        s: float,
    ) -> Array: ...

class FdmBoundaryCondition:
    class Side(IntEnum):
        None_
        Upper
        Lower

    def __init__(self) -> None: ...
    def applyBeforeApplying(
        self,
        arg0: FdmLinearOp,
    ) -> None: ...
    def applyAfterApplying(
        self,
        arg0: Array,
    ) -> None: ...
    def applyBeforeSolving(
        self,
        arg0: FdmLinearOp,
        rhs: Array,
    ) -> None: ...
    def applyAfterSolving(
        self,
        arg0: Array,
    ) -> None: ...
    def setTime(
        self,
        t: float,
    ) -> None: ...

class FdmDirichletBoundary(FdmBoundaryCondition):
    def __init__(
        self,
        mesher: FdmMesher,
        valueOnBoundary: float,
        direction: int,
        side: FdmDirichletBoundary.Side,
    ) -> None: ...
    @overload
    def applyAfterApplying(
        self,
        arg0: Array,
    ) -> None: ...
    @overload
    def applyAfterApplying(
        self,
        x: float,
        value: float,
    ) -> float: ...

class FdmDiscountDirichletBoundary(FdmBoundaryCondition):
    def __init__(
        self,
        mesher: FdmMesher,
        rTS: YieldTermStructure,
        maturityTime: float,
        valueOnBoundary: float,
        direction: int,
        side: FdmDiscountDirichletBoundary.Side,
    ) -> None: ...

class FdmBatesOp(FdmLinearOpComposite):
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        batesProcess: BatesProcess,
        bcSet: FdmBoundaryConditionSet,
        integroIntegrationOrder: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        batesProcess: BatesProcess,
        bcSet: FdmBoundaryConditionSet,
        integroIntegrationOrder: int,
        quantoHelper: FdmQuantoHelper,
    ) -> None: ...

class FdmBlackScholesOp(FdmLinearOpComposite):
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: GeneralizedBlackScholesProcess,
        strike: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: GeneralizedBlackScholesProcess,
        strike: float,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: GeneralizedBlackScholesProcess,
        strike: float,
        localVol: bool,
        illegalLocalVolOverwrite: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: GeneralizedBlackScholesProcess,
        strike: float,
        localVol: bool,
        illegalLocalVolOverwrite: Optional[float],
        direction: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: GeneralizedBlackScholesProcess,
        strike: float,
        localVol: bool,
        illegalLocalVolOverwrite: Optional[float],
        direction: int,
        quantoHelper: FdmQuantoHelper,
    ) -> None: ...

class Fdm2dBlackScholesOp(FdmLinearOpComposite):
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        maturity: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        maturity: float,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        p1: GeneralizedBlackScholesProcess,
        p2: GeneralizedBlackScholesProcess,
        correlation: float,
        maturity: float,
        localVol: bool,
        illegalLocalVolOverwrite: Optional[float],
    ) -> None: ...

class FdmCEVOp(FdmLinearOpComposite):
    def __init__(
        self,
        mesher: FdmMesher,
        rTS: YieldTermStructure,
        f0: float,
        alpha: float,
        beta: float,
        direction: int,
    ) -> None: ...

class FdmG2Op(FdmLinearOpComposite):
    def __init__(
        self,
        mesher: FdmMesher,
        model: G2,
        direction1: int,
        direction2: int,
    ) -> None: ...

class FdmHestonHullWhiteOp(FdmLinearOpComposite):
    def __init__(
        self,
        mesher: FdmMesher,
        hestonProcess: HestonProcess,
        hwProcess: HullWhiteProcess,
        equityShortRateCorrelation: float,
    ) -> None: ...

class FdmHestonOp(FdmLinearOpComposite):
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        hestonProcess: HestonProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        hestonProcess: HestonProcess,
        quantoHelper: FdmQuantoHelper,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        hestonProcess: HestonProcess,
        quantoHelper: FdmQuantoHelper,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...

class FdmHullWhiteOp(FdmLinearOpComposite):
    def __init__(
        self,
        mesher: FdmMesher,
        model: HullWhite,
        direction: int,
    ) -> None: ...

class FdmLocalVolFwdOp(FdmLinearOpComposite):
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        spot: Quote,
        rTS: YieldTermStructure,
        qTS: YieldTermStructure,
        localVol: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        spot: Quote,
        rTS: YieldTermStructure,
        qTS: YieldTermStructure,
        localVol: LocalVolTermStructure,
        direction: int,
    ) -> None: ...

class FdmOrnsteinUhlenbeckOp(FdmLinearOpComposite):
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        p: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        p: OrnsteinUhlenbeckProcess,
        rTS: YieldTermStructure,
        direction: int,
    ) -> None: ...

class FdmSabrOp(FdmLinearOpComposite):
    def __init__(
        self,
        mesher: FdmMesher,
        rTS: YieldTermStructure,
        f0: float,
        alpha: float,
        beta: float,
        nu: float,
        rho: float,
    ) -> None: ...

class FdmZabrOp(FdmLinearOpComposite):
    def __init__(
        self,
        mesher: FdmMesher,
        beta: float,
        nu: float,
        rho: float,
        gamma: float,
    ) -> None: ...

class FdmDupire1dOp(FdmLinearOpComposite):
    def __init__(
        self,
        mesher: FdmMesher,
        localVolatility: Array,
    ) -> None: ...

class FdmBlackScholesFwdOp(FdmLinearOpComposite):
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: GeneralizedBlackScholesProcess,
        strike: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: GeneralizedBlackScholesProcess,
        strike: float,
        localVol: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: GeneralizedBlackScholesProcess,
        strike: float,
        localVol: bool,
        illegalLocalVolOverwrite: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: GeneralizedBlackScholesProcess,
        strike: float,
        localVol: bool,
        illegalLocalVolOverwrite: float,
        direction: int,
    ) -> None: ...

class FdmSquareRootFwdOp(FdmLinearOpComposite):
    class TransformationType(IntEnum):
        Plain
        Power
        Log

    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        kappa: float,
        theta: float,
        sigma: float,
        direction: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        kappa: float,
        theta: float,
        sigma: float,
        direction: int,
        type: FdmSquareRootFwdOp.TransformationType,
    ) -> None: ...

class FdmHestonFwdOp(FdmLinearOpComposite):
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: HestonProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: HestonProcess,
        type: FdmSquareRootFwdOp.TransformationType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mesher: FdmMesher,
        process: HestonProcess,
        type: FdmSquareRootFwdOp.TransformationType,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...

class FdmWienerOp(FdmLinearOpComposite):
    def __init__(
        self,
        mesher: FdmMesher,
        rTS: YieldTermStructure,
        lambdas: Array,
    ) -> None: ...

class TripleBandLinearOp(FdmLinearOp):
    def __init__(
        self,
        direction: int,
        mesher: FdmMesher,
    ) -> None: ...
    def apply(
        self,
        r: Array,
    ) -> Array: ...
    @overload
    def solve_splitting(
        self,
        r: Array,
        a: float,
    ) -> Array: ...
    @overload
    def solve_splitting(
        self,
        r: Array,
        a: float,
        b: float,
    ) -> Array: ...
    def mult(
        self,
        u: Array,
    ) -> TripleBandLinearOp: ...
    def multR(
        self,
        u: Array,
    ) -> TripleBandLinearOp: ...
    @overload
    def add(
        self,
        m: TripleBandLinearOp,
    ) -> TripleBandLinearOp: ...
    @overload
    def add(
        self,
        u: Array,
    ) -> TripleBandLinearOp: ...
    def axpyb(
        self,
        a: Array,
        x: TripleBandLinearOp,
        y: TripleBandLinearOp,
        b: Array,
    ) -> None: ...
    def swap(
        self,
        m: TripleBandLinearOp,
    ) -> None: ...

class FirstDerivativeOp(TripleBandLinearOp):
    def __init__(
        self,
        direction: int,
        mesher: FdmMesher,
    ) -> None: ...

class SecondDerivativeOp(TripleBandLinearOp):
    def __init__(
        self,
        direction: int,
        mesher: FdmMesher,
    ) -> None: ...

class NinePointLinearOp(FdmLinearOp):
    def __init__(
        self,
        d0: int,
        d1: int,
        mesher: FdmMesher,
    ) -> None: ...

class SecondOrderMixedDerivativeOp(NinePointLinearOp):
    def __init__(
        self,
        d0: int,
        d1: int,
        mesher: FdmMesher,
    ) -> None: ...

class NthOrderDerivativeOp(FdmLinearOp):
    def __init__(
        self,
        direction: int,
        order: int,
        nPoints: int,
        mesher: FdmMesher,
    ) -> None: ...

class CraigSneydScheme:
    @overload
    def __init__(
        self,
        theta: float,
        mu: float,
        map: FdmLinearOpComposite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theta: float,
        mu: float,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
    ) -> None: ...
    def step(
        self,
        a: Array,
        t: float,
    ) -> None: ...
    def setStep(
        self,
        dt: float,
    ) -> None: ...

class ImplicitEulerScheme:
    class SolverType(IntEnum):
        BiCGstab
        GMRES

    @overload
    def __init__(
        self,
        map: FdmLinearOpComposite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
    ) -> None: ...
    @overload
    def __init__(
        self,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
        relTol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
        relTol: float,
        solverType: ImplicitEulerScheme.SolverType,
    ) -> None: ...
    def step(
        self,
        a: Array,
        t: float,
    ) -> None: ...
    def setStep(
        self,
        dt: float,
    ) -> None: ...
    def numberOfIterations(self) -> int: ...

class CrankNicolsonScheme:
    @overload
    def __init__(
        self,
        theta: float,
        map: FdmLinearOpComposite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theta: float,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theta: float,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
        relTol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theta: float,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
        relTol: float,
        solverType: ImplicitEulerScheme.SolverType,
    ) -> None: ...
    def step(
        self,
        a: Array,
        t: float,
    ) -> None: ...
    def setStep(
        self,
        dt: float,
    ) -> None: ...
    def numberOfIterations(self) -> int: ...

class DouglasScheme:
    @overload
    def __init__(
        self,
        theta: float,
        map: FdmLinearOpComposite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theta: float,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
    ) -> None: ...
    def step(
        self,
        a: Array,
        t: float,
    ) -> None: ...
    def setStep(
        self,
        dt: float,
    ) -> None: ...

class ExplicitEulerScheme:
    @overload
    def __init__(
        self,
        map: FdmLinearOpComposite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
    ) -> None: ...
    def step(
        self,
        a: Array,
        t: float,
    ) -> None: ...
    def setStep(
        self,
        dt: float,
    ) -> None: ...

class HundsdorferScheme:
    @overload
    def __init__(
        self,
        theta: float,
        mu: float,
        map: FdmLinearOpComposite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theta: float,
        mu: float,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
    ) -> None: ...
    def step(
        self,
        a: Array,
        t: float,
    ) -> None: ...
    def setStep(
        self,
        dt: float,
    ) -> None: ...

class MethodOfLinesScheme:
    @overload
    def __init__(
        self,
        eps: float,
        relInitStepSize: float,
        map: FdmLinearOpComposite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        eps: float,
        relInitStepSize: float,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
    ) -> None: ...
    def step(
        self,
        a: Array,
        t: float,
    ) -> None: ...
    def setStep(
        self,
        dt: float,
    ) -> None: ...

class ModifiedCraigSneydScheme:
    @overload
    def __init__(
        self,
        theta: float,
        mu: float,
        map: FdmLinearOpComposite,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theta: float,
        mu: float,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
    ) -> None: ...
    def step(
        self,
        a: Array,
        t: float,
    ) -> None: ...
    def setStep(
        self,
        dt: float,
    ) -> None: ...

class FdmInnerValueCalculator:
    def __init__(self) -> None: ...
    def innerValue(
        self,
        iter: FdmLinearOpIterator,
        t: float,
    ) -> float: ...
    def avgInnerValue(
        self,
        iter: FdmLinearOpIterator,
        t: float,
    ) -> float: ...

class FdmCellAveragingInnerValue(FdmInnerValueCalculator):
    pass

class FdmLogInnerValue(FdmCellAveragingInnerValue):
    def __init__(
        self,
        payoff: Payoff,
        mesher: FdmMesher,
        direction: int,
    ) -> None: ...

class FdmLogBasketInnerValue(FdmInnerValueCalculator):
    def __init__(
        self,
        payoff: BasketPayoff,
        mesher: FdmMesher,
    ) -> None: ...

class FdmZeroInnerValue(FdmInnerValueCalculator):
    def __init__(self) -> None: ...

class FdmSnapshotCondition(StepCondition[Array]):
    def __init__(
        self,
        t: float,
    ) -> None: ...
    def getTime(self) -> float: ...
    def getValues(self) -> Array: ...

class FdmStepConditionComposite(StepCondition[Array]):
    def stoppingTimes(self) -> list[float]: ...
    def conditions(self) -> list[StepCondition[Array]]: ...
    def joinConditions(
        self,
        c1: FdmSnapshotCondition,
        c2: FdmStepConditionComposite,
    ) -> FdmStepConditionComposite: ...
    def vanillaComposite(
        self,
        schedule: list[Dividend],
        exercise: Exercise,
        mesher: FdmMesher,
        calculator: FdmInnerValueCalculator,
        refDate: Date,
        dayCounter: DayCounter,
    ) -> FdmStepConditionComposite: ...

class FdmAmericanStepCondition(StepCondition[Array]):
    def __init__(
        self,
        mesher: FdmMesher,
        calculator: FdmInnerValueCalculator,
    ) -> None: ...

class FdmArithmeticAverageCondition(StepCondition[Array]):
    def __init__(
        self,
        averageTimes: list[float],
        arg1: float,
        pastFixings: int,
        mesher: FdmMesher,
        equityDirection: int,
    ) -> None: ...

class FdmBermudanStepCondition(StepCondition[Array]):
    def __init__(
        self,
        exerciseDates: list[Date],
        referenceDate: Date,
        dayCounter: DayCounter,
        mesher: FdmMesher,
        calculator: FdmInnerValueCalculator,
    ) -> None: ...
    def exerciseTimes(self) -> list[float]: ...

class FdmSimpleStorageCondition(StepCondition[Array]):
    def __init__(
        self,
        exerciseTimes: list[float],
        mesher: FdmMesher,
        calculator: FdmInnerValueCalculator,
        changeRate: float,
    ) -> None: ...

class FdmSimpleSwingCondition(StepCondition[Array]):
    @overload
    def __init__(
        self,
        exerciseTimes: list[float],
        mesher: FdmMesher,
        calculator: FdmInnerValueCalculator,
        swingDirection: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        exerciseTimes: list[float],
        mesher: FdmMesher,
        calculator: FdmInnerValueCalculator,
        swingDirection: int,
        minExercises: int,
    ) -> None: ...

class FdmDividendHandler(StepCondition[Array]):
    def __init__(
        self,
        schedule: list[Dividend],
        mesher: FdmMesher,
        referenceDate: Date,
        dayCounter: DayCounter,
        equityDirection: int,
    ) -> None: ...
    def dividendTimes(self) -> list[float]: ...
    def dividendDates(self) -> list[Date]: ...
    def dividends(self) -> list[float]: ...

class FdmSolverDesc:
    pass

class Fdm1DimSolver:
    def __init__(
        self,
        solverDesc: FdmSolverDesc,
        schemeDesc: FdmSchemeDesc,
        op: FdmLinearOpComposite,
    ) -> None: ...
    def interpolateAt(
        self,
        x: float,
    ) -> float: ...
    def thetaAt(
        self,
        x: float,
    ) -> float: ...
    def derivativeX(
        self,
        x: float,
    ) -> float: ...
    def derivativeXX(
        self,
        x: float,
    ) -> float: ...

class FdmBackwardSolver:
    def __init__(
        self,
        map: FdmLinearOpComposite,
        bcSet: FdmBoundaryConditionSet,
        condition: FdmStepConditionComposite,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...
    def rollback(
        self,
        a: Array,
        from_: float,
        to: float,
        steps: int,
        dampingSteps: int,
    ) -> None: ...

class Fdm2dBlackScholesSolver:
    def valueAt(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def thetaAt(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def deltaXat(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def deltaYat(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def gammaXat(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def gammaYat(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def gammaXYat(
        self,
        x: float,
        y: float,
    ) -> float: ...

class Fdm2DimSolver:
    def __init__(
        self,
        solverDesc: FdmSolverDesc,
        schemeDesc: FdmSchemeDesc,
        op: FdmLinearOpComposite,
    ) -> None: ...
    def interpolateAt(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def thetaAt(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def derivativeX(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def derivativeY(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def derivativeXX(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def derivativeYY(
        self,
        x: float,
        y: float,
    ) -> float: ...
    def derivativeXY(
        self,
        x: float,
        y: float,
    ) -> float: ...

class Fdm3DimSolver:
    def __init__(
        self,
        solverDesc: FdmSolverDesc,
        schemeDesc: FdmSchemeDesc,
        op: FdmLinearOpComposite,
    ) -> None: ...
    def performCalculations(self) -> None: ...
    def interpolateAt(
        self,
        x: float,
        y: float,
        z: float,
    ) -> float: ...
    def thetaAt(
        self,
        x: float,
        y: float,
        z: float,
    ) -> float: ...

class FdmG2Solver:
    def valueAt(
        self,
        x: float,
        y: float,
    ) -> float: ...

class FdmHestonHullWhiteSolver:
    def valueAt(
        self,
        s: float,
        v: float,
        r: float,
    ) -> float: ...
    def thetaAt(
        self,
        s: float,
        v: float,
        r: float,
    ) -> float: ...
    def deltaAt(
        self,
        s: float,
        v: float,
        r: float,
        eps: float,
    ) -> float: ...
    def gammaAt(
        self,
        s: float,
        v: float,
        r: float,
        eps: float,
    ) -> float: ...

class FdmHestonSolver:
    def valueAt(
        self,
        s: float,
        v: float,
    ) -> float: ...
    def thetaAt(
        self,
        s: float,
        v: float,
    ) -> float: ...
    def deltaAt(
        self,
        s: float,
        v: float,
    ) -> float: ...
    def gammaAt(
        self,
        s: float,
        v: float,
    ) -> float: ...
    def meanVarianceDeltaAt(
        self,
        s: float,
        v: float,
    ) -> float: ...
    def meanVarianceGammaAt(
        self,
        s: float,
        v: float,
    ) -> float: ...

class FdmHullWhiteSolver:
    def valueAt(
        self,
        r: float,
    ) -> float: ...

class FdmIndicesOnBoundary:
    def __init__(
        self,
        l: FdmLinearOpLayout,
        direction: int,
        side: FdmDirichletBoundary.Side,
    ) -> None: ...

class RiskNeutralDensityCalculator:
    def __init__(self) -> None: ...
    def pdf(
        self,
        x: float,
        t: float,
    ) -> float: ...
    def cdf(
        self,
        x: float,
        t: float,
    ) -> float: ...
    def invcdf(
        self,
        p: float,
        t: float,
    ) -> float: ...

class BSMRNDCalculator(RiskNeutralDensityCalculator):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class CEVRNDCalculator(RiskNeutralDensityCalculator):
    def __init__(
        self,
        f0: float,
        alpha: float,
        beta: float,
    ) -> None: ...
    def massAtZero(
        self,
        t: float,
    ) -> float: ...

class GBSMRNDCalculator(RiskNeutralDensityCalculator):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class HestonRNDCalculator(RiskNeutralDensityCalculator):
    @overload
    def __init__(
        self,
        hestonProcess: HestonProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        hestonProcess: HestonProcess,
        integrationEps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        hestonProcess: HestonProcess,
        integrationEps: float,
        maxIntegrationIterations: int,
    ) -> None: ...

class LocalVolRNDCalculator(RiskNeutralDensityCalculator):
    @overload
    def __init__(
        self,
        spot: Quote,
        rTS: YieldTermStructure,
        qTS: YieldTermStructure,
        localVol: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spot: Quote,
        rTS: YieldTermStructure,
        qTS: YieldTermStructure,
        localVol: LocalVolTermStructure,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spot: Quote,
        rTS: YieldTermStructure,
        qTS: YieldTermStructure,
        localVol: LocalVolTermStructure,
        xGrid: int,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spot: Quote,
        rTS: YieldTermStructure,
        qTS: YieldTermStructure,
        localVol: LocalVolTermStructure,
        xGrid: int,
        tGrid: int,
        x0Density: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spot: Quote,
        rTS: YieldTermStructure,
        qTS: YieldTermStructure,
        localVol: LocalVolTermStructure,
        xGrid: int,
        tGrid: int,
        x0Density: float,
        localVolProbEps: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spot: Quote,
        rTS: YieldTermStructure,
        qTS: YieldTermStructure,
        localVol: LocalVolTermStructure,
        xGrid: int,
        tGrid: int,
        x0Density: float,
        localVolProbEps: float,
        maxIter: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spot: Quote,
        rTS: YieldTermStructure,
        qTS: YieldTermStructure,
        localVol: LocalVolTermStructure,
        xGrid: int,
        tGrid: int,
        x0Density: float,
        localVolProbEps: float,
        maxIter: int,
        gaussianStepSize: float,
    ) -> None: ...
    def mesher(
        self,
        t: float,
    ) -> Fdm1dMesher: ...

class SquareRootProcessRNDCalculator(RiskNeutralDensityCalculator):
    def __init__(
        self,
        v0: float,
        kappa: float,
        theta: float,
        sigma: float,
    ) -> None: ...
    def stationary_pdf(
        self,
        v: float,
    ) -> float: ...
    def stationary_cdf(
        self,
        v: float,
    ) -> float: ...
    def stationary_invcdf(
        self,
        q: float,
    ) -> float: ...

class FittingMethod:
    def size(self) -> int: ...
    def solution(self) -> Array: ...
    def numberOfIterations(self) -> int: ...
    def minimumCostValue(self) -> float: ...
    def constrainAtZero(self) -> bool: ...
    def weights(self) -> Array: ...

class FittedBondDiscountCurve(YieldTermStructure):
    @overload
    def __init__(
        self,
        referenceDate: Date,
        fittingMethod: FittingMethod,
        parameters: Array,
        maxDate: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
        accuracy: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
        accuracy: float,
        maxEvaluations: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
        accuracy: float,
        maxEvaluations: int,
        guess: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
        accuracy: float,
        maxEvaluations: int,
        guess: Array,
        simplexLambda: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        fittingMethod: FittingMethod,
        parameters: Array,
        maxDate: Date,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
        accuracy: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
        accuracy: float,
        maxEvaluations: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
        accuracy: float,
        maxEvaluations: int,
        guess: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        helpers: list[BondHelper],
        dayCounter: DayCounter,
        fittingMethod: FittingMethod,
        accuracy: float,
        maxEvaluations: int,
        guess: Array,
        simplexLambda: float,
    ) -> None: ...
    def fitResults(self) -> FittingMethod: ...
    def resetGuess(
        self,
        guess: Array,
    ) -> None: ...

class ExponentialSplinesFitting(FittingMethod):
    @overload
    def __init__(
        self,
        constrainAtZero: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        constrainAtZero: bool,
        weights: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
        numCoeffs: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
        numCoeffs: int,
        fixedKappa: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
        numCoeffs: int,
        fixedKappa: float,
        constraint: Constraint,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class NelsonSiegelFitting(FittingMethod):
    @overload
    def __init__(
        self,
        weights: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
        l2: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
        l2: Array,
        minCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
        constraint: Constraint,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SvenssonFitting(FittingMethod):
    @overload
    def __init__(
        self,
        weights: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
        l2: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
        l2: Array,
        minCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        weights: Array,
        optimizationMethod: OptimizationMethod,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
        constraint: Constraint,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class CubicBSplinesFitting(FittingMethod):
    @overload
    def __init__(
        self,
        knotVector: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        knotVector: list[float],
        constrainAtZero: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        knotVector: list[float],
        constrainAtZero: bool,
        weights: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        knotVector: list[float],
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        knotVector: list[float],
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        knotVector: list[float],
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        knotVector: list[float],
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
        constraint: Constraint,
    ) -> None: ...
    def basisFunction(
        self,
        i: int,
        t: float,
    ) -> float: ...

class SimplePolynomialFitting(FittingMethod):
    @overload
    def __init__(
        self,
        degree: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        degree: int,
        constrainAtZero: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        degree: int,
        constrainAtZero: bool,
        weights: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        degree: int,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
    ) -> None: ...
    @overload
    def __init__(
        self,
        degree: int,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        degree: int,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        degree: int,
        constrainAtZero: bool,
        weights: Array,
        l2: Array,
        minCutoffTime: float,
        maxCutoffTime: float,
        constraint: Constraint,
    ) -> None: ...

class SpreadFittingMethod(FittingMethod):
    @overload
    def __init__(
        self,
        method: FittingMethod,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        method: FittingMethod,
        discountCurve: Handle[YieldTermStructure],
        minCutoffTime: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        method: FittingMethod,
        discountCurve: Handle[YieldTermStructure],
        minCutoffTime: float,
        maxCutoffTime: float,
    ) -> None: ...

class Position:
    class Type(IntEnum):
        Long
        Short

    def __init__(self) -> None: ...

class ForwardRateAgreement(Instrument):
    @overload
    def __init__(
        self,
        index: IborIndex,
        valueDate: Date,
        maturityDate: Date,
        type: Position.Type,
        strikeForwardRate: float,
        notionalAmount: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        index: IborIndex,
        valueDate: Date,
        maturityDate: Date,
        type: Position.Type,
        strikeForwardRate: float,
        notionalAmount: float,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        index: IborIndex,
        valueDate: Date,
        type: Position.Type,
        strikeForwardRate: float,
        notionalAmount: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        index: IborIndex,
        valueDate: Date,
        type: Position.Type,
        strikeForwardRate: float,
        notionalAmount: float,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    def amount(self) -> float: ...
    def fixingDate(self) -> Date: ...
    def forwardRate(self) -> InterestRate: ...

class Gaussian1dModel(TermStructureConsistentModel):
    def stateProcess(self) -> StochasticProcess1D: ...
    @overload
    def numeraire(
        self,
        referenceDate: Date,
    ) -> float: ...
    @overload
    def numeraire(
        self,
        referenceDate: Date,
        y: float,
    ) -> float: ...
    @overload
    def numeraire(
        self,
        referenceDate: Date,
        y: float,
        yts: Handle[YieldTermStructure],
    ) -> float: ...
    @overload
    def numeraire(
        self,
        t: float,
    ) -> float: ...
    @overload
    def numeraire(
        self,
        t: float,
        y: float,
    ) -> float: ...
    @overload
    def numeraire(
        self,
        t: float,
        y: float,
        yts: Handle[YieldTermStructure],
    ) -> float: ...
    @overload
    def zerobond(
        self,
        T: float,
    ) -> float: ...
    @overload
    def zerobond(
        self,
        T: float,
        t: float,
    ) -> float: ...
    @overload
    def zerobond(
        self,
        T: float,
        t: float,
        y: float,
    ) -> float: ...
    @overload
    def zerobond(
        self,
        T: float,
        t: float,
        y: float,
        yts: Handle[YieldTermStructure],
    ) -> float: ...
    @overload
    def zerobond(
        self,
        maturity: Date,
    ) -> float: ...
    @overload
    def zerobond(
        self,
        maturity: Date,
        referenceDate: Date,
    ) -> float: ...
    @overload
    def zerobond(
        self,
        maturity: Date,
        referenceDate: Date,
        y: float,
    ) -> float: ...
    @overload
    def zerobond(
        self,
        maturity: Date,
        referenceDate: Date,
        y: float,
        yts: Handle[YieldTermStructure],
    ) -> float: ...
    @overload
    def zerobondOption(
        self,
        type: Option.Type,
        expiry: Date,
        valueDate: Date,
        maturity: Date,
        strike: float,
    ) -> float: ...
    @overload
    def zerobondOption(
        self,
        type: Option.Type,
        expiry: Date,
        valueDate: Date,
        maturity: Date,
        strike: float,
        referenceDate: Date,
    ) -> float: ...
    @overload
    def zerobondOption(
        self,
        type: Option.Type,
        expiry: Date,
        valueDate: Date,
        maturity: Date,
        strike: float,
        referenceDate: Date,
        y: float,
    ) -> float: ...
    @overload
    def zerobondOption(
        self,
        type: Option.Type,
        expiry: Date,
        valueDate: Date,
        maturity: Date,
        strike: float,
        referenceDate: Date,
        y: float,
        yts: Handle[YieldTermStructure],
    ) -> float: ...
    @overload
    def zerobondOption(
        self,
        type: Option.Type,
        expiry: Date,
        valueDate: Date,
        maturity: Date,
        strike: float,
        referenceDate: Date,
        y: float,
        yts: Handle[YieldTermStructure],
        yStdDevs: float,
    ) -> float: ...
    @overload
    def zerobondOption(
        self,
        type: Option.Type,
        expiry: Date,
        valueDate: Date,
        maturity: Date,
        strike: float,
        referenceDate: Date,
        y: float,
        yts: Handle[YieldTermStructure],
        yStdDevs: float,
        yGridPoints: int,
    ) -> float: ...
    @overload
    def zerobondOption(
        self,
        type: Option.Type,
        expiry: Date,
        valueDate: Date,
        maturity: Date,
        strike: float,
        referenceDate: Date,
        y: float,
        yts: Handle[YieldTermStructure],
        yStdDevs: float,
        yGridPoints: int,
        extrapolatePayoff: bool,
    ) -> float: ...
    @overload
    def zerobondOption(
        self,
        type: Option.Type,
        expiry: Date,
        valueDate: Date,
        maturity: Date,
        strike: float,
        referenceDate: Date,
        y: float,
        yts: Handle[YieldTermStructure],
        yStdDevs: float,
        yGridPoints: int,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
    ) -> float: ...
    @overload
    def forwardRate(
        self,
        fixing: Date,
    ) -> float: ...
    @overload
    def forwardRate(
        self,
        fixing: Date,
        referenceDate: Date,
    ) -> float: ...
    @overload
    def forwardRate(
        self,
        fixing: Date,
        referenceDate: Date,
        y: float,
    ) -> float: ...
    @overload
    def forwardRate(
        self,
        fixing: Date,
        referenceDate: Date,
        y: float,
        iborIdx: IborIndex,
    ) -> float: ...
    @overload
    def swapRate(
        self,
        fixing: Date,
        tenor: Period,
    ) -> float: ...
    @overload
    def swapRate(
        self,
        fixing: Date,
        tenor: Period,
        referenceDate: Date,
    ) -> float: ...
    @overload
    def swapRate(
        self,
        fixing: Date,
        tenor: Period,
        referenceDate: Date,
        y: float,
    ) -> float: ...
    @overload
    def swapRate(
        self,
        fixing: Date,
        tenor: Period,
        referenceDate: Date,
        y: float,
        swapIdx: SwapIndex,
    ) -> float: ...
    @overload
    def swapAnnuity(
        self,
        fixing: Date,
        tenor: Period,
    ) -> float: ...
    @overload
    def swapAnnuity(
        self,
        fixing: Date,
        tenor: Period,
        referenceDate: Date,
    ) -> float: ...
    @overload
    def swapAnnuity(
        self,
        fixing: Date,
        tenor: Period,
        referenceDate: Date,
        y: float,
    ) -> float: ...
    @overload
    def swapAnnuity(
        self,
        fixing: Date,
        tenor: Period,
        referenceDate: Date,
        y: float,
        swapIdx: SwapIndex,
    ) -> float: ...

class Gsr(Gaussian1dModel):
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        volstepdates: list[Date],
        volatilities: list[Handle[Quote]],
        reversions: list[Handle[Quote]],
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        volstepdates: list[Date],
        volatilities: list[Handle[Quote]],
        reversions: list[Handle[Quote]],
        T: float,
    ) -> None: ...
    @overload
    def calibrateVolatilitiesIterative(
        self,
        helpers: list[BlackCalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def calibrateVolatilitiesIterative(
        self,
        helpers: list[BlackCalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
        constraint: Constraint,
    ) -> None: ...
    @overload
    def calibrateVolatilitiesIterative(
        self,
        helpers: list[BlackCalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
        constraint: Constraint,
        weights: list[float],
    ) -> None: ...
    def reversion(self) -> Array: ...
    def volatility(self) -> Array: ...
    def params(self) -> Array: ...
    @overload
    def calibrate(
        self,
        instruments: list[CalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def calibrate(
        self,
        instruments: list[CalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
        constraint: Constraint,
    ) -> None: ...
    @overload
    def calibrate(
        self,
        instruments: list[CalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
        constraint: Constraint,
        weights: list[float],
    ) -> None: ...
    @overload
    def calibrate(
        self,
        instruments: list[CalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
        constraint: Constraint,
        weights: list[float],
        fixParameters: list[bool],
    ) -> None: ...
    def setParams(
        self,
        params: Array,
    ) -> None: ...
    def value(
        self,
        params: Array,
        instruments: list[CalibrationHelper],
    ) -> float: ...
    def constraint(self) -> Constraint: ...
    def endCriteria(self) -> EndCriteria.Type: ...
    def problemValues(self) -> Array: ...
    def functionEvaluation(self) -> int: ...

class MarkovFunctional(Gaussian1dModel):
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        reversion: float,
        volstepdates: list[Date],
        volatilities: list[float],
        capletVol: Handle[OptionletVolatilityStructure],
        capletExpiries: list[Date],
        iborIndex: IborIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        reversion: float,
        volstepdates: list[Date],
        volatilities: list[float],
        capletVol: Handle[OptionletVolatilityStructure],
        capletExpiries: list[Date],
        iborIndex: IborIndex,
        modelSettings: MarkovFunctional.ModelSettings,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        reversion: float,
        volstepdates: list[Date],
        volatilities: list[float],
        swaptionVol: Handle[SwaptionVolatilityStructure],
        swaptionExpiries: list[Date],
        swaptionTenors: list[Period],
        swapIndexBase: SwapIndex,
    ) -> None: ...
    @overload
    def __init__(
        self,
        termStructure: Handle[YieldTermStructure],
        reversion: float,
        volstepdates: list[Date],
        volatilities: list[float],
        swaptionVol: Handle[SwaptionVolatilityStructure],
        swaptionExpiries: list[Date],
        swaptionTenors: list[Period],
        swapIndexBase: SwapIndex,
        modelSettings: MarkovFunctional.ModelSettings,
    ) -> None: ...
    def volatility(self) -> Array: ...
    @overload
    def calibrate(
        self,
        helper: list[CalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
    ) -> None: ...
    @overload
    def calibrate(
        self,
        helper: list[CalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
        constraint: Constraint,
    ) -> None: ...
    @overload
    def calibrate(
        self,
        helper: list[CalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
        constraint: Constraint,
        weights: list[float],
    ) -> None: ...
    @overload
    def calibrate(
        self,
        helper: list[CalibrationHelper],
        method: OptimizationMethod,
        endCriteria: EndCriteria,
        constraint: Constraint,
        weights: list[float],
        fixParameters: list[bool],
    ) -> None: ...
    def params(self) -> Array: ...
    def setParams(
        self,
        params: Array,
    ) -> None: ...
    def value(
        self,
        params: Array,
        instruments: list[CalibrationHelper],
    ) -> float: ...
    def constraint(self) -> Constraint: ...
    def endCriteria(self) -> EndCriteria.Type: ...
    def problemValues(self) -> Array: ...
    def functionEvaluation(self) -> int: ...

class ModelSettings:
    class Adjustments(IntEnum):
        AdjustNone = 0
        AdjustDigitals = 1 << 0
        AdjustYts = 1 << 1
        ExtrapolatePayoffFlat = 1 << 2
        NoPayoffExtrapolation = 1 << 3
        KahaleSmile = 1 << 4
        SmileExponentialExtrapolation = 1 << 5
        KahaleInterpolation = 1 << 6
        SmileDeleteArbitragePoints = 1 << 7
        SabrSmile = 1 << 8

    @overload
    def __init__(
        self,
        yGridPoints: int,
        yStdDevs: float,
        gaussHermitePoints: int,
        digitalGap: float,
        marketRateAccuracy: float,
        lowerRateBound: float,
        upperRateBound: float,
        adjustments: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        yGridPoints: int,
        yStdDevs: float,
        gaussHermitePoints: int,
        digitalGap: float,
        marketRateAccuracy: float,
        lowerRateBound: float,
        upperRateBound: float,
        adjustments: int,
        smileMoneyCheckpoints: list[float],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def validate(self) -> None: ...

class Gaussian1dCapFloorEngine(PricingEngine):
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...

class Gaussian1dSwaptionEngine(PricingEngine):
    class Probabilities(IntEnum):
        None_
        Naive
        Digital

    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        discountCurve: Handle[YieldTermStructure],
        probabilities: Gaussian1dSwaptionEngine.Probabilities,
    ) -> None: ...

class Gaussian1dJamshidianSwaptionEngine(PricingEngine):
    def __init__(
        self,
        model: Gaussian1dModel,
    ) -> None: ...

class Gaussian1dNonstandardSwaptionEngine(PricingEngine):
    class Probabilities(IntEnum):
        None_
        Naive
        Digital

    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        oas: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        oas: Handle[Quote],
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        oas: Handle[Quote],
        discountCurve: Handle[YieldTermStructure],
        probabilities: Gaussian1dNonstandardSwaptionEngine.Probabilities,
    ) -> None: ...

class Gaussian1dFloatFloatSwaptionEngine(PricingEngine):
    class Probabilities(IntEnum):
        None_
        Naive
        Digital

    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        oas: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        oas: Handle[Quote],
        discountCurve: Handle[YieldTermStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        oas: Handle[Quote],
        discountCurve: Handle[YieldTermStructure],
        includeTodaysExercise: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        model: Gaussian1dModel,
        integrationPoints: int,
        stddevs: float,
        extrapolatePayoff: bool,
        flatPayoffExtrapolation: bool,
        oas: Handle[Quote],
        discountCurve: Handle[YieldTermStructure],
        includeTodaysExercise: bool,
        probabilities: Gaussian1dFloatFloatSwaptionEngine.Probabilities,
    ) -> None: ...

class SegmentIntegral:
    def __init__(
        self,
        intervals: int,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...

class SimpsonIntegral:
    def __init__(
        self,
        accuracy: float,
        maxIterations: int,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...

class GaussKronrodAdaptive:
    @overload
    def __init__(
        self,
        tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        tolerance: float,
        maxFunctionEvaluations: int,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...

class GaussKronrodNonAdaptive:
    def __init__(
        self,
        absoluteAccuracy: float,
        maxEvaluations: int,
        relativeAccuracy: float,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...

class GaussLobattoIntegral:
    @overload
    def __init__(
        self,
        maxIterations: int,
        absAccuracy: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maxIterations: int,
        absAccuracy: float,
        relAccuracy: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maxIterations: int,
        absAccuracy: float,
        relAccuracy: float,
        useConvergenceEstimate: bool,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...

class GaussianQuadrature:
    def __init__(self) -> None: ...
    def order(self) -> int: ...

class GaussLaguerreIntegration(GaussianQuadrature):
    @overload
    def __init__(
        self,
        n: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        s: float,
    ) -> None: ...

class GaussHermiteIntegration(GaussianQuadrature):
    @overload
    def __init__(
        self,
        n: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        mu: float,
    ) -> None: ...

class GaussJacobiIntegration(GaussianQuadrature):
    def __init__(
        self,
        n: int,
        alpha: float,
        beta: float,
    ) -> None: ...

class GaussHyperbolicIntegration(GaussianQuadrature):
    def __init__(
        self,
        n: int,
    ) -> None: ...

class GaussLegendreIntegration(GaussianQuadrature):
    def __init__(
        self,
        n: int,
    ) -> None: ...

class GaussChebyshevIntegration(GaussianQuadrature):
    def __init__(
        self,
        n: int,
    ) -> None: ...

class GaussChebyshev2ndIntegration(GaussianQuadrature):
    def __init__(
        self,
        n: int,
    ) -> None: ...

class GaussGegenbauerIntegration(GaussianQuadrature):
    def __init__(
        self,
        n: int,
        lambda_: float,
    ) -> None: ...

class TanhSinhIntegral:
    @overload
    def __init__(
        self,
        relTolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        relTolerance: float,
        maxRefinements: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        relTolerance: float,
        maxRefinements: int,
        minComplement: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def numberOfEvaluations(self) -> int: ...

class ExpSinhIntegral:
    @overload
    def __init__(
        self,
        relTolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        relTolerance: float,
        maxRefinements: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def numberOfEvaluations(self) -> int: ...

class LocalConstantVol(LocalVolTermStructure):
    @overload
    def __init__(
        self,
        referenceDate: Date,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        volatility: float,
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        volatility: Handle[Quote],
        dayCounter: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        volatility: float,
        dayCounter: DayCounter,
    ) -> None: ...

class LocalVolSurface(LocalVolTermStructure):
    @overload
    def __init__(
        self,
        blackTS: Handle[Any],
        riskFreeTS: Handle[YieldTermStructure],
        dividendTS: Handle[YieldTermStructure],
        underlying: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        blackTS: Handle[Any],
        riskFreeTS: Handle[YieldTermStructure],
        dividendTS: Handle[YieldTermStructure],
        underlying: float,
    ) -> None: ...

class NoExceptLocalVolSurface(LocalVolSurface):
    @overload
    def __init__(
        self,
        blackTS: Handle[Any],
        riskFreeTS: Handle[YieldTermStructure],
        dividendTS: Handle[YieldTermStructure],
        underlying: Handle[Quote],
        illegalLocalVolOverwrite: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        blackTS: Handle[Any],
        riskFreeTS: Handle[YieldTermStructure],
        dividendTS: Handle[YieldTermStructure],
        underlying: float,
        illegalLocalVolOverwrite: float,
    ) -> None: ...

class FixedLocalVolSurface(LocalVolTermStructure):
    class Extrapolation(IntEnum):
        ConstantExtrapolation
        InterpolatorDefaultExtrapolation


class GridModelLocalVolSurface(LocalVolTermStructure, CalibratedModel):
    pass

class LecuyerUniformRng:
    @overload
    def __init__(
        self,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def next(self) -> Sample[float]: ...

class KnuthUniformRng:
    @overload
    def __init__(
        self,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def next(self) -> Sample[float]: ...

class MersenneTwisterUniformRng:
    @overload
    def __init__(
        self,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def next(self) -> Sample[float]: ...

class Xoshiro256StarStarUniformRng:
    @overload
    def __init__(
        self,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def next(self) -> Sample[float]: ...

class UniformRandomGenerator:
    @overload
    def __init__(
        self,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def next(self) -> Sample[float]: ...

class GaussianRandomGenerator:
    def __init__(
        self,
        rng: UniformRandomGenerator,
    ) -> None: ...
    def next(self) -> Sample[float]: ...

class HaltonRsg:
    @overload
    def __init__(
        self,
        dimensionality: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
        randomStart: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
        randomStart: bool,
        randomShift: bool,
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def lastSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...

class SobolRsg:
    class DirectionIntegers(IntEnum):
        Unit
        Jaeckel
        SobolLevitan
        SobolLevitanLemieux
        JoeKuoD5
        JoeKuoD6
        JoeKuoD7
        Kuo
        Kuo2
        Kuo3

    @overload
    def __init__(
        self,
        dimensionality: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
        directionIntegers: SobolRsg.DirectionIntegers,
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def lastSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...
    def skipTo(
        self,
        n: int,
    ) -> None: ...

class Burley2020SobolRsg:
    @overload
    def __init__(
        self,
        dimensionality: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
        directionIntegers: SobolRsg.DirectionIntegers,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
        directionIntegers: SobolRsg.DirectionIntegers,
        scrambleSeed: int,
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def lastSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...

class SobolBrownianBridgeRsg:
    def __init__(
        self,
        factors: int,
        steps: int,
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def lastSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...

class Burley2020SobolBrownianBridgeRsg:
    def __init__(
        self,
        factors: int,
        steps: int,
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def lastSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...

class UniformRandomSequenceGenerator:
    def __init__(
        self,
        dimensionality: int,
        rng: UniformRandomGenerator,
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...

class UniformLowDiscrepancySequenceGenerator:
    @overload
    def __init__(
        self,
        dimensionality: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dimensionality: int,
        seed: int,
        directionIntegers: SobolRsg.DirectionIntegers,
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...

class ZigguratXoshiro256StarStarGaussianRsg:
    def __init__(
        self,
        dimensionality: int,
        rng: ZigguratGaussianRng[Xoshiro256StarStarUniformRng],
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...

class GaussianRandomSequenceGenerator:
    def __init__(
        self,
        uniformSequenceGenerator: UniformRandomSequenceGenerator,
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...

class GaussianLowDiscrepancySequenceGenerator:
    def __init__(
        self,
        u: UniformLowDiscrepancySequenceGenerator,
    ) -> None: ...
    def nextSequence(self) -> Sample[list[float]]: ...
    def dimension(self) -> int: ...

class BrownianGenerator:
    def __init__(self) -> None: ...
    def nextStep(
        self,
        arg0: list[float],
    ) -> float: ...
    def nextPath(self) -> float: ...
    def numberOfFactors(self) -> int: ...
    def numberOfSteps(self) -> int: ...

class BrownianGeneratorFactory:
    def __init__(self) -> None: ...
    def create(
        self,
        factors: int,
        steps: int,
    ) -> BrownianGenerator: ...

class MTBrownianGenerator(BrownianGenerator):
    @overload
    def __init__(
        self,
        factors: int,
        steps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        factors: int,
        steps: int,
        seed: int,
    ) -> None: ...

class MTBrownianGeneratorFactory(BrownianGeneratorFactory):
    @overload
    def __init__(
        self,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SobolBrownianGenerator(BrownianGenerator):
    class Ordering(IntEnum):
        Factors
        Steps
        Diagonal

    @overload
    def __init__(
        self,
        factors: int,
        steps: int,
        ordering: SobolBrownianGenerator.Ordering,
    ) -> None: ...
    @overload
    def __init__(
        self,
        factors: int,
        steps: int,
        ordering: SobolBrownianGenerator.Ordering,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        factors: int,
        steps: int,
        ordering: SobolBrownianGenerator.Ordering,
        seed: int,
        directionIntegers: SobolRsg.DirectionIntegers,
    ) -> None: ...

class SobolBrownianGeneratorFactory(BrownianGeneratorFactory):
    @overload
    def __init__(
        self,
        ordering: SobolBrownianGenerator.Ordering,
    ) -> None: ...
    @overload
    def __init__(
        self,
        ordering: SobolBrownianGenerator.Ordering,
        seed: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        ordering: SobolBrownianGenerator.Ordering,
        seed: int,
        directionIntegers: SobolRsg.DirectionIntegers,
    ) -> None: ...

class EvolutionDescription:
    def rateTimes(self) -> list[float]: ...
    def rateTaus(self) -> list[float]: ...
    def evolutionTimes(self) -> list[float]: ...
    def numberOfRates(self) -> int: ...
    def numberOfSteps(self) -> int: ...

class MarketModel:
    def __init__(self) -> None: ...
    def initialRates(self) -> list[float]: ...
    def displacements(self) -> list[float]: ...
    def evolution(self) -> EvolutionDescription: ...
    def numberOfRates(self) -> int: ...
    def numberOfFactors(self) -> int: ...
    def numberOfSteps(self) -> int: ...
    def pseudoRoot(
        self,
        i: int,
    ) -> Matrix: ...
    def covariance(
        self,
        i: int,
    ) -> Matrix: ...
    def totalCovariance(
        self,
        endIndex: int,
    ) -> Matrix: ...
    def timeDependentVolatility(
        self,
        i: int,
    ) -> list[float]: ...

class MarketModelFactory:
    def __init__(self) -> None: ...
    def create(
        self,
        arg0: EvolutionDescription,
        numberOfFactors: int,
    ) -> MarketModel: ...

class PiecewiseConstantCorrelation:
    def __init__(self) -> None: ...
    def times(self) -> list[float]: ...
    def rateTimes(self) -> list[float]: ...
    def correlations(self) -> list[Matrix]: ...
    def correlation(
        self,
        i: int,
    ) -> Matrix: ...
    def numberOfRates(self) -> int: ...

class ExponentialForwardCorrelation(PiecewiseConstantCorrelation):
    @overload
    def __init__(
        self,
        rateTimes: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        rateTimes: list[float],
        longTermCorr: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rateTimes: list[float],
        longTermCorr: float,
        beta: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rateTimes: list[float],
        longTermCorr: float,
        beta: float,
        gamma: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rateTimes: list[float],
        longTermCorr: float,
        beta: float,
        gamma: float,
        times: list[float],
    ) -> None: ...

class CurveState:
    def __init__(self) -> None: ...
    def numberOfRates(self) -> int: ...
    def rateTimes(self) -> list[float]: ...
    def rateTaus(self) -> list[float]: ...
    def discountRatio(
        self,
        i: int,
        j: int,
    ) -> float: ...
    def forwardRate(
        self,
        i: int,
    ) -> float: ...
    def coterminalSwapAnnuity(
        self,
        numeraire: int,
        i: int,
    ) -> float: ...
    def coterminalSwapRate(
        self,
        i: int,
    ) -> float: ...
    def cmSwapAnnuity(
        self,
        numeraire: int,
        i: int,
        spanningForwards: int,
    ) -> float: ...
    def cmSwapRate(
        self,
        i: int,
        spanningForwards: int,
    ) -> float: ...
    def forwardRates(self) -> list[float]: ...
    def coterminalSwapRates(self) -> list[float]: ...
    def cmSwapRates(
        self,
        spanningForwards: int,
    ) -> list[float]: ...
    def swapRate(
        self,
        begin: int,
        end: int,
    ) -> float: ...

class LMMCurveState(CurveState):
    def __init__(
        self,
        rateTimes: list[float],
    ) -> None: ...
    @overload
    def setOnForwardRates(
        self,
        fwdRates: list[float],
    ) -> None: ...
    @overload
    def setOnForwardRates(
        self,
        fwdRates: list[float],
        firstValidIndex: int,
    ) -> None: ...
    @overload
    def setOnDiscountRatios(
        self,
        discRatios: list[float],
    ) -> None: ...
    @overload
    def setOnDiscountRatios(
        self,
        discRatios: list[float],
        firstValidIndex: int,
    ) -> None: ...

class LMMDriftCalculator:
    def __init__(
        self,
        pseudo: Matrix,
        displacements: list[float],
        taus: list[float],
        numeraire: int,
        alive: int,
    ) -> None: ...
    @overload
    def compute(
        self,
        cs: LMMCurveState,
        drifts: list[float],
    ) -> None: ...
    @overload
    def compute(
        self,
        fwds: list[float],
        drifts: list[float],
    ) -> None: ...
    @overload
    def computePlain(
        self,
        cs: LMMCurveState,
        drifts: list[float],
    ) -> None: ...
    @overload
    def computePlain(
        self,
        fwds: list[float],
        drifts: list[float],
    ) -> None: ...
    @overload
    def computeReduced(
        self,
        cs: LMMCurveState,
        drifts: list[float],
    ) -> None: ...
    @overload
    def computeReduced(
        self,
        fwds: list[float],
        drifts: list[float],
    ) -> None: ...

class MarketModelEvolver:
    def __init__(self) -> None: ...
    def startNewPath(self) -> float: ...
    def advanceStep(self) -> float: ...
    def currentStep(self) -> int: ...
    def currentState(self) -> CurveState: ...
    def setInitialState(
        self,
        arg0: CurveState,
    ) -> None: ...

class LogNormalFwdRateIpc(MarketModelEvolver):
    pass

class AbcdVol(MarketModel):
    def __init__(
        self,
        a: float,
        b: float,
        c: float,
        d: float,
        ks: list[float],
        corr: PiecewiseConstantCorrelation,
        evolution: EvolutionDescription,
        numberOfFactors: int,
        initialRates: list[float],
        displacements: list[float],
    ) -> None: ...

class AbcdMathFunction:
    @overload
    def __init__(
        self,
        a: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        a: float,
        b: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        a: float,
        b: float,
        c: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        a: float,
        b: float,
        c: float,
        d: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        abcd: list[float],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __call__(
        self,
        t: float,
    ) -> float: ...
    def maximumLocation(self) -> float: ...
    def maximumValue(self) -> float: ...
    def longTermValue(self) -> float: ...
    def derivative(
        self,
        t: float,
    ) -> float: ...
    def primitive(
        self,
        t: float,
    ) -> float: ...
    def definiteIntegral(
        self,
        t1: float,
        t2: float,
    ) -> float: ...
    def a(self) -> float: ...
    def b(self) -> float: ...
    def c(self) -> float: ...
    def d(self) -> float: ...
    def coefficients(self) -> list[float]: ...
    def derivativeCoefficients(self) -> list[float]: ...
    def definiteIntegralCoefficients(
        self,
        t: float,
        t2: float,
    ) -> list[float]: ...
    def definiteDerivativeCoefficients(
        self,
        t: float,
        t2: float,
    ) -> list[float]: ...
    def validate(
        self,
        a: float,
        b: float,
        c: float,
        d: float,
    ) -> None: ...

class AbcdFunction(AbcdMathFunction):
    @overload
    def __init__(
        self,
        a: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        a: float,
        b: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        a: float,
        b: float,
        c: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        a: float,
        b: float,
        c: float,
        d: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def maximumVolatility(self) -> float: ...
    def shortTermVolatility(self) -> float: ...
    def longTermVolatility(self) -> float: ...
    @overload
    def covariance(
        self,
        t1: float,
        t2: float,
        T: float,
        S: float,
    ) -> float: ...
    @overload
    def covariance(
        self,
        t: float,
        T: float,
        S: float,
    ) -> float: ...
    def volatility(
        self,
        tMin: float,
        tMax: float,
        T: float,
    ) -> float: ...
    def variance(
        self,
        tMin: float,
        tMax: float,
        T: float,
    ) -> float: ...
    def instantaneousVolatility(
        self,
        t: float,
        T: float,
    ) -> float: ...
    def instantaneousVariance(
        self,
        t: float,
        T: float,
    ) -> float: ...
    def instantaneousCovariance(
        self,
        u: float,
        T: float,
        S: float,
    ) -> float: ...
    def primitive(
        self,
        t: float,
        T: float,
        S: float,
    ) -> float: ...

class ContinuousFloatingLookbackOption(OneAssetOption):
    def __init__(
        self,
        currentMinmax: float,
        payoff: TypePayoff,
        exercise: Exercise,
    ) -> None: ...

class ContinuousFixedLookbackOption(OneAssetOption):
    def __init__(
        self,
        currentMinmax: float,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class ContinuousPartialFloatingLookbackOption(ContinuousFloatingLookbackOption):
    def __init__(
        self,
        currentMinmax: float,
        lambda_: float,
        lookbackPeriodEnd: Date,
        payoff: TypePayoff,
        exercise: Exercise,
    ) -> None: ...

class ContinuousPartialFixedLookbackOption(ContinuousFixedLookbackOption):
    def __init__(
        self,
        lookbackPeriodStart: Date,
        payoff: StrikedTypePayoff,
        exercise: Exercise,
    ) -> None: ...

class AnalyticContinuousFloatingLookbackEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticContinuousFixedLookbackEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticContinuousPartialFloatingLookbackEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class AnalyticContinuousPartialFixedLookbackEngine(PricingEngine):
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...

class Path:
    def __init__(self) -> None: ...
    def length(self) -> int: ...
    def value(
        self,
        i: int,
    ) -> float: ...
    def front(self) -> float: ...
    def back(self) -> float: ...
    def time(
        self,
        i: int,
    ) -> float: ...

class MultiPath:
    def __init__(self) -> None: ...
    def pathSize(self) -> int: ...
    def assetNumber(self) -> int: ...
    def at(
        self,
        j: int,
    ) -> Path: ...

class BrownianBridge:
    @overload
    def __init__(
        self,
        steps: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeGrid: TimeGrid,
    ) -> None: ...
    @overload
    def __init__(
        self,
        times: list[float],
    ) -> None: ...
    def size(self) -> int: ...
    def times(self) -> list[float]: ...
    def leftWeight(self) -> list[float]: ...
    def rightWeight(self) -> list[float]: ...
    def stdDeviation(self) -> list[float]: ...

class DefaultBoundaryCondition:
    class Side(IntEnum):
        None_
        Upper
        Lower

    def __init__(self) -> None: ...

class NeumannBC(DefaultBoundaryCondition):
    def __init__(
        self,
        value: float,
        side: DefaultBoundaryCondition.Side,
    ) -> None: ...

class DirichletBC(DefaultBoundaryCondition):
    def __init__(
        self,
        value: float,
        side: DefaultBoundaryCondition.Side,
    ) -> None: ...

class TridiagonalOperator:
    def __init__(
        self,
        low: Array,
        mid: Array,
        high: Array,
    ) -> None: ...
    def solveFor(
        self,
        rhs: Array,
    ) -> Array: ...
    def applyTo(
        self,
        v: Array,
    ) -> Array: ...
    def size(self) -> int: ...
    def setFirstRow(
        self,
        arg0: float,
        arg1: float,
    ) -> None: ...
    def setMidRow(
        self,
        arg0: int,
        arg1: float,
        arg2: float,
        arg3: float,
    ) -> None: ...
    def setMidRows(
        self,
        arg0: float,
        arg1: float,
        arg2: float,
    ) -> None: ...
    def setLastRow(
        self,
        arg0: float,
        arg1: float,
    ) -> None: ...
    def identity(
        self,
        size: int,
    ) -> TridiagonalOperator: ...

class DPlus(TridiagonalOperator):
    def __init__(
        self,
        gridPoints: int,
        h: float,
    ) -> None: ...

class DMinus(TridiagonalOperator):
    def __init__(
        self,
        gridPoints: int,
        h: float,
    ) -> None: ...

class DZero(TridiagonalOperator):
    def __init__(
        self,
        gridPoints: int,
        h: float,
    ) -> None: ...

class DPlusDMinus(TridiagonalOperator):
    def __init__(
        self,
        gridPoints: int,
        h: float,
    ) -> None: ...

class HestonSLVProcess(StochasticProcess):
    @overload
    def __init__(
        self,
        hestonProcess: HestonProcess,
        leverageFct: LocalVolTermStructure,
    ) -> None: ...
    @overload
    def __init__(
        self,
        hestonProcess: HestonProcess,
        leverageFct: LocalVolTermStructure,
        mixingFactor: float,
    ) -> None: ...

class HestonSLVMCModel:
    def hestonProcess(self) -> HestonProcess: ...
    def localVol(self) -> LocalVolTermStructure: ...
    def leverageFunction(self) -> LocalVolTermStructure: ...

class FdmHestonGreensFct:
    class Algorithm(IntEnum):
        ZeroCorrelation
        Gaussian
        SemiAnalytical

    def __init__(self) -> None: ...

class HestonSLVFokkerPlanckFdmParams:
    pass

class HestonSLVFDMModel:
    def hestonProcess(self) -> HestonProcess: ...
    def localVol(self) -> LocalVolTermStructure: ...
    def leverageFunction(self) -> LocalVolTermStructure: ...

class SpreadOption(MultiAssetOption):
    def __init__(
        self,
        payoff: PlainVanillaPayoff,
        exercise: Exercise,
    ) -> None: ...

class KirkSpreadOptionEngine(PricingEngine):
    def __init__(
        self,
        process1: BlackProcess,
        process2: BlackProcess,
        correlation: Handle[Quote],
    ) -> None: ...

class Statistics:
    def __init__(self) -> None: ...
    def samples(self) -> int: ...
    def weightSum(self) -> float: ...
    def mean(self) -> float: ...
    def variance(self) -> float: ...
    def standardDeviation(self) -> float: ...
    def errorEstimate(self) -> float: ...
    def skewness(self) -> float: ...
    def kurtosis(self) -> float: ...
    def min(self) -> float: ...
    def max(self) -> float: ...
    def reset(self) -> None: ...
    @overload
    def add(
        self,
        value: float,
    ) -> None: ...
    @overload
    def add(
        self,
        value: float,
        weight: float,
    ) -> None: ...

class IncrementalStatistics:
    def __init__(self) -> None: ...
    def samples(self) -> int: ...
    def weightSum(self) -> float: ...
    def mean(self) -> float: ...
    def variance(self) -> float: ...
    def standardDeviation(self) -> float: ...
    def errorEstimate(self) -> float: ...
    def skewness(self) -> float: ...
    def kurtosis(self) -> float: ...
    def min(self) -> float: ...
    def max(self) -> float: ...
    def reset(self) -> None: ...
    @overload
    def add(
        self,
        value: float,
    ) -> None: ...
    @overload
    def add(
        self,
        value: float,
        weight: float,
    ) -> None: ...

class RiskStatistics(Statistics):
    def __init__(self) -> None: ...
    def semiVariance(self) -> float: ...
    def semiDeviation(self) -> float: ...
    def downsideVariance(self) -> float: ...
    def downsideDeviation(self) -> float: ...
    def regret(
        self,
        target: float,
    ) -> float: ...
    def potentialUpside(
        self,
        percentile: float,
    ) -> float: ...
    def valueAtRisk(
        self,
        percentile: float,
    ) -> float: ...
    def expectedShortfall(
        self,
        percentile: float,
    ) -> float: ...
    def shortfall(
        self,
        target: float,
    ) -> float: ...
    def averageShortfall(
        self,
        target: float,
    ) -> float: ...

class CapFloorTermVolatilityStructure(VolatilityTermStructure):
    def __init__(self) -> None: ...
    @overload
    def volatility(
        self,
        end: Date,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        end: Date,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def volatility(
        self,
        end: float,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        end: float,
        strike: float,
        extrapolate: bool,
    ) -> float: ...
    @overload
    def volatility(
        self,
        length: Period,
        strike: float,
    ) -> float: ...
    @overload
    def volatility(
        self,
        length: Period,
        strike: float,
        extrapolate: bool,
    ) -> float: ...

class CapFloorTermVolCurve(CapFloorTermVolatilityStructure):
    @overload
    def __init__(
        self,
        referenceDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        lengths: list[Period],
        vols: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        referenceDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        lengths: list[Period],
        vols: list[float],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        lengths: list[Period],
        vols: list[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        lengths: list[Period],
        vols: list[float],
        dc: DayCounter,
    ) -> None: ...

class CapFloorTermVolSurface(CapFloorTermVolatilityStructure):
    @overload
    def __init__(
        self,
        settlementDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        strikes: list[float],
        quotes: list[list[Handle[Quote]]],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        strikes: list[float],
        quotes: list[list[Handle[Quote]]],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        strikes: list[float],
        volatilities: Matrix,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDate: Date,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        strikes: list[float],
        volatilities: Matrix,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        strikes: list[float],
        quotes: list[list[Handle[Quote]]],
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        strikes: list[float],
        quotes: list[list[Handle[Quote]]],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        strikes: list[float],
        volatilities: Matrix,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        optionTenors: list[Period],
        strikes: list[float],
        volatilities: Matrix,
        dc: DayCounter,
    ) -> None: ...
    def maxDate(self) -> Date: ...
    def minStrike(self) -> float: ...
    def maxStrike(self) -> float: ...
    def optionTenors(self) -> list[Period]: ...
    def optionDates(self) -> list[Date]: ...
    def optionTimes(self) -> list[float]: ...
    def strikes(self) -> list[float]: ...

class StrippedOptionletBase:
    def __init__(self) -> None: ...
    def optionletStrikes(
        self,
        i: int,
    ) -> list[float]: ...
    def optionletVolatilities(
        self,
        i: int,
    ) -> list[float]: ...
    def optionletFixingDates(self) -> list[Date]: ...
    def optionletFixingTimes(self) -> list[float]: ...
    def optionletMaturities(self) -> int: ...
    def atmOptionletRates(self) -> list[float]: ...
    def dayCounter(self) -> DayCounter: ...
    def calendar(self) -> Calendar: ...
    def settlementDays(self) -> int: ...
    def businessDayConvention(self) -> BusinessDayConvention: ...
    def volatilityType(self) -> VolatilityType: ...
    def displacement(self) -> float: ...

class StrippedOptionlet(StrippedOptionletBase):
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        iborIndex: IborIndex,
        optionletDates: list[Date],
        strikes: list[float],
        volatilities: list[list[Handle[Quote]]],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        iborIndex: IborIndex,
        optionletDates: list[Date],
        strikes: list[float],
        volatilities: list[list[Handle[Quote]]],
        dc: DayCounter,
        type: VolatilityType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        settlementDays: int,
        calendar: Calendar,
        bdc: BusinessDayConvention,
        iborIndex: IborIndex,
        optionletDates: list[Date],
        strikes: list[float],
        volatilities: list[list[Handle[Quote]]],
        dc: DayCounter,
        type: VolatilityType,
        displacement: float,
    ) -> None: ...

class OptionletStripper1(StrippedOptionletBase):
    def capFloorPrices(self) -> Matrix: ...
    def capFloorVolatilities(self) -> Matrix: ...
    def optionletPrices(self) -> Matrix: ...
    def switchStrike(self) -> float: ...

class StrippedOptionletAdapter(OptionletVolatilityStructure):
    def __init__(
        self,
        arg0: StrippedOptionletBase,
    ) -> None: ...

class Settlement:
    class Type(IntEnum):
        Physical
        Cash

    class Method(IntEnum):
        PhysicalOTC
        PhysicalCleared
        CollateralizedCashPrice
        ParYieldCurve

    def __init__(self) -> None: ...

class Swaption(Option):
    class PriceType(IntEnum):
        Spot
        Forward

    @overload
    def __init__(
        self,
        swap: FixedVsFloatingSwap,
        exercise: Exercise,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swap: FixedVsFloatingSwap,
        exercise: Exercise,
        type: Settlement.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swap: FixedVsFloatingSwap,
        exercise: Exercise,
        type: Settlement.Type,
        settlementMethod: Settlement.Method,
    ) -> None: ...
    def settlementType(self) -> Settlement.Type: ...
    def settlementMethod(self) -> Settlement.Method: ...
    def type(self) -> VanillaSwap.Type: ...
    def underlying(self) -> FixedVsFloatingSwap: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        discountCurve: Handle[YieldTermStructure],
        guess: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        discountCurve: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        discountCurve: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        discountCurve: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        discountCurve: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        discountCurve: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
        type: VolatilityType,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        discountCurve: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
        type: VolatilityType,
        displacement: float,
    ) -> float: ...
    @overload
    def impliedVolatility(
        self,
        price: float,
        discountCurve: Handle[YieldTermStructure],
        guess: float,
        accuracy: float,
        maxEvaluations: int,
        minVol: float,
        maxVol: float,
        type: VolatilityType,
        displacement: float,
        priceType: Swaption.PriceType,
    ) -> float: ...

class NonstandardSwaption(Instrument):
    @overload
    def __init__(
        self,
        swap: NonstandardSwap,
        exercise: Exercise,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swap: NonstandardSwap,
        exercise: Exercise,
        type: Settlement.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swap: NonstandardSwap,
        exercise: Exercise,
        type: Settlement.Type,
        settlementMethod: Settlement.Method,
    ) -> None: ...
    def underlyingSwap(self) -> NonstandardSwap: ...

class FloatFloatSwaption(Instrument):
    @overload
    def __init__(
        self,
        swap: FloatFloatSwap,
        exercise: Exercise,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swap: FloatFloatSwap,
        exercise: Exercise,
        delivery: Settlement.Type,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swap: FloatFloatSwap,
        exercise: Exercise,
        delivery: Settlement.Type,
        settlementMethod: Settlement.Method,
    ) -> None: ...
    def underlyingSwap(self) -> FloatFloatSwap: ...

class BlackSwaptionEngine(PricingEngine):
    class CashAnnuityModel(IntEnum):
        SwapRate
        DiscountCurve

    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        v: Handle[SwaptionVolatilityStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        v: Handle[SwaptionVolatilityStructure],
        model: BlackSwaptionEngine.CashAnnuityModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        vol: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        vol: Handle[Quote],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        vol: Handle[Quote],
        dc: DayCounter,
        displacement: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        vol: Handle[Quote],
        dc: DayCounter,
        displacement: float,
        model: BlackSwaptionEngine.CashAnnuityModel,
    ) -> None: ...

class BachelierSwaptionEngine(PricingEngine):
    class CashAnnuityModel(IntEnum):
        SwapRate
        DiscountCurve

    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        v: Handle[SwaptionVolatilityStructure],
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        v: Handle[SwaptionVolatilityStructure],
        model: BachelierSwaptionEngine.CashAnnuityModel,
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        vol: Handle[Quote],
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        vol: Handle[Quote],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        discountCurve: Handle[YieldTermStructure],
        vol: Handle[Quote],
        dc: DayCounter,
        model: BachelierSwaptionEngine.CashAnnuityModel,
    ) -> None: ...

class MakeSwaption:
    @overload
    def __init__(
        self,
        swapIndex: SwapIndex,
        fixingDate: Date,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swapIndex: SwapIndex,
        fixingDate: Date,
        strike: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        swapIndex: SwapIndex,
        optionTenor: Period,
    ) -> None: ...
    @overload
    def __init__(
        self,
        swapIndex: SwapIndex,
        optionTenor: Period,
        strike: Optional[float],
    ) -> None: ...
    def withNominal(
        self,
        n: float,
    ) -> MakeSwaption: ...
    def withSettlementType(
        self,
        delivery: Settlement.Type,
    ) -> MakeSwaption: ...
    def withSettlementMethod(
        self,
        settlementMethod: Settlement.Method,
    ) -> MakeSwaption: ...
    def withOptionConvention(
        self,
        bdc: BusinessDayConvention,
    ) -> MakeSwaption: ...
    def withExerciseDate(
        self,
        arg0: Date,
    ) -> MakeSwaption: ...
    def withUnderlyingType(
        self,
        type: Swap.Type,
    ) -> MakeSwaption: ...
    @overload
    def withIndexedCoupons(
        self,
        flag: bool,
    ) -> MakeSwaption: ...
    @overload
    def withIndexedCoupons(self) -> MakeSwaption: ...
    @overload
    def withAtParCoupons(
        self,
        flag: bool,
    ) -> MakeSwaption: ...
    @overload
    def withAtParCoupons(self) -> MakeSwaption: ...
    def withPricingEngine(
        self,
        engine: PricingEngine,
    ) -> MakeSwaption: ...

class VanillaSwingOption(OneAssetOption):
    def __init__(
        self,
        payoff: Payoff,
        ex: SwingExercise,
        minExerciseRights: int,
        maxExerciseRights: int,
    ) -> None: ...

class FdSimpleBSSwingEngine(PricingEngine):
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        process: GeneralizedBlackScholesProcess,
        tGrid: int,
        xGrid: int,
        schemeDesc: FdmSchemeDesc,
    ) -> None: ...

class FdSimpleExtOUJumpSwingEngine(PricingEngine):
    pass

class ConstantEstimator:
    def __init__(
        self,
        size: int,
    ) -> None: ...
    def calculate(
        self,
        arg0: TimeSeries[float],
    ) -> TimeSeries[float]: ...

class ParkinsonSigma:
    def __init__(
        self,
        yearFraction: float,
    ) -> None: ...
    def calculate(
        self,
        arg0: TimeSeries[IntervalPrice],
    ) -> TimeSeries[float]: ...

class GarmanKlassSigma1:
    def __init__(
        self,
        yearFraction: float,
        marketOpenFraction: float,
    ) -> None: ...
    def calculate(
        self,
        arg0: TimeSeries[IntervalPrice],
    ) -> TimeSeries[float]: ...

class GarmanKlassSigma3:
    def __init__(
        self,
        yearFraction: float,
        marketOpenFraction: float,
    ) -> None: ...
    def calculate(
        self,
        arg0: TimeSeries[IntervalPrice],
    ) -> TimeSeries[float]: ...

class GarmanKlassSigma4:
    def __init__(
        self,
        yearFraction: float,
    ) -> None: ...
    def calculate(
        self,
        arg0: TimeSeries[IntervalPrice],
    ) -> TimeSeries[float]: ...

class GarmanKlassSigma5:
    def __init__(
        self,
        yearFraction: float,
    ) -> None: ...
    def calculate(
        self,
        arg0: TimeSeries[IntervalPrice],
    ) -> TimeSeries[float]: ...

class GarmanKlassSigma6:
    def __init__(
        self,
        yearFraction: float,
        marketOpenFraction: float,
    ) -> None: ...
    def calculate(
        self,
        arg0: TimeSeries[IntervalPrice],
    ) -> TimeSeries[float]: ...
