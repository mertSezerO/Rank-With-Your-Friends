from kivy.uix.screenmanager import ScreenManager

class ScreenHandler(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_screens(self, *args):
        for arg in args:
            self.add_widget(arg)