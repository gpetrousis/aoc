package main

import (
	"fmt"
	"strings"

	readfile "github.com/gpetrousis/aoc2019/readFile"
)

func main() {
	input, err := readfile.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}
	inputArray := strings.Split(input, ",")

	fmt.Println("[Part1]")
	fmt.Println("[Part2]")
}
