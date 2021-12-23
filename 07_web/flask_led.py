from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


app = Flask(__name__)

#0.0.0.0:5000
@app.route("/")
def hello():
    return''' 
      <a href="/led/on">LED ON</a>
      <a href="/led/off">LED OFF/a>
    '''
@app.route("/led/<op>")
def first(op):
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
         <p>LED ON</p>
         <a href="/">Go Home</a>
         '''
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
         <p>LED OFF</p>
         <a href="/">Go Home</a>
         '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:    
        GPIO.cleanup()
        print('cleanup and exit')