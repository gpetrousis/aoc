package readfile

import (
	"os"
	"fmt"
	"bufio"
)

func ReadFile(input string) ([]string, error) {
	file, err := os.Open(input)
	if err != nil {
        fmt.Println("File reading error", err)
        return nil, err 
	}
	defer file.Close()
	var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}