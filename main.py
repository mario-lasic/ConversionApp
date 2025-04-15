from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from weight_screen import WeightScreen
from length_screen import LengthScreen


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
