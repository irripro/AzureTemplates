package main

import (
	"fmt"
)

type triangle struct {
	height float64
	base   float64
}

type square struct {
	sideLength float64
}

type shape interface {
	getArea() float64
}

func main() {
	ms := square{
		sideLength: 2,
	}
	mt := triangle{
		height: 3,
		base:   2,
	}
	fmt.Printf("The square side is %v\n", ms.sideLength)
	fmt.Printf("The square area is: %v\n", ms.getArea())
	fmt.Printf("The triangle height is %v\n", mt.height)
	fmt.Printf("The triangle base is %v\n", mt.base)
	fmt.Printf("The triangle area is: %v\n", mt.getArea())

	printArea(mt)
	printArea(ms)

}

func printArea(s shape) {
	fmt.Println("This if from the interface function", s.getArea())
}

func (s square) getArea() float64 {
	return s.sideLength * s.sideLength
}

func (t triangle) getArea() float64 {
	return t.base * .5 * t.height
}
