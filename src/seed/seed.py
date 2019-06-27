from abc import ABCMeta, abstractmethod

class Seed(metaclass=ABCMeta):
    """
    シードです。
    内部でキャッシュの機構を持たせることによって、インデックスによる、データの冪等性を保証しています。
    """

    def __init__(self):
        self.cache = dict()
    
    def __call__(self, index):
        return self.get(index)

    def get(self, index):
        """
        値を取得します
        """
        value = self.cache.get(index)
        if value is None:
            generated = self.generate()
            self._save(index=index, value=generated)
            return generated
        else:
            return value

    @abstractmethod
    def generate(self):
        """
        値を新たに生成します
        """
        pass

    def toStr(self, ):
        return str()

    def _save(self, index, value):
        """
        値をキャッシュに保存します
        """
        self.cache[index] = value
