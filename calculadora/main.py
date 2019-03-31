import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.mi_display.text = str(eval(calculation))
            except Exception:
                self.mi_display.text = "Error"

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()