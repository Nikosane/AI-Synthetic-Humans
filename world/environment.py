import random

class Environment:
    def __init__(self, temperature=None, weather=None):
        self.temperature = temperature if temperature else self.generate_temperature()
        self.weather = weather if weather else self.generate_weather()

    def generate_temperature(self):
        return random.uniform(-10, 40)  # Temperature range in Celsius

    def generate_weather(self):
        return random.choice(["Sunny", "Rainy", "Stormy", "Snowy", "Cloudy"])

    def update_conditions(self):
        self.temperature = self.generate_temperature()
        self.weather = self.generate_weather()

    def __repr__(self):
        return f"Environment(temperature={self.temperature}C, weather={self.weather})"
