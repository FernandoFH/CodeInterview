#include <cstdio>

struct Hucha {
 private:
  int moneda;

 public:
  Hucha() : moneda(20) {}  // Constructor que inicializa moneda a 200

  Hucha(int moneda_in) {  // Constructor que inicializa moneda a un valor
    if (!set_moneda(moneda_in)) {
      moneda = 200;
    } else {
      moneda = moneda_in;
    }
  }

  void add_moneda() { moneda++; }
  int get_moneda() { return moneda; }
  bool set_moneda(int nueva_moneda) {
    if (nueva_moneda < 200) return false;

    moneda = nueva_moneda;
    return true;
  }
};

int main() {
  Hucha miHucha;
  Hucha miHucha2(150);

  // miHucha.add_moneda();
  printf("Monedas en la hucha desde le constructor: %d\n",
         miHucha.get_moneda());
  printf("Monedas en la hucha desde le constructor 2: %d\n",
         miHucha2.get_moneda());
}