package main

import (
	"fmt"
	"strings"
)

type tree struct {
	value    string
	parent   *tree
	children []*tree
}

func insertChildren(root *tree, dep map[string][]string) {
	children := dep[(*root).value]
	for _, child := range children {
		newNode := new(tree)
		(*newNode).value = child
		(*newNode).parent = root
		(*root).children = append((*root).children, newNode)
		insertChildren(newNode, dep)
	}
}

func populateMap(dep map[string][]string) *tree {
	root := new(tree)
	(*root).value = "COM"

	insertChildren(root, dep)
	return root
}

func countOrbits(root *tree, count int) int {
	if root == nil {
		return 0
	}
	parentCount := count
	for _, node := range (*root).children {
		count += countOrbits(node, parentCount+1)
	}
	return count
}

func printMap(orbitMap *tree) {
	fmt.Println((*orbitMap).value)
	for _, node := range (*orbitMap).children {
		fmt.Print((*orbitMap).value, ": ")
		printMap(node)
	}
}

func createDependencyMap(orbits []string) map[string][]string {
	dep := make(map[string][]string)
	for _, orbit := range orbits {
		inputs := strings.Split(orbit, ")")
		parent := inputs[0]
		child := inputs[1]
		_, ok := dep[parent]
		if !ok {
			dep[parent] = []string{child}
		} else {
			dep[parent] = append(dep[parent], child)
		}
	}
	return dep
}

func findChild(currentNode *tree, value string, dist int) (*tree, int) {
	if (*currentNode).value == value {
		return currentNode, dist
	}

	currentDist := dist
	for _, node := range (*currentNode).children {
		result, newDist := findChild(node, value, currentDist+1)
		if result != nil {
			return result, newDist
		}
	}

	return nil, 0
}

func nodeDistance(A *tree, B *tree, dist int) int {
	node, childDist := findChild(A, (*B).value, 0)
	if node != nil {
		return dist + childDist
	}

	if (*A).parent != nil {
		return nodeDistance((*A).parent, B, dist+1)
	}

	return -1
}
