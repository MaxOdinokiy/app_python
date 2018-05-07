import os


class DirDict:
    def __init__(self, way_to_dir):
        if not os.path.exists(way_to_dir):
            os.mkdir(way_to_dir)
        self.way_to_dir = way_to_dir
        self.keys = []

    def __getitem__(self, key):
        if str(key) in self.keys:
            with open (self.way_to_dir + str(key), "r") as f:
                return f.read()

    def __setitem__(self, key, value):
        if str(key) not in self.keys:
            self.keys.append(str(key))
        with open(self.way_to_dir + str(key), "w") as f:
            f.write(str(value))

    def __delitem__(self, key):
        if str(key) in self.keys:
            os.remove(self.way_to_dir + str(key))
            for i, v in enumerate(self.keys):
                if str(key) == v:
                    del self.keys[i]
                    break
            return
        else:
            raise KeyError
    def __iter__(self):
        for i in self.keys:
            yield i

    def __len__(self):
        return len(self.keys)


X = DirDict('./dir-dict/')

X[777] = 1

print(X[777])

X[4566] = 34566
print(X[4566])
X["file"] = "'irtht"

del X[777]
