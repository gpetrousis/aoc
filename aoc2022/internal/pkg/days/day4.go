package days

import (
	"strconv"
	"strings"
)

type section struct {
	start, end int
}

func newSection(start, end int) *section {
	return &section{start: start, end: end}
}

func (s section) contains(other section) bool {
	if s.start <= other.start && s.end >= other.end {
		return true
	}

	if other.start <= s.start && other.end >= s.end {
		return true
	}

	return false
}

func (s section) overlap(other section) bool {
	if s.start <= other.start && other.start <= s.end {
		return true
	}

	if other.start <= s.start && s.start <= other.end {
		return true
	}

	return false
}

func parseSection(input string) *section {
	parts := strings.Split(input, "-")
	start, err := strconv.Atoi(parts[0])
	if err != nil {
		panic(err)
	}

	end, err := strconv.Atoi(parts[1])
	if err != nil {
		panic(err)
	}

	return newSection(start, end)
}

func Day4Part1(data []string) int {
	overlaping := 0

	for _, value := range data {
		sections := strings.Split(value, ",")
		sec1 := parseSection(sections[0])
		sec2 := parseSection(sections[1])

		if sec1.contains(*sec2) {
			overlaping += 1
		}
	}

	return overlaping
}

func Day4Part2(data []string) int {
	overlaping := 0

	for _, value := range data {
		sections := strings.Split(value, ",")
		sec1 := parseSection(sections[0])
		sec2 := parseSection(sections[1])

		if sec1.overlap(*sec2) {
			overlaping += 1
		}
	}

	return overlaping
}
