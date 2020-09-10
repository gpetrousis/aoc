package main

import (
	"fmt"
	"strconv"

	readfile "github.com/gpetrousis/aoc2019/readFile"
)

func parseInput(input string) []int {
	intArray := make([]int, 0, len(input))

	for _, i := range input {
		j, err := strconv.Atoi(string(i))
		if err != nil {
			fmt.Println("File reading error", err)
		}
		intArray = append(intArray, j)
	}
	return intArray
}

func parsePixels(pixels []int, layerCount int) [][][]int {
	layers := make([][][]int, layerCount)

	inputIndex := 0
	for z := 0; z < layerCount; z++ {
		layers[z] = make([][]int, 6)
		for j := 0; j < 6; j++ {
			layers[z][j] = make([]int, 25)

			for i := 0; i < 25; i++ {
				layers[z][j][i] = pixels[inputIndex]
				inputIndex++
			}
		}
	}
	return layers
}

func countDigits(layer [][]int, digit int) int {
	count := 0
	for j := 0; j < len(layer); j++ {
		for i := 0; i < len(layer[j]); i++ {
			if layer[j][i] == digit {
				count++
			}
		}
	}
	return count
}

func getLessZeros(layers [][][]int) int {
	minCount := 0
	minLayer := 0
	minCount = countDigits(layers[0], 0)
	for z := 1; z < len(layers); z++ {
		layerCount := countDigits(layers[z], 0)
		if layerCount < minCount {
			minCount = layerCount
			minLayer = z
		}
	}
	return minLayer
}

func printLayers(layers [][][]int) {
	for z := 0; z < len(layers); z++ {
		fmt.Println()
		for j := 0; j < len(layers[z]); j++ {
			fmt.Println(layers[z][j])
		}
	}
}

func generateImage(layers [][][]int) [][]int {
	image := layers[0]

	for z := 1; z < len(layers); z++ {
		for j := 0; j < len(layers[z]); j++ {
			for i := 0; i < len(layers[z][j]); i++ {
				if image[j][i] == 2 {
					image[j][i] = layers[z][j][i]
				}
			}
		}
	}
	return image
}

func printImage(image [][]int) {
	for j := 0; j < len(image); j++ {
		for i := 0; i < len(image[j]); i++ {
			switch image[j][i] {
			case 2:
				fmt.Print(" ")
			case 1:
				fmt.Print("*")
			case 0:
				fmt.Print(".")
			}
		}
		fmt.Println()
	}
}

func main() {
	input, err := readfile.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
	}
	pixels := parseInput(input)
	layerCount := len(pixels) / (25 * 6)
	layers := parsePixels(pixels, layerCount)

	// printLayers(layers)
	minLayer := getLessZeros(layers)
	ones := countDigits(layers[minLayer], 1)
	twos := countDigits(layers[minLayer], 2)

	image := generateImage(layers)
	printImage(image)
	fmt.Println("[Part1]", minLayer, ones, twos, ones*twos)
}
