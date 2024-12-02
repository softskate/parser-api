import json
from fastapi import FastAPI
from threading import Thread
import ozon, citilink, wildberries, mvideo, \
    norbel, resurs_media, absolut_trade, pronet, f5it, logic
from bot import bot


app = FastAPI()

# Include routers with prefixes
app.include_router(ozon.app, prefix="/ozon", tags=["Ozon"])
app.include_router(citilink.app, prefix="/citilink", tags=["Citilink"])
app.include_router(wildberries.app, prefix="/wb", tags=["Wildberries"])
app.include_router(mvideo.app, prefix="/mvideo", tags=["MVideo"])
app.include_router(norbel.app, prefix="/norbel", tags=["Norbel"])
app.include_router(resurs_media.app, prefix="/resurs-media", tags=["Resurs-Media"])
app.include_router(absolut_trade.app, prefix="/absolut-trade", tags=["Elko"])
app.include_router(pronet.app, prefix="/pronet", tags=["ProNet"])
app.include_router(f5it.app, prefix="/f5it", tags=["F5IT"])
app.include_router(logic.app, prefix="/logic", tags=["3Logic"])

Thread(target=bot.infinity_polling, daemon=True).start()
