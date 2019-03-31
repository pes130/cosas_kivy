import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class PageLayoutApp(App):

    def build(self):
        return PageLayout()

plApp = PageLayoutApp()
plApp.run()