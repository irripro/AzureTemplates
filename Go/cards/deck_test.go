package main

import (
	"os"
	"testing"
)

func TestNewDeck(t *testing.T) {
	d := newDeck()
	if len(d) != 56 {
		t.Errorf("Expected deck length of 52, but got %v", len(d))
	}

	if d[0] != "Ace of Spades" {
		t.Errorf("The first card should have been 'Ace of Spades', but got: %v", d[0])
	}

	if d[len(d)-1] != "King of Hearts" {
		t.Errorf("The last card should have been 'King of Hearts' but got: %v", d[len(d)-1])
	}
}

func TestSaveToDeckAndNewDeckFromFile(t *testing.T) {
	os.Remove("_decktesting")

	deck := newDeck()
	deck.saveToFile("_decktesting")

	loadedDeck := newDeckFromFile("_decktesting")

	if len(loadedDeck) != 56 {
		t.Errorf("Test failed because expected 56 cards, but got %v", len(loadedDeck))
	}

	os.Remove("_decktesting")
}
