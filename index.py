from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)  # Utilizando a numeração BCM dos pinos

red_led = 11
yellow_led = 13
green_led = 15
purple_led = 16
            
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(purple_led, GPIO.OUT)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/led/<color>')
def control_led(color):
    
    pin = 0

    match(color):
        case 'red':
            pin = red_led
        case 'yellow':
            pin = yellow_led
        case 'green':
            pin = green_led
        case 'purple':
            pin = purple_led 

    if(pin == 0): 
        return

    if(GPIO.input(pin) == GPIO.HIGH):
        GPIO.output(pin, GPIO.LOW)
        return "LED Desligado"
    else:
        GPIO.output(pin, GPIO.HIGH)
        return "LED Ligado"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 