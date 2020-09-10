package main

import "fmt"

// Point ...
type Point struct {
	x int
	y int
}

func updatePosition(current Point, direction string, steps int) (Point, error) {
	switch direction {
	case "U":
		current.y -= steps
	case "R":
		current.x += steps
	case "L":
		current.x -= steps
	case "D":
		current.y += steps
	default:
		return Point{0, 0}, fmt.Errorf("Unknown direction %s", direction)
	}
	return current, nil
}

func nextStep(current Point, direction string) Point {
	switch direction {
	case "U":
		current.y--
	case "R":
		current.x++
	case "L":
		current.x--
	case "D":
		current.y++
	default:
		return Point{0, 0}
	}
	return current
}

func updateMinMax(minPoint Point, maxPoint Point, current Point) (Point, Point) {
	if current.x > maxPoint.x {
		maxPoint.x = current.x
	}
	if current.y > maxPoint.y {
		maxPoint.y = current.y
	}
	if current.x < minPoint.x {
		minPoint.x = current.x
	}
	if current.y < minPoint.y {
		minPoint.y = current.y
	}
	return minPoint, maxPoint
}

func pointToIndex(current Point, size int) int {
	return size*current.y + current.x
}
