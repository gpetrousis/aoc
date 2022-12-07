package days_test

import (
	"testing"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
)

func TestDay3Part1(t *testing.T) {
	type args struct {
		data []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Test Input",
			args: args{
				data: []string{
					"vJrwpWtwJgWrhcsFMMfFFhFp",
					"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
					"PmmdzqPrVvPwwTWBwg",
					"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
					"ttgJtRGJQctTZtZT",
					"CrZsJsPPZsGzwwsLwLmpwMDw",
				},
			},
			want: 157,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day3Part1(testCase.args.data); got != testCase.want {
				t.Errorf("Day3Part1() = %v, want %v", got, testCase.want)
			}
		})
	}
}

func TestDay3Part2(t *testing.T) {
	type args struct {
		data []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Test Input",
			args: args{
				data: []string{
					"vJrwpWtwJgWrhcsFMMfFFhFp",
					"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
					"PmmdzqPrVvPwwTWBwg",
					"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
					"ttgJtRGJQctTZtZT",
					"CrZsJsPPZsGzwwsLwLmpwMDw",
				},
			},
			want: 70,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day3Part2(testCase.args.data); got != testCase.want {
				t.Errorf("Day3Part2() = %v, want %v", got, testCase.want)
			}
		})
	}
}
