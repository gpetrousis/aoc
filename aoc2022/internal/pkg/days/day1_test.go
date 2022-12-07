package days_test

import (
	"testing"

	"github.com/gpetrousis/aoc/aoc2022/internal/pkg/days"
)

func TestDay1Part1(t *testing.T) {
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
					"1000",
					"2000",
					"3000",
					"",
					"4000",
					"",
					"5000",
					"6000",
					"",
					"7000",
					"8000",
					"9000",
					"",
					"10000",
				},
			},
			want: "24000",
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day1Part1(testCase.args.data); got != testCase.want {
				t.Errorf("Day1Part1() = %v, want %v", got, testCase.want)
			}
		})
	}
}

func TestDay1Part2(t *testing.T) {
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
					"1000",
					"2000",
					"3000",
					"",
					"4000",
					"",
					"5000",
					"6000",
					"",
					"7000",
					"8000",
					"9000",
					"",
					"10000",
				},
			},
			want: "45000",
		},
	}
	for _, tt := range tests {
		testCase := tt
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()
			if got := days.Day1Part2(testCase.args.data); got != testCase.want {
				t.Errorf("Day1Part2() = %v, want %v", got, testCase.want)
			}
		})
	}
}
