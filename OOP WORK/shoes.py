class Shoes:
    # Constructor to initialize attributes
    def __init__(self, size, color, brand):
        self.size = size  #(e.g., 8, 9, 10)
        self.color = color  #(e.g., Black, White)
        self.brand = brand  # (e.g., Nike, Adidas)

    # Method to display shoe details
    def display_details(self):
        print("Size:", self.size)
        print("Color:", self.color)
        print("Brand:", self.brand)

    # Method to change the size of the shoes
    def change_size(self, new_size):
        self.size = new_size

    # Method to update the color of the shoes
    def update_color(self, new_color):
        self.color = new_color
