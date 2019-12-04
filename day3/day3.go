package main

import (
	"fmt"
	"strings"

	readfile "github.com/gpetrousis/aoc2019/readFile"
)

func main() {
	paths, err := readfile.ReadLines("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}

	wire1path := strings.Split(paths[0], ",")
	wire2path := strings.Split(paths[1], ",")

	panelSize, centralPort := calculatePanelInfo(wire1path, wire2path)

	panel := make([]string, panelSize*panelSize)
	panel[pointToIndex(centralPort, panelSize)] = "o"

	colisions := populatePanel(panel, wire1path, centralPort, panelSize, "-")
	colisions = append(colisions, populatePanel(panel, wire2path, centralPort, panelSize, "=")...)

	closest := getClosestColision(centralPort, colisions)
	fmt.Println("[Part1] ", closest, manhatan(closest, centralPort))

	fmt.Println("[Part2] ")
}
