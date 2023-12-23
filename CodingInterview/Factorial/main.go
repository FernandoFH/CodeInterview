package main

import (
	"fmt"
	"log"
)

// Output: 120 - 5!
// Output: 1 - 0!
// Output: 6 - 3!
// The input integer n is non-negative (0 <= n <= 10)

func main() {
	fmt.Println(CalculateFactorial(5))
	fmt.Println(CalculateFactorial(0))
	fmt.Println(CalculateFactorial(3))
}

func CalculateFactorial(n int) int {
	if n < 0 {
		log.Println("Factorial not defined for negative numbres")
		return 0
	}
	if n > 100 {
		log.Println("n must be less than or equal to 10")
		return 0
	}

	for i := n; i > 0; i-- {

	}

	return 0
}
