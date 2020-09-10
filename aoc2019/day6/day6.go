package main

import (
	"fmt"

	readfile "github.com/gpetrousis/aoc2019/readFile"
)

func main() {
	orbits, err := readfile.ReadLines("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}

	depenencyMap := createDependencyMap(orbits)
	orbitMap := populateMap(depenencyMap)

	fmt.Println("[Part1]", countOrbits(orbitMap, 0))

	youNode, _ := findChild(orbitMap, "YOU", 0)
	sanNode, _ := findChild(orbitMap, "SAN", 0)

	fmt.Println("[Part2]", nodeDistance((*youNode).parent, (*sanNode).parent, 0))
}
