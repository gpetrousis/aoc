package main

import (
	"fmt"
	"os"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/command"
)

func main() {
	cmd := command.RootCmd()
	if err := cmd.Execute(); err != nil {
		_, _ = fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
