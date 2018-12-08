package main

import (
	"fmt"
)

type contact struct {
	city   string
	number int
}

type person struct {
	firstName string
	lastName  string
	contact
}

func main() {
	alex := person{
		firstName: "Alex",
		lastName:  "Jones",
		contact: contact{
			city:   "Seattle",
			number: 98007,
		},
	}
	alex.print()
	alex.updateName("Ali")
	alex.print()
}

func (p *person) updateName(newName string) {
	(*p).firstName = newName
}

func (p person) print() {
	fmt.Println(p)
}
