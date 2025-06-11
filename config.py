import os

class Config:
    def __init__(self):
        self.BOT_TOKEN = os.getenv("BOT_TOKEN", "")
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN environment variable is required")

        self.CAFE_NAME = "Brownies Café"
        self.OPENING_HOURS = "Mon–Sun: 9AM – 9PM"
        self.LOCATION = "123 Jalan Brownies, KL"
        self.PHONE = "+60 3-1234 5678"
        self.EMAIL = "hello@browniescafe.com"
        self.MAIN_PHOTO_URL = "https://i.imgur.com/r0zJfFq.jpg"  # sample placeholder

        self.MENU = {
            "☕ Hot Drinks": [
                "Sea Salt Caramel Latte - RM 12",
                "Hot Chocolate - RM 10",
                "Cappuccino - RM 9",
                "Flat White - RM 9",
                "Mocha - RM 11"
            ],
            "🧊 Cold Drinks": [
                "Iced Americano - RM 8",
                "Iced Latte - RM 10",
                "Cold Brew - RM 9",
                "Frappé - RM 12",
                "Iced Matcha Latte - RM 11"
            ],
            "🍫 Brownies": [
                "Classic Fudge - RM 8",
                "Nutella Swirl - RM 9",
                "Vegan Choco Chip - RM 9",
                "Salted Caramel - RM 10",
                "Double Chocolate - RM 9"
            ],
            "🥪 Light Bites": [
                "Grilled Sandwich - RM 12",
                "Croissant - RM 6",
                "Muffin - RM 5",
                "Scone - RM 6",
                "Bagel - RM 7"
            ]
        }

        self.FIRST_TIME_MESSAGE = (
            f"🎉 Welcome to {self.CAFE_NAME}! ☕🍫\n\n"
            "We're delighted to have you here! Our cozy café offers the finest brownies and coffee in town.\n\n"
            "Use the buttons below to navigate the menu, hours, and more!"
        )

        self.WELCOME_MESSAGE = (
            f"Welcome to {self.CAFE_NAME}! ☕🍫\n\n"
            "I'm here to help you with:\n"
            "• 📋 Menu information\n"
            "• 📍 Location\n"
            "• 🕘 Opening hours\n\n"
            "Use the buttons below or type your query!"
        )

        self.OPENAI_ENABLED = bool(self.OPENAI_API_KEY)

    def get_menu_text(self) -> str:
        menu_text = f"📋 *{self.CAFE_NAME} Menu*\n\n"
        for category, items in self.MENU.items():
            menu_text += f"*{category}*\n"
            for item in items:
                menu_text += f"• {item}\n"
            menu_text += "\n"
        menu_text += "💳 We accept cash and cards\n🚚 Delivery via Grab/Foodpanda"
        return menu_text

    def get_location_text(self) -> str:
        return (
            f"📍 *{self.CAFE_NAME} Location*\n\n"
            f"Address: {self.LOCATION}\n"
            f"Phone: {self.PHONE}\n"
            f"Email: {self.EMAIL}\n\n"
            f"🕘 Hours: {self.OPENING_HOURS}\n"
            "🚗 Parking available\n🚇 5 mins from LRT"
        )

    def get_hours_text(self) -> str:
        return (
            f"🕘 *{self.CAFE_NAME} Opening Hours*\n\n"
            f"{self.OPENING_HOURS}\n\n"
            "We're open daily — perfect for breakfast or evening brownies!"
        )
