package main

import (
	"fmt"

	readfile "github.com/gpetrousis/aoc2019/readFile"
)

func main() {
	paths, err := readfile.ReadLines("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}

	fmt.Println("[Part1] ", paths)
	fmt.Println("[Part2] ")
}
