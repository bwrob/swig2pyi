%module vector_typedefs

%{
#include <vector>
%}

namespace std {
    template <typename T> class vector {
    public:
        typedef size_t size_type;
        typedef T value_type;
        vector();
        vector(size_type n);
        vector(size_type n, const T& value);
        void push_back(const T& x);
    };
}

%template(DoubleVector) std::vector<double>;
%template(DoubleVectorVector) std::vector<std::vector<double>>;

namespace Synthetic {

typedef std::vector<double> RealVector;
typedef std::vector<std::vector<double>> Matrix;

class Maths {
public:
    Maths();
    double sum(const std::vector<double>& v);
    double sum_relaxed(const RealVector& v);
    double sum_matrix(const Matrix& m);
    
    RealVector get_vector() const;
};

}
