package main

import (
	"fmt"
)

type bot interface{
	getGreetings() string

}

type englishBot struct{}
type spanishBot struct{}


func main(){
	myEB := englishBot{}
	printGreetings(myEB)

	mySB := spanishBot{}
	printGreetings(mySB)
}

func printGreetings(b bot){
	fmt.Println(b.getGreetings())
}

func (englishBot) getGreetings() string{
	return "Hello!"
}

func (spanishBot) getGreetings() string{
	return "Hola!"
}