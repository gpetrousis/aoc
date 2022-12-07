package days_test

import (
	"testing"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
)

func TestDay2Part1(t *testing.T) {
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
					"A Y",
					"B X",
					"C Z",
				},
			},
			want: 15,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day2Part1(testCase.args.data); got != testCase.want {
				t.Errorf("Day2Part1() = %v, want %v", got, testCase.want)
			}
		})
	}
}

func TestDay2Part2(t *testing.T) {
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
					"A Y",
					"B X",
					"C Z",
				},
			},
			want: 12,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day2Part2(testCase.args.data); got != testCase.want {
				t.Errorf("Day2Part2() = %v, want %v", got, testCase.want)
			}
		})
	}
}
