from kivy.app import App

from .screen_handler import ScreenHandler
from views.screens import EntryScreen
from util.common.constants import SCREEN_ENTRY

class RankTierApp(App):
    def build(self):
        self.screen_handler = ScreenHandler()
        self.__create_screens()
        return self.screen_handler

    def __create_screens(self):
        # Generic method implementation
        self.screen_handler.add_widget(EntryScreen(name=SCREEN_ENTRY))