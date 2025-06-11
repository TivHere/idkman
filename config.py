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
            "☕ Hot Drinks": [
                "Sea Salt Caramel Latte - RM 12",
                "Hot Chocolate - RM 10",
                "Cappuccino - RM 9",
            ],
            "🍫 Brownies": [
                "Classic Fudge - RM 8",
                "Salted Caramel - RM 10",
            ],
        }

        self.START_IMAGE_URL = "https://i.imgur.com/0XvYJfr.jpg"
        self.WELCOME_MESSAGE = (
            f"Welcome to {self.CAFE_NAME}! ☕🍫\n\n"
            "I'm here to help you with:\n"
            "• 📋 Menu information (/menu)\n"
            "• 📍 Location details (/location)\n"
            "• 🕘 Opening hours (/hours)\n\n"
            "Just type what you're looking for!"
        )

    def get_menu_text(self) -> str:
        menu = f"📋 *{self.CAFE_NAME} Menu*\n\n"
        for cat, items in self.MENU.items():
            menu += f"*{cat}*\n"
            for i in items:
                menu += f"• {i}\n"
            menu += "\n"
        return menu

    def get_location_text(self) -> str:
        return (
            f"📍 *{self.CAFE_NAME} Location*\n\n"
            f"Address: {self.LOCATION}\n"
            f"Phone: {self.PHONE}\n"
            f"Email: {self.EMAIL}"
        )

    def get_hours_text(self) -> str:
        return f"🕘 *Opening Hours*\n\n{self.OPENING_HOURS}"
