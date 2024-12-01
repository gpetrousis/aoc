package cmd

import (
	"github.com/spf13/cobra"
)

var cliRootCommand = "aoc"

var persistentFlags struct {
	verbose bool
}

func NewRootCmd(version string) *cobra.Command {
	cmd := &cobra.Command{
		Use:     cliRootCommand,
		Version: version,
		Short:   "CLI to execute the AoC challenges",
		Long: `A CLI to run the code for the AoC challenges that provides useful
features such as timming`,
	}

	cmd.PersistentFlags().BoolVarP(&persistentFlags.verbose, "verbose", "v", false, "Enable verbose output")

	return cmd
}

func Execute(version string) error {
	rootCmd := NewRootCmd("0.1.0")
	return rootCmd.Execute()
}
