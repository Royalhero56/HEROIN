import asyncio
import importlib

# ✅ EVENT LOOP FIX (Railway + Python 3.14 issue killer)
try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyrogram import idle
from AarohiX import LOGGER, AarohiX
from AarohiX.modules import ALL_MODULES


async def anony_boot():
    try:
        await AarohiX.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("AarohiX.modules." + all_module)

    LOGGER.info(f"@{AarohiX.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.run(anony_boot())
    LOGGER.info("Stopping AarohiX Bot...")
