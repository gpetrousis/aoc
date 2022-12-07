package days

import (
	"sort"
)

func compareCompartments(comp1, comp2 []rune) rune {
	len1 := len(comp1)
	len2 := len(comp2)

	if len1 != len2 {
		panic("The lengths do not match")
	}

	i := 0
	j := 0

	for i < len1 && j < len2 {
		val1 := comp1[i]
		val2 := comp2[j]

		if val1 == val2 {
			return val1
		}

		if val1 < val2 {
			i++
			continue
		}

		j++
		continue
	}

	return 0
}

func compare3Compartments(comp1, comp2, comp3 []rune) rune {
	len1 := len(comp1)
	len2 := len(comp2)
	len3 := len(comp3)

	i := 0
	j := 0
	k := 0

	for i < len1 && j < len2 && k < len3 {
		val1 := comp1[i]
		val2 := comp2[j]
		val3 := comp3[k]

		if val1 == val2 {
			if val1 == val3 {
				return val1
			}
			if val3 < val1 {
				k++
				continue
			}
			i++
			j++
			continue
		}

		if val1 < val2 {
			i++
			continue
		}

		j++
		continue
	}

	return 0
}

func sortItems(items string) []rune {
	r := []rune(items)

	sort.Slice(r, func(i, j int) bool {
		return r[i] < r[j]
	})

	return r
}

func priority(item rune) int {
	p := int(item)
	if p > 96 {
		return p - 96
	}

	return p - (64 - 26)
}

func Day3Part1(data []string) int {
	priorities := 0

	for _, rucksack := range data {
		comp1 := sortItems(rucksack[:len(rucksack)/2])
		comp2 := sortItems(rucksack[len(rucksack)/2:])

		item := compareCompartments(comp1, comp2)
		priorities += priority(item)
	}

	return priorities
}

func Day3Part2(data []string) int {
	priorities := 0

	for i := 0; i < len(data); i += 3 {
		comp1 := sortItems(data[i])
		comp2 := sortItems(data[i+1])
		comp3 := sortItems(data[i+2])

		item := compare3Compartments(comp1, comp2, comp3)
		priorities += priority(item)
	}

	return priorities
}
