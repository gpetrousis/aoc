package main

import (
	"reflect"
	"testing"
)

func TestParseInput(t *testing.T) {
	cases := []struct {
		in   string
		want []int
	}{
		{"1,0,0,0,99", []int{1, 0, 0, 0, 99}},
		{"2,3,0,3,99", []int{2, 3, 0, 3, 99}},
		{"2,4,4,5,99,0", []int{2, 4, 4, 5, 99, 0}},
		{"1,1,1,4,99,5,6,0,99", []int{1, 1, 1, 4, 99, 5, 6, 0, 99}},
	}

	for _, c := range cases {
		var got []int = parseInput(c.in)
		if !reflect.DeepEqual(got, c.want) {
			t.Errorf("ParseInput(%s) == %v, want %v", c.in, got, c.want)
		}
	}

}

func TestIntcode(t *testing.T) {
	cases := []struct {
		in   string
		want []int
	}{
		{"1,0,0,0,99", []int{2, 0, 0, 0, 99}},
		{"2,3,0,3,99", []int{2, 3, 0, 6, 99}},
		{"2,4,4,5,99,0", []int{2, 4, 4, 5, 99, 9801}},
		{"1,1,1,4,99,5,6,0,99", []int{30, 1, 1, 4, 2, 5, 6, 0, 99}},
	}
	for _, c := range cases {
		array := parseInput(c.in)

		intcode(array, 0)
		if !reflect.DeepEqual(array, c.want) {
			t.Errorf("Intcode(%s) == %v, want %v", c.in, array, c.want)
		}
	}
}
