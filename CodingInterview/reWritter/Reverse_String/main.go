package main

import (
	"fmt"
)

func main() {
	//Reverse String
	// abcd --> dbca
	// 0, 1, 2, 3
	s := "abcd"

	fmt.Println(reverseString(s))
	fmt.Println(reverseStringPro(s))
}

func reverseStringPro(s string) string {
	r := []rune(s)

	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}

	return string(r)
}

func reverseString(s string) string {
	r := []rune(s)
	//rReverse := make([]rune, len(s))

	fmt.Println("Impresion Original")
	for i := 0; i < len(r); i++ {
		fmt.Println(string(r[i]))
	}

	fmt.Println("Impresion Reversa")
	for j := len(r) - 1; j >= 0; j-- {
		fmt.Println(string(r[j]))
	}
	return ""
}
