from kivy.app import App                            # Import all neccessary lib's
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config


saveInput = ""					# Global variable for inputText

class CalculatorApp(App):

	def calculate(self, symbol):							# Main calculation function
		global saveInput
		if symbol.text is 'C':													# For Clear Button
			saveInput = self.result.text = ""
		elif symbol.text is '<':
			saveInput = self.result.text = self.result.text[0:-1]
		elif symbol.text is not '=':											# For adding text 
			self.result.text += symbol.text
			saveInput += symbol.text
		else:																    # For result
			try: saveInput = self.result.text = str(eval(saveInput))
			except: saveInput = self.result.text = ""

	def build(self):                                        # Interface
		root = BoxLayout(orientation = "vertical")

		self.result = TextInput(
        	text = "", readonly = True, font_size = 25, 
        	size_hint = [1, .75], background_color = [1,1,1,.95])
		root.add_widget(self.result)

		allButtons = GridLayout(cols = 5)
		allButtonsArray = ['7', '8', '9', "+", "<", '4', '5', '6', "-", "(", '1', '2', '3', "*", ")", '0', ".", "=", "/", "%"]

		for i in allButtonsArray:
			allButtons.add_widget(Button(text = i, on_press = self.calculate))

		root.add_widget(allButtons)
		root.add_widget(Button(text = "C", on_press = self.calculate, size_hint = [1, 0.2]))
		return root

if __name__ == "__main__":
    CalculatorApp().run()