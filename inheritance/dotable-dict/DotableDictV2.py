# class DotableDict(dict):
#     def __getitem__(self, keys):
#         keys = keys.split(".", 1)
#         first_key = keys[0]
#         temp = self.get(first_key)

#         if len(keys) == 1:
#             return temp
#         rest_keys = keys[1]
#         if type(temp) == int:
#             raise KeyError(f"\"{first_key}\" does not have \"{rest_keys}\"")

#         return DotableDict.__getitem__(temp, rest_keys)


class DotableDict(dict):
    def __getitem__(self, keys):
        keys = keys.split(".", 1)
        temp = self.get(keys[0])

        if len(keys) == 1:
            return temp

        return DotableDict.__getitem__(temp, keys[1])


dd = DotableDict({"a" : 1, "b" : {"c" : 3}, "d" : {"f" : {"g" : 5}}})

# expected results

print(dd["a"])
assert dd["a"] == 1

print(dd["b"])
assert dd["b"] == {"c" : 3}

print(dd["b.c"])
assert dd["b.c"] == 3
assert dd["b.c"] == dd["b"]["c"]

print(dd["d.f.g"])
assert dd["d.f.g"] == 5

print(dd["b.c.a"])