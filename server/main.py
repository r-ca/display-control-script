from fastapi import FastAPI

from executer import hyprland

app = FastAPI()


@app.get("/state")
async def state():
    return {"state": hyprland.HyprlandDisplayOperate().state()}


# Debug
@app.post("/turn_on")
async def turn_on():
    hyprland.HyprlandDisplayOperate().turn_on()
    return {"state": hyprland.HyprlandDisplayOperate().state()}


# Debug
@app.post("/turn_off")
async def turn_off():
    hyprland.HyprlandDisplayOperate().turn_off()
    return {"state": hyprland.HyprlandDisplayOperate().state()}
