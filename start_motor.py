import RPi.GPIO as GPIO
from time import sleep

# GPIO ayarları
MOTOR_PIN = 18  # Motorun bağlı olduğu GPIO pini
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)

# PWM ayarları
pwm = GPIO.PWM(MOTOR_PIN, 50)  # 50 Hz PWM sinyali (ESC için uygun)
pwm.start(0)

try:
    print("Motor çalıştırılıyor...")
    pwm.ChangeDutyCycle(10)  # Motoru başlatmak için PWM sinyali
    sleep(2)  # ESC’ye 2 saniye sinyal gönder
    pwm.ChangeDutyCycle(10)  # Motoru düşük hızda döndür
    print("Motor çalışıyor...")
    while True:
        sleep(1)  # Sürekli döndür

except KeyboardInterrupt:
    print("Motor başlatma işlemi iptal edildi.")

finally:
    pwm.ChangeDutyCycle(0)  # Motoru durdur
    pwm.stop()
    GPIO.cleanup()

