from fastapi import FastAPI
from uvicorn import run
from reactpy.backend.fastapi import configure, Options

from components.game import Game
from components.head import Head

app = FastAPI()

configure(
    app,
    Game,
    Options(head=Head()),
)

run(app)
