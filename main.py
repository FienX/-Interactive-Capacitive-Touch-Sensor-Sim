from sensor_simulator import CapacitiveSensor

def main():
    sensor = CapacitiveSensor(threshold=2, name="TouchPad1")
    sensor.calibrate()
    
    print("\nSimulating capacitive touch sensor. Enter 'q' to quit.")
    while True:
        user_input = input("Enter sensor reading (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            reading = float(user_input)
            sensor.process_reading(reading)
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    sensor.save_log()
    print("Simulation ended.")

if __name__ == "__main__":
    main()
