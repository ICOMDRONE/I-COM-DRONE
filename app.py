
from flask import Flask, render_template
import RPi.GPIO as GPIO
from time import sleep

# GPIO Ayarları
MOTOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)

# PWM Ayarları
pwm = GPIO.PWM(MOTOR_PIN, 50)  # 50 Hz PWM sinyali (ESC için uygun)
pwm.start(0)

app = Flask(__name__)

@app.route('/')
def home():
    """Ana sayfa: HTML arayüzünü gösterir."""
    return render_template('index.html')

@app.route('/start_motor')
def start_motor():
    """Motoru başlatır."""
    print("Motor çalıştırılıyor...")
    pwm.ChangeDutyCycle(10)  # Motoru başlatmak için PWM sinyali
    sleep(2)
    pwm.ChangeDutyCycle(10)  # Motoru düşük hızda döndür
    print("Motor çalışıyor...")
    return "Motor çalıştırıldı!"

@app.route('/stop_motor')
def stop_motor():
    """Motoru durdurur."""
    print("Motor durduruluyor...")
    pwm.ChangeDutyCycle(0)  # Motoru durdur
    return "Motor durduruldu!"

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        pwm.ChangeDutyCycle(0)
        pwm.stop()
        GPIO.cleanup()
        print("Uygulama kapatıldı ve GPIO temizlendi.")

