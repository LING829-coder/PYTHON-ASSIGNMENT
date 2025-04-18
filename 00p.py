class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"

class SmartphonePro(Smartphone):
    def __init__(self, brand, model, price, camera_quality):
        super().__init__(brand, model, price)
        self.camera_quality = camera_quality

    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality}MP camera.")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Camera: {self.camera_quality}MP"

# Example usage
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Galaxy S21", 799)
    phone_pro = SmartphonePro("Apple", "iPhone 14 Pro", 999, 48)

    print(phone.get_info())
    phone.make_call("123-456-7890")

    print(phone_pro.get_info())
    phone_pro.take_photo()
