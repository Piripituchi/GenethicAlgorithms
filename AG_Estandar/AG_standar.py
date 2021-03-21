##```python
import random

def generateCromosoma(len_cromosoma):
    cromosoma=[]
    for alelo in range(len_cromosoma):
        aux=random.random()
        if aux>0.5:
            cromosoma.append(1)
        else:
            cromosoma.append(0)
    return cromosoma

def generateGeneration(len_poblation,len_cromosoma):
    poblation=[]
    for cromosoma in range(len_poblation):
        cromosoma=generateCromosoma(len_cromosoma)
        poblation.append(cromosoma)
        cromosoma.clear
    return poblation

first_gen_len=4
len_cromosoma=4

first_gen=generateGeneration(first_gen_len,len_cromosoma)
print(first_gen)

##```
