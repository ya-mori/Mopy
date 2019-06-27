import random
from seed.seed import Seed

class EnumSeed(Seed):

    def __init__(self, values):
        self.values = values
        super().__init__()

    def generate(self):
        return random.choice(self.values)

if __name__ == "__main__":
    pass