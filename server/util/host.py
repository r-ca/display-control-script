import os


class HostUtils:
    def __init__(self):
        # Host system type
        if (os.name == "nt"):
            self.SYSTEM_TYPE = "windows"
        else:
            if (os.name == "posix"):
                self.SYSTEM_TYPE = "linux"
            else:
                self.SYSTEM_TYPE = "unknown"

    def get_hostname(self) -> str:
        return os.uname().nodename
