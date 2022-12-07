package days_test

import (
	"testing"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
)

func TestDay5Part1(t *testing.T) {
	type args struct {
		data []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "Test Input",
			args: args{
				data: []string{
					"    [D]    ",
					"[N] [C]    ",
					"[Z] [M] [P]",
					" 1   2   3 ",
					"",
					"move 1 from 2 to 1",
					"move 3 from 1 to 3",
					"move 2 from 2 to 1",
					"move 1 from 1 to 2",
				},
			},
			want: "CMZ",
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day5Part1(testCase.args.data); got != testCase.want {
				t.Errorf("Day5Part1() = %v, want %v", got, testCase.want)
			}
		})
	}
}

func TestDay5Part2(t *testing.T) {
	type args struct {
		data []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "Test Input",
			args: args{
				data: []string{
					"    [D]    ",
					"[N] [C]    ",
					"[Z] [M] [P]",
					" 1   2   3 ",
					"",
					"move 1 from 2 to 1",
					"move 3 from 1 to 3",
					"move 2 from 2 to 1",
					"move 1 from 1 to 2",
				},
			},
			want: "MCD",
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day5Part2(testCase.args.data); got != testCase.want {
				t.Errorf("Day5Part2() = %v, want %v", got, testCase.want)
			}
		})
	}
}
