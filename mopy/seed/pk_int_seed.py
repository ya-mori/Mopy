from mopy.seed.seed import Seed


class PkIntSeed(Seed):

    def __init__(self):
        self.counter = 0
        super().__init__()

    def generate(self):
        self.counter += 1
        return self.counter

    def to_str(self, value):
        return str(value)


if __name__ == "__main__":
    pass
