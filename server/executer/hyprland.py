from interface.display_operate import IDisplayOperate
import os


class Utils:
    def __init__(self):
        self.STATE_FILE = "/tmp/dctrl/hyprland_state"

    def get_state_file_exists(self) -> bool:
        return os.path.exists(self.STATE_FILE)

    def create_state_file(self):
        with open(self.STATE_FILE, "w") as f:
            f.write("1")

    def get_state(self) -> bool:
        with open(self.STATE_FILE, "r") as f:
            return f.read() == "1"

    def set_state(self, state: bool):
        with open(self.STATE_FILE, "w") as f:
            f.write("1" if state else "0")

    def exec_cmd(self, cmd: str) -> str:
        return os.system(cmd)


class HyprlandDisplayOperate(IDisplayOperate):
    def state(self) -> bool:
        if (Utils().get_state_file_exists()):
            return Utils().get_state()
        else:
            Utils().create_state_file()
            return self.state()

    def turn_on(self):
        result = Utils().exec_cmd("hyprctl dispatch dpms on")
        if result == "ok":
            Utils().set_state(True)

    def turn_off(self):
        result = Utils().exec_cmd("hyprctl dispatch dpms off")
        if result == "ok":
            Utils().set_state(False)
