from utils import *
import random
from copy import deepcopy

class PizzaProblem:
    def __init__(self):
        self.clientChoiceArray = getClientsChoice('ip.txt')
        self.itemList = getAllItems(parseInput('ip.txt'))
        self.gen_cnt = 100
        self.populationSize = 50
        self.presentGeneration = []
        self.geneSize = len(self.clientChoiceArray[0])
        self.generationGone = 0


    def fitness_func(self,gene):
        ans = 0

        for i in self.clientChoiceArray:

            brokeInMiddleOfLoop = False

            if len(i) != len(gene) : print(f'{self.generationGone} is gen_cnt')

            for j in range(len(i)):
                if(i[j] == -1):
                    continue

                if(i[j] == gene[j]):
                    continue
                
                if(i[j] != gene[j]):
                    brokeInMiddleOfLoop = True
                    break
            
            if brokeInMiddleOfLoop:
                ans += 1
            
        return ans


    def generate_first_gen(self):
        for i in range(self.populationSize):
            self.presentGeneration.append([random.randint(0,1) for i in range(self.geneSize)])


    def getBestfromPresentGeneration(self,cnt):
        tempListForFitnessScores = []
        for i in self.presentGeneration:
            tempListForFitnessScores.append([self.fitness_func(i),i])
        tempListForFitnessScores.sort()

        ans = []
        for i in range(cnt):
            ans.append(tempListForFitnessScores[i][1])

        return ans


    def crossOverFunction(self,gene1,gene2):
        crossingIndex = len(gene1) // 2
        child1 = gene1[:crossingIndex] + gene2[crossingIndex:]
        child2 = gene1[crossingIndex:] + gene2[:crossingIndex]

        return [child1,child2]


    def mutate(self,gene):
        idx = random.randint(0,len(gene) - 1)
        if gene[idx] == 1: 
            gene[idx] = 0 
        else: 
            gene[idx] = 1 
        return gene


    def evolve(self):
        # Generating the Initial Population
        self.generate_first_gen()

        for i in range(self.gen_cnt):
            nextGen = []

            # Elitism
            twoBestGenes = self.getBestfromPresentGeneration(2)
            nextGen.append(twoBestGenes[0])
            nextGen.append(twoBestGenes[1])

            # Single Point Crossover
            childrenFromBestParents = self.crossOverFunction(twoBestGenes[0],twoBestGenes[1])
            nextGen.append(childrenFromBestParents[0])
            nextGen.append(childrenFromBestParents[1])


            # Random crossover to make the population for the next generation
            fitnessArray = [self.fitness_func(i) for i in self.presentGeneration]
            while(len(nextGen) != self.populationSize):
                twoRandomParents = random.choices(self.presentGeneration,fitnessArray,k = 2)
                childrenFromRandomParents = self.crossOverFunction(twoRandomParents[0],twoRandomParents[1])
                nextGen.append(childrenFromRandomParents[0])
                nextGen.append(childrenFromRandomParents[1])

            # Mutate some genes from the whole nextGen Array
            for i in range(len(nextGen)):
                n = random.randint(1,100)
                if(n >=5):
                    continue
                else:
                    nextGen[i] = self.mutate(nextGen[i])
            

            # Replacing the Prev Generation with the Newly Created Generation
            self.presentGeneration = deepcopy(nextGen)
            self.generationGone +=1


        # Now getting the Best from Final Generation
        self.answer = self.getBestfromPresentGeneration(1)[0]


    def printAnswer(self):
        items = []
        for i in range(len(self.itemList)):
            if(self.answer[i]):
                items.append(self.itemList[i])
            else:
                continue
        
        print(items)
        opString = str(len(items)) + ' ' +' '.join(items) + '\n'

        with open('op.txt','w') as fp:
            fp.write(opString)


if __name__ == '__main__':
    p1 = PizzaProblem()
    p1.evolve()
    p1.printAnswer()
