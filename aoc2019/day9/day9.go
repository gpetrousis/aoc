package main

import (
	"fmt"
	"strconv"
	"strings"

	intcode "github.com/gpetrousis/aoc2019/intcode"
	readfile "github.com/gpetrousis/aoc2019/readFile"
)

func parseInput(input string) []int {
	inputArray := strings.Split(input, ",")
	intArray := make([]int, 0, len(inputArray))

	for _, i := range inputArray {
		j, err := strconv.Atoi(i)
		if err != nil {
			fmt.Println("File reading error", err)
		}
		intArray = append(intArray, j)
	}
	return intArray
}

func main() {
	input, err := readfile.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}

	memory := parseInput(input)
	computer := intcode.New(memory)

	intcode.AddToBuffer(&computer, 1)
	intcode.Run(&computer)

	fmt.Println("[Part1]", intcode.GetBuffer(computer))

	computerBoost := intcode.New(memory)

	intcode.AddToBuffer(&computerBoost, 2)
	intcode.Run(&computerBoost)

	fmt.Println("[Part2]", intcode.GetBuffer(computerBoost))
}
