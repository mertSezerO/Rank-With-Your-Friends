from kivy.lang import Builder

from util.common import KIVY_FILE
from views import RankTierApp

Builder.load_file(KIVY_FILE)

app = RankTierApp()
app.run()
