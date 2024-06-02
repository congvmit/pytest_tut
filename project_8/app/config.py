import os


class Config:
    # async sqlite memory database
    DB_CONFIG = "sqlite+aiosqlite:///:memory:"


config = Config()
