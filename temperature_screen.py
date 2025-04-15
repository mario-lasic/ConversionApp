from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout


class TemperatureScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# Create the main grid layout
		layout = BoxLayout(padding=10, spacing=40, orientation='vertical')

		# Row 0 - Weight conversion label and back button
		row_0 = BoxLayout(size_hint_y=0.2)
		label = Label(text="Length conversion", size_hint=(1, None), height=30)
		back_button = Button(text="Back", size_hint=(None, None), height=30, width=100)
		back_button.bind(on_press=self.switch_back)
		row_0.add_widget(label)
		row_0.add_widget(back_button)
		layout.add_widget(row_0)

		# Row 1 - TextInput and Spinner
		row_1 = BoxLayout(size_hint_y=1, spacing=20)
		self.temperature_input = TextInput(hint_text="Enter temperature", multiline=False, size_hint=(None, None), size_hint_x=2,
		                              input_filter='float', font_size='30sp')
		self.spinner = Spinner(text="Length", values=("Celsius","Kelvin","Fahrenheit",),
		                       size_hint=(None, None), size_hint_x=1)
		self.spinner.bind(text=self.update_label)
		row_1.add_widget(self.temperature_input)
		row_1.add_widget(self.spinner)
		layout.add_widget(row_1)

		# Row 2 - Convert button spanning both columns
		row_2 = BoxLayout(size_hint_y=1)
		convert_button = Button(text="Convert", size_hint=(1, None))
		convert_button.bind(on_press=self.convert_length)
		row_2.add_widget(convert_button)
		layout.add_widget(row_2)

		# Row 3 - Labels for non-selected options
		row_3 = BoxLayout(size_hint_y=2, orientation='horizontal')
		col_1 = BoxLayout(size_hint_y=1, orientation='vertical', size_hint_x=1)
		self.temperature1_label = Label(text="Result 1", size_hint=(1, 0.5), valign="top", font_size="20sp")
		self.temperature1 = Label(text="0", size_hint=(1, 1), valign="center")
		col_1.add_widget(self.temperature1_label)
		col_1.add_widget(self.temperature1)
		col_2 = BoxLayout(size_hint_y=1, orientation='vertical', size_hint_x=1)
		self.temperature2_label = Label(text="Result 1", size_hint=(1, 0.5), valign="top", font_size="20sp")
		self.temperature2 = Label(text="0", size_hint=(1, 1), valign="center")
		col_2.add_widget(self.temperature2_label)
		col_2.add_widget(self.temperature2)
		row_3.add_widget(col_1)
		row_3.add_widget(col_2)
		layout.add_widget(row_3)
		# Add the layout to the screen
		self.add_widget(layout)

	def convert_length(self, instance):
		try:
			temperature = float(self.temperature_input.text)
		except ValueError:
			return

		conversions = {
			"Celsius": (1, lambda x: x + 273.15, lambda x: x * 9 / 5 + 32),
			"Kelvin": (lambda x: x - 273.15, 1, lambda x: (x - 273.15) * 9 / 5 + 32),
			"Fahrenheit": (lambda x: (x - 32) * 5 / 9, lambda x: (x - 32) * 5 / 9 + 273.15, 1)
		}

		unit = self.spinner.text
		all_options = self.spinner.values
		options = [option for option in self.spinner.values if unit != option]
		labels = [self.temperature1, self.temperature2]
		for i, option in enumerate(options):
			from_index = all_options.index(unit)
			to_index = all_options.index(option)

			conversion_function = conversions[unit][to_index]
			if callable(conversion_function):
				result = conversion_function(temperature)
			else:
				result = temperature * conversion_function

			labels[i].text = f"{result:.2f}"
	def switch_back(self, instance):
		self.manager.current = 'main'

	def update_label(self, spinner, value):
		options = [option for option in spinner.values if value != option]
		labels = [self.temperature1_label, self.temperature2_label]
		for i in range(len(options)):
			labels[i].text = options[i]
