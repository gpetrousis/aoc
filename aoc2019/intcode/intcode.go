package intcode

import (
	"fmt"
)

type intcode struct {
	memory       []int
	buffer       []int
	pointer      int
	relativeBase int
}

// New ....
func New(memory []int) intcode {
	_memory := make([]int, 100000)
	copy(_memory, memory)
	i := intcode{_memory, []int{}, 0, 0}
	return i
}

func parseOperator(op int) (int, []int) {
	opCode := op % 100
	modes := []int{0, 0, 0}
	modes[0] = (op / 100) % 10
	modes[1] = (op / 1000) % 10
	modes[2] = (op / 10000) % 10
	return opCode, modes
}

func getParamValue(i *intcode, index int, mode int) int {
	if mode == 0 {
		return i.memory[index]
	} else if mode == 1 {
		return index
	} else if mode == 2 {
		return i.memory[index] + i.relativeBase
	}
	fmt.Println("Invalid param mode")
	return 0
}

func AddToBuffer(i *intcode, value int) {
	i.buffer = append(i.buffer, value)
}

func GetFromBuffer(i *intcode) (int, error) {
	if len(i.buffer) == 0 {
		return 0, fmt.Errorf("The buffer is empty")
	}
	input := i.buffer[0]
	i.buffer = i.buffer[1:]
	return input, nil
}

func GetBuffer(i intcode) []int {
	return i.buffer
}

func Run(i *intcode) error {
	operator := i.memory[i.pointer]

	opCode, modes := parseOperator(operator)
	switch opCode {
	case 99:
		return nil
	case 1:
		input1 := getParamValue(i, i.pointer+1, modes[0])
		input2 := getParamValue(i, i.pointer+2, modes[1])
		target := getParamValue(i, i.pointer+3, modes[2])

		i.memory[target] = i.memory[input1] + i.memory[input2]
		i.pointer += 4
	case 2:
		input1 := getParamValue(i, i.pointer+1, modes[0])
		input2 := getParamValue(i, i.pointer+2, modes[1])
		target := getParamValue(i, i.pointer+3, modes[2])

		i.memory[target] = i.memory[input1] * i.memory[input2]
		i.pointer += 4
	case 3:
		input, err := GetFromBuffer(i)
		if err != nil {
			return nil
		}
		target := getParamValue(i, i.pointer+1, modes[0])
		i.memory[target] = input
		i.pointer += 2
	case 4:
		param := getParamValue(i, i.pointer+1, modes[0])
		AddToBuffer(i, i.memory[param])
		i.pointer += 2
	case 5:
		param1 := getParamValue(i, i.pointer+1, modes[0])
		param2 := getParamValue(i, i.pointer+2, modes[1])
		if i.memory[param1] != 0 {
			i.pointer = i.memory[param2]
		} else {
			i.pointer += 3
		}
	case 6:
		param1 := getParamValue(i, i.pointer+1, modes[0])
		param2 := getParamValue(i, i.pointer+2, modes[1])
		if i.memory[param1] == 0 {
			i.pointer = i.memory[param2]
		} else {
			i.pointer += 3
		}
	case 7:
		param1 := getParamValue(i, i.pointer+1, modes[0])
		param2 := getParamValue(i, i.pointer+2, modes[1])
		target := getParamValue(i, i.pointer+3, modes[2])
		if i.memory[param1] < i.memory[param2] {
			i.memory[target] = 1
		} else {
			i.memory[target] = 0
		}
		i.pointer += 4
	case 8:
		param1 := getParamValue(i, i.pointer+1, modes[0])
		param2 := getParamValue(i, i.pointer+2, modes[1])
		target := getParamValue(i, i.pointer+3, modes[2])
		if i.memory[param1] == i.memory[param2] {
			i.memory[target] = 1
		} else {
			i.memory[target] = 0
		}
		i.pointer += 4
	case 9:
		param := getParamValue(i, i.pointer+1, modes[0])
		i.relativeBase += i.memory[param]
		i.pointer += 2
	default:
		return fmt.Errorf("Invalid Op code: %d", opCode)
	}

	return Run(i)
}
