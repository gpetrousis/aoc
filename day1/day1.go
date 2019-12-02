package main

import (
	"fmt"
	"strconv"
	"github.com/gpetrousis/aoc2019/readfile"
)


func main() {
	masses, err := readfile.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}

	var totalConsumption int = 0
	var totalConsumptionWithExtra int = 0
	for _, mass := range masses {
		intMass, err := strconv.Atoi(mass)
		if err != nil {
			fmt.Println("Cannot convert string to int", err)
		}
		// Not the most optimal solution. Just for the sake of two parts for the
		// challenge
		totalConsumption += calculateConsumption(intMass)
		totalConsumptionWithExtra += calculateConsumptionWithExtra(intMass)
	}

	fmt.Println("[Part1] Total fuel consumption:", totalConsumption)

	// totalConspumption := sumConsumption + calculateExtraConsumption(sumConsumption)
	// fmt.Println("Total fuel consumption:", totalConspumption)
}
