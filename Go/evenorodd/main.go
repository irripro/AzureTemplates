package main

import (
	"fmt"
)

func main() {
	evenNumbers := []int{}
	oddNumbers := []int{}
	n := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	for _, value := range n {
		if (value % 2) == 0 {
			evenNumbers = append(evenNumbers, value)
			fmt.Println(value, " - This number is even")
		} else {
			oddNumbers = append(oddNumbers, value)
			fmt.Println(value, " - This number is odd")
		}
	}

	fmt.Println("The even numbers are:", evenNumbers)
	fmt.Println("The odd numbers are:", oddNumbers)
}
