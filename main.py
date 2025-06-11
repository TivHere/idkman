#!/usr/bin/env python3
import os
import sys
import logging
from bot import BrowniesCafeBot
from keep_alive import keep_alive

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('bot.log', mode='a')
        ]
    )

def main():
    try:
        setup_logging()
        logger = logging.getLogger(__name__)
        logger.info("Starting Brownies Café Bot...")

        keep_alive()
        bot = BrowniesCafeBot()
        bot.start()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
