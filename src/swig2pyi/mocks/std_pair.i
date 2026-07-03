namespace std {
  template<class T1, class T2> struct pair {
    T1 first;
    T2 second;
    pair() {}
    pair(T1 first, T2 second) : first(first), second(second) {}
  };
}
