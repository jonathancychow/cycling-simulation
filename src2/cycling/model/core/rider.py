class Rider:
    def __init__(self, name, mass, cda, cp=380, w_prime=19800):
        self.name = name
        self.mass = mass
        self.cda = cda
        self.cp = cp
        self.w_prime = w_prime

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'
