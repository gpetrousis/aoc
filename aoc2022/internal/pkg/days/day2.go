package days

import "strings"

func calculateRoundPart1(p1 string, p2 string) int {
	// A for Rock, B for Paper, and C for Scissors.
	// X for Rock, Y for Paper, and Z for Scissors
	// 1 for Rock, 2 for Paper, and 3 for Scissors
	// 0 if you lost, 3 if the round was a draw, and 6 if you won
	switch p1 {
	case "A":
		switch p2 {
		case "X":
			return 1 + 3
		case "Y":
			return 2 + 6
		case "Z":
			return 3 + 0
		}
	case "B":
		switch p2 {
		case "X":
			return 1 + 0
		case "Y":
			return 2 + 3
		case "Z":
			return 3 + 6
		}
	case "C":
		switch p2 {
		case "X":
			return 1 + 6
		case "Y":
			return 2 + 0
		case "Z":
			return 3 + 3
		}
	}

	return 0
}

func calculateRoundPart2(p1 string, p2 string) int {
	switch p1 {
	case "A":
		switch p2 {
		case "X":
			// Loose + Scissors
			return 0 + 3
		case "Y":
			// Draw + Rock
			return 3 + 1
		case "Z":
			// Win + Paper
			return 6 + 2
		}
	case "B":
		switch p2 {
		case "X":
			// Loose + Rock
			return 0 + 1
		case "Y":
			// Draw + Paper
			return 3 + 2
		case "Z":
			// Win + Scisors
			return 6 + 3
		}
	case "C":
		switch p2 {

		// A for Rock, B for Paper, and C for Scissors.
		// X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
		// 1 for Rock, 2 for Paper, and 3 for Scissors
		// 0 if you lost, 3 if the round was a draw, and 6 if you won
		case "X":
			// Loose + Paper
			return 0 + 2
		case "Y":
			// Draw + Scissors
			return 3 + 3
		case "Z":
			// Win + Rock
			return 6 + 1
		}
	}

	return 0
}

func Day2Part1(data []string) int {
	score := 0
	for _, round := range data {
		choices := strings.Split(round, " ")
		score += calculateRoundPart1(choices[0], choices[1])
	}
	return score
}

func Day2Part2(data []string) int {
	score := 0
	for _, round := range data {
		choices := strings.Split(round, " ")
		score += calculateRoundPart2(choices[0], choices[1])
	}
	return score
}
