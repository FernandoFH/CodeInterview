# C++ Moderno

[Curso CPP Moderno](https://www.youtube.com/playlist?list=PLEtcGQaT56ch7CfcboVPyN1Klnh7LwaRq)

- C++ Moderno / C++ 11.
- New version every 3 years.
- A simple and direct mapping to hardware.
- Zero-overhead adstraction mechanisms.

- C++ is object-oriented and strongly typed.
- All objects in C++ must have

### C++ Dataypes

- Built-in / Primitive
  - Integer
    - int
    - char
  - Floating
    - float
    - double
  - Void
- Derived
  - Array
  - Pointers
  - References
- User-Defined
  - Structures
  - Unions
  - Clases
  - Enumerations

```
struct Book {
    char title;
    char author;
    char subject;
}
```

POD Classes (Plain Old Data)

- Data containers, they do not have functions.
- Struct sets its members as public by default.

Encapsulation

- Data
- Functions

- Access Control
  - Public
  - Private
  - Protected

### Classes

- Data -> Variables
- Actions -> Methods
- Permissions -> Access controls

Constructors and Destructors

- Special methods declared without a return type and with the same name as the class.
- Object initialization
- Enforces class invariants.
- The destructor is executed automatically and is invoked with the ~

### Pointers

- Low-level objects
- Type of data stored
- Assigned memory address
- Unary address operator &
- Unary dereference operator \*
- Arrow operator ->
  - Dereferences the pointer, like the \* operator
  - Accesses the member of the pointed object that we specify.

### References

- A reference is declared using the &
- We cannot create NULL references.
- Once a reference is initialized, it cannot be changed to refer to another object.
- A reference must be initialized when it

### Object Lifecycle

Object lifetime

-> Type
-> Value

- Assignment
- Constructor
- Object Lifetime
- Usage
- Finalization
- Destructor
- Deallocation

  -> Type
  -> Value

### Runtime Polymorphism. Interfaces.

Address Space Layout Randomization

/009/017/

### [Complete Modern C++ (C++11/14/17) Specialization](https://www.coursera.org/specializations/packt-complete-modern-c-c-11-14-17)

### (PACKT) C++ High Performance, Second Edition: Master the art of optimizing the functioning of your C++

### (PACKT) Hands-On Design Patterns with C++: Solve common C++ problems with modern design patterns and build robust applications

---

| Content                                         | Status        |
| ----------------------------------------------- | ------------- |
| [Curso CPP Moderno](#c-moderno)                 | In Process 🟡 |
| [A Tour of C++](./RoadMapBook/00_ATourOfCpp.md) | In Process 🟡 |

### Data Structures and Algorithm Analysis

https://people.cs.vt.edu/~shaffer/Book/C++3e20120102.pdf

### Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14

https://ia902804.us.archive.org/23/items/EffectiveModernC/Effective-Modern-C%2B%2B.pdf

Thinking in C++, Volume 1, 2nd Edition
https://micc.unifi.it/bertini/download/programmazione/TICPP-2nd-ed-Vol-one-printed.pdf

https://micc.unifi.it/bertini/download/programmazione/TICPP-2nd-ed-Vol-two-printed.pdf

Modern C++ Tutorial: C++11/14/17/20 On the Fly
https://changkun.de/modern-cpp/pdf/modern-cpp-tutorial-en-us.pdf

## - C++ In-Depth Series

### Discovering Modern C++

### C++ Coding Standards: 101 Rules, Guidelines, and Best Practices

### C++ Template Metaprogramming: Concepts, Tools, and Techniques from Boost and Beyond

---

### [Modern-CPP-Programming](https://federico-busato.github.io/Modern-CPP-Programming/)

### Exceptional C++ Style: 40 New Engineering Puzzles, Programming Problems, and Solutions

### Modern C++ Design: Generic Programming and Design Patterns Applied

### Accelerated C++: Practical Programming

### C++ Software Design: Design Principles and Patterns for High-Quality Software

### Exceptional C++: 47 Engineering Puzzles, Programming Problems

### Learning Modern C++ for Finance: Foundations for Quantitative Programming

### Data Structure And Algorithms In C++ - Adam Drozdek

### Efective STL - Scott Meyers

---

(PACKT)

C++ Memory Management: Write leaner and safer C++ code using proven memory-management techniques

The C++ Programmer's Mindset: Learn computational, algorithmic, and systems thinking to become a better C++ programmer

- auto
- STL
- Package Manager
- Error Messages
- Backward Compatibility
