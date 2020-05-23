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
Now we evaluate the chromosomes based on the objective function and their fitness values (*`fitness = 1 / obj_fn`*)

```
F_obj [1] = 93
F_obj [2] = 80
F_obj [3] = 83
F_obj [4] = 46
F_obj [5] = 94
F_obj [6] = 55
```

And the fitness values are

```
Fitness [1] = 0.0106
Fitness [2] = 0.0123
Fitness [3] = 0.0119
Fitness [4] = 0.0213
Fitness [5] = 0.0105
Fitness [6] = 0.0179
```

3. **Selection**
Here we perform Tournament based selection strategy. There will a `n` tournaments (`n=total_population`). In each tournament, we randomly select 2 or more candidates. Then we select the candidate with highest fitness value. When the tournament ends, we get a new population of 6 members, that may or may not contain repeated elements.

```
New_Chromosome [1] = a b c d ] = [20;05;17;01]
New_Chromosome [2] = a b c d ] = [02;21;18;03]
New_Chromosome [3] = a b c d ] = [20;01;10;06]
New_Chromosome [4] = a b c d ] = [20;01;10;06]
New_Chromosome [5] = a b c d ] = [01;04;13;19]
New_Chromosome [6] = a b c d ] = [12;05;23;08]
```

Let's say this is our new population

4. **Cross Over**