from flask import Flask, render_template, jsonify, request, redirect, url_for
import RPi.GPIO as GPIO
from RFID import read_rfid

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

rdids = []

@app.before_request
def validate_header():
    excluded_routes = ['/login', "/", "/login/scanRFID"] 

    if request.path in excluded_routes:
        return

    token = request.headers.get('X-Auth-Token')

    if not token or not (token in rdids):
        return redirect(url_for('login'))

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/scanRFID', methods=['GET'])
def wait_for_rfid():
    try:
        card_id, card_text = read_rfid()   
        rdids.append(str(card_id))     
        return jsonify({ 'rfid': card_id }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
        return jsonify({ "error": "Pino não existe" }), 404

    if(GPIO.input(pin) == GPIO.HIGH):
        GPIO.output(pin, GPIO.LOW)
        return jsonify({ "msg": "Pino Desligado" }), 200
    else:
        GPIO.output(pin, GPIO.HIGH)
        return jsonify({ 'msg': "Pino Ligado" }), 200

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Erro ao iniciar o aplicativo: {e}")
    finally:
        GPIO.cleanup()