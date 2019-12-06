package main

import (
	"fmt"
)

func parseOperator(op int) (int, []int) {
	opCode := op % 100
	modes := []int{0, 0, 0}
	modes[0] = (op / 100) % 10
	modes[1] = (op / 1000) % 10
	modes[2] = (op / 10000) % 10
	return opCode, modes
}

func getParamValue(memory []int, index int, mode int) int {
	if mode == 0 {
		return memory[index]
	} else if mode == 1 {
		return index
	}
	fmt.Println("Invalid param mode")
	return 0
}

func intcode(memory []int, pointer int) (int, error) {
	operator := memory[pointer]

	opCode, modes := parseOperator(operator)
	switch opCode {
	case 99:
		return 0, nil
	case 1:
		input1 := getParamValue(memory, pointer+1, modes[0])
		input2 := getParamValue(memory, pointer+2, modes[1])
		target := getParamValue(memory, pointer+3, modes[2])

		memory[target] = memory[input1] + memory[input2]
		pointer += 4
	case 2:
		input1 := getParamValue(memory, pointer+1, modes[0])
		input2 := getParamValue(memory, pointer+2, modes[1])
		target := getParamValue(memory, pointer+3, modes[2])

		memory[target] = memory[input1] * memory[input2]
		pointer += 4
	case 3:
		fmt.Print("Enter input: ")
		var input int
		_, err := fmt.Scanf("%d", &input)
		if err != nil {
			return 0, fmt.Errorf("Invalid Input: %d", input)
		}

		target := getParamValue(memory, pointer+1, modes[0])

		memory[target] = input
		pointer += 2
	case 4:
		param := getParamValue(memory, pointer+1, modes[0])
		fmt.Println("Output:", memory[param])
		pointer += 2
	case 5:
		param1 := getParamValue(memory, pointer+1, modes[0])
		param2 := getParamValue(memory, pointer+2, modes[1])
		if memory[param1] != 0 {
			pointer = memory[param2]
		} else {
			pointer += 3
		}
	case 6:
		param1 := getParamValue(memory, pointer+1, modes[0])
		param2 := getParamValue(memory, pointer+2, modes[1])
		if memory[param1] == 0 {
			pointer = memory[param2]
		} else {
			pointer += 3
		}
	case 7:
		param1 := getParamValue(memory, pointer+1, modes[0])
		param2 := getParamValue(memory, pointer+2, modes[1])
		target := getParamValue(memory, pointer+3, modes[2])
		if memory[param1] < memory[param2] {
			memory[target] = 1
		} else {
			memory[target] = 0
		}
		pointer += 4
	case 8:
		param1 := getParamValue(memory, pointer+1, modes[0])
		param2 := getParamValue(memory, pointer+2, modes[1])
		target := getParamValue(memory, pointer+3, modes[2])
		if memory[param1] == memory[param2] {
			memory[target] = 1
		} else {
			memory[target] = 0
		}
		pointer += 4
	default:
		return 0, fmt.Errorf("Invalid Op code: %d at position: %d", opCode, pointer)
	}

	return intcode(memory, pointer)
}
