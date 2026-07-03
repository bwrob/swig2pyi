%echo "Loaded mock std_vector.i"
namespace std {
    template<class T> class vector {
    public:
        typedef size_t size_type;
        typedef T value_type;
        // Add necessary methods for recognition if needed
    };
}
