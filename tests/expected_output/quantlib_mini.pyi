from typing import Any, Optional, overload, Generic, TypeVar, Union, Sequence, Iterable, Iterator
from enum import IntEnum

_T = TypeVar('_T')

class Handle(Generic[_T]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p: _T) -> None: ...
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

Sunday: Weekday
Monday: Weekday
Tuesday: Weekday
Wednesday: Weekday
Thursday: Weekday
Friday: Weekday
Saturday: Weekday

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

January: Month
February: Month
March: Month
April: Month
May: Month
June: Month
July: Month
August: Month
September: Month
October: Month
November: Month
December: Month

class TimeUnit(IntEnum):
    Days = ...
    Weeks = ...
    Months = ...
    Years = ...
    Hours = ...
    Minutes = ...
    Seconds = ...
    Milliseconds = ...
    Microseconds = ...

Days: TimeUnit
Weeks: TimeUnit
Months: TimeUnit
Years: TimeUnit
Hours: TimeUnit
Minutes: TimeUnit
Seconds: TimeUnit
Milliseconds: TimeUnit
Microseconds: TimeUnit

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

NoFrequency: Frequency
Once: Frequency
Annual: Frequency
Semiannual: Frequency
EveryFourthMonth: Frequency
Quarterly: Frequency
Bimonthly: Frequency
Monthly: Frequency
EveryFourthWeek: Frequency
Biweekly: Frequency
Weekly: Frequency
Daily: Frequency
OtherFrequency: Frequency

class BusinessDayConvention(IntEnum):
    Following = ...
    ModifiedFollowing = ...
    Preceding = ...
    ModifiedPreceding = ...
    Unadjusted = ...
    HalfMonthModifiedFollowing = ...
    Nearest = ...

Following: BusinessDayConvention
ModifiedFollowing: BusinessDayConvention
Preceding: BusinessDayConvention
ModifiedPreceding: BusinessDayConvention
Unadjusted: BusinessDayConvention
HalfMonthModifiedFollowing: BusinessDayConvention
Nearest: BusinessDayConvention

class JointCalendarRule(IntEnum):
    JoinHolidays = ...
    JoinBusinessDays = ...

JoinHolidays: JointCalendarRule
JoinBusinessDays: JointCalendarRule

class Compounding(IntEnum):
    Simple = ...
    Compounded = ...
    Continuous = ...
    SimpleThenCompounded = ...
    CompoundedThenSimple = ...

Simple: Compounding
Compounded: Compounding
Continuous: Compounding
SimpleThenCompounded: Compounding
CompoundedThenSimple: Compounding

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
def inverse(m: Union[Matrix, Sequence[Sequence[float]]]) -> Matrix: ...
def transpose(m: Union[Matrix, Sequence[Sequence[float]]]) -> Matrix: ...
def outerProduct(
    v1: Union[Array, Sequence[float]],
    v2: Union[Array, Sequence[float]],
) -> Matrix: ...
def pseudoSqrt(
    m: Union[Matrix, Sequence[Sequence[float]]],
    a: Union[SalvagingAlgorithm.Type, int],
) -> Matrix: ...
@overload
def CholeskyDecomposition(
    m: Union[Matrix, Sequence[Sequence[float]]],
    flexible: bool = ...,
) -> Matrix: ...
@overload
def CholeskyDecomposition(m: Union[Matrix, Sequence[Sequence[float]]]) -> Matrix: ...
def CholeskySolveFor(
    L: Union[Matrix, Sequence[Sequence[float]]],
    b: Union[Array, Sequence[float]],
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
class string:
    def __init__(self) -> None: ...

class Period:
    @overload
    def __init__(
        self,
        arg0: Union[Frequency, int],
    ) -> None: ...
    @overload
    def __init__(
        self,
        n: int,
        units: Union[TimeUnit, int],
    ) -> None: ...
    @overload
    def __init__(
        self,
        str: str,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def length(self) -> int: ...
    def units(self) -> TimeUnit: ...
    def frequency(self) -> Frequency: ...
    def normalized(self) -> Period: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __neg__(self) -> Period: ...
    def __add__(
        self,
        p: Period,
    ) -> Period: ...
    def __sub__(
        self,
        p: Period,
    ) -> Period: ...
    def __mul__(
        self,
        n: int,
    ) -> Period: ...
    def __rmul__(
        self,
        n: int,
    ) -> Period: ...
    def __lt__(
        self,
        other: Period,
    ) -> bool: ...
    def __gt__(
        self,
        other: Period,
    ) -> bool: ...
    def __le__(
        self,
        other: Period,
    ) -> bool: ...
    def __ge__(
        self,
        other: Period,
    ) -> bool: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __ne__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...

class PeriodVector(list[Period]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Period] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: Period) -> None: ...
    def push_back(self, x: Period) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class Date:
    @overload
    def __init__(
        self,
        d: int,
        m: Union[Month, int],
        y: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: int,
        m: Union[Month, int],
        y: int,
        hours: int,
        minutes: int,
        seconds: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: int,
        m: Union[Month, int],
        y: int,
        hours: int,
        minutes: int,
        seconds: int,
        millisec: int = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        d: int,
        m: Union[Month, int],
        y: int,
        hours: int,
        minutes: int,
        seconds: int,
        millisec: int = ...,
        microsec: int = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        serialNumber: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        str: str,
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
    @staticmethod
    def isLeap(y: int) -> bool: ...
    @staticmethod
    def minDate() -> Date: ...
    @staticmethod
    def maxDate() -> Date: ...
    @staticmethod
    def todaysDate() -> Date: ...
    @staticmethod
    def localDateTime() -> Date: ...
    @staticmethod
    def universalDateTime() -> Date: ...
    @staticmethod
    def startOfMonth(arg0: Date) -> Date: ...
    @staticmethod
    def endOfMonth(arg0: Date) -> Date: ...
    @staticmethod
    def isStartOfMonth(arg0: Date) -> bool: ...
    @staticmethod
    def isEndOfMonth(arg0: Date) -> bool: ...
    @staticmethod
    def nextWeekday(
        arg0: Date,
        arg1: Union[Weekday, int],
    ) -> Date: ...
    @staticmethod
    def nthWeekday(
        n: int,
        arg1: Union[Weekday, int],
        m: Union[Month, int],
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
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __ne__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __lt__(
        self,
        other: Date,
    ) -> bool: ...
    def __gt__(
        self,
        other: Date,
    ) -> bool: ...
    def __le__(
        self,
        other: Date,
    ) -> bool: ...
    def __ge__(
        self,
        other: Date,
    ) -> bool: ...
    def to_date(self) -> PyObject: ...
    @staticmethod
    def from_date(date: PyObject) -> Date: ...

class DateParser:
    def __init__(self) -> None: ...
    @staticmethod
    def parseFormatted(
        str: str,
        fmt: str,
    ) -> Date: ...
    @staticmethod
    def parseISO(str: str) -> Date: ...
    @staticmethod
    def parse(
        str: str,
        fmt: str,
    ) -> Date: ...

class PeriodParser:
    def __init__(self) -> None: ...
    @staticmethod
    def parse(str: str) -> Period: ...

class DateVector(list[Date]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Date] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: Date) -> None: ...
    def push_back(self, x: Date) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

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

    F: Month
    G: Month
    H: Month
    J: Month
    K: Month
    M: Month
    N: Month
    Q: Month
    U: Month
    V: Month
    X: Month
    Z: Month
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def isIMMdate(
        d: Date,
        mainCycle: bool = ...,
    ) -> bool: ...
    @overload
    @staticmethod
    def isIMMdate(d: Date) -> bool: ...
    @overload
    @staticmethod
    def isIMMcode(
        code: str,
        mainCycle: bool = ...,
    ) -> bool: ...
    @overload
    @staticmethod
    def isIMMcode(code: str) -> bool: ...
    @staticmethod
    def code(immDate: Date) -> str: ...
    @overload
    @staticmethod
    def date(
        immCode: str,
        referenceDate: Date = ...,
    ) -> Date: ...
    @overload
    @staticmethod
    def date(immCode: str) -> Date: ...
    @overload
    @staticmethod
    def nextDate() -> Date: ...
    @overload
    @staticmethod
    def nextDate(
        d: Date = ...,
        mainCycle: bool = ...,
    ) -> Date: ...
    @overload
    @staticmethod
    def nextDate(
        immCode: str,
        mainCycle: bool = ...,
    ) -> Date: ...
    @overload
    @staticmethod
    def nextDate(
        immCode: str,
        mainCycle: bool = ...,
        referenceDate: Date = ...,
    ) -> Date: ...
    @overload
    @staticmethod
    def nextDate(d: Date = ...) -> Date: ...
    @overload
    @staticmethod
    def nextDate(immCode: str) -> Date: ...
    @overload
    @staticmethod
    def nextCode() -> str: ...
    @overload
    @staticmethod
    def nextCode(
        d: Date = ...,
        mainCycle: bool = ...,
    ) -> str: ...
    @overload
    @staticmethod
    def nextCode(
        immCode: str,
        mainCycle: bool = ...,
    ) -> str: ...
    @overload
    @staticmethod
    def nextCode(
        immCode: str,
        mainCycle: bool = ...,
        referenceDate: Date = ...,
    ) -> str: ...
    @overload
    @staticmethod
    def nextCode(d: Date = ...) -> str: ...
    @overload
    @staticmethod
    def nextCode(immCode: str) -> str: ...

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

    F: Month
    G: Month
    H: Month
    J: Month
    K: Month
    M: Month
    N: Month
    Q: Month
    U: Month
    V: Month
    X: Month
    Z: Month
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def isASXdate(
        d: Date,
        mainCycle: bool = ...,
    ) -> bool: ...
    @overload
    @staticmethod
    def isASXdate(d: Date) -> bool: ...
    @overload
    @staticmethod
    def isASXcode(
        code: str,
        mainCycle: bool = ...,
    ) -> bool: ...
    @overload
    @staticmethod
    def isASXcode(code: str) -> bool: ...
    @staticmethod
    def code(asxDate: Date) -> str: ...
    @overload
    @staticmethod
    def date(
        asxCode: str,
        referenceDate: Date = ...,
    ) -> Date: ...
    @overload
    @staticmethod
    def date(asxCode: str) -> Date: ...
    @overload
    @staticmethod
    def nextDate() -> Date: ...
    @overload
    @staticmethod
    def nextDate(
        asxCode: str,
        mainCycle: bool = ...,
    ) -> Date: ...
    @overload
    @staticmethod
    def nextDate(
        asxCode: str,
        mainCycle: bool = ...,
        referenceDate: Date = ...,
    ) -> Date: ...
    @overload
    @staticmethod
    def nextDate(
        d: Date = ...,
        mainCycle: bool = ...,
    ) -> Date: ...
    @overload
    @staticmethod
    def nextDate(asxCode: str) -> Date: ...
    @overload
    @staticmethod
    def nextDate(d: Date = ...) -> Date: ...
    @overload
    @staticmethod
    def nextCode() -> str: ...
    @overload
    @staticmethod
    def nextCode(
        asxCode: str,
        mainCycle: bool = ...,
    ) -> str: ...
    @overload
    @staticmethod
    def nextCode(
        asxCode: str,
        mainCycle: bool = ...,
        referenceDate: Date = ...,
    ) -> str: ...
    @overload
    @staticmethod
    def nextCode(
        d: Date = ...,
        mainCycle: bool = ...,
    ) -> str: ...
    @overload
    @staticmethod
    def nextCode(asxCode: str) -> str: ...
    @overload
    @staticmethod
    def nextCode(d: Date = ...) -> str: ...

class Calendar:
    def __init__(self) -> None: ...
    def isWeekend(
        self,
        w: Union[Weekday, int],
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
        convention: Union[BusinessDayConvention, int] = ...,
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        n: int,
        unit: Union[TimeUnit, int],
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        n: int,
        unit: Union[TimeUnit, int],
        convention: Union[BusinessDayConvention, int] = ...,
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        n: int,
        unit: Union[TimeUnit, int],
        convention: Union[BusinessDayConvention, int] = ...,
        endOfMonth: bool = ...,
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
        convention: Union[BusinessDayConvention, int] = ...,
    ) -> Date: ...
    @overload
    def advance(
        self,
        d: Date,
        period: Period,
        convention: Union[BusinessDayConvention, int] = ...,
        endOfMonth: bool = ...,
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
        includeFirst: bool = ...,
    ) -> int: ...
    @overload
    def businessDaysBetween(
        self,
        from_: Date,
        to: Date,
        includeFirst: bool = ...,
        includeLast: bool = ...,
    ) -> int: ...
    @overload
    def holidayList(
        self,
        from_: Date,
        to: Date,
    ) -> DateVector: ...
    @overload
    def holidayList(
        self,
        from_: Date,
        to: Date,
        includeWeekEnds: bool = ...,
    ) -> DateVector: ...
    def businessDayList(
        self,
        from_: Date,
        to: Date,
    ) -> DateVector: ...
    def name(self) -> str: ...
    def empty(self) -> bool: ...
    def __str__(self) -> str: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __ne__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...

class CalendarVector(list[Calendar]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Calendar] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: Calendar) -> None: ...
    def push_back(self, x: Calendar) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class Argentina(Calendar):
    class Market(IntEnum):
        Merval = ...

    Merval: Market
    @overload
    def __init__(
        self,
        m: Union[Argentina.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Australia(Calendar):
    class Market(IntEnum):
        Settlement = ...
        ASX = ...

    Settlement: Market
    ASX: Market
    @overload
    def __init__(
        self,
        market: Union[Australia.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Austria(Calendar):
    class Market(IntEnum):
        Settlement = ...
        Exchange = ...

    Settlement: Market
    Exchange: Market
    @overload
    def __init__(
        self,
        m: Union[Austria.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Botswana(Calendar):
    def __init__(self) -> None: ...

class Brazil(Calendar):
    class Market(IntEnum):
        Settlement = ...
        Exchange = ...

    Settlement: Market
    Exchange: Market
    @overload
    def __init__(
        self,
        m: Union[Brazil.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Canada(Calendar):
    class Market(IntEnum):
        Settlement = ...
        TSX = ...

    Settlement: Market
    TSX: Market
    @overload
    def __init__(
        self,
        m: Union[Canada.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Chile(Calendar):
    class Market(IntEnum):
        SSE = ...

    SSE: Market
    @overload
    def __init__(
        self,
        m: Union[Chile.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class China(Calendar):
    class Market(IntEnum):
        SSE = ...
        IB = ...

    SSE: Market
    IB: Market
    @overload
    def __init__(
        self,
        m: Union[China.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class CzechRepublic(Calendar):
    class Market(IntEnum):
        PSE = ...

    PSE: Market
    @overload
    def __init__(
        self,
        m: Union[CzechRepublic.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Denmark(Calendar):
    def __init__(self) -> None: ...

class Finland(Calendar):
    def __init__(self) -> None: ...

class France(Calendar):
    class Market(IntEnum):
        Settlement = ...
        Exchange = ...

    Settlement: Market
    Exchange: Market
    @overload
    def __init__(
        self,
        m: Union[France.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Germany(Calendar):
    class Market(IntEnum):
        Settlement = ...
        FrankfurtStockExchange = ...
        Xetra = ...
        Eurex = ...

    Settlement: Market
    FrankfurtStockExchange: Market
    Xetra: Market
    Eurex: Market
    @overload
    def __init__(
        self,
        m: Union[Germany.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class HongKong(Calendar):
    class Market(IntEnum):
        HKEx = ...

    HKEx: Market
    @overload
    def __init__(
        self,
        m: Union[HongKong.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Hungary(Calendar):
    def __init__(self) -> None: ...

class Iceland(Calendar):
    class Market(IntEnum):
        ICEX = ...

    ICEX: Market
    @overload
    def __init__(
        self,
        m: Union[Iceland.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class India(Calendar):
    class Market(IntEnum):
        NSE = ...

    NSE: Market
    @overload
    def __init__(
        self,
        m: Union[India.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Indonesia(Calendar):
    class Market(IntEnum):
        BEJ = ...
        JSX = ...

    BEJ: Market
    JSX: Market
    @overload
    def __init__(
        self,
        m: Union[Indonesia.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Israel(Calendar):
    class Market(IntEnum):
        Settlement = ...
        TASE = ...
        SHIR = ...

    Settlement: Market
    TASE: Market
    SHIR: Market
    @overload
    def __init__(
        self,
        m: Union[Israel.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Italy(Calendar):
    class Market(IntEnum):
        Settlement = ...
        Exchange = ...

    Settlement: Market
    Exchange: Market
    @overload
    def __init__(
        self,
        m: Union[Italy.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Japan(Calendar):
    def __init__(self) -> None: ...

class Mexico(Calendar):
    class Market(IntEnum):
        BMV = ...

    BMV: Market
    @overload
    def __init__(
        self,
        m: Union[Mexico.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class NewZealand(Calendar):
    class Market(IntEnum):
        Wellington = ...
        Auckland = ...

    Wellington: Market
    Auckland: Market
    @overload
    def __init__(
        self,
        m: Union[NewZealand.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Norway(Calendar):
    def __init__(self) -> None: ...

class Poland(Calendar):
    class Market(IntEnum):
        Settlement = ...
        WSE = ...

    Settlement: Market
    WSE: Market
    @overload
    def __init__(
        self,
        m: Union[Poland.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Romania(Calendar):
    class Market(IntEnum):
        Public = ...
        BVB = ...

    Public: Market
    BVB: Market
    @overload
    def __init__(
        self,
        m: Union[Romania.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Russia(Calendar):
    class Market(IntEnum):
        Settlement = ...
        MOEX = ...

    Settlement: Market
    MOEX: Market
    @overload
    def __init__(
        self,
        m: Union[Russia.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SaudiArabia(Calendar):
    class Market(IntEnum):
        Tadawul = ...

    Tadawul: Market
    @overload
    def __init__(
        self,
        m: Union[SaudiArabia.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Singapore(Calendar):
    class Market(IntEnum):
        SGX = ...

    SGX: Market
    @overload
    def __init__(
        self,
        m: Union[Singapore.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Slovakia(Calendar):
    class Market(IntEnum):
        BSSE = ...

    BSSE: Market
    @overload
    def __init__(
        self,
        m: Union[Slovakia.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class SouthAfrica(Calendar):
    def __init__(self) -> None: ...

class SouthKorea(Calendar):
    class Market(IntEnum):
        Settlement = ...
        KRX = ...

    Settlement: Market
    KRX: Market
    @overload
    def __init__(
        self,
        m: Union[SouthKorea.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Sweden(Calendar):
    def __init__(self) -> None: ...

class Switzerland(Calendar):
    def __init__(self) -> None: ...

class Taiwan(Calendar):
    class Market(IntEnum):
        TSEC = ...

    TSEC: Market
    @overload
    def __init__(
        self,
        m: Union[Taiwan.Market, int] = ...,
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
        USE = ...

    USE: Market
    @overload
    def __init__(
        self,
        m: Union[Ukraine.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class UnitedKingdom(Calendar):
    class Market(IntEnum):
        Settlement = ...
        Exchange = ...
        Metals = ...

    Settlement: Market
    Exchange: Market
    Metals: Market
    @overload
    def __init__(
        self,
        m: Union[UnitedKingdom.Market, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class UnitedStates(Calendar):
    class Market(IntEnum):
        Settlement = ...
        NYSE = ...
        GovernmentBond = ...
        NERC = ...
        LiborImpact = ...
        FederalReserve = ...
        SOFR = ...

    Settlement: Market
    NYSE: Market
    GovernmentBond: Market
    NERC: Market
    LiborImpact: Market
    FederalReserve: Market
    SOFR: Market
    def __init__(
        self,
        m: Union[UnitedStates.Market, int],
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
        rule: Union[JointCalendarRule, int] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Calendar,
        arg1: Calendar,
        arg2: Calendar,
        rule: Union[JointCalendarRule, int] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Calendar,
        arg1: Calendar,
        rule: Union[JointCalendarRule, int] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Union[CalendarVector, Sequence[Calendar]],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Union[CalendarVector, Sequence[Calendar]],
        arg1: Union[JointCalendarRule, int] = ...,
    ) -> None: ...

class BespokeCalendar(Calendar):
    def __init__(
        self,
        name: str,
    ) -> None: ...
    def addWeekend(
        self,
        arg0: Union[Weekday, int],
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
        startRef: Date = ...,
    ) -> float: ...
    @overload
    def yearFraction(
        self,
        d1: Date,
        d2: Date,
        startRef: Date = ...,
        endRef: Date = ...,
    ) -> float: ...
    def name(self) -> str: ...
    def empty(self) -> bool: ...
    def __str__(self) -> str: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __ne__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...

class Actual360(DayCounter):
    @overload
    def __init__(
        self,
        includeLastDay: bool = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Actual366(DayCounter):
    @overload
    def __init__(
        self,
        includeLastDay: bool = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Actual36525(DayCounter):
    @overload
    def __init__(
        self,
        includeLastDay: bool = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Actual364(DayCounter):
    def __init__(self) -> None: ...

class Actual365Fixed(DayCounter):
    class Convention(IntEnum):
        Standard = ...
        Canadian = ...
        NoLeap = ...

    Standard: Convention
    Canadian: Convention
    NoLeap: Convention
    @overload
    def __init__(
        self,
        c: Union[Actual365Fixed.Convention, int] = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Thirty360(DayCounter):
    class Convention(IntEnum):
        USA = ...
        BondBasis = ...
        European = ...
        EurobondBasis = ...
        Italian = ...
        German = ...
        ISMA = ...
        ISDA = ...
        NASD = ...

    USA: Convention
    BondBasis: Convention
    European: Convention
    EurobondBasis: Convention
    Italian: Convention
    German: Convention
    ISMA: Convention
    ISDA: Convention
    NASD: Convention
    @overload
    def __init__(
        self,
        c: Union[Thirty360.Convention, int],
    ) -> None: ...
    @overload
    def __init__(
        self,
        c: Union[Thirty360.Convention, int],
        terminationDate: Date = ...,
    ) -> None: ...

class Thirty365(DayCounter):
    def __init__(self) -> None: ...

class ActualActual(DayCounter):
    class Convention(IntEnum):
        ISMA = ...
        Bond = ...
        ISDA = ...
        Historical = ...
        Actual365 = ...
        AFB = ...
        Euro = ...

    ISMA: Convention
    Bond: Convention
    ISDA: Convention
    Historical: Convention
    Actual365: Convention
    AFB: Convention
    Euro: Convention
    @overload
    def __init__(
        self,
        c: Union[ActualActual.Convention, int],
    ) -> None: ...
    @overload
    def __init__(
        self,
        c: Union[ActualActual.Convention, int],
        schedule: Schedule = ...,
    ) -> None: ...

class OneDayCounter(DayCounter):
    def __init__(self) -> None: ...

class SimpleDayCounter(DayCounter):
    def __init__(self) -> None: ...

class Business252(DayCounter):
    @overload
    def __init__(
        self,
        c: Calendar = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

class Observable:
    def __init__(self) -> None: ...

class Observer:
    def __init__(
        self,
        callback: PyObject,
    ) -> None: ...
    def registerWith(
        self,
        arg0: ObservableOrHandle,
    ) -> None: ...
    def unregisterWith(
        self,
        arg0: ObservableOrHandle,
    ) -> None: ...

class Array:
    @overload
    def __init__(
        self,
        arg0: Union[Array, Sequence[float]],
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
        fill: float = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __ne__(
        self,
        other: object,
    ) -> bool: ...
    def __neg__(self) -> Array: ...
    @overload
    def __add__(
        self,
        a: Union[Array, Sequence[float]],
    ) -> Array: ...
    @overload
    def __add__(
        self,
        a: float,
    ) -> Array: ...
    @overload
    def __sub__(
        self,
        a: Union[Array, Sequence[float]],
    ) -> Array: ...
    @overload
    def __sub__(
        self,
        a: float,
    ) -> Array: ...
    @overload
    def __mul__(
        self,
        a: Union[Array, Sequence[float]],
    ) -> Array: ...
    @overload
    def __mul__(
        self,
        a: Union[Matrix, Sequence[Sequence[float]]],
    ) -> Array: ...
    @overload
    def __mul__(
        self,
        a: float,
    ) -> Array: ...
    @overload
    def __truediv__(
        self,
        a: Union[Array, Sequence[float]],
    ) -> Array: ...
    @overload
    def __truediv__(
        self,
        a: float,
    ) -> Array: ...
    def __rmul__(
        self,
        a: float,
    ) -> Array: ...
    def __matmul__(
        self,
        a: Union[Array, Sequence[float]],
    ) -> float: ...
    def __getslice__(
        self,
        i: int,
        j: int,
    ) -> Array: ...
    def __setslice__(
        self,
        i: int,
        j: int,
        rhs: Union[Array, Sequence[float]],
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __getitem__(
        self,
        i: int,
    ) -> float: ...
    def __setitem__(
        self,
        i: int,
        x: float,
    ) -> None: ...
    def __iter__(self) -> Iterator[float]: ...

class MatrixRow:
    def __init__(self) -> None: ...
    def __getitem__(
        self,
        i: int,
    ) -> float: ...
    def __setitem__(
        self,
        i: int,
        x: float,
    ) -> None: ...
    def __iter__(self) -> Iterator[float]: ...

class Matrix:
    @overload
    def __init__(
        self,
        arg0: Union[Matrix, Sequence[Sequence[float]]],
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
        fill: float = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def rows(self) -> int: ...
    def columns(self) -> int: ...
    def __str__(self) -> str: ...
    def __add__(
        self,
        m: Union[Matrix, Sequence[Sequence[float]]],
    ) -> Matrix: ...
    def __sub__(
        self,
        m: Union[Matrix, Sequence[Sequence[float]]],
    ) -> Matrix: ...
    @overload
    def __mul__(
        self,
        x: Union[Array, Sequence[float]],
    ) -> Array: ...
    @overload
    def __mul__(
        self,
        x: Union[Matrix, Sequence[Sequence[float]]],
    ) -> Matrix: ...
    @overload
    def __mul__(
        self,
        x: float,
    ) -> Matrix: ...
    def __div__(
        self,
        x: float,
    ) -> Matrix: ...
    def __getitem__(
        self,
        i: int,
    ) -> MatrixRow: ...
    @overload
    def __rmul__(
        self,
        x: Union[Array, Sequence[float]],
    ) -> Array: ...
    @overload
    def __rmul__(
        self,
        x: Union[Matrix, Sequence[Sequence[float]]],
    ) -> Matrix: ...
    @overload
    def __rmul__(
        self,
        x: float,
    ) -> Matrix: ...
    def __iter__(self) -> Iterator[MatrixRow]: ...

class SalvagingAlgorithm:
    class Type(IntEnum):
        NoAlgorithm = ...
        Spectral = ...
        Hypersphere = ...
        LowerDiagonal = ...
        Higham = ...
        Principal = ...

    NoAlgorithm: Type
    Spectral: Type
    Hypersphere: Type
    LowerDiagonal: Type
    Higham: Type
    Principal: Type
    def __init__(self) -> None: ...

class SVD:
    def __init__(
        self,
        arg0: Union[Matrix, Sequence[Sequence[float]]],
    ) -> None: ...
    def U(self) -> Matrix: ...
    def V(self) -> Matrix: ...
    def S(self) -> Matrix: ...
    def singularValues(self) -> Array: ...

class SymmetricSchurDecomposition:
    def __init__(
        self,
        s: Union[Matrix, Sequence[Sequence[float]]],
    ) -> None: ...
    def eigenvalues(self) -> Array: ...
    def eigenvectors(self) -> Matrix: ...

class MatrixMultiplicationProxy:
    def __init__(
        self,
        matrixMult: PyObject,
    ) -> None: ...
    def __call__(
        self,
        x: Union[Array, Sequence[float]],
    ) -> Array: ...

class BiCGstab:
    @overload
    def __init__(
        self,
        proxy: MatrixMultiplicationProxy,
        maxIter: int,
        relTol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        proxy: MatrixMultiplicationProxy,
        maxIter: int,
        relTol: float,
        preconditioner: MatrixMultiplicationProxy,
    ) -> None: ...
    @overload
    def solve(
        self,
        b: Union[Array, Sequence[float]],
    ) -> Array: ...
    @overload
    def solve(
        self,
        b: Union[Array, Sequence[float]],
        x0: Union[Array, Sequence[float]] = ...,
    ) -> Array: ...

class GMRES:
    @overload
    def __init__(
        self,
        proxy: MatrixMultiplicationProxy,
        maxIter: int,
        relTol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        proxy: MatrixMultiplicationProxy,
        maxIter: int,
        relTol: float,
        preconditioner: MatrixMultiplicationProxy,
    ) -> None: ...
    @overload
    def solve(
        self,
        b: Union[Array, Sequence[float]],
    ) -> Array: ...
    @overload
    def solve(
        self,
        b: Union[Array, Sequence[float]],
        x0: Union[Array, Sequence[float]] = ...,
    ) -> Array: ...
    @overload
    def solveWithRestart(
        self,
        restart: int,
        b: Union[Array, Sequence[float]],
    ) -> Array: ...
    @overload
    def solveWithRestart(
        self,
        restart: int,
        b: Union[Array, Sequence[float]],
        x0: Union[Array, Sequence[float]] = ...,
    ) -> Array: ...

class RungeKutta:
    @overload
    def __init__(
        self,
        eps: float = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        eps: float = ...,
        h1: float = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        eps: float = ...,
        h1: float = ...,
        hmin: float = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __call__(
        self,
        fct: PyObject,
        y1: Union[DoubleVector, Sequence[float]],
        x1: float,
        x2: float,
    ) -> DoubleVector: ...
    @overload
    def __call__(
        self,
        fct: PyObject,
        y1: float,
        x1: float,
        x2: float,
    ) -> float: ...

class DefaultBoundaryCondition:
    class Side(IntEnum):
        NoSide = ...
        Upper = ...
        Lower = ...

    NoSide: Side
    Upper: Side
    Lower: Side
    def __init__(self) -> None: ...

class NeumannBC(DefaultBoundaryCondition):
    def __init__(
        self,
        value: float,
        side: Union[DefaultBoundaryCondition.Side, int],
    ) -> None: ...

class DirichletBC(DefaultBoundaryCondition):
    def __init__(
        self,
        value: float,
        side: Union[DefaultBoundaryCondition.Side, int],
    ) -> None: ...

class TridiagonalOperator:
    def __init__(
        self,
        low: Union[Array, Sequence[float]],
        mid: Union[Array, Sequence[float]],
        high: Union[Array, Sequence[float]],
    ) -> None: ...
    def solveFor(
        self,
        rhs: Union[Array, Sequence[float]],
    ) -> Array: ...
    def applyTo(
        self,
        v: Union[Array, Sequence[float]],
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
    @staticmethod
    def identity(size: int) -> TridiagonalOperator: ...
    def __add__(
        self,
        O: TridiagonalOperator,
    ) -> TridiagonalOperator: ...
    def __sub__(
        self,
        O: TridiagonalOperator,
    ) -> TridiagonalOperator: ...
    def __mul__(
        self,
        a: float,
    ) -> TridiagonalOperator: ...
    def __div__(
        self,
        a: float,
    ) -> TridiagonalOperator: ...
    def __iadd__(
        self,
        O: TridiagonalOperator,
    ) -> TridiagonalOperator: ...
    def __isub__(
        self,
        O: TridiagonalOperator,
    ) -> TridiagonalOperator: ...
    def __imul__(
        self,
        a: float,
    ) -> TridiagonalOperator: ...
    def __rmul__(
        self,
        a: float,
    ) -> TridiagonalOperator: ...
    def __idiv__(
        self,
        a: float,
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

class IntVector(list[int]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[int] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: int) -> None: ...
    def push_back(self, x: int) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class UnsignedIntVector(list[int]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[int] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: int) -> None: ...
    def push_back(self, x: int) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class DoubleVector(list[float]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[float] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: float) -> None: ...
    def push_back(self, x: float) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class StrVector(list[str]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[str] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: str) -> None: ...
    def push_back(self, x: str) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class BoolVector(list[bool]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[bool] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: bool) -> None: ...
    def push_back(self, x: bool) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class DoubleVectorVector(list[list[float]]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[list[float]] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: list[float]) -> None: ...
    def push_back(self, x: list[float]) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class DoublePair(tuple[float, float]):
    @overload
    def __init__(
        self,
        first: float,
        second: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    first: float
    second: float

class DoublePairVector(list[tuple[float, float]]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[tuple[float, float]] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: tuple[float, float]) -> None: ...
    def push_back(self, x: tuple[float, float]) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class PairDoubleVector(tuple[list[float], list[float]]):
    @overload
    def __init__(
        self,
        first: Union[DoubleVector, Sequence[float]],
        second: Union[DoubleVector, Sequence[float]],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    first: DoubleVector
    second: DoubleVector

class UnsignedIntPair(tuple[int, int]):
    @overload
    def __init__(
        self,
        first: int,
        second: int,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    first: int
    second: int

class UnsignedIntPairVector(list[tuple[int, int]]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[tuple[int, int]] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: tuple[int, int]) -> None: ...
    def push_back(self, x: tuple[int, int]) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class NodePair(tuple[Date, float]):
    @overload
    def __init__(
        self,
        first: Date,
        second: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    first: Date
    second: float

class NodeVector(list[tuple[Date, float]]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[tuple[Date, float]] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: tuple[Date, float]) -> None: ...
    def push_back(self, x: tuple[Date, float]) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class SegmentIntegral:
    def __init__(
        self,
        intervals: int,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...
    def __call__(
        self,
        pyFunction: PyObject,
        a: float,
        b: float,
    ) -> float: ...

class TrapezoidIntegralDefault:
    def __init__(
        self,
        accuracy: float,
        maxIterations: int,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...
    def __call__(
        self,
        pyFunction: PyObject,
        a: float,
        b: float,
    ) -> float: ...

class TrapezoidIntegralMidPoint:
    def __init__(
        self,
        accuracy: float,
        maxIterations: int,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...
    def __call__(
        self,
        pyFunction: PyObject,
        a: float,
        b: float,
    ) -> float: ...

class SimpsonIntegral:
    def __init__(
        self,
        accuracy: float,
        maxIterations: int,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...
    def __call__(
        self,
        pyFunction: PyObject,
        a: float,
        b: float,
    ) -> float: ...

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
        maxFunctionEvaluations: int = ...,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...
    def __call__(
        self,
        pyFunction: PyObject,
        a: float,
        b: float,
    ) -> float: ...

class GaussKronrodNonAdaptive:
    def __init__(
        self,
        absoluteAccuracy: float,
        maxEvaluations: int,
        relativeAccuracy: float,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...
    def __call__(
        self,
        pyFunction: PyObject,
        a: float,
        b: float,
    ) -> float: ...

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
        relAccuracy: float = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        maxIterations: int,
        absAccuracy: float,
        relAccuracy: float = ...,
        useConvergenceEstimate: bool = ...,
    ) -> None: ...
    def numberOfEvaluations(self) -> int: ...
    def __call__(
        self,
        pyFunction: PyObject,
        a: float,
        b: float,
    ) -> float: ...

class GaussianQuadrature:
    def __init__(self) -> None: ...
    def order(self) -> int: ...
    def weights(self) -> Array: ...
    def x(self) -> Array: ...
    def __call__(
        self,
        pyFunction: PyObject,
    ) -> float: ...

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
        s: float = ...,
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
        mu: float = ...,
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
        relTolerance: float = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        relTolerance: float = ...,
        maxRefinements: int = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        relTolerance: float = ...,
        maxRefinements: int = ...,
        minComplement: float = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def numberOfEvaluations(self) -> int: ...
    def __call__(
        self,
        pyFunction: PyObject,
        a: float,
        b: float,
    ) -> float: ...

class ExpSinhIntegral:
    @overload
    def __init__(
        self,
        relTolerance: float = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        relTolerance: float = ...,
        maxRefinements: int = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def integrate(
        self,
        pyFunction: PyObject,
    ) -> float: ...
    def numberOfEvaluations(self) -> int: ...
    def __call__(
        self,
        pyFunction: PyObject,
        a: float,
        b: float,
    ) -> float: ...

class InterestRate:
    @overload
    def __init__(
        self,
        r: float,
        dc: DayCounter,
        comp: Union[Compounding, int],
        freq: Union[Frequency, int],
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
        refStart: Date = ...,
    ) -> float: ...
    @overload
    def discountFactor(
        self,
        d1: Date,
        d2: Date,
        refStart: Date = ...,
        refEnd: Date = ...,
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
        refStart: Date = ...,
    ) -> float: ...
    @overload
    def compoundFactor(
        self,
        d1: Date,
        d2: Date,
        refStart: Date = ...,
        refEnd: Date = ...,
    ) -> float: ...
    @overload
    def compoundFactor(
        self,
        t: float,
    ) -> float: ...
    @overload
    @staticmethod
    def impliedRate(
        compound: float,
        resultDC: DayCounter,
        comp: Union[Compounding, int],
        freq: Union[Frequency, int],
        d1: Date,
        d2: Date,
    ) -> InterestRate: ...
    @overload
    @staticmethod
    def impliedRate(
        compound: float,
        resultDC: DayCounter,
        comp: Union[Compounding, int],
        freq: Union[Frequency, int],
        d1: Date,
        d2: Date,
        refStart: Date = ...,
    ) -> InterestRate: ...
    @overload
    @staticmethod
    def impliedRate(
        compound: float,
        resultDC: DayCounter,
        comp: Union[Compounding, int],
        freq: Union[Frequency, int],
        d1: Date,
        d2: Date,
        refStart: Date = ...,
        refEnd: Date = ...,
    ) -> InterestRate: ...
    @overload
    @staticmethod
    def impliedRate(
        compound: float,
        resultDC: DayCounter,
        comp: Union[Compounding, int],
        freq: Union[Frequency, int],
        t: float,
    ) -> InterestRate: ...
    @overload
    def equivalentRate(
        self,
        comp: Union[Compounding, int],
        freq: Union[Frequency, int],
        t: float,
    ) -> InterestRate: ...
    @overload
    def equivalentRate(
        self,
        resultDayCounter: DayCounter,
        comp: Union[Compounding, int],
        freq: Union[Frequency, int],
        d1: Date,
        d2: Date,
    ) -> InterestRate: ...
    @overload
    def equivalentRate(
        self,
        resultDayCounter: DayCounter,
        comp: Union[Compounding, int],
        freq: Union[Frequency, int],
        d1: Date,
        d2: Date,
        refStart: Date = ...,
    ) -> InterestRate: ...
    @overload
    def equivalentRate(
        self,
        resultDayCounter: DayCounter,
        comp: Union[Compounding, int],
        freq: Union[Frequency, int],
        d1: Date,
        d2: Date,
        refStart: Date = ...,
        refEnd: Date = ...,
    ) -> InterestRate: ...
    def __str__(self) -> str: ...

class InterestRateVector(list[InterestRate]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[InterestRate] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: InterestRate) -> None: ...
    def push_back(self, x: InterestRate) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class LazyObject(Observable):
    def __init__(self) -> None: ...
    def recalculate(self) -> None: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...
    @staticmethod
    def forwardFirstNotificationOnly() -> None: ...
    @staticmethod
    def alwaysForwardNotifications() -> None: ...
    @staticmethod
    def forwardsAllNotifications() -> bool: ...

class DateGeneration:
    class Rule(IntEnum):
        Backward = ...
        Forward = ...
        Zero = ...
        ThirdWednesday = ...
        ThirdWednesdayInclusive = ...
        Twentieth = ...
        TwentiethIMM = ...
        OldCDS = ...
        CDS = ...
        CDS2015 = ...

    Backward: Rule
    Forward: Rule
    Zero: Rule
    ThirdWednesday: Rule
    ThirdWednesdayInclusive: Rule
    Twentieth: Rule
    TwentiethIMM: Rule
    OldCDS: Rule
    CDS: Rule
    CDS2015: Rule
    def __init__(self) -> None: ...

class Schedule:
    @overload
    def __init__(
        self,
        arg0: Union[DateVector, Sequence[Date]],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Union[DateVector, Sequence[Date]],
        calendar: Calendar = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Union[DateVector, Sequence[Date]],
        calendar: Calendar = ...,
        convention: Union[BusinessDayConvention, int] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Union[DateVector, Sequence[Date]],
        calendar: Calendar = ...,
        convention: Union[BusinessDayConvention, int] = ...,
        terminationDateConvention: Optional[BusinessDayConvention] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Union[DateVector, Sequence[Date]],
        calendar: Calendar = ...,
        convention: Union[BusinessDayConvention, int] = ...,
        terminationDateConvention: Optional[BusinessDayConvention] = ...,
        tenor: Optional[Period] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Union[DateVector, Sequence[Date]],
        calendar: Calendar = ...,
        convention: Union[BusinessDayConvention, int] = ...,
        terminationDateConvention: Optional[BusinessDayConvention] = ...,
        tenor: Optional[Period] = ...,
        rule: Optional[DateGeneration.Rule] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Union[DateVector, Sequence[Date]],
        calendar: Calendar = ...,
        convention: Union[BusinessDayConvention, int] = ...,
        terminationDateConvention: Optional[BusinessDayConvention] = ...,
        tenor: Optional[Period] = ...,
        rule: Optional[DateGeneration.Rule] = ...,
        endOfMonth: Optional[bool] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: Union[DateVector, Sequence[Date]],
        calendar: Calendar = ...,
        convention: Union[BusinessDayConvention, int] = ...,
        terminationDateConvention: Optional[BusinessDayConvention] = ...,
        tenor: Optional[Period] = ...,
        rule: Optional[DateGeneration.Rule] = ...,
        endOfMonth: Optional[bool] = ...,
        isRegular: Union[BoolVector, Sequence[bool]] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        effectiveDate: Date,
        terminationDate: Date,
        tenor: Period,
        calendar: Calendar,
        convention: Union[BusinessDayConvention, int],
        terminationDateConvention: Union[BusinessDayConvention, int],
        rule: Union[DateGeneration.Rule, int],
        endOfMonth: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        effectiveDate: Date,
        terminationDate: Date,
        tenor: Period,
        calendar: Calendar,
        convention: Union[BusinessDayConvention, int],
        terminationDateConvention: Union[BusinessDayConvention, int],
        rule: Union[DateGeneration.Rule, int],
        endOfMonth: bool,
        firstDate: Date = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        effectiveDate: Date,
        terminationDate: Date,
        tenor: Period,
        calendar: Calendar,
        convention: Union[BusinessDayConvention, int],
        terminationDateConvention: Union[BusinessDayConvention, int],
        rule: Union[DateGeneration.Rule, int],
        endOfMonth: bool,
        firstDate: Date = ...,
        nextToLastDate: Date = ...,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def previousDate(
        self,
        refDate: Date,
    ) -> Date: ...
    def nextDate(
        self,
        refDate: Date,
    ) -> Date: ...
    def dates(self) -> DateVector: ...
    def hasIsRegular(self) -> bool: ...
    @overload
    def isRegular(
        self,
        i: int,
    ) -> bool: ...
    @overload
    def isRegular(self) -> BoolVector: ...
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
    def __getitem__(
        self,
        i: int,
    ) -> Date: ...
    def __iter__(self) -> Iterator[Date]: ...

class _MakeSchedule:
    def __init__(self) -> None: ...
    def fromDate(
        self,
        effectiveDate: Date,
    ) -> _MakeSchedule: ...
    def to(
        self,
        terminationDate: Date,
    ) -> _MakeSchedule: ...
    def withTenor(
        self,
        arg0: Period,
    ) -> _MakeSchedule: ...
    def withFrequency(
        self,
        arg0: Union[Frequency, int],
    ) -> _MakeSchedule: ...
    def withCalendar(
        self,
        arg0: Calendar,
    ) -> _MakeSchedule: ...
    def withConvention(
        self,
        arg0: Union[BusinessDayConvention, int],
    ) -> _MakeSchedule: ...
    def withTerminationDateConvention(
        self,
        arg0: Union[BusinessDayConvention, int],
    ) -> _MakeSchedule: ...
    def withRule(
        self,
        arg0: Union[DateGeneration.Rule, int],
    ) -> _MakeSchedule: ...
    def forwards(self) -> _MakeSchedule: ...
    def backwards(self) -> _MakeSchedule: ...
    @overload
    def endOfMonth(
        self,
        flag: bool = ...,
    ) -> _MakeSchedule: ...
    @overload
    def endOfMonth(self) -> _MakeSchedule: ...
    def withFirstDate(
        self,
        d: Date,
    ) -> _MakeSchedule: ...
    def withNextToLastDate(
        self,
        d: Date,
    ) -> _MakeSchedule: ...
    def schedule(self) -> Schedule: ...

class RealTimeSeries(TimeSeries[float]):
    @overload
    def __init__(
        self,
        d: Union[DateVector, Sequence[Date]],
        v: Union[DoubleVector, Sequence[float]],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def dates(self) -> DateVector: ...
    def values(self) -> DoubleVector: ...
    def firstDate(self) -> Date: ...
    def lastDate(self) -> Date: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __getitem__(
        self,
        d: Date,
    ) -> float: ...
    def __setitem__(
        self,
        d: Date,
        value: float,
    ) -> None: ...
    def __iter__(self) -> Iterator[float]: ...

class IntervalPriceTimeSeries(TimeSeries[IntervalPrice]):
    @overload
    def __init__(
        self,
        d: Union[DateVector, Sequence[Date]],
        v: Union[IntervalPriceVector, Sequence[IntervalPrice]],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def dates(self) -> DateVector: ...
    def values(self) -> IntervalPriceVector: ...
    def firstDate(self) -> Date: ...
    def lastDate(self) -> Date: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __getitem__(
        self,
        d: Date,
    ) -> IntervalPrice: ...
    def __setitem__(
        self,
        d: Date,
        value: IntervalPrice,
    ) -> None: ...
    def __iter__(self) -> Iterator[IntervalPrice]: ...

class IntervalPriceVector(list[IntervalPrice]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[IntervalPrice] = ...) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, value: IntervalPrice) -> None: ...
    def push_back(self, x: IntervalPrice) -> None: ...
    def resize(self, n: int) -> None: ...
    def size(self) -> int: ...
    def empty(self) -> bool: ...
    def clear(self) -> None: ...

class IntervalPrice:
    class Type(IntEnum):
        Open = ...
        Close = ...
        High = ...
        Low = ...

    Open: Type
    Close: Type
    High: Type
    Low: Type
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
        arg1: Union[IntervalPrice.Type, int],
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
        t: Union[IntervalPrice.Type, int],
    ) -> float: ...
    def open(self) -> float: ...
    def close(self) -> float: ...
    def high(self) -> float: ...
    def low(self) -> float: ...
    @staticmethod
    def makeSeries(
        d: Union[DateVector, Sequence[Date]],
        open: Sequence[float],
        close: Sequence[float],
        high: Sequence[float],
        low: Sequence[float],
    ) -> IntervalPriceTimeSeries: ...
    @staticmethod
    def extractValues(
        arg0: Union[IntervalPriceTimeSeries, TimeSeries[IntervalPrice]],
        t: Union[IntervalPrice.Type, int],
    ) -> list[float]: ...
    @staticmethod
    def extractComponent(
        arg0: Union[IntervalPriceTimeSeries, TimeSeries[IntervalPrice]],
        t: Union[IntervalPrice.Type, int],
    ) -> RealTimeSeries: ...

def MakeSchedule(effectiveDate = ..., terminationDate = ..., tenor = ..., frequency = ..., calendar = ..., convention = ..., terminalDateConvention = ..., rule = ..., forwards = ..., backwards = ..., endOfMonth = ..., firstDate = ..., nextToLastDate = ...) -> Any: ...
