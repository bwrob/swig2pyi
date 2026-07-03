%module handle_overloads

%{
#include <string>
%}

namespace Synthetic {

class Underlying {
public:
    void foo(int x);
    void foo(const std::string& s);
};

template <typename T>
class Handle {
public:
    Handle(T* ptr);
    T* operator->();
};

}

%template(UnderlyingHandle) Synthetic::Handle<Synthetic::Underlying>;
