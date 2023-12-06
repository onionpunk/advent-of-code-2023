package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type SourceDestination struct {
	destination int
	source      int
	length      int
}

func (sd SourceDestination) GetDestination(value int) int {
	min := sd.source
	max := min + sd.length - 1
	if value >= min && value <= max {
		diff := value - min
		return (sd.destination + diff)
	}

	return -1
}

func setup() ([]int, [][]SourceDestination) {
	file, _ := os.ReadFile("./input.txt")

	content := string(file)
	noNewlines := strings.Replace(content, "\n\n", "\n", -1)
	lines := strings.Split(noNewlines, "\n")

	seeds := []int{}
	var dataMap []SourceDestination
	mapOfMaps := [][]SourceDestination{}

	for _, line := range lines {
		if strings.Contains(line, "seeds:") {
			seedsString := strings.Replace(line, "seeds: ", "", -1)
			seedsArray := strings.Split(seedsString, " ")
			for _, seed := range seedsArray {
				seedValue, _ := strconv.Atoi(seed)
				seeds = append(seeds, seedValue)
			}
		} else if strings.Contains(line, "map:") {
			if dataMap != nil {
				mapOfMaps = append(mapOfMaps, dataMap)
			}
			dataMap = []SourceDestination{}
		} else {
			data := strings.Split(line, " ")
			destination, _ := strconv.Atoi(data[0])
			source, _ := strconv.Atoi(data[1])
			length, _ := strconv.Atoi(data[2])
			dataMap = append(dataMap, SourceDestination{
				destination: destination,
				source:      source,
				length:      length,
			})
		}
	}

	mapOfMaps = append(mapOfMaps, dataMap)

	return seeds, mapOfMaps
}

func part1(seeds []int, dataset [][]SourceDestination) {
	lowestDestination := -1

	for index, seed := range seeds {
		currentValue := seed
		for _, sourceDestinations := range dataset {
			for _, sourceDestination := range sourceDestinations {
				destination := sourceDestination.GetDestination(currentValue)
				if destination >= 0 {
					currentValue = destination
					break
				}
			}
		}

		if index == 0 || currentValue < lowestDestination {
			lowestDestination = currentValue
		}
	}

	fmt.Println(lowestDestination)
}

func part2BruteForce(seeds []int, dataset [][]SourceDestination) {
	trueSeeds := []int{}
	startSeed := -1

	for index, seed := range seeds {
		if index%2 == 0 {
			startSeed = seed
		} else {
			for i := 0; i < seed; i++ {
				trueSeeds = append(trueSeeds, startSeed+i)
			}
		}
	}

	part1(trueSeeds, dataset)
}

func main() {
	setup()
	seeds, dataset := setup()

	part1(seeds, dataset)
	part2BruteForce(seeds, dataset)
}
