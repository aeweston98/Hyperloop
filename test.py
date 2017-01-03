import serial

ser = serial.Serial('/dev/cu.usbmodem0E218D01')

while True:
	data = ser.read()
	print(data)
