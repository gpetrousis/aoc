package days

import (
	"testing"
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
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Day1Part1(tt.args.data); got != tt.want {
				t.Errorf("Day1Part1() = %v, want %v", got, tt.want)
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
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Day1Part2(tt.args.data); got != tt.want {
				t.Errorf("Day1Part2() = %v, want %v", got, tt.want)
			}
		})
	}
}
