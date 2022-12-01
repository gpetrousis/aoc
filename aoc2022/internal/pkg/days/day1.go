package days

import (
	"sort"
	"strconv"
)

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

	return strconv.Itoa(sum)
}
