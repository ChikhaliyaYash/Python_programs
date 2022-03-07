import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# random_side = random.randint(0, 1)
if test_seed == 1:
    print("Heads")
else:
    print("Tails")

# second method of this programme
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")