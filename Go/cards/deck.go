package main

import (
	"fmt"
)

// Create a new type of 'deck'
// which is a slice of string

type deck []string

func newDeck() deck {
	cards := deck{}

	cardSuits := []string{"Spades", "Diamonds", "Clubs", "Hearts"}
	cardValues := []string{"Ace", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jacks", "Queens", "King"}

	for _, value := range cardValues {
		for _, suit := range cardSuits {
			cards = append(cards, value+" of "+suit)
		}
	}

	return cards
}

func (d deck) print() {
	for i, card := range d {
		fmt.Println(i, card)
	}
}
