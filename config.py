import os

class Config:
    def __init__(self):
        self.BOT_TOKEN = os.getenv("BOT_TOKEN", "")
        self.CAFE_NAME = "Brownies Café"
        self.OPENING_HOURS = "Mon–Sun: 9AM – 9PM"
        self.LOCATION = "123 Jalan Brownies, KL"
        self.PHONE = "+60 3-1234 5678"
        self.EMAIL = "hello@browniescafe.com"
        self.MAIN_PHOTO_URL = "https://cdn.pixabay.com/photo/2017/04/23/20/24/brownies-2254318_1280.jpg"

        self.MENU = {
            "☕ Hot Drinks": [
                "Sea Salt Caramel Latte - RM 12",
                "Hot Chocolate - RM 10"
            ],
            "🍫 Brownies": [
                "Classic Fudge - RM 8",
                "Salted Caramel - RM 10"
            ]
        }

    def get_menu_text(self):
        menu_text = "📋 *Menu*\n\n"
        for category, items in self.MENU.items():
            menu_text += f"*{category}*\n"
            for item in items:
                menu_text += f"• {item}\n"
            menu_text += "\n"
        return menu_text

    def get_location_text(self):
        return f"📍 *Location*\n\n{self.LOCATION}\n📞 {self.PHONE}\n✉️ {self.EMAIL}"

    def get_hours_text(self):
        return f"🕘 *Opening Hours*\n\n{self.OPENING_HOURS}\nOpen every day!"