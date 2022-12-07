package command

import (
	"fmt"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/runner"
	"github.com/spf13/cobra"
)

var (
	inputFile string
)

func RootCmd() *cobra.Command {
	days := map[string]func(inputFile string){
		"day1": runner.Day1Runner,
		"day2": runner.Day2Runner,
		"day3": runner.Day3Runner,
		"day4": runner.Day4Runner,
		"day5": runner.Day5Runner,
		"day6": runner.Day6Runner,
		"day7": runner.Day7Runner,
	}

	cmd := &cobra.Command{
		Use:   "aoc2022",
		Short: "aoc2022 CLI",
		Long:  `Advent Of Code 2022 CLI to execute the problems of each day`,
	}

	cmd.PersistentFlags().StringVarP(&inputFile, "input", "i", "", "Input File")
	_ = cmd.MarkFlagRequired("input")

	for day, runnerFunction := range days {
		localDay := day
		localRunner := runnerFunction
		dayCmd := &cobra.Command{
			Use:   localDay,
			Short: fmt.Sprintf("aoc2022 %s", day),
			Run: func(cmd *cobra.Command, args []string) {
				localRunner(inputFile)
			},
		}
		cmd.AddCommand(dayCmd)
	}

	return cmd
}
