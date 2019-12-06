package main

import (
	"fmt"

	readfile "github.com/gpetrousis/aoc2019/readFile"
)

func main() {
	input, err := readfile.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}

	memory := parseInput(input)

	_, err = intcode(memory, 0)
	if err != nil {
		fmt.Println("Intcode error", err)
	}
}
