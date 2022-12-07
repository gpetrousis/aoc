package days

import (
	"fmt"
	"regexp"
	"strconv"
)

type crates struct {
	stacks [][]rune
}

func (c *crates) Size() int {
	return len(c.stacks)
}

func (c *crates) AddStack() {
	c.stacks = append(c.stacks, []rune{})
}

func (c *crates) AddBack(pos int, crate rune) {
	c.stacks[pos] = append([]rune{crate}, c.stacks[pos]...)
}

func (c *crates) Move(qty, from, to int) {
	lenFrom := len(c.stacks[from])
	toMove := c.stacks[from][lenFrom-qty:]

	c.stacks[from] = c.stacks[from][:lenFrom-qty]
	for i := len(toMove) - 1; i >= 0; i-- {
		c.stacks[to] = append(c.stacks[to], toMove[i])
	}
}

func (c *crates) MoveMultiple(qty, from, to int) {
	lenFrom := len(c.stacks[from])
	toMove := c.stacks[from][lenFrom-qty:]

	c.stacks[from] = c.stacks[from][:lenFrom-qty]
	c.stacks[to] = append(c.stacks[to], toMove...)
}

func (c *crates) Top() string {
	top := ""
	for _, stack := range c.stacks {
		top = top + string(stack[len(stack)-1])
	}
	return top
}

func (c *crates) Print() {
	output := ""
	stacksLine := ""

	for i := 0; i < len(c.stacks); i++ {
		stacksLine = stacksLine + " " + strconv.Itoa(i+1) + "  "
	}

	hasMore := true
	j := 0
	for hasMore {
		lineOutput := ""
		hasMore = false
		for _, stack := range c.stacks {
			if j >= len(stack) {
				lineOutput = lineOutput + "    "
				continue
			}

			lineOutput = lineOutput + "[" + string(stack[j]) + "] "
			hasMore = true
		}

		output = lineOutput + "\n" + output
		j++
	}

	output = output + stacksLine

	fmt.Println(output)
}

func parseInputStacks(data []string) (*crates, []string) {
	moves := []string{}
	c := &crates{}

	for i, line := range data {
		if line == "" {
			moves = append(moves, data[i+1:]...)
			break
		}

		for j := 0; j < len(line); j++ {
			if line[j] == '[' {
				pos := j / 4
				for c.Size() <= pos {
					c.AddStack()
				}

				c.AddBack(pos, rune(line[j+1]))
				j = j + 2
			}
		}
	}

	return c, moves
}

func parseMove(move string) (int, int, int) {
	r := regexp.MustCompile(`move (\d*) from (\d*) to (\d*)`)
	result := r.FindStringSubmatch(move)

	qty, _ := strconv.Atoi(result[1])
	from, _ := strconv.Atoi(result[2])
	to, _ := strconv.Atoi(result[3])

	return qty, from - 1, to - 1
}

func Day5Part1(data []string) string {
	c, moves := parseInputStacks(data)

	for _, move := range moves {
		qty, from, to := parseMove(move)

		c.Move(qty, from, to)
	}

	return c.Top()
}

func Day5Part2(data []string) string {
	c, moves := parseInputStacks(data)

	for _, move := range moves {
		qty, from, to := parseMove(move)

		c.MoveMultiple(qty, from, to)
	}

	return c.Top()
}
