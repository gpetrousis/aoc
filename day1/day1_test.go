package main

import "testing"

func TestCalculateConsumption(t *testing.T) {
	cases := []struct {
		in, want int
	}{
		{12, 2},
		{14, 2},
		{1969, 654},
		{100756, 33583},
	}
	for _, c := range cases {
		got := calculateConsumption(c.in)
		if got != c.want {
			t.Errorf("calculateFuelConsumption(%d) == %d, want %d", c.in, got, c.want)
		}
	}
}

func TestCalculateConsumptionWithExtra(t *testing.T) {
	cases := []struct {
		in, want int
	}{
		{14, 2},
		{1969, 966},
		{100756, 50346},
	}
	for _, c := range cases {
		got := calculateConsumptionWithExtra(c.in)
		if got != c.want {
			t.Errorf("calculateExtraFuelConsumption(%d) == %d, want %d", c.in, got, c.want)
		}
	}
}
