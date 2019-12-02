package main

import "fmt"

func intcode(array []int, index int) {
	operator := array[index]
	if operator == 99 {
		return
	}

	input1 := array[index+1]
	input2 := array[index+2]
	target := array[index+3]

	if operator == 1 {
		array[target] = array[input1] + array[input2]
	} else if operator == 2 {
		array[target] = array[input1] * array[input2]
	} else {
		fmt.Println("Invalid Op code")
		return
	}

	intcode(array, index+4)
}
