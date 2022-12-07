package filereader

import (
	"os"
	"strconv"
	"strings"
)

type filereader struct {
	data string
}

func NewFileReader(inputFile string) *filereader {
	data, err := readFile(inputFile)
	if err != nil {
		panic(err)
	}

	fr := filereader{data: data}

	return &fr
}

func (f *filereader) GetData() string {
	return f.data
}

func (f *filereader) ToIntArray(delimieter rune) []int {
	intArray := []int{}

	for _, str := range f.data {
		if str == delimieter {
			continue
		}

		intVal, err := strconv.Atoi(string(str))
		if err != nil {
			panic(err)
		}
		intArray = append(intArray, intVal)
	}

	return intArray
}

func (f *filereader) ToStrArray(delimieter string) []string {
	dataArray := strings.Split(f.data, delimieter)
	return dataArray
}

func readFile(inputFile string) (string, error) {
	data, err := os.ReadFile(inputFile)
	if err != nil {
		return "", err
	}

	stringData := string(data)

	return stringData, nil
}
