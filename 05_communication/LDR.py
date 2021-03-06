import spidev
import time
import RPi.GPIO as GPIO

# SPI 인스턴스 생성
spi = spidev.SpiDev()

PIN_LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

# SPI 통신 시작
spi.open(0, 0) #bus : 0, device  : 0 (CE0, CE1)

# SPI 최대 통신 속도 설정
spi.max_speed_hz = 100000

# 채널에서 읽어온 아날로그값을 디지털로 변환하여 리턴하는 함수
def analog_read(channel):
    # [byte_1, byte_2, byte_3]
    # byte_1 : 1
    # byte_2 : channel(0) + 8 = 0000 1000 << 4 -> 1000 0000
    # byte_3 : 0
    ret = spi.xfer2([1, (channel + 8) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0)

        if(reading > 512):
            GPIO.output(PIN_LED, GPIO.HIGH)
        else:
             GPIO.output(PIN_LED, GPIO.LOW)

        print("Reading=%d" % reading) # 0~1023
        time.sleep(0.5)
finally:
    spi.close()




import spidev
import time

# SPI 인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작
spi.open(0, 0) #bus : 0, device  : 0 (CE0, CE1)

# SPI 최대 통신 속도 설정
spi.max_speed_hz = 100000

# 채널에서 읽어온 아날로그값을 디지털로 변환하여 리턴하는 함수
def analog_read(channel):
    # [byte_1, byte_2, byte_3]
    # byte_1 : 1
    # byte_2 : channel(0) + 8 = 0000 1000 << 4 -> 1000 0000
    # byte_3 : 0
    ret = spi.xfer2([1, (channel + 8) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0)
        if(reading<512):
            GPIO.output(LED_PIN_1, GPIO.HIGH) 
        time.sleep(1)
finally:
    spi.close()