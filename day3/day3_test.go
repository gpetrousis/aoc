package main

import (
	"testing"
)

// func TestManhatan(t *testing.T) {
// 	cases := []struct {
// 		ax   int
// 		ay   int
// 		bx   int
// 		by   int
// 		want int
// 	}{
// 		{1, 4, 6, 7, 8},
// 		{-1, 4, -6, 7, 8},
// 	}

// 	for _, c := range cases {
// 		got := manhatan(c.ax, c.ay, c.bx, c.by)
// 		if got != c.want {
// 			t.Errorf("manhatan(%d, %d, %d, %d) == %d want %d", c.ax, c.ay, c.bx, c.by, got, c.want)
// 		}
// 	}
// }

func TestParseStep(t *testing.T) {
	cases := []struct {
		step      string
		direction string
		steps     int
	}{
		{"R75", "R", 75},
		{"U1", "U", 1},
	}

	for _, c := range cases {
		gotDir, gotSteps := parseStep(c.step)
		if gotDir != c.direction || gotSteps != c.steps {
			t.Errorf("parseInput(%s) == %s, %d want %s, %d", c.step, gotDir, gotSteps, c.direction, c.steps)
		}
	}
}

// func TestIntersection(t *testing.T) {
// 	cases := []struct {
// 		in1  string
// 		in2  string
// 		want int
// 	}{
// 		{"R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159},
// 		{"R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 135},
// 	}

// 	for _, c := range cases {
// 		if got != c.want {
// 			t.Errorf("Intersection for wires (%s) and (%s) == %d, want %d", c.in1, c.in2, got, c.want)
// 		}
// 	}

// }
