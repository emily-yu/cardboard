from pykeyboard import PyKeyboard
import math

class PhoneShortCuts:
    def __init__(self):
        self.k = PyKeyboard()
        self.starter_path = "stouch "
        self.max_x = 347
        self.max_y = 650

    def home(self):
        full_command = self.starter_path + "button 1 1\n"
        self.k.type_string(full_command)

    def touch(self, x, y):
        real_x = math.floor(self.max_x * x)
        real_y = math.floor(self.max_y * y)

        full_command = self.starter_path + "touch " + str(real_x) + " " + str(real_y) + "\n"

        print (full_command)
        self.k.type_string(full_command)

k = PyKeyboard()
