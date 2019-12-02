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
	array := parseInput(input)

	array[1] = 12
	array[2] = 2

	intcode(array, 0)

	fmt.Println("[Part1]", array[0])
	fmt.Println("[Part2]")
}
