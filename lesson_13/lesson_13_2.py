class String(str):
    def __add__(self, other):
        return super().__add__(str(other))

    def __sub__(self, other):
        return self.replace(other, "", 1)
