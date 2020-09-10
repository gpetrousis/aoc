package main

import (
	"strconv"
)

func absInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func parseStep(step string) (string, int) {
	stepRune := []rune(step)
	direction := string(stepRune[0:1])
	steps, _ := strconv.Atoi(string(stepRune[1:]))
	return direction, steps
}

func manhatan(a Point, b Point) int {
	return absInt(a.x-b.x) + absInt(a.y-b.y)
}
