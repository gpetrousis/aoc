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

	part1memory := make([]int, len(memory))
	copy(part1memory, memory)

	part1memory[1] = 12
	part1memory[2] = 2

	intcode(part1memory, 0)

	fmt.Println("[Part1]", part1memory[0])
	noun, verb, err := calculateNounAndVerb(memory, 19690720)
	if err != nil {
		fmt.Println("[Part2] Error", err)

	}
	fmt.Println("[Part2] 100 *", noun, "+", verb, "=", 100*noun+verb)
}
