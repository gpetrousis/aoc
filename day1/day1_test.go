package main

import "testing"

func TestCalculateFuelConsumption(t *testing.T) {
	cases := []struct {
		in, want int
	}{
		{12, 2},
		{14, 2},
		{1969, 654},
		{100756, 33583},
	}
	for _, c := range cases {
		got := calculateFuelConsumption(c.in)
		if got != c.want {
			t.Errorf("calculateFuelConsumption(%d) == %d, want %d", c.in, got, c.want)
		}
	}
}

func TestCalculateTotalFuelConsumption(t *testing.T) {
	cases := []struct {
		in   []string
		want int
	}{
		{[]string{"12", "14", "1969", "100756"}, 34241},
	}
	for _, c := range cases {
		got := calculateTotalFuelConsumption(c.in)
		if got != c.want {
			t.Errorf("calculateTotalFuelConsumption(%v) == %d, want %d", c.in, got, c.want)
		}
	}
}
