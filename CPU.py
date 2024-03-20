import tkinter as tk

class Clock():
    def __init__(self) -> None:
        self.bit = 0
    def tick(self):
        if self.bit == 0:
            self.bit = 1
        else:
            self.bit = 0
    def getBit(self):
        return self.bit