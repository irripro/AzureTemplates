package main

import "fmt"

func main() {
	colors := map[string]string{
		"red":   "#ff000",
		"green": "#gg000",
		"white": "#II000",
	}
	mapPrint(colors)
}

func mapPrint(c map[string]string) {
	for color, value := range c {
		fmt.Printf("Color is: %v \t\t Hex Value is: %v", color, value)
		fmt.Println("")
	}
}

E52