package main

import (
	"fmt"
	"strconv"

	"github.com/gpetrousis/aoc2019/readFile"
)

func calculateFuelConsumption(mass int) int {
	return mass/3 - 2
}

func calculateTotalFuelConsumption(masses []string) int {
	var totalConspumption int = 0
	for _, mass := range masses {
		intMass, err := strconv.Atoi(mass)
		if err != nil {
			fmt.Println("Cannot convert string to int", err)
		}
		totalConspumption += calculateFuelConsumption(intMass)
	}
	return totalConspumption
}

func main() {
	masses, err := readFile.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}
	totalConspumption := calculateTotalFuelConsumption(masses)
	fmt.Println("Total fuel consumption:", totalConspumption)
}
