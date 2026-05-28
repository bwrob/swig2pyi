%module operators

%rename("operator[]") Synthetic::OpClass::operator[];

namespace Synthetic {

class OpClass {
public:
    OpClass();
    
    bool operator==(const OpClass& other) const;
    bool operator!=(const OpClass& other) const;
    bool operator<(const OpClass& other) const;
    bool operator<=(const OpClass& other) const;
    bool operator>(const OpClass& other) const;
    bool operator>=(const OpClass& other) const;
    
    double operator()(double x, int y);
    
    double operator[](int index) const;
    
    OpClass operator+(const OpClass& other) const;
    OpClass operator-(const OpClass& other) const;
    OpClass operator*(const OpClass& other) const;
    OpClass operator/(const OpClass& other) const;
    
    OpClass* operator->() const;
};

}
