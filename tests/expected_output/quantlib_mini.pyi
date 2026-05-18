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

def asObservable() -> Observable: ...
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
def first() -> T1: ...
def second() -> T2: ...
def third() -> T3: ...
def numberOfEvaluations() -> int: ...
def dates() -> list[Date]: ...
def firstDate() -> Date: ...
def lastDate() -> Date: ...
def size() -> int: ...
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
    def __init__(
        self,
        str_: str,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def length(self) -> int: ...
    def units(self) -> TimeUnit: ...
    def frequency(self) -> Frequency: ...
    def normalized(self) -> Period: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

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
        d: int,
        m: Month,
        y: int,
        hours: int,
        minutes: int,
        seconds: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: int,
        m: Month,
        y: int,
        hours: int,
        minutes: int,
        seconds: int,
        millisec: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: int,
        m: Month,
        y: int,
        hours: int,
        minutes: int,
        seconds: int,
        millisec: int,
        microsec: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        serialNumber: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        str_: str,
        fmt: str,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def weekday(self) -> Weekday: ...
    def dayOfMonth(self) -> int: ...
    def dayOfYear(self) -> int: ...
    def month(self) -> Month: ...
    def year(self) -> int: ...
    def hours(self) -> int: ...
    def minutes(self) -> int: ...
    def seconds(self) -> int: ...
    def milliseconds(self) -> int: ...
    def microseconds(self) -> int: ...
    def fractionOfDay(self) -> float: ...
    def fractionOfSecond(self) -> float: ...
    def serialNumber(self) -> int: ...
    def isLeap(
        self,
        y: int,
    ) -> bool: ...
    def minDate(self) -> Date: ...
    def maxDate(self) -> Date: ...
    def todaysDate(self) -> Date: ...
    def localDateTime(self) -> Date: ...
    def universalDateTime(self) -> Date: ...
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
    @overload
    def __sub__(
        self,
        other: Date,
    ) -> int: ...
    def weekdayNumber(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def ISO(self) -> str: ...

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
    def parse(
        self,
        str_: str,
        fmt: str,
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
    def __str__(self) -> str: ...

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
    def __str__(self) -> str: ...

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
    def __str__(self) -> str: ...

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
    def __str__(self) -> str: ...

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
    def weights(self) -> Array: ...
    def x(self) -> Array: ...

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
    def __str__(self) -> str: ...

class LazyObject(Observable):
    def __init__(self) -> None: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...
    def forwardFirstNotificationOnly(self) -> None: ...
    def alwaysForwardNotifications(self) -> None: ...
    def forwardsAllNotifications(self) -> bool: ...

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
    def schedule(self) -> Schedule: ...

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
