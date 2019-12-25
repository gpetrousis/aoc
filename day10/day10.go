package main

import (
	"fmt"
	"math"
	"sort"

	readfile "github.com/gpetrousis/aoc2019/readFile"
)

type point struct {
	x float64
	y float64
}

func dist(a, b point) float64 {
	return math.Sqrt(math.Pow(b.x-a.x, 2) + math.Pow(b.y-a.y, 2))
}

func parseInput(lines []string) []point {
	asteroids := []point{}

	for j, line := range lines {
		for i, char := range line {
			if char == '#' {
				asteroids = append(asteroids, point{float64(i), float64(j)})
			}
		}
	}
	return asteroids
}

func getAngles(asteroids []point, base point) map[float64][]point {
	angles := make(map[float64][]point)
	for _, p := range asteroids {
		if p != base {
			dx := base.x - p.x
			dy := base.y - p.y
			angle := math.Atan2(dy, dx)
			angles[angle] = append(angles[angle], p)
		}
	}

	return angles
}

func main() {
	lines, err := readfile.ReadLines("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}

	asteroids := parseInput(lines)

	maxCount := 0
	station := point{-1, -1}
	var stationAngles map[float64][]point
	for _, asteroid := range asteroids {
		angles := getAngles(asteroids, asteroid)
		if len(angles) > maxCount {
			station = asteroid
			maxCount = len(angles)
			stationAngles = angles
		}
	}

	fmt.Println("[Part1]", station, maxCount)

	for th := range stationAngles {
		if len(stationAngles[th]) > 1 {
			sort.Slice(stationAngles[th], func(i, j int) bool {
				return dist(stationAngles[th][i], station) < dist(stationAngles[th][j], station)
			})
		}
	}

	sortedAngles := []float64{}
	for th := range stationAngles {
		sortedAngles = append(sortedAngles, th)
	}

	sort.Float64s(sortedAngles)

	index := sort.SearchFloat64s(sortedAngles, math.Pi/2)
	fmt.Println("[Part2] Start", index)
	count := 0

	target := point{-1, -1}
	for len(sortedAngles) > 0 && count < 200 {
		if index >= len(sortedAngles) {
			index = 0
		}
		angle := sortedAngles[index]
		target = stationAngles[angle][0]
		count++

		copy(stationAngles[angle][:], stationAngles[angle][1:])
		stationAngles[angle] = stationAngles[angle][:len(stationAngles[angle])-1]

		if len(stationAngles[angle]) > 0 {
			index++
		} else {
			copy(sortedAngles[index:], sortedAngles[index+1:])
			sortedAngles = sortedAngles[:len(sortedAngles)-1]
		}

		// fmt.Println("[Part2] Next target", count, target)
	}
	fmt.Println("[Part2]", target.x*100+target.y)
}
