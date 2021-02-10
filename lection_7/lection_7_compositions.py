class WindowDoor:

    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height


class Room:

    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []

    def add_win_door(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
            return main_square


upshot = Room(1, 3, 6)
print(upshot.square)
upshot.add_win_door(2, 2)
upshot.add_win_door(1, 2)
print(upshot.common_square())