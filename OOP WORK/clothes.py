class Clothes:
    # Constructor to initialize attributes
    def __init__(self, type_of_cloth, size, color):
        self.type_of_cloth = type_of_cloth  # (e.g., Shirt, Pants)
        self.size = size  # (e.g., S, M, L)
        self.color = color  # (e.g., Red, Blue)

    # Method to display cloth details
    def display_details(self):
        print("Type:", self.type_of_cloth)
        print("Size:", self.size)
        print("Color:", self.color)

    # Method to update the size of the cloth
    def update_size(self, new_size):
        self.size = new_size

    # Method to change the color of the cloth
    def change_color(self, new_color):
        self.color = new_color
