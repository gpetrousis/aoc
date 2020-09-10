package main

import "strconv"

func isIncremental(password int) bool {
	passString := strconv.Itoa(password)
	for i := 1; i < len(passString); i++ {
		if passString[i-1] > passString[i] {
			return false
		}
	}
	return true
}

func hasDuplicateDigits(password int) bool {
	passString := strconv.Itoa(password)
	for i := 1; i < len(passString); i++ {
		if passString[i-1] == passString[i] {
			return true
		}
	}
	return false
}

func hasMaxOneDuplicateDigits(password int) bool {
	passString := strconv.Itoa(password)
	multiples := make(map[string]int)

	for i := 1; i < len(passString); i++ {
		if passString[i-1] == passString[i] {
			key := string(passString[i])
			if _, ok := multiples[key]; ok {
				multiples[key]++
			} else {
				multiples[key] = 2
			}
		}
	}
	for _, i := range multiples {
		if i == 2 {
			return true
		}
	}
	return false
}

func getFirstPossiblePasswork(s string) int {
	var minStart string = string(s[0])
	for i := 1; i < len(s); i++ {
		if s[i] < s[i-1] {
			for j := i; j < len(s); j++ {
				minStart += string(s[i-1])
			}
			result, _ := strconv.Atoi(minStart)
			return result
		}
		minStart += string(s[i])
	}
	result, _ := strconv.Atoi(minStart)
	return result
}

func getLastPossiblePasswork(s string) int {
	maxEnd := ""
	for i := 0; i < len(s)-1; i++ {
		if s[i] > s[i+1] {
			maxEnd += string(s[i] - 1)
			for j := i + 1; j < len(s); j++ {
				maxEnd += "9"
			}
			result, _ := strconv.Atoi(maxEnd)
			return result
		}
		maxEnd += string(s[i])
	}
	maxEnd += string(s[len(s)-1])
	result, _ := strconv.Atoi(maxEnd)
	return result
}

func countPossiblePasswords(start int, end int) int {
	count := 0
	for i := start; i <= end; i++ {
		if isIncremental(i) && hasDuplicateDigits(i) {
			count++
		}
	}
	return count
}

func countPossiblePasswordsPart2(start int, end int) int {
	count := 0
	for i := start; i <= end; i++ {
		if isIncremental(i) && hasMaxOneDuplicateDigits(i) {
			count++
		}
	}
	return count
}
