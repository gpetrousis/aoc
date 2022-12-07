package runner

import (
	"fmt"
	"time"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/filereader"
)

func Day6Runner(inputFile string) {
	fr := filereader.NewFileReader(inputFile)
	data := fr.GetData()

	start := time.Now()
	part1 := days.Day6Part1(data)
	fmt.Println("Day6 Part1: ", part1, "(", time.Since(start), ")")

	start = time.Now()
	part2 := days.Day6Part2(data)
	fmt.Println("Day6 Part2: ", part2, "(", time.Since(start), ")")
}
