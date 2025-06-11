#!/usr/bin/env python3
"""
Main entry point for Brownies Café Telegram Bot
Initializes and starts the bot
"""

import os
import sys
import logging
from bot import BrowniesCafeBot
from keep_alive import keep_alive

def setup_logging():
    """Configure logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('bot.log', mode='a')
        ]
    )

def main():
    """Start the bot"""
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        logger.info("Starting Brownies Café Bot...")
        
        # Start keep_alive web server for uptime (Replit only)
        keep_alive()
        
        # Initialize and run the bot
        bot = BrowniesCafeBot()
        bot.start()

    except KeyboardInterrupt:
        logger.info("Bot manually stopped.")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
