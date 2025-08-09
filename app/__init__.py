"""Volume Bot - Telegram Bot for volume control."""

__version__ = "1.0.0"
__author__ = "Volume Bot Team"

from .main import main
from .telegram_bot import TelegramBot
from .mm import VolumeController
from .config import Config

__all__ = ['main', 'TelegramBot', 'VolumeController', 'Config']
