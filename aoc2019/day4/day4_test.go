package main

import "testing"

func TestGetFirstPossiblePasswork(t *testing.T) {
	cases := []struct {
		in   string
		want int
	}{
		{"12", 12},
		{"649", 666},
		{"1969", 1999},
		{"100756", 111111},
	}
	for _, c := range cases {
		got := getFirstPossiblePasswork(c.in)
		if got != c.want {
			t.Errorf("getFirstPossiblePasswork(%s) == %d, want %d", c.in, got, c.want)
		}
	}
}

func TestGetLastPossiblePasswork(t *testing.T) {
	cases := []struct {
		in   string
		want int
	}{
		{"12", 12},
		{"649", 599},
		{"1969", 1899},
		{"100756", 99999},
	}
	for _, c := range cases {
		got := getLastPossiblePasswork(c.in)
		if got != c.want {
			t.Errorf("getLastPossiblePasswork(%s) == %d, want %d", c.in, got, c.want)
		}
	}
}
