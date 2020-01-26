class Square:

    def __init__(self, edge):
        self.edge = edge

    def calculate_area(self):
        area = self.edge ** 2
        return area

    def calculate_circuit(self):
        circuit = 4 * self.edge
        return circuit


square_1 = Square(5)
print(square_1.calculate_area())
