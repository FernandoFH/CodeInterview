#include <cstdio>

struct Element {
  Element* next{};  // Pointer to the next element
  void insert_afetr(Element* new_element) {
    new_element->next = next;  // Set the next pointer of the new element
    next = new_element;        // Update the current element's next pointer
  }
  char prefix[2];
  short operating_number;
};

int main() {
  Element trooper1, trooper2, trooper3;
  trooper1.prefix[0] = 'T';
  trooper1.prefix[1] = 'K';
  trooper1.operating_number = 421;
  // trooper1.next = &trooper2;  // Link to the next element
  trooper1.insert_afetr(&trooper2);  // Insert trooper2 after trooper1

  trooper2.prefix[0] = 'F';
  trooper2.prefix[1] = 'N';
  trooper2.operating_number = 2187;
  trooper2.insert_afetr(&trooper3);

  trooper3.prefix[0] = 'L';
  trooper3.prefix[1] = 'S';
  trooper3.operating_number = 005;

  for (Element* current = &trooper1; current != nullptr;
       current = current->next) {
    printf("Stormtrooper %c%c%d\n", current->prefix[0], current->prefix[1],
           current->operating_number);
  }
}