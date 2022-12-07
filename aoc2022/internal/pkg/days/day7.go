package days

import (
	"strings"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/utils/day7"
)

func parseCommands(data []string) *day7.Fs {
	fileSystem := day7.NewFs("/")

	for _, cmd := range data {
		if strings.HasPrefix(cmd, "$ cd") {
			fileSystem.Cd(cmd[5:])
			continue
		}

		if cmd == "$ ls" {
			continue
		}

		if strings.HasPrefix(cmd, "dir") {
			fileSystem.AddDir(cmd[4:])
			continue
		}

		fileSystem.AddFile(cmd)
	}

	return fileSystem
}

func Day7Part1(data []string) int {
	fileSystem := parseCommands(data)

	return fileSystem.GetSumDirSize(100000)
}

func Day7Part2(data []string) int {
	total := 70000000
	updateSize := 30000000
	fileSystem := parseCommands(data)

	freeSpace := total - fileSystem.GetSize()
	toFree := updateSize - freeSpace

	return fileSystem.GetSmallestDirSize(toFree)
}
