package main

import (
	"fmt"
	"net/http"
	"time"
)

func main() {
	links := []string{
		"http://google.com",
		"http://microsoft.com",
		"http://amazon.com",
		"http://golang.org",
		"http://espn.com",
		"http://bose.com",
		"http://apple.com",
	}

	c := make(chan string)

	for _, link := range links {
		go checkLink(link, c)
	}

	for l := range c {
		go func(link string) {
			time.Sleep(10 * time.Second)
			checkLink(link, c)
		}(l)
	}
}

func checkLink(l string, c chan string) {
	_, err := http.Get(l)
	if err != nil {
		c <- l
		fmt.Println(l, " is down!")
		return
	}
	fmt.Println(l, "is up!")
	c <- l
}
