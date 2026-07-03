%module QuantLib
%include stl.i

%{
QL_DEPRECATED_DISABLE_WARNING
%}

%include calendars.i
%include common.i
%include date.i
%include daycounters.i
%include null.i
%include observer.i
%include ode.i
%include operators.i
%include tuple.i
%include types.i
%include vectors.i
%include integrals.i
%include interestrate.i
// %include interpolation.i  // depends on optimizers.i
%include lazyobject.i
%include linearalgebra.i
%include scheduler.i
%include functions.i
// %include currencies.i    // depends on rounding.i
%include timeseries.i
// %include marketelements.i // depends on indexes.i
