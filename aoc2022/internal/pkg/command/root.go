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
