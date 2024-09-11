class Vaseline:
    # Constructor to initialize attributes
    def __init__(self, size, scent, usage):
        self.size = size  #(e.g., Small, Medium, Large)
        self.scent = scent  #(e.g., Aloe, Cocoa Butter)
        self.usage = usage  #(e.g., Moisturizing, Healing)

    # Method to display Vaseline details
    def display_details(self):
        print("Size:", self.size)
        print("Scent:", self.scent)
        print("Usage:", self.usage)

    # Method to change the scent of the Vaseline
    def change_scent(self, new_scent):
        self.scent = new_scent

    # Method to update the usage description of the Vaseline
    def update_usage(self, new_usage):
        self.usage = new_usage
