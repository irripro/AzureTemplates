package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	fileName := string(os.Args[1])
	myFile, err := os.Open(fileName)
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}
	io.Copy(os.Stdout, myFile)
}
