package days_test

import (
	"testing"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
)

func TestDay4Part1(t *testing.T) {
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
					"2-4,6-8",
					"2-3,4-5",
					"5-7,7-9",
					"2-8,3-7",
					"6-6,4-6",
					"2-6,4-8",
				},
			},
			want: 2,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day4Part1(testCase.args.data); got != testCase.want {
				t.Errorf("Day4Part1() = %v, want %v", got, testCase.want)
			}
		})
	}
}

func TestDay4Part2(t *testing.T) {
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
					"2-4,6-8",
					"2-3,4-5",
					"5-7,7-9",
					"2-8,3-7",
					"6-6,4-6",
					"2-6,4-8",
				},
			},
			want: 4,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day4Part2(testCase.args.data); got != testCase.want {
				t.Errorf("Day4Part2() = %v, want %v", got, testCase.want)
			}
		})
	}
}
