import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rfid_reader = SimpleMFRC522()

def read_rfid():
    try:
        print("Aproxime o cartão RFID...")
        card_id, card_text = rfid_reader.read()
        return card_id, card_text
    finally:
        GPIO.cleanup()
