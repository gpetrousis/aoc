package runner

import (
	"fmt"
	"time"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/filereader"
)

func Day1Runner(inputFile string) {
	fr := filereader.NewFileReader(inputFile)
	data := fr.ToStrArray("\n")

	start := time.Now()
	part1 := days.Day1Part1(data)
	fmt.Println("Day1 Part1: ", part1, "(", time.Since(start), ")")

	start = time.Now()
	part2 := days.Day1Part2(data)
	fmt.Println("Day1 Part2: ", part2, "(", time.Since(start), ")")
}
