import os
from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label

os.environ["KIVY_NO_ENV_CONFIG"] = "1"
Config.set('graphics', 'width', '450')
Config.set('graphics', 'heigth', '200')


class MyApp(App):
	label_input = Label(text = "0",
		  				color = [1, 0, 0, 1],
		  				halign = 'right')
	label_display = Label(text = "",
		  				color = [1, 0, 0, 1],
		  				halign = 'right')
	operation = ''
	num_1 = ''
	result = ''

	def build(self):
		main_win = BoxLayout(orientation = "vertical")
		display = AnchorLayout(
			anchor_x = 'right',
			anchor_y = 'top',
			size_hint = [1, .2])
		user_input = AnchorLayout(
			anchor_x = 'right',
			anchor_y = 'bottom',
			size_hint = [.5, .2])
		actions = GridLayout(cols = 5, spacing = 3)

		display.add_widget(self.label_display)

		user_input.add_widget(self.label_input)

		actions.add_widget( Button(text = "7", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "8", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "9", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "+", font_size = 24, on_press = self.on_update_operation))
		actions.add_widget( Button(text = "-", font_size = 34, on_press = self.on_update_operation))

		actions.add_widget( Button(text = "4", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "5", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "6", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "%", font_size = 24, on_press = self.on_update_operation))
		actions.add_widget( Button(text = "//", font_size = 24, on_press = self.on_update_operation))

		actions.add_widget( Button(text = "1", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "2", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "3", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "*", font_size = 34, on_press = self.on_update_operation))
		actions.add_widget( Button(text = "^", font_size = 34, on_press = self.on_update_operation))

		actions.add_widget( Button(text = "Clear", on_press = self.on_update_clear))
		actions.add_widget( Button(text = "0", on_press = self.on_update_numeric))
		actions.add_widget( Button(text = "<", font_size = 34, on_press = self.on_update_delete))
		actions.add_widget( Widget())
		actions.add_widget( Button(text = "=", font_size = 24, on_press = self.on_update_equally))
		
		main_win.add_widget(display)
		main_win.add_widget(user_input)
		main_win.add_widget(actions)
		return main_win

	def on_update_numeric(self, instance):
		if self.result == "0" or self.operation == "=":
			self.result = ""
			self.label_display.text = ""
		self.result += instance.text
		self.label_input.text = self.result

	def on_update_operation(self, instance):
		if self.num_1 != "" and self.result != "":
			self.final()

		if self.result != "":
			self.num_1 = self.result

		self.operation = instance.text

		self.label_display.text = self.num_1 + ' ' + self.operation
		self.result = ""

	def on_update_equally(self, instance):
		if self.num_1 != "" and self.result != "":
			self.label_display.text = self.num_1 + ' ' +\
									  self.operation + ' ' +\
									  self.result + ' ' +\
									  instance.text
			self.final()
			self.num_1 = ""
			self.operation = instance.text

	def on_update_clear(self, instance):
		operation = ''
		num_1 = ''
		result = ''
		self.label_display.text = ""
		self.label_input.text = "0"

	def on_update_delete(self, instance):
		if self.operation != "":
			self.label_display.text = ""
			self.operation = ''
		else:
			if len(self.result) > 1:
				self.result = self.result[:-1]
				self.label_input.text = self.result
			else:
				self.result = "0"
				self.label_input.text = self.result

	def final(self):
		if self.operation == "+":
			self.result = str(int(self.result) + int(self.num_1))
		elif self.operation == "-":
			self.result = str(int(self.num_1) - int(self.result))
		elif self.operation == "%":
			self.result = str(int(self.num_1) % int(self.result))
		elif self.operation == "//":
			self.result = str(int(self.num_1) // int(self.result))
		elif self.operation == "*":
			self.result = str(int(self.result) * int(self.num_1))
		elif self.operation == "^":
			self.result = str(int(self.num_1) ** int(self.result))
		self.label_input.text = self.result

	def callback(self, instance):
		pass

if __name__ == "__main__":
	MyApp().run()
