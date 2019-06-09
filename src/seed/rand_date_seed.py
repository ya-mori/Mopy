import datetime
import random
from seed.seed import Seed

class RandDateSeed(Seed):

    def __init__(self, format=None):
        self.format = format
        super().__init__()

    def generate(self):
        year = random.randint(1900, 2100)
        month = random.randint(1, 12)
        day = random.randint(1, 31)

        if self.format is None:
            return datetime.date(year, month, day) 
        else:
            return datetime.date(year, month, day).strftime(self.format)


if __name__ == "__main__":
    pass