import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class GridLayoutApp(App):

    def build(self):
        return GridLayout()

gridApp = GridLayoutApp()
gridApp.run()