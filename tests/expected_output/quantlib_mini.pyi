import typing
from typing import Any, Optional, overload
import collections.abc

class Weekday(int):
    Sunday: int = 1
    Monday: int = 2
    Tuesday: int = 3
    Wednesday: int = 4
    Thursday: int = 5
    Friday: int = 6
    Saturday: int = 7

class Month(int):
    January: int = 1
    February: int = 2
    March: int = 3
    April: int = 4
    May: int = 5
    June: int = 6
    July: int = 7
    August: int = 8
    September: int = 9
    October: int = 10
    November: int = 11
    December: int = 12

class TimeUnit(int):
    Days: int
    Weeks: int
    Months: int
    Years: int
    Hours: int
    Minutes: int
    Seconds: int
    Milliseconds: int
    Microseconds: int

class Frequency(int):
    NoFrequency: int = -1
    Once: int = 0
    Annual: int = 1
    Semiannual: int = 2
    EveryFourthMonth: int = 3
    Quarterly: int = 4
    Bimonthly: int = 6
    Monthly: int = 12
    EveryFourthWeek: int = 13
    Biweekly: int = 26
    Weekly: int = 52
    Daily: int = 365
    OtherFrequency: int = 999

class BusinessDayConvention(int):
    Following: int
    ModifiedFollowing: int
    Preceding: int
    ModifiedPreceding: int
    Unadjusted: int
    HalfMonthModifiedFollowing: int
    Nearest: int

class JointCalendarRule(int):
    JoinHolidays: int
    JoinBusinessDays: int

class Compounding(int):
    Simple: int
    Compounded: int
    Continuous: int
    SimpleThenCompounded: int
    CompoundedThenSimple: int

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
def as_iborindex(
    index: InterestRateIndex,
) -> IborIndex: ...
def as_swap_index(
    index: InterestRateIndex,
) -> SwapIndex: ...
def makeQuoteHandle(
    value: float,
) -> RelinkableHandle[Quote]: ...
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
        str: str,
        fmt: str,
    ) -> Date: ...
    def parseISO(
        self,
        str: str,
    ) -> Date: ...

class PeriodParser:
    def __init__(self) -> None: ...
    def parse(
        self,
        str: str,
    ) -> Period: ...

class IMM:
    class Month(int):
        F: int = 1
        G: int = 2
        H: int = 3
        J: int = 4
        K: int = 5
        M: int = 6
        N: int = 7
        Q: int = 8
        U: int = 9
        V: int = 10
        X: int = 11
        Z: int = 12
    
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
    class Month(int):
        F: int = 1
        G: int = 2
        H: int = 3
        J: int = 4
        K: int = 5
        M: int = 6
        N: int = 7
        Q: int = 8
        U: int = 9
        V: int = 10
        X: int = 11
        Z: int = 12
    
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
    ) -> typing.MutableSequence[Date]: ...
    @overload
    def holidayList(
        self,
        from_: Date,
        to: Date,
        includeWeekEnds: bool,
    ) -> typing.MutableSequence[Date]: ...
    def businessDayList(
        self,
        from_: Date,
        to: Date,
    ) -> typing.MutableSequence[Date]: ...
    def name(self) -> str: ...
    def empty(self) -> bool: ...

class Argentina(Calendar):
    class Market(int):
        Merval: int
    
    @overload
    def __init__(
        self,
        m: Argentina.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Australia(Calendar):
    class Market(int):
        Settlement: int
        ASX: int
    
    @overload
    def __init__(
        self,
        market: Australia.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Austria(Calendar):
    class Market(int):
        Settlement: int
        Exchange: int
    
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
    class Market(int):
        Settlement: int
        Exchange: int
    
    @overload
    def __init__(
        self,
        m: Brazil.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Canada(Calendar):
    class Market(int):
        Settlement: int
        TSX: int
    
    @overload
    def __init__(
        self,
        m: Canada.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Chile(Calendar):
    class Market(int):
        SSE: int
    
    @overload
    def __init__(
        self,
        m: Chile.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class China(Calendar):
    class Market(int):
        SSE: int
        IB: int
    
    @overload
    def __init__(
        self,
        m: China.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class CzechRepublic(Calendar):
    class Market(int):
        PSE: int
    
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
    class Market(int):
        Settlement: int
        Exchange: int
    
    @overload
    def __init__(
        self,
        m: France.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Germany(Calendar):
    class Market(int):
        Settlement: int
        FrankfurtStockExchange: int
        Xetra: int
        Eurex: int
    
    @overload
    def __init__(
        self,
        m: Germany.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class HongKong(Calendar):
    class Market(int):
        HKEx: int
    
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
    class Market(int):
        ICEX: int
    
    @overload
    def __init__(
        self,
        m: Iceland.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class India(Calendar):
    class Market(int):
        NSE: int
    
    @overload
    def __init__(
        self,
        m: India.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Indonesia(Calendar):
    class Market(int):
        BEJ: int
        JSX: int
    
    @overload
    def __init__(
        self,
        m: Indonesia.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Israel(Calendar):
    class Market(int):
        Settlement: int
        TASE: int
        SHIR: int
    
    @overload
    def __init__(
        self,
        m: Israel.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Italy(Calendar):
    class Market(int):
        Settlement: int
        Exchange: int
    
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
    class Market(int):
        BMV: int
    
    @overload
    def __init__(
        self,
        m: Mexico.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class NewZealand(Calendar):
    class Market(int):
        Wellington: int
        Auckland: int
    
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
    class Market(int):
        Settlement: int
        WSE: int
    
    @overload
    def __init__(
        self,
        m: Poland.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Romania(Calendar):
    class Market(int):
        Public: int
        BVB: int
    
    @overload
    def __init__(
        self,
        m: Romania.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Russia(Calendar):
    class Market(int):
        Settlement: int
        MOEX: int
    
    @overload
    def __init__(
        self,
        m: Russia.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SaudiArabia(Calendar):
    class Market(int):
        Tadawul: int
    
    @overload
    def __init__(
        self,
        m: SaudiArabia.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Singapore(Calendar):
    class Market(int):
        SGX: int
    
    @overload
    def __init__(
        self,
        m: Singapore.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Slovakia(Calendar):
    class Market(int):
        BSSE: int
    
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
    class Market(int):
        Settlement: int
        KRX: int
    
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
    class Market(int):
        TSEC: int
    
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
    class Market(int):
        USE: int
    
    @overload
    def __init__(
        self,
        m: Ukraine.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class UnitedKingdom(Calendar):
    class Market(int):
        Settlement: int
        Exchange: int
        Metals: int
    
    @overload
    def __init__(
        self,
        m: UnitedKingdom.Market,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class UnitedStates(Calendar):
    class Market(int):
        Settlement: int
        NYSE: int
        GovernmentBond: int
        NERC: int
        LiborImpact: int
        FederalReserve: int
        SOFR: int
    
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
        arg0: typing.MutableSequence[Calendar],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: typing.MutableSequence[Calendar],
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
    class Convention(int):
        Standard: int
        Canadian: int
        NoLeap: int
    
    @overload
    def __init__(
        self,
        c: Actual365Fixed.Convention,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Thirty360(DayCounter):
    class Convention(int):
        USA: int
        BondBasis: int
        European: int
        EurobondBasis: int
        Italian: int
        German: int
        ISMA: int
        ISDA: int
        NASD: int
    
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
    class Convention(int):
        ISMA: int
        Bond: int
        ISDA: int
        Historical: int
        Actual365: int
        AFB: int
        Euro: int
    
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
    class Type(int):
        None: int
        Spectral: int
        Hypersphere: int
        LowerDiagonal: int
        Higham: int
        Principal: int
    
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
    class Side(int):
        None: int
        Upper: int
        Lower: int
    
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
    ) -> DiscountFactor: ...
    @overload
    def discountFactor(
        self,
        d1: Date,
        d2: Date,
        refStart: Date,
    ) -> DiscountFactor: ...
    @overload
    def discountFactor(
        self,
        d1: Date,
        d2: Date,
        refStart: Date,
        refEnd: Date,
    ) -> DiscountFactor: ...
    @overload
    def discountFactor(
        self,
        t: float,
    ) -> DiscountFactor: ...
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
    class Type(int):
        None: int
        MaxIterations: int
        StationaryPoint: int
        StationaryFunctionValue: int
        StationaryFunctionAccuracy: int
        ZeroGradientNorm: int
        FunctionEpsilonTooSmall: int
        Unknown: int
    
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
    def lambda(self) -> float: ...

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
    class ResetScheme(int):
        NoResetScheme: int
        ResetToBestPoint: int
        ResetToOrigin: int
    
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
    class ResetScheme(int):
        NoResetScheme: int
        ResetToBestPoint: int
        ResetToOrigin: int
    
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
    class ResetScheme(int):
        NoResetScheme: int
        ResetToBestPoint: int
        ResetToOrigin: int
    
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
    class DerivativeApprox(int):
        Spline: int
        SplineOM1: int
        SplineOM2: int
        FourthOrder: int
        Parabolic: int
        FritschButland: int
        Akima: int
        Kruger: int
        Harmonic: int
    

class MixedInterpolation:
    class Behavior(int):
        ShareRanges: int
        SplitRanges: int
    

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
    class PointsType(int):
        FirstKind: int
        SecondKind: int
    
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

class LazyObject(Observable):
    def __init__(self) -> None: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...

class DateGeneration:
    class Rule(int):
        Backward: int
        Forward: int
        Zero: int
        ThirdWednesday: int
        ThirdWednesdayInclusive: int
        Twentieth: int
        TwentiethIMM: int
        OldCDS: int
        CDS: int
        CDS2015: int
    
    def __init__(self) -> None: ...

class Schedule:
    @overload
    def __init__(
        self,
        arg0: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: typing.MutableSequence[Date],
        calendar: Calendar,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: typing.MutableSequence[Date],
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
    def dates(self) -> typing.MutableSequence[Date]: ...
    def hasIsRegular(self) -> bool: ...
    @overload
    def isRegular(
        self,
        i: int,
    ) -> bool: ...
    @overload
    def isRegular(self) -> typing.MutableSequence[bool]: ...
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
    def from(
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

class IntervalPrice:
    class Type(int):
        Open: int
        Close: int
        High: int
        Low: int
    
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
    def open(self) -> float: ...
    def close(self) -> float: ...
    def high(self) -> float: ...
    def low(self) -> float: ...
    def makeSeries(
        self,
        d: typing.MutableSequence[Date],
        open: typing.MutableSequence[float],
        close: typing.MutableSequence[float],
        high: typing.MutableSequence[float],
        low: typing.MutableSequence[float],
    ) -> TimeSeries[IntervalPrice]: ...
    def extractValues(
        self,
        arg0: TimeSeries[IntervalPrice],
        t: IntervalPrice.Type,
    ) -> typing.MutableSequence[float]: ...
    def extractComponent(
        self,
        arg0: TimeSeries[IntervalPrice],
        t: IntervalPrice.Type,
    ) -> TimeSeries[float]: ...

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
    ) -> DiscountFactor: ...
    @overload
    def discount(
        self,
        arg0: Date,
        extrapolate: bool,
    ) -> DiscountFactor: ...
    @overload
    def discount(
        self,
        arg0: float,
    ) -> DiscountFactor: ...
    @overload
    def discount(
        self,
        arg0: float,
        extrapolate: bool,
    ) -> DiscountFactor: ...
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
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
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
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
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
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
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
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
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
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
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
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
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
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
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
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        comp: Compounding,
        freq: Frequency,
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
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
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        dc: DayCounter,
        factory: BackwardFlat,
    ) -> None: ...

class PiecewiseLinearForwardSpreadedTermStructure(YieldTermStructure):
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
        dc: DayCounter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        baseCurve: Handle[YieldTermStructure],
        spreads: typing.MutableSequence[Handle[Quote]],
        dates: typing.MutableSequence[Date],
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
        roundingDigits: ext.optional[int],
    ) -> None: ...
    @overload
    def __init__(
        self,
        curveHandle: Handle[YieldTermStructure],
        lastLiquidForwardRate: Handle[Quote],
        ultimateForwardRate: Handle[Quote],
        firstSmoothingPoint: Period,
        alpha: float,
        roundingDigits: ext.optional[int],
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
        roundingDigits: ext.optional[int],
        compounding: Compounding,
        frequency: Frequency,
    ) -> None: ...

class QuantoTermStructure(YieldTermStructure):
    def __init__(
        self,
        underlyingDividendTS: Handle[YieldTermStructure],
        riskFreeTS: Handle[YieldTermStructure],
        foreignRiskFreeTS: Handle[YieldTermStructure],
        underlyingBlackVolTS: Handle[BlackVolTermStructure],
        strike: float,
        exchRateBlackVolTS: Handle[BlackVolTermStructure],
        exchRateATMlevel: float,
        underlyingExchRateCorrelation: float,
    ) -> None: ...

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
    def histories(self) -> typing.MutableSequence[str]: ...
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

class Quote(Observable):
    def __init__(self) -> None: ...
    def value(self) -> float: ...
    def isValid(self) -> bool: ...

class SimpleQuote(Quote):
    @overload
    def __init__(
        self,
        value: doubleOrNull,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def setValue(
        self,
        value: doubleOrNull,
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
