from collections import UserDict


class Save(UserDict):

    def __setitem__(self, key, value):
        if key:
            self.data[key] = value

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]

    def __delitem__(self, key):
        del self.data[key]
