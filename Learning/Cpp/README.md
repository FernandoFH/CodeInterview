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

### Polimofismo

- Tiempo de Ejecución
  - Interfaces
  - Composition
  - Herecia
  - Virtual Functions

- Tiempo de Compilación
  - Templates

### Interfaces

- Abstract class: A class that contains at least one pure virtual function.
- Pure virtual function: A virtual function that is declared by assigning 0 in its declaration.

### Funciones Virtuales puras y Clases Abstractas

- Palabra reservada virtual
- Destructor virtual
- Sufijo = 0
- Herencia de la Clase Base
- Palabra reservada override

### Polimorfismo

- Tiempo de Compilación
  - Templates

- Tiempo de Ejecución
  - Interfaces

### Sobrecargar el Operador New

```Cpp
void* operator new(size_t size) {
    // Custom memory allocation logic
    void* ptr = malloc(size);
    if (!ptr) {
        throw std::bad_alloc();
    }
    return ptr;
}

```

### STL (Standard Template Library)

- Contenedores
- Iteradores
- Algoritmos

### Curso CPP AVANZADO

[Playlist](https://www.youtube.com/playlist?list=PL8cp2fMJ9qLb9ITfBdsEHpqcN_mjo6CYg)

---

## Complete Modern C++ (C++11/14/17) Specialization

#### [Specializations Coursera](https://www.coursera.org/programs/plan-bronce-2026-36k-75k11/specializations/packt-complete-modern-c-c-11-14-17?source=search) | Packt - Course Instructors

1. [Foundations of Modern C++](#foundations-of-modern-c)
2. [Advanced Object-Oriented & Generic Programming in C++](#advanced-object-oriented--generic-programming-in-c)
3. [Modern C++ Features & Concurrency](#modern-c-features--concurrency)

### Foundations of Modern C++

### Advanced Object-Oriented & Generic Programming in C++

### Modern C++ Features & Concurrency

### LeetCode

- 001 / 121 / 217
- 206 / 021 / 019
- 20 / 155 / 150
- 933 / 232 / 279
- 215 / 023 / 347
- 049 / 560
- 098 / 104 / 102
- 217 / 128 / 202 !!!

### (PACKT) C++ High Performance, Second Edition: Master the art of optimizing the functioning of your C++

### (PACKT) Hands-On Design Patterns with C++: Solve common C++ problems with modern design patterns and build robust applications

### (PACKT) Debunking C++ Myths

### (PACKT) Bare-Metal Embedded C Programming: Develop high-performance embedded systems with C for Arm microcontrollers

---

| Content                                                                                                         | Status        |
| --------------------------------------------------------------------------------------------------------------- | ------------- |
| [Curso CPP Moderno](#c-moderno)                                                                                 | In Process 🟡 |
| [A Tour of C++](./RoadMapBook/00_ATourOfCpp.md)                                                                 | In Process 🟡 |
| [Complete Modern C++ (C++11/14/17) Specialization](#complete-modern-c-c111417-specialization)                   |               |
| 1. [Foundations of Modern C++](#foundations-of-modern-c)                                                        |               |
| 2. [Advanced Object-Oriented & Generic Programming in C++](#advanced-object-oriented--generic-programming-in-c) |               |
| 3. [Modern C++ Features & Concurrency](#modern-c-features--concurrency)                                         |               |
| [C++ AVANZADO](#c-moderno)                                                                                      |               |

Writing Secure Code in C++ Specialization

- https://www.coursera.org/organizations/centro-graduados/specializations/secure-code-c

| Book                                        | Status        |
| ------------------------------------------- | ------------- |
| [A Tour of C++]()                           | In Process 🟡 |
| [Effective Modern C++]()                    | In Process 🟡 |
| [Object-Oriented Software Design in C+++]() | In Process 🟡 |
| [C++ Software Design]()                     | In Process 🟡 |
| [C++ Network Programming - Volume 1]()      | In Process 🟡 |
| [C++ Network Programming - Volume 2]()      | In Process 🟡 |
| [C++ High Performance]()                    | In Process 🟡 |
| [Hands-On Design Patterns with C++]()       | In Process 🟡 |

### [Modern-CPP-Programming](https://federico-busato.github.io/Modern-CPP-Programming/)

### Data Structures and Algorithm Analysis

https://people.cs.vt.edu/~shaffer/Book/C++3e20120102.pdf

---

### Modernes Cpp

https://www.modernescpp.com/index.php/table-of-content/

---

### Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14

https://ia902804.us.archive.org/23/items/EffectiveModernC/Effective-Modern-C%2B%2B.pdf

Thinking in C++, Volume 1, 2nd Edition
https://micc.unifi.it/bertini/download/programmazione/TICPP-2nd-ed-Vol-one-printed.pdf

https://micc.unifi.it/bertini/download/programmazione/TICPP-2nd-ed-Vol-two-printed.pdf

Modern C++ Tutorial: C++11/14/17/20 On the Fly
https://changkun.de/modern-cpp/pdf/modern-cpp-tutorial-en-us.pdf

## C++ In-Depth Series

### Discovering Modern C++

### C++ Coding Standards: 101 Rules, Guidelines, and Best Practices

### C++ Template Metaprogramming: Concepts, Tools, and Techniques from Boost and Beyond

---

### Exceptional C++ Style: 40 New Engineering Puzzles, Programming Problems, and Solutions

### Modern C++ Design: Generic Programming and Design Patterns Applied

### Accelerated C++: Practical Programming

### C++ Software Design: Design Principles and Patterns for High-Quality Software

### Exceptional C++: 47 Engineering Puzzles, Programming Problems

### Learning Modern C++ for Finance: Foundations for Quantitative Programming

### Data Structure And Algorithms In C++ - Adam Drozdek

### Efective STL - Scott Meyers

### Working Effectively with Legacy Code (Robert C. Martin Series)

### Your Code as a Crime Scene: Use Forensic Techniques to Arrest Defects, Bottlenecks, and Bad Design in Your Programs (The Pragmatic Programmers)

### Domain-Driven Design: Tackling Complexity in the Heart of Software

---

(PACKT)

C++ Memory Management: Write leaner and safer C++ code using proven memory-management techniques

The C++ Programmer's Mindset: Learn computational, algorithmic, and systems thinking to become a better C++ programmer

- Auto
- STL
- Package Manager
- Error Messages
- Backward Compatibility

---

Especialización en Lenguaje C y C++ (CODAERUS)
50 horas académicas · Instructor: Christian Quispe Canchari
Bloque 1 — Fundamentos C/C++

Clase 1: Implementación — Tipos de lenguajes, RAM, CPU/GPU/TPU, diagrama de bloques, GCC y G++, memoria estática vs dinámica
Clase 2: Tipos de datos — Enteros, flotantes, double, short; comparativa C vs C++; modificadores (short, long, signed)
Clase 3: Operadores — E/S en C/C++, aritméticos, lógicos, relacionales
Clase 4: Sentencias I — Diagramas de flujo, if, if-else, switch
Clase 5: Punteros I — Dirección en memoria, declaración/inicialización, indirección, null y void, punteros a punteros
Clase 6: Sentencias II — while, bucles cero iteraciones, centinelas, break, for, bucles infinitos
Clase 7: Funciones I — Tipos de retorno, prototipo, parámetros, paso por valor/referencia, parámetros const
Clase 8: Funciones II (offline)
Clase 9: Arrays — Declaración, subíndices, almacenamiento en memoria, tamaño, rango, inicialización, multidimensionales
Clase 10: Estructuras — Declaración, tamaño, acceso, anidadas, arrays de estructuras, uniones, enumeraciones
Clase 11: Master Class — Integración — Punteros + funciones + arrays + estructuras, typedef, structs como argumentos vía punteros
Clase 12: Memoria dinámica — Heap, malloc/realloc/free, new/delete, arrays dinámicos

Bloque 2 — Sistemas embebidos y estructuras de datos

Clase 13: Microcontroladores I — Intro, ESP32, C en ESP32, GPIO (encender LED)
Clase 14: Microcontroladores II — Salidas/entradas digitales, parpadeo LED, lectura de pulsadores
Clase 15: Cadenas (offline)
Clase 16: Archivos (offline) — Puntero FILE, apertura/cierre, NULL y EOF, binarios, argumentos de main()
Clase 17: Listas enlazadas — Nodos, cabecera/cola, construcción, doblemente enlazadas, circulares
Clase 18: Pilas y colas — Implementación con arrays y con listas enlazadas
Clase 19: Árboles — Binarios, BST, operaciones, algoritmos de exploración

Bloque 3 — POO y GUI con Qt

Clase 20: POO I — Paradigmas, objetos/clases/métodos/atributos, sobrecarga, constructor/destructor
Clase 21: POO II y Qt I — Herencia, modificadores de acceso, puntero this, intro a Qt, POO en GUI
Clase 22: POO III y Qt II — Botones, sliders, progressbar, señales y slots
Clase 23: POO IV — Herencia múltiple, templates, encapsulamiento, clases amigas
Clase 24: Comunicación serial — Recepción de datos analógicos, gráficos, envío desde Qt, comunicación bidireccional
Clase 25: POO V — Polimorfismo, funciones virtuales, sobreescritura, punteros polimórficos, clases abstractas

Embedded C ++ Interview Questions
https://www.youtube.com/watch?v=aSsKaKG43yE&list=PL3uLubnzL2Tn-EHL14y_SnmRPQjBs8hb0

Master Embedded C++ Interviews
https://www.youtube.com/playlist?list=PLs0W21hBB9a_f7YHjxTzC0zT0pneIBF1Q
