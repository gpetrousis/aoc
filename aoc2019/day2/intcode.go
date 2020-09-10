package main

import "fmt"

func intcode(memory []int, pointer int) error {
	operator := memory[pointer]
	if operator == 99 {
		return nil
	}

	input1 := memory[pointer+1]
	input2 := memory[pointer+2]
	target := memory[pointer+3]

	if operator == 1 {
		memory[target] = memory[input1] + memory[input2]
	} else if operator == 2 {
		memory[target] = memory[input1] * memory[input2]
	} else {
		return fmt.Errorf("Invalid Op code: %d", operator)
	}

	intcode(memory, pointer+4)
	return nil
}

func calculateNounAndVerb(memory []int, result int) (int, int, error) {
	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			newMemory := make([]int, len(memory))
			copy(newMemory, memory)

			newMemory[1] = noun
			newMemory[2] = verb

			err := intcode(newMemory, 0)
			if err != nil {
				return 0, 0, err
			}

			if newMemory[0] == result {
				return noun, verb, nil
			}
		}
	}
	return 0, 0, fmt.Errorf("Could not find proper values")
}
