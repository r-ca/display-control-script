from fastapi import FastAPI

from executer.hyprland import HyprlandDisplayOperate

app = FastAPI()


@app.get("/state")
async def state():
    return {"state": HyprlandDisplayOperate().state()}


# Debug
@app.post("/turn_on")
async def turn_on():
    HyprlandDisplayOperate().turn_on()
    return {"state": HyprlandDisplayOperate().state()}


# Debug
@app.post("/turn_off")
async def turn_off():
    HyprlandDisplayOperate().turn_off()
    return {"state": HyprlandDisplayOperate().state()}
