print("main")

# From: https://www.hackster.io/shilleh/connect-mpu-6050-to-raspberry-pi-pico-w-7f3345

# Shows Pi is on by turning on LED when plugged in
LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()


from GY_521.imu import MPU6050
from time import sleep
from machine import Pin, I2C
from GY_521.orientation import calculate_orientation


# i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000) # XIAO RP2040
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000) # Pico
imu = MPU6050(i2c)


while True:
	ax=round(imu.accel.x,2)
	ay=round(imu.accel.y,2)
	az=round(imu.accel.z,2)
	gx=round(imu.gyro.x)
	gy=round(imu.gyro.y)
	gz=round(imu.gyro.z)
	tem=round(imu.temperature,2)
	pitch, roll, yaw = calculate_orientation(imu.accel.x, imu.accel.y, imu.accel.z, imu.gyro.x, imu.gyro.y, imu.gyro.z, delta_time=0.2)
	print(f"Pitch: {pitch:.2f}°, Roll: {roll:.2f}°, Yaw: {yaw:.2f}°")
	#print("ax",ax,"\t","ay",ay,"\t","az",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","Temperature",tem,"        ",end="\r")
	sleep(0.2)