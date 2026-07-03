%module synthetic

%{
#include <string>
%}

namespace Synthetic {

enum Color {
    RED = 1,
    GREEN = 2,
    BLUE = 3
};

class BaseClass {
public:
    virtual ~BaseClass() {}
    virtual void doSomething(int x = 10, double y = 3.14) = 0;
};

class DerivedClass : public BaseClass {
public:
    enum Status {
        OK = 0,
        ERROR = 1
    };

    DerivedClass();
    void doSomething(int x = 10, double y = 3.14) override;

    int value() const;
    void setValue(int val);

    DerivedClass operator+(const DerivedClass& other);
};

template <typename T>
class SmartPtr {
public:
    SmartPtr(T* ptr);
    T* operator->();
};

}

%template(DerivedClassPtr) Synthetic::SmartPtr<Synthetic::DerivedClass>;
