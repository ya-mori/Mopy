import random
from seed.seed import Seed

class RandBoolSeed(Seed):

    def __init__(self):
        super().__init__()

    def generate(self):
        bite = random.randint(0, 1)
        if bite == 0 :
            return True
        else:
            return False
             


if __name__ == "__main__":
    pass