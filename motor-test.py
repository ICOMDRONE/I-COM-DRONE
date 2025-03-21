import RPi.GPIO as GPIO
from time import sleep

# GPIO ayarları
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # ESC için PWM çıkışı

# PWM ayarları
pwm = GPIO.PWM(18, 50)  # 50 Hz frekans (ESC için uygun)
pwm.start(0)

def calibrate_esc():
    """ESC'yi kalibre etmek için yüksek, düşük ve normal PWM sinyali gönderir."""
    print("ESC kalibrasyonu başlıyor...")
    pwm.ChangeDutyCycle(10)  # Maksimum throttle (örneğin 2 ms PWM, %10 duty cycle)
    sleep(2)  # ESC'yi bu seviyede 2 saniye beklet
    pwm.ChangeDutyCycle(5)  # Minimum throttle (örneğin 1 ms PWM, %5 duty cycle)
    sleep(2)  # ESC'yi bu seviyede 2 saniye beklet
    print("ESC kalibrasyonu tamamlandı.")

try:
    calibrate_esc()
    print("Motor döndürülüyor...")
    pwm.ChangeDutyCycle(6)  # Motoru düşük hızda döndürmek için PWM sinyali
    while True:
        sleep(1)  # Motoru döndürmeye devam et
except KeyboardInterrupt:
    print("Çıkılıyor...")
finally:
    pwm.ChangeDutyCycle(0)  # Motoru durdur
    pwm.stop()
    GPIO.cleanup()
