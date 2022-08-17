import pandas as pd

ds = pd.DataFrame({"__str__" : [1, 2, 3], "b" : [6, 7, 8]})
print(ds.__str__)
print()
print(ds.b)
print()
print(ds["b"])

d = dict({"a" : 1, "b" : {"c" : 3}})
print(d["a"])
print(d.__getitem__("a"))


class DotableDict(dict):
    def __getattribute__(self, __name: str):
        if __name in super().keys():
            return super().__getitem__(__name)
        return super().__getattribute__(__name)


dd = DotableDict({"a" : 1, "b" : {"c" : 3}})

# # expected results

print(dd["a"])
print(dd.__getitem__("a"))
assert dd["a"] == 1

print(dd.a)
assert dd.a == 1
assert dd.a == dd["a"]

assert dd.b == {"c" : 3}

print(dd.__str__)
dd["__str__"] = 4
print(dd.__str__) # this

# assert dd.b.c == 3    # but this does not work.

dd2 = DotableDict({"a" : 1, "b" : DotableDict({"c" : 3})})

print(dd2.b.c)
assert dd2.b.c == 3    # but this does not work.