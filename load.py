class load:
    def __inti__(self, name, bus1, p, q, g):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.q = q
        self.g = g

    @classmethod
    def calc_g(self):
        self.g = self.q / self.p
