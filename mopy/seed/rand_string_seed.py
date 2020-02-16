import random
import string

from mopy.seed.seed import Seed


class RandStrSeed(Seed):

    def __init__(self, size):
        self.size = size
        super().__init__()

    def generate(self):
        return ''.join(
            random.choices(string.ascii_letters + string.digits, k=self.size)
        )

    def to_str(self, value):
        return f"'{value}'"
