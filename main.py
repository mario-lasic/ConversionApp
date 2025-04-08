from operator import indexOf

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout


class MainScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# Create the BoxLayout with vertical orientation
		layout = BoxLayout(orientation='vertical', padding=[50, 50, 50, 50], spacing=20)

		# Button for Weight Screen
		weight_button = Button(text="Weight")
		weight_button.bind(on_press=lambda instance: self.change_screen("weight"))

		# Button for Length Screen
		length_button = Button(text="Length")
		length_button.bind(on_press=lambda instance: self.change_screen("length"))

		# Button for Temperature Screen
		temperature_button = Button(text="Temperature")
		temperature_button.bind(on_press=lambda instance: self.change_screen("temperature"))

		# Add buttons to the layout
		layout.add_widget(weight_button)
		layout.add_widget(length_button)
		layout.add_widget(temperature_button)

		# Add the layout to the screen
		self.add_widget(layout)

	def change_screen(self, name):
		self.manager.current = name


class WeightScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# Create the main grid layout
		layout = BoxLayout(padding=10, spacing=40, orientation='vertical')

		# Row 0 - Weight conversion label and back button
		row_0 = BoxLayout(size_hint_y=0.2)
		label = Label(text="Weight Conversion", size_hint=(1, None), height=30)
		back_button = Button(text="Back", size_hint=(None, None), height=30, width=100)
		back_button.bind(on_press=self.switch_back)
		row_0.add_widget(label)
		row_0.add_widget(back_button)
		layout.add_widget(row_0)

		# Row 1 - TextInput and Spinner
		row_1 = BoxLayout(size_hint_y=1, spacing=20)
		self.weight_input = TextInput(hint_text="Enter weight", multiline=False, size_hint=(None, None), size_hint_x=2,
		                              input_filter='float', font_size='30sp')
		self.spinner = Spinner(text="Weight", values=("Kilograms", "Grams", "Pounds", "Stones"),
		                       size_hint=(None, None), size_hint_x=1)
		self.spinner.bind(text=self.update_label)
		row_1.add_widget(self.weight_input)
		row_1.add_widget(self.spinner)
		layout.add_widget(row_1)

		# Row 2 - Convert button spanning both columns
		row_2 = BoxLayout(size_hint_y=1)
		convert_button = Button(text="Convert", size_hint=(1, None))
		convert_button.bind(on_press=self.convert_weight)
		row_2.add_widget(convert_button)
		layout.add_widget(row_2)

		# Row 3 - Labels for non-selected options
		row_3 = BoxLayout(size_hint_y=2, orientation='horizontal')
		col_1 = BoxLayout(size_hint_y=1, orientation='vertical', size_hint_x=1)
		self.weight_label1 = Label(text="Result 1", size_hint=(1, 0.5), valign="top", font_size="20sp")
		self.weight1 = Label(text="0", size_hint=(1, 1), valign="center")
		col_1.add_widget(self.weight_label1)
		col_1.add_widget(self.weight1)
		col_2 = BoxLayout(size_hint_y=1, orientation='vertical', size_hint_x=1)
		self.weight_label2 = Label(text="Result 1", size_hint=(1, 0.5), valign="top", font_size="20sp")
		self.weight2 = Label(text="0", size_hint=(1, 1), valign="center")
		col_2.add_widget(self.weight_label2)
		col_2.add_widget(self.weight2)
		col_3 = BoxLayout(size_hint_y=1, orientation='vertical', size_hint_x=1)
		self.weight_label3 = Label(text="Result 1", size_hint=(1, 0.5), valign="top", font_size="20sp")
		self.weight3 = Label(text="0", size_hint=(1, 1), valign="center")
		col_3.add_widget(self.weight_label3)
		col_3.add_widget(self.weight3)
		row_3.add_widget(col_1)
		row_3.add_widget(col_2)
		row_3.add_widget(col_3)
		layout.add_widget(row_3)
		# Add the layout to the screen
		self.add_widget(layout)

	def convert_weight(self, instance):
		try:
			weight = float(self.weight_input.text)
		except ValueError:
			return

		conversions = {
			"Kilograms": (1, 1000, 2.20462, 0.15747),
			"Grams": (0.001, 1, 0.00220462, 0.00015747),
			"Pounds": (0.453592, 453.592, 1, 0.0714286),
			"Stones": (6.35029, 6350.29, 14, 1)
		}

		unit = self.spinner.text
		all_options = self.spinner.values
		options = [option for option in self.spinner.values if unit != option]
		labels = [self.weight1, self.weight2, self.weight3]
		for i, option in enumerate(options):
			index = all_options.index(unit)
			result = weight / conversions[option][index]
			print(option)
			print(conversions[option][index])

			labels[i].text = f"{result:.2f}"


	def switch_back(self):
		self.manager.current = 'main'

	def update_label(self, spinner, value):
		options = [option for option in spinner.values if value != option]
		labels = [self.weight_label1, self.weight_label2, self.weight_label3]
		for i in range(len(options)):
			labels[i].text = options[i]


class LengthScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def convert_length(self):
		length_input = self.ids.length_input.text
		result_label = self.ids.result_label
		try:
			length_meters = float(length_input)
			length_feet = length_meters * 3.28084
			result_label.text = f"{length_meters} meters = {length_feet:.2f} feet"
		except ValueError:
			result_label.text = "Please enter a valid number for length."

	def switch_back(self):
		self.manager.current = 'main'


class TemperatureScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def convert_temperature(self):
		temp_input = self.ids.temp_input.text
		result_label = self.ids.result_label
		try:
			temp_celsius = float(temp_input)
			temp_fahrenheit = (temp_celsius * 9 / 5) + 32
			result_label.text = f"{temp_celsius} °C = {temp_fahrenheit:.2f} °F"
		except ValueError:
			result_label.text = "Please enter a valid number for temperature."

	def switch_back(self):
		self.manager.current = 'main'


# Main app class
class ConverterApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MainScreen(name='main'))
		sm.add_widget(WeightScreen(name='weight'))
		sm.add_widget(LengthScreen(name='length'))
		sm.add_widget(TemperatureScreen(name='temperature'))
		return sm


if __name__ == '__main__':
	ConverterApp().run()
