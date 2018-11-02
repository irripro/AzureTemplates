package main

func main() {
	// cards := newDeck()
	// cards.print("Original")
	// hand, remainingDeck := deal(cards, 10)
	// hand.print("Hand")
	// remainingDeck.print("Remaining Deck")
	// fmt.Println("Giant String: " + cards.toString())
	// cards.saveToFile("my_cards.txt")
	myCards := newDeckFromFile("my_cards.txt")
	myCards.print("Read from file")
	myCards.shuffle()
}
