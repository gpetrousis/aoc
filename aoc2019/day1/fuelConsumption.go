package main

func calculateConsumption(mass int) int {
	return mass / 3 - 2
}

func calculateExtraConsumptionTail(mass int, total int) int {
	extra := calculateConsumption(mass)
	if extra > 0 {
		return calculateExtraConsumptionTail(extra, total+extra)
	}
	return total
}

func calculateExtraConsumption(mass int) int {
	return calculateExtraConsumptionTail(mass, 0)
}

func calculateConsumptionWithExtra(mass int) int {
	consumption := calculateConsumption(mass)
	extraConsumption := calculateExtraConsumption(consumption)
	return consumption + extraConsumption
}