class Fruits:
    # Constructor to initialize attributes
    def __init__(self, name, color, taste):
        self.name = name  #(e.g., Apple, Banana)
        self.color = color  #(e.g., Red, Yellow)
        self.taste = taste  # (e.g., Sweet, Sour)

    # Method to display fruit details
    def display_details(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Taste:", self.taste)

    # Method to change the color of the fruit
    def change_color(self, new_color):
        self.color = new_color

    # Method to update the taste of the fruit
    def update_taste(self, new_taste):
        self.taste = new_taste
