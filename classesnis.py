class abc:
    x = 1
    def __init__(self, y):
        self.x = y

class mnl:
    z = 3
class xyz(abc, mnl):
    x = 2

    def __init__(self):
        super().__init__(10)


print(xyz.x)
a = xyz()
b = abc(3)
print(a.super().x)
print(a.x)
print(b.x)
a.x = 10
print(a.x)