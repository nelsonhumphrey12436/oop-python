class Smartphone:
    def __init__(self, brand, model, battery_percentage, storage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        self.storage = storage
    
    def make_call(self, phone_number):
        return f"Calling {phone_number}..."
    
    def check_battery(self):
        return f"Battery is at {self.battery_percentage}%"
    
    def check_storage(self):
        return f"Storage used: {self.storage}GB"
    
    def charge_phone(self):
        self.battery_percentage = 100
        return "Phone is fully charged!"

# Inherited Class: Smartphone with Camera (extends Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_percentage, storage, camera_quality):
        super().__init__(brand, model, battery_percentage, storage)
        self.camera_quality = camera_quality
    
    def take_photo(self):
        return f"Taking a photo with {self.camera_quality} quality camera!"
    
    def check_battery(self):
        return f"Battery status: {self.battery_percentage}%. Charge your phone!"

# Creating Objects
phone1 = Smartphone("Apple", "iPhone 13", 65, 128)
phone2 = SmartphoneWithCamera("Samsung", "Galaxy S21", 85, 256, "108MP")

# Example methods
print(phone1.make_call("555-1234"))
print(phone2.take_photo())
print(phone1.check_battery())
print(phone2.check_storage())
print(phone2.charge_phone())