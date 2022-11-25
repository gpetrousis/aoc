package runner

import (
	"fmt"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/filereader"
)

func Day1Runner(inputFile string) {
	fr := filereader.NewFileReader(inputFile, "\n")

	part1 := days.Day1Part1(fr.ToStrArray())
	fmt.Println("Day1 Part1: ", part1)

	part2 := days.Day1Part2(fr.ToStrArray())
	fmt.Println("Day1 Part2: ", part2)
}
