import os

class Config:
    def __init__(self):
        self.BOT_TOKEN = os.getenv("BOT_TOKEN", "")
        self.MAIN_PHOTO_URL = "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80"
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
        self.LOCATION = "123 Jalan Brownies, KL"
        self.PHONE = "+60 3-1234 5678"
        self.EMAIL = "hello@browniescafe.com"
        self.OPENING_HOURS = "Mon–Sun: 9AM – 9PM"

    def get_menu_text(self):
        menu_text = "*📋 Menu*\n\n"
        for category, items in self.MENU.items():
            menu_text += f"*{category}*\n"
            for item in items:
                menu_text += f"• {item}\n"
            menu_text += "\n"
        return menu_text.strip()

    def get_location_text(self):
        return f"📍 *Location*\n\n{self.LOCATION}\n📞 {self.PHONE}\n✉️ {self.EMAIL}"

    def get_hours_text(self):
        return f"🕘 *Opening Hours*\n\n{self.OPENING_HOURS}\nOpen every day!"
