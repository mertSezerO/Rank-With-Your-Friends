from kivy.uix.screenmanager import Screen

from views import ScreenHandler

class AppScreen(Screen):

    def __init__(self, screen_handler: ScreenHandler, **kw):
        super().__init__(**kw)
        self.root_handler = screen_handler