class HashMap:
    def __init__(self, capacity=8, load_factor=0.75):
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0
        self.load_factor = load_factor

    def index(self, key):
        return (hash(key) & 0x7FFFFFFF) % len(self.buckets)

    def resize(self):
        if self.size / len(self.buckets) > self.load_factor:
            old_buckets = self.buckets
            self.buckets = [[] for _ in range(len(old_buckets) * 2)]
            for bucket in old_buckets:
                for k, v in bucket:
                    idx = self.index(k)
                    self.buckets[idx].append((k, v))

    def put(self, key, value):
        idx = self.index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        self.resize()

    def get(self, key):
        idx = self.index(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        idx = self.index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def keys(self):
        for bucket in self.buckets:
            for k, _ in bucket:
                yield k

    def values(self):
        for bucket in self.buckets:
            for _, v in bucket:
                yield v

    def items(self):
        for bucket in self.buckets:
            for kv in bucket:
                yield kv
