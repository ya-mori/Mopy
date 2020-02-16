import random

from mopy.seed.seed import Seed


class EnumSeed(Seed):

    def __init__(self, values):
        self.values = values
        super().__init__()

    def generate(self):
        return random.choice(self.values)

    def to_str(self, value):
        return f"'{value}'"
