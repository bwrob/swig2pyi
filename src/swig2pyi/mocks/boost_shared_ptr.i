namespace boost {
  template<class T> class shared_ptr {
  public:
    T* operator->();
  };
}

%define %shared_ptr(T...)
   // Macro to handle shared_ptr directive. 
   // In XML generation, we might want to ensure the type is visible as boost::shared_ptr<T>
   %template() boost::shared_ptr<T>;
%enddef
