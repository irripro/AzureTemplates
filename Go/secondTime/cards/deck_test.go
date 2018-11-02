package main

import (
	"os"
	"testing"
)

func TestNewDec(t *testing.T) {
	d := newDeck()
	if (len(d) == 16) && (d[0] == "Ace of Spades") && (d[len(d)-1] == "Four of Clubs") {
		d.print("Things are Good")
	} else {
		t.Errorf("Something went wrong and the length of deck is %v", len(d))
	}
}

func TestNewDeckFromFileAndSaveToFile(t *testing.T) {
	os.Remove("_decktesting")
	
	d := newDeck()
	d.saveToFile("_decktesting")
	nd := newDeckFromFile("_decktesting")
	if len(nd) != 16 {
		t.Errorf("The loaded deck was not the correct size. Its size was %v", len(nd))
	}
	nd.print("Test Deck")
	os.Remove("_decktesting")
}
