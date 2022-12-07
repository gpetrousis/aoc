package days

func findInitSequence(input string, size int) int {
	duplicate := false

	i := 0
	for i < len(input)-size {
		duplicate = false

		for j := i; j < i+size-1; j++ {
			for k := j + 1; k < i+size; k++ {
				if input[j] == input[k] {
					duplicate = true
					i = j + 1
					break
				}
			}
			if duplicate {
				break
			}
		}

		if duplicate {
			continue
		}

		return i + size
	}

	return 0
}

func Day6Part1(data string) int {
	initSequence := findInitSequence(data, 4)
	return initSequence
}

func Day6Part2(data string) int {
	initSequence := findInitSequence(data, 14)
	return initSequence
}
