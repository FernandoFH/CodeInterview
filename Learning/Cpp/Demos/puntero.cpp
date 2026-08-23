#include <cstdio>

int main() {
  int puntos{};
  int* puntos_direcc{&puntos};
  // int* puntos_direcc2 = &puntos;

  printf("puntos: %d\n", puntos);
  printf("puntos_direcc: %p\n", puntos_direcc);

  *puntos_direcc = 2332;
  printf("puntos: %d\n", puntos);
  printf("puntos: %d\n", *puntos_direcc);
  printf("puntos_direcc: %p\n", puntos_direcc);
}
