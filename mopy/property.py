from mopy.seed.seed import Seed


class Property(dict):
    """
    プロパティです。
    """

    def __setitem__(self, name, seed):
        if not isinstance(name, str):
            raise ValueError("name must be str.")
        if not isinstance(seed, Seed):
            raise ValueError("seed must be Seed.")
        super().__setitem__(name, seed)
