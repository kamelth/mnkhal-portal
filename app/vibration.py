import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin where the vibration sensor is connected
VIBRATION_PIN = 17

# Set the pin as input
GPIO.setup(VIBRATION_PIN, GPIO.IN)

def pulse_in(pin, level, timeout=1000000):
    """
    Emulate pulseIn function similar to Arduino.
    Waits for the pin to go to 'level', and then measures how long it stays at that level.
    The timeout is in microseconds.
    """
    start_time = time.time()
    # Wait for the pin to reach the desired level
    while GPIO.input(pin) != level:
        if (time.time() - start_time) > timeout / 1000000.0:
            return 0  # Timeout occurred

    # Record the time when the pulse starts
    pulse_start = time.time()

    # Wait for the pin to change state
    while GPIO.input(pin) == level:
        if (time.time() - start_time) > timeout / 1000000.0:
            return 0  # Timeout occurred

    # Record the time when the pulse ends
    pulse_end = time.time()

    # Return the duration of the pulse in microseconds
    pulse_duration = (pulse_end - pulse_start) * 1000000
    return pulse_duration

def read_vibration():
    while True:
        # Measure the duration of the HIGH pulse
        measurement = pulse_in(VIBRATION_PIN, GPIO.HIGH)
        
        print(f"Vibration Measurement: {measurement}")
        # You can add a notification or threshold like your original code

        time.sleep(1)  # Delay for 1 second

if __name__ == "__main__":
    try:
        read_vibration()
    except KeyboardInterrupt:
        print("Program stopped by user")
    finally:
        GPIO.cleanup()
