import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class FloatingApp(App):

    def build(self):
        return FloatLayout()

flApp = FloatingApp()
flApp.run()