#!/usr/bin/env python3
import logging
from bot import BrowniesCafeBot

def main():
    logging.basicConfig(level=logging.INFO)
    bot = BrowniesCafeBot()
    bot.start()

if __name__ == "__main__":
    main()