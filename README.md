## A Genetic Algorithm Implementation in Python

#### Implementation of genetic algorithm to solve an equation of degree `1`

##### *Objective Function*
```
We need to solve the equation, a + 2b + 3c + 4d = 30
Therefore our objective function is f(x) = a + 2b + 3c + 4d - 30
```

#### Steps for performing Genetic Algorithm

1. **Initialize the population**
Every chromosome is a potential solution to the above problem. So each chromosome should contain 4 variables, representing `a`, `b`, `c` and `d` respectievely.

Let's generate a population of chromosomes. The values of each variable is generated randomly.

```
Chromosome [1] = a b c d ] = [12;05;23;08]
Chromosome [2] = a b c d ] = [02;21;18;03]
Chromosome [3] = a b c d ] = [10;04;13;14]
Chromosome [4] = a b c d ] = [20;01;10;06]
Chromosome [5] = a b c d ] = [01;04;13;19]
Chromosome [6] = a b c d ] = [20;05;17;01]
```

Here we have randomly initialized 6 chromosomes
2. **Evaluation**
