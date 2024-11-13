import asyncio

from src.facade_app import get_app_factory

if __name__ == "__main__":
    app = get_app_factory()
    asyncio.run(app.run())
