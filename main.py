from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from weight_screen import WeightScreen
from length_screen import LengthScreen
from temperature_screen import  TemperatureScreen


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
