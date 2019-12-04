package main

import "fmt"

func calculatePanelInfo(wire1 []string, wire2 []string) (int, Point) {
	maxPoint := Point{0, 0}
	minPoint := Point{0, 0}
	current := Point{0, 0}

	for _, step := range wire1 {
		direction, steps := parseStep(step)
		var err error
		current, err = updatePosition(current, direction, steps)
		if err != nil {
			fmt.Println("Cannot update position", err)
			return 0, Point{0, 0}
		}
		minPoint, maxPoint = updateMinMax(minPoint, maxPoint, current)
	}

	current = Point{0, 0}
	for _, step := range wire2 {
		direction, steps := parseStep(step)
		var err error
		current, err = updatePosition(current, direction, steps)
		if err != nil {
			fmt.Println("Cannot update position", err)
			return 0, Point{0, 0}
		}
		minPoint, maxPoint = updateMinMax(minPoint, maxPoint, current)
	}
	fmt.Println("MaxPoint", maxPoint)
	fmt.Println("MinPoint", minPoint)
	maxSide := maxInt(absInt(maxPoint.x-minPoint.x), absInt(maxPoint.y-minPoint.y)) + 1

	centralPort := Point{-minPoint.x, -minPoint.y}
	return maxSide, centralPort
}

func populatePanel(panel []string, wire []string, centralPort Point, panelSize int, wireChar string) []Point {
	colisions := []Point{}
	current := centralPort

	for _, step := range wire {
		direction, steps := parseStep(step)
		for i := 0; i < steps; i++ {
			current = nextStep(current, direction)
			currentIndex := pointToIndex(current, panelSize)
			if panel[currentIndex] == "" || panel[currentIndex] == wireChar {
				panel[currentIndex] = wireChar
			} else {
				panel[currentIndex] = "x"
				colisions = append(colisions, current)
			}
		}
	}
	return colisions
}

func getClosestColision(centralPanel Point, colisions []Point) Point {
	closest := colisions[0]
	for _, colision := range colisions {
		if manhatan(centralPanel, closest) > manhatan(centralPanel, colision) {
			closest = colision
		}
	}
	return closest
}

func printPanel(panel []string, panelSize int) {
	for y := 0; y < panelSize; y++ {
		for x := 0; x < panelSize; x++ {
			char := panel[pointToIndex(Point{x, y}, panelSize)]
			if char == "" {
				char = "."
			}
			fmt.Printf("%s ", char)
		}
		fmt.Printf("\n")
	}
}
