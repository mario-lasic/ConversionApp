from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_weight(self):
        self.manager.current = 'weight'

    def switch_to_length(self):
        self.manager.current = 'length'

    def switch_to_temperature(self):
        self.manager.current = 'temperature'


class WeightScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def convert_weight(self):
        weight_input = self.ids.weight_input.text
        result_label = self.ids.result_label

        try:
            weight_kg = float(weight_input)
            weight_lbs = weight_kg * 2.20462
            result_label.text = f"{weight_kg} kg = {weight_lbs:.2f} lbs"
        except ValueError:
            result_label.text = "Please enter a valid number for weight."

    def switch_back(self):
        self.manager.current = 'main'


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
            temp_fahrenheit = (temp_celsius * 9/5) + 32
            result_label.text = f"{temp_celsius} °C = {temp_fahrenheit:.2f} °F"
        except ValueError:
            result_label.text = "Please enter a valid number for temperature."

    def switch_back(self):
        self.manager.current = 'main'


# Main app class
class ConverterApp(App):
    def build(self):
        # Load the .kv file after class definitions
        Builder.load_file('design.kv')

        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(WeightScreen(name='weight'))
        sm.add_widget(LengthScreen(name='length'))
        sm.add_widget(TemperatureScreen(name='temperature'))
        return sm


if __name__ == '__main__':
    ConverterApp().run()
