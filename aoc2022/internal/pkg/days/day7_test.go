package days_test

import (
	"testing"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
)

func TestDay7Part1(t *testing.T) {
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
					"$ cd /",
					"$ ls",
					"dir a",
					"14848514 b.txt",
					"8504156 c.dat",
					"dir d",
					"$ cd a",
					"$ ls",
					"dir e",
					"29116 f",
					"2557 g",
					"62596 h.lst",
					"$ cd e",
					"$ ls",
					"584 i",
					"$ cd ..",
					"$ cd ..",
					"$ cd d",
					"$ ls",
					"4060174 j",
					"8033020 d.log",
					"5626152 d.ext",
					"7214296 k",
				},
			},
			want: 95437,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day7Part1(testCase.args.data); got != testCase.want {
				t.Errorf("Day7Part1() = %v, want %v", got, testCase.want)
			}
		})
	}
}

func TestDay7Part2(t *testing.T) {
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
					"$ cd /",
					"$ ls",
					"dir a",
					"14848514 b.txt",
					"8504156 c.dat",
					"dir d",
					"$ cd a",
					"$ ls",
					"dir e",
					"29116 f",
					"2557 g",
					"62596 h.lst",
					"$ cd e",
					"$ ls",
					"584 i",
					"$ cd ..",
					"$ cd ..",
					"$ cd d",
					"$ ls",
					"4060174 j",
					"8033020 d.log",
					"5626152 d.ext",
					"7214296 k",
				},
			},
			want: 24933642,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day7Part2(testCase.args.data); got != testCase.want {
				t.Errorf("Day7Part2() = %v, want %v", got, testCase.want)
			}
		})
	}
}
