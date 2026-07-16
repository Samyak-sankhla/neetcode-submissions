class MyHashMap:
    def __init__(self):
        self.data = [None] * 1000001
    def put(self, key: int, val: int) -> None:
        self.data[key] = val
    def get(self, key: int) -> int:
        return self.data[key] if self.data[key] != None else -1
    def remove(self, key: int) -> None:
        self.data[key] = None