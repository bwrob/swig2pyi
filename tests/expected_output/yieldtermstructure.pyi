from typing import overload

class YieldTermStructure:
    @overload
    def discount(
        self,
        arg0: Date,
        extrapolate: bool = False,
    ) -> float: ...
    @overload
    def discount(
        self,
        arg0: float,
        extrapolate: bool = False,
    ) -> float: ...
    @overload
    def zeroRate(
        self,
        d: Date,
        arg1: DayCounter,
        arg2: Compounding,
        f: Frequency = ...,
        extrapolate: bool = False,
    ) -> float: ...
    @overload
    def zeroRate(
        self,
        t: float,
        arg1: Compounding,
        f: Frequency = ...,
        extrapolate: bool = False,
    ) -> float: ...
    @overload
    def forwardRate(
        self,
        d1: Date,
        d2: Date,
        arg2: DayCounter,
        arg3: Compounding,
        f: Frequency = ...,
        extrapolate: bool = False,
    ) -> float: ...
    @overload
    def forwardRate(
        self,
        t1: float,
        t2: float,
        arg2: Compounding,
        f: Frequency = ...,
        extrapolate: bool = False,
    ) -> float: ...
