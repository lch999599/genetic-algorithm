from ga import generate_chromosomes
from ga import Config

a = generate_chromosomes()
for i in a:
    print(Config.OBJ_FUN(*i))