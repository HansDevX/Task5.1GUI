import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO pins for the LEDs
LED_PINS = {
    "Red": 17,
    "Green": 27,
    "Blue": 22
}

# Set up each pin as an output and turn all off
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to turn on the selected LED
def turn_on_led():
    selected_color = selected_led.get()
    for color, pin in LED_PINS.items():
        GPIO.output(pin, GPIO.HIGH if color == selected_color else GPIO.LOW)

# Function to close the window and clean up GPIO
def close_gui():
    GPIO.cleanup()
    window.destroy()

# Create the GUI window
window = tk.Tk()
window.title("Raspberry Pi LED Controller")
window.geometry("300x200")
window.configure(bg="white")

# Tkinter variable to store selected radio button
selected_led = tk.StringVar()
selected_led.set("Red")

# Create radio buttons for each LED
for color in LED_PINS:
    tk.Radiobutton(window,
                   text=color,
                   variable=selected_led,
                   value=color,
                   command=turn_on_led,
                   bg="white").pack(anchor="w", padx=20, pady=5)


tk.Button(window,
          text="Exit",
          command=close_gui,
          bg="red",
          fg="white").pack(pady=20)


window.mainloop()
