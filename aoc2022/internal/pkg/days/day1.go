package days

import (
	"sort"
	"strconv"
)

func maxArray(data []int) (int, int) {
	index := 0
	max := data[0]
	for i, value := range data {
		if value > max {
			max = value
			index = i
		}
	}
	return index, max
}

func sumTopThree(data []int) (int, int) {
	index := 0
	max := data[0]
	for i, value := range data {
		if value > max {
			max = value
			index = i
		}
	}
	return index, max
}

func getCalories(data []string) []int {
	var calories []int
	sum := 0
	for _, val := range data {
		if val == "" {
			calories = append(calories, sum)
			sum = 0
			continue
		}

		intVar, err := strconv.Atoi(val)
		if err != nil {
			panic("Could not parse string value")
		}

		sum += intVar
	}
	calories = append(calories, sum)

	return calories
}

func Day1Part1(data []string) string {
	calories := getCalories(data)

	sort.Ints(calories)

	return strconv.Itoa(calories[len(calories)-1])
}

func Day1Part2(data []string) string {
	calories := getCalories(data)

	sort.Ints(calories)

	len := len(calories)
	sum := 0
	for _, val := range calories[len-3:] {
		sum += val
	}
	// Placeholder
	return strconv.Itoa(sum)
}
