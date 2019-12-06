package main

import (
	"fmt"
	"strconv"
	"strings"
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
