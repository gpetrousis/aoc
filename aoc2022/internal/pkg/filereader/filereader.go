package filereader

import (
	"io/ioutil"
	"strconv"
	"strings"
)

type filereader struct {
	data []string
}

func NewFileReader(inputFile string, delimieter string) *filereader {
	data, err := readFile(inputFile)
	if err != nil {
		panic(err)
	}

	dataArray := strings.Split(data, delimieter)
	fr := filereader{data: dataArray}

	return &fr
}

func (f filereader) ToIntArray() []int {
	intArray := []int{}

	for _, str := range f.data {
		intVal, err := strconv.Atoi(str)
		if err != nil {
			panic(err)
		}
		intArray = append(intArray, intVal)
	}

	return intArray
}

func (f filereader) ToStrArray() []string {
	return f.data
}

func readFile(inputFile string) (string, error) {
	data, err := ioutil.ReadFile(inputFile)
	if err != nil {
		return "", err
	}

	stringData := string(data)

	return stringData, nil
}
