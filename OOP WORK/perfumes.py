class Perfumes:
    # Constructor to initialize attributes
    def __init__(self, brand, scent, volume):
        self.brand = brand  #(e.g., Chanel, Dior)
        self.scent = scent  # (e.g., Floral, Citrus)
        self.volume = volume  # (e.g., 50ml, 100ml)

    # Method to display perfume details
    def display_details(self):
        print("Brand:", self.brand)
        print("Scent:", self.scent)
        print("Volume:", self.volume)

    # Method to change the scent of the perfume
    def change_scent(self, new_scent):
        self.scent = new_scent

    # Method to update the volume of the perfume
    def update_volume(self, new_volume):
        self.volume = new_volume
