import mysql.connector
import Adafruit_DHT
import time

# Connect to MariaDB
cnx = mysql.connector.connect(user='anshu', password='Anshu@1234', port='3306',
                              host='127.0.0.1', database='WEATHERSTATION')
cursor = cnx.cursor()

# DHT sensor setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    # Read temperature and humidity values from DHT sensor
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    # Insert values into database
    add_reading = ("INSERT INTO weathereadings "
                   "(temperature, humidity) "
                   "VALUES (%s, %s)")
    data = (temperature, humidity)
    cursor.execute(add_reading, data)
    cnx.commit()

    # Wait for 5 seconds before taking another reading
    time.sleep(5)

# Clean up
cursor.close()
cnx.close()

