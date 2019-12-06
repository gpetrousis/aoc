package main

import (
	"reflect"
	"testing"
)

func TestParseOperator(t *testing.T) {
	cases := []struct {
		in       int
		wantCode int
		wantMode []int
	}{
		{12, 12, []int{0, 0, 0}},
		{1002, 2, []int{0, 1, 0}},
		{123, 23, []int{1, 0, 0}},
		{1234, 34, []int{2, 1, 0}},
		{12345, 45, []int{3, 2, 1}},
	}
	for _, c := range cases {
		gotCode, gotMode := parseOperator(c.in)
		if gotCode != c.wantCode || !reflect.DeepEqual(gotMode, c.wantMode) {
			t.Errorf("parseOperator(%d) == %d, %v, want %d, %v", c.in, gotCode, gotMode, c.wantCode, c.wantMode)
		}
	}
}
