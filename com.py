from QUBE_PYTHON.Control import Control


class Packet:
    def __init__(self):
        self.control = Control()
        self.plot_data = [[] * 6]
        self.resetEncoders = False

    def unpack(self):
        return [
            self.control,
            self.resetEncoders,
        ]
