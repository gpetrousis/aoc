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

	buffer := []int{}

	memory := parseInput(input)
	maxOutput := 0
	maxPerm := []int{}

	perms := permutations([]int{0, 1, 2, 3, 4})
	permsFeedback := permutations([]int{5, 6, 7, 8, 9})

	for _, p := range perms {
		ampMemory := make([][]int, 5)

		previousOutput := 0

		for i, phase := range p {
			ampMemory[i] = make([]int, len(memory))
			copy(ampMemory[i], memory)

			buffer = append(buffer, phase, previousOutput)
			buffer, _, _ = intcode(ampMemory[i], 0, buffer)
			if err != nil {
				fmt.Println("Intcode error", err)
			}
			previousOutput = buffer[0]

			buffer = buffer[1:]
			ampMemory[i] = nil
		}
		if previousOutput >= maxOutput {
			maxOutput = previousOutput
			maxPerm = p
		}

	}

	fmt.Println("[Part1]", maxOutput, maxPerm)

	maxOutput = 0
	for _, p := range permsFeedback {
		ampMemory := make([][]int, 5)
		ampDone := []bool{false, false, false, false, false}
		ampPointer := []int{0, 0, 0, 0, 0}

		done := false
		for i, phase := range p {
			ampMemory[i] = make([]int, len(memory))
			copy(ampMemory[i], memory)
			buffer = append(buffer, phase)
			buffer, ampPointer[i], ampDone[i] = intcode(ampMemory[i], 0, buffer)
		}

		i := 0
		buffer = append(buffer, 0)
		for done == false {
			ampIndex := i % 5
			if (ampDone[ampIndex]) == true {
				done = true
			}

			buffer, ampPointer[ampIndex], ampDone[ampIndex] = intcode(ampMemory[ampIndex], ampPointer[ampIndex], buffer)
			i++
		}
		output := buffer[0]
		buffer = buffer[1:]
		if output >= maxOutput {
			maxOutput = output
			maxPerm = p
		}
		ampMemory = nil
	}
	fmt.Println("[Part2]", maxOutput, maxPerm)
}
