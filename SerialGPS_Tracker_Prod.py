import serial
import time
import os

ser = serial.Serial('COM3')  # open serial port
print(ser.name)         # check which port was really used


at1= [b'AT\r\n',b'AT+VER=?\r\n',b'AT+DEUI=?\r\n',b'AT+APPEUI=?\r\n',
      b'AT+APPKEY=?\r\n',b'AT+NWKSKEY=?\r\n',b'AT+MD=?\r\n',
      b'AT+KAT=?\r\n',b'AT+TDC=?\r\n',b'AT+FTIME=?\r\n',
      b'AT+CHE=?\r\n',b'AT+LON=?\r\n',b'AT+MLON=?\r\n',b'AT+SGM=?\r\n']

for i in at1:
	ser.write(i)
	time.sleep(2)
	print(i.decode())
	reply=ser.read(ser.inWaiting()) #clear buffer
	reply = reply.decode()
	print('Linea:'+reply)


ser.close()


print("DIGA S O s PARA CONTINUAR")
respuesta = input("¿Desea continuar el programa?: ")

while respuesta == "S" or respuesta == "s":
	print('Settiando valores para el contexto....')

	ser = serial.Serial('COM3')  # open serial port
	print(ser.name)         # check which port was really used

		
	appeui=b'AT+APPEUI=a000000000000119\r\n'

	at1= [b'AT\r\n',appeui,b'AT+MD=1\r\n',
	      b'AT+KAT=21600000\r\n',b'AT+TDC=60000\r\n',b'AT+FTIME=600\r\n',
	      b'AT+CHE=2\r\n',b'AT+LON=0\r\n',b'AT+MLON=0\r\n',b'AT+SGM=0\r\n',b'ATZ\r\n']

	for i in at1:
		ser.write(i)
		time.sleep(3)
		if i==b'ATZ\r\n':
			time.sleep(10)
		print(i.decode())
		reply=ser.read(ser.inWaiting()) #clear buffer
		reply = reply.decode()
		print('Linea:'+reply)


	ser.close()
	
	respuesta = input("¿Desea continuar el programa?: ")
	
print("¡Hasta la vista!")




