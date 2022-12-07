package runner

import (
	"fmt"
	"time"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/filereader"
)

func Day7Runner(inputFile string) {
	fr := filereader.NewFileReader(inputFile)
	data := fr.ToStrArray("\n")

	start := time.Now()
	part1 := days.Day7Part1(data)
	fmt.Println("Day7 Part1: ", part1, "(", time.Since(start), ")")

	start = time.Now()
	part2 := days.Day7Part2(data)
	fmt.Println("Day7 Part2: ", part2, "(", time.Since(start), ")")
}
