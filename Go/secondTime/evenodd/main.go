package main

import (
	"fmt"
)

func main() {
	is := []int{1,2,3,4,5,6,7,8,9,0}
	for _, value := range is {
		if (value % 2) == 0 {
			fmt.Println("The value is even: ", value)
		} else {
			fmt.Println("The value is odd: ", value)
		}
	}

}