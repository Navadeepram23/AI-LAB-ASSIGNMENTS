import random
import time

class RoomTemperatureAgent:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound 
        self.upper_bound = upper_bound 
        self.current_temperature = random.uniform(15, 30)

    def sense_temperature(self):
        self.current_temperature += random.uniform(-1, 1)
        return self.current_temperature

    def decide_action(self):
        if self.current_temperature < self.lower_bound:
            action = "Turn on heater"
        elif self.current_temperature > self.upper_bound:
            action = "Turn on cooler"
        else:
            action = "Do nothing"
        return action

    def execute(self, action):
        if action == "Turn on heater":
            self.current_temperature += 1 
        elif action == "Turn on cooler":
            self.current_temperature -= 1

    def run(self, cycles=5, delay=2):
        for cycle in range(cycles):
            print(f"\nCycle {cycle + 1}:")
            temperature = self.sense_temperature()
            print(f"Current temperature: {temperature:.2f}°C")
            action = self.decide_action()
            print(f"Action: {action}")
            self.execute(action)
            time.sleep(delay)

agent = RoomTemperatureAgent(lower_bound=20, upper_bound=25)
agent.run()
