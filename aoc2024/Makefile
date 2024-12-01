.PHONY: init
init:
	go mod tidy

.PHONY: lint
lint:
	go vet ./...
	go fmt ./...
	golangci-lint run

.PHONY: test
test:
	go test -run=Test -race -covermode=atomic -coverprofile=coverage.out -count=3 ./...

.PHONY: build
build:
	echo "Building cli"
	CGO_ENABLED=1 go build -ldflags="-s -w" -o bin/aoc2022 cmd/aoc2022/main.go

.PHONY: clean
clean:
	rm -rf ./bin
	rm -rf ./coverage.out