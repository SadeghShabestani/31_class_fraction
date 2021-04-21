class Fraction:
    def __init__(self):
        self.s1 = int(input("Enter S1: "))
        self.m1 = int(input("Enter m1: "))
        self.s2 = int(input("Enter S2: "))
        self.m2 = int(input("Enter m2: "))

    def sum(self):
        return f"Fraction Sum: {(self.s1 * self.m2) + (self.s2 * self.m1)} / {self.m1 * self.m2} "

    def show_sum(self):
        print(self.sum())

    def multi(self):
        return f"Fraction Multiplication: {(self.s1 * self.s2)} / {self.m1 * self.m2} "

    def show_multi(self):
        print(self.multi())

    def minus(self):
        m = self.m1 * self.m2
        return f"Fraction Minus: {(m // self.m1) * self.s1 - (m // self.m2) * self.s2} / {m} "

    def show_minus(self):
        print(self.minus())

    def divide(self):
        return f"Fraction Divide: {self.s1 * self.m2} / {self.s2 * self.m1} "

    def show_divide(self):
        print(self.divide())


res = Fraction()

res.show_sum()

res.show_multi()

res.show_minus()

res.show_divide()
