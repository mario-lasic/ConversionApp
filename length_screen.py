from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout

class LengthScreen(Screen):
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
		self.length_input = TextInput(hint_text="Enter length", multiline=False, size_hint=(None, None), size_hint_x=2,
		                              input_filter='float', font_size='30sp')
		self.spinner = Spinner(text="Length", values=("Centimeters", "Meters", "Inches", "Feet"),
		                       size_hint=(None, None), size_hint_x=1)
		self.spinner.bind(text=self.update_label)
		row_1.add_widget(self.length_input)
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
		self.length1_label = Label(text="Result 1", size_hint=(1, 0.5), valign="top", font_size="20sp")
		self.length1 = Label(text="0", size_hint=(1, 1), valign="center")
		col_1.add_widget(self.length1_label)
		col_1.add_widget(self.length1)
		col_2 = BoxLayout(size_hint_y=1, orientation='vertical', size_hint_x=1)
		self.length2_label = Label(text="Result 1", size_hint=(1, 0.5), valign="top", font_size="20sp")
		self.length2 = Label(text="0", size_hint=(1, 1), valign="center")
		col_2.add_widget(self.length2_label)
		col_2.add_widget(self.length2)
		col_3 = BoxLayout(size_hint_y=1, orientation='vertical', size_hint_x=1)
		self.length3_label = Label(text="Result 1", size_hint=(1, 0.5), valign="top", font_size="20sp")
		self.length3 = Label(text="0", size_hint=(1, 1), valign="center")
		col_3.add_widget(self.length3_label)
		col_3.add_widget(self.length3)
		row_3.add_widget(col_1)
		row_3.add_widget(col_2)
		row_3.add_widget(col_3)
		layout.add_widget(row_3)
		# Add the layout to the screen
		self.add_widget(layout)

	def convert_length(self, instance):
		try:
			length = float(self.length_input.text)
		except ValueError:
			return

		conversions = {
			"Centimeters": (1, 0.01, 0.393701, 0.0328084),
			"Meters": (100, 1, 39.3701, 3.28084),
			"Inches": (2.54, 0.0254, 1, 0.0833333),
			"Feet": (30.48, 0.3048, 12, 1)
		}

		unit = self.spinner.text
		all_options = self.spinner.values
		options = [option for option in self.spinner.values if unit != option]
		labels = [self.length1, self.length2, self.length3]
		for i, option in enumerate(options):
			index = all_options.index(unit)
			result = length / conversions[option][index]
			labels[i].text = f"{result:.2f}"

	def switch_back(self, instance):
		self.manager.current = 'main'

	def update_label(self, spinner, value):
		options = [option for option in spinner.values if value != option]
		labels = [self.length1_label, self.length2_label, self.length3_label]
		for i in range(len(options)):
			labels[i].text = options[i]