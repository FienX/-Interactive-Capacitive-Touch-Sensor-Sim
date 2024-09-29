import time
from datetime import datetime

class CapacitiveSensor:
    def __init__(self, threshold=5, name="Sensor"):
        self.threshold = threshold
        self.baseline = 0
        self.name = name
        self.log = []

    def calibrate(self):
        print(f"Calibrating {self.name}...")
        readings = [float(input(f"Enter calibration value {i+1}/5: ")) for i in range(5)]
        self.baseline = sum(readings) / len(readings)
        print(f"Baseline set to: {self.baseline:.2f}")

    def is_touched(self, reading):
        return (reading - self.baseline) > self.threshold

    def get_touch_strength(self, reading):
        return max(0, reading - self.baseline)

    def process_reading(self, reading):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.is_touched(reading):
            strength = self.get_touch_strength(reading)
            message = f"Touch detected! Strength: {strength:.2f}"
        else:
            message = "No touch detected"
        
        log_entry = f"{timestamp} - {self.name} - Raw: {reading:.2f} - {message}"
        self.log.append(log_entry)
        print(log_entry)

    def save_log(self):
        with open(f"{self.name}_log.txt", "w") as f:
            for entry in self.log:
                f.write(entry + "\n")
        print(f"Log saved to {self.name}_log.txt")
