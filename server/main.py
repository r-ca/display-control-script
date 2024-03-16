from fastapi import FastAPI
from interface.display_operate import IDisplayOperate
from executer.hyprland import HyprlandDisplayOperate
from model.display_state import DisplayState
from model.display_request import DisplayRequest
from util.host import HostUtils

app = FastAPI()

executer: IDisplayOperate = HyprlandDisplayOperate()


@app.get("/display")
async def display_get():
    return DisplayState(
            hostname=HostUtils().get_hostname(),
            state=executer.state())


@app.post("/display")
async def display_post(req: DisplayRequest):
    if (req.state):
        executer.turn_on()
    else:
        executer.turn_off()
    return DisplayState(
            hostname=HostUtils().get_hostname(),
            state=executer.state())
