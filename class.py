class car():
    def __init__(self, type, color):
        self.type = type
        self.color = color
        self.return_value = ''
        if self.color == 'black':
            self.print_color()

        else:
            self.return_value = None
    def print_color(self):
        print(self.color)

