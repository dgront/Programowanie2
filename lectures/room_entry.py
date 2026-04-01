import sys


import datetime


class RoomEntry:

    __slots__ = ["__state", "__room"]

    def __init__(self, room: str):
        self.__state = 0
        self.__room = room

    def flip(self, card_id: int = 0):

        if not self.__is_valid_card(card_id): return

        if self.__state == 0:
            self.__open()
        else:
            self.__close()

    def __is_valid_card(self, card_id):
        return True

    def __open(self):
        self.__state = 1
        self.__logger("OPEN")

    def __close(self):
        self.__state = 0
        self.__logger("CLOSE")

    def __logger(self, event):
        now = datetime.now()
        print(f"Event: {event} to {self.__room} at {now}")







class_1_34 = RoomEntry("1.34")
# class_1_33 = RoomEntry("1.33")
# print("class_1_34", class_1_34)
class_1_34.flip()
# print("class_1_33", class_1_33)
# class_1_33.flip()
# # class_1_34.flip()

