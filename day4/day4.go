package main

import (
	"fmt"
	"strings"

	readfile "github.com/gpetrousis/aoc2019/readFile"
)

func main() {
	passRange, err := readfile.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}
	passLimits := strings.Split(passRange, "-")
	minStart := getFirstPossiblePasswork(passLimits[0])
	maxEnd := getLastPossiblePasswork(passLimits[1])

	possiblePasswords := countPossiblePasswords(minStart, maxEnd)

	fmt.Println("[Part1]", possiblePasswords)
	possiblePasswordsPart2 := countPossiblePasswordsPart2(minStart, maxEnd)
	fmt.Println("[Part2]", possiblePasswordsPart2)
}
