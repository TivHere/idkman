import os

class Config:
    def __init__(self):
        self.BOT_TOKEN = os.getenv("BOT_TOKEN", "")
        self.CAFE_NAME = "Brownies Café"
        self.OPENING_HOURS = "Mon–Sun: 9AM – 9PM"
        self.LOCATION = "123 Jalan Brownies, KL"
        self.PHONE = "+60 3-1234 5678"
        self.EMAIL = "hello@browniescafe.com"
        self.MENU = {
            "Hot Drinks": ["Sea Salt Caramel Latte - RM 12", "Hot Chocolate - RM 10"],
            "Brownies": ["Classic Fudge - RM 8", "Salted Caramel - RM 10"]
        }

    def get_menu_text(self):
        text = f"{self.CAFE_NAME} Menu\n\n"
        for category, items in self.MENU.items():
            text += f"{category}:\n"
            for item in items:
                text += f"• {item}\n"
            text += "\n"
        return text

    def get_location_text(self):
        return f"{self.CAFE_NAME} Location:\n{self.LOCATION}\n{self.PHONE}\n{self.EMAIL}"

    def get_hours_text(self):
        return f"{self.CAFE_NAME} Opening Hours:\n{self.OPENING_HOURS}"