package days_test

import (
	"testing"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
)

func TestDay6Part1(t *testing.T) {
	type args struct {
		data string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Test Input 1",
			args: args{
				data: "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
			},
			want: 7,
		},
		{
			name: "Test Input 2",
			args: args{
				data: "bvwbjplbgvbhsrlpgdmjqwftvncz",
			},
			want: 5,
		},
		{
			name: "Test Input 3",
			args: args{
				data: "nppdvjthqldpwncqszvftbrmjlhg",
			},
			want: 6,
		},
		{
			name: "Test Input 4",
			args: args{
				data: "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
			},
			want: 10,
		},
		{
			name: "Test Input 5",
			args: args{
				data: "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
			},
			want: 11,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day6Part1(testCase.args.data); got != testCase.want {
				t.Errorf("Day6Part1() = %v, want %v", got, testCase.want)
			}
		})
	}
}

func TestDay6Part2(t *testing.T) {
	type args struct {
		data string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Test Input 1",
			args: args{
				data: "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
			},
			want: 19,
		},
		{
			name: "Test Input 2",
			args: args{
				data: "bvwbjplbgvbhsrlpgdmjqwftvncz",
			},
			want: 23,
		},
		{
			name: "Test Input 3",
			args: args{
				data: "nppdvjthqldpwncqszvftbrmjlhg",
			},
			want: 23,
		},
		{
			name: "Test Input 4",
			args: args{
				data: "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
			},
			want: 29,
		},
		{
			name: "Test Input 5",
			args: args{
				data: "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
			},
			want: 26,
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day6Part2(testCase.args.data); got != testCase.want {
				t.Errorf("Day6Part2() = %v, want %v", got, testCase.want)
			}
		})
	}
}
