from random import randint
import random

# Daily Challenge


class Gene:
    def __init__(self, gene=0):
        self.gene = gene

    def mutate(self):
        self.gene = randint(0, 1)
        return self.gene


class Chromosome(Gene):
    def __init__(self, chrom_series=0):
        self.chrom_series = chrom_series
        self.chromosome = []

    def chrom_mutate(self):
        self.chromosome = [
            f'{self.mutate()}, {self.mutate()}, {self.mutate()}, {self.mutate()}, {self.mutate()}, {self.mutate()}, {self.mutate()}, {self.mutate()}, {self.mutate()}, {self.mutate()}']
        return(self.chromosome)


class Dna(Chromosome):
    def __init__(self, dna_series=0):
        self.dna_series = dna_series
        self.dna = []

    def dna_mutate(self):
        self.dna = [
            f'{self.chrom_mutate()},{self.chrom_mutate()}, {self.chrom_mutate()}, {self.chrom_mutate()}, {self.chrom_mutate()}, {self.chrom_mutate()}, {self.chrom_mutate()}, {self.chrom_mutate()}, {self.chrom_mutate()}, {self.chrom_mutate()}']
        return(self.dna)


ofir_genetics = Dna()
ofir_genetics_dna = ofir_genetics.dna_mutate()


class Organism():
    def __init__(self, dna_result, environment=0):
        self.dna_result = dna_result
        self.environment = environment

    def mutate_probability(self):
        generation = 0
        while self.environment == 0:
            if 0 in self.dna_result:
                generation += 1
                self.environment == 0
            else:
                self.environment == 1
            print(
                f'The numbet of generations it took to create a mutate is: {generation}')
            print(self.dna_result)


ofir_organism = Organism(ofir_genetics_dna)
ofir_organism.mutate_probability()
