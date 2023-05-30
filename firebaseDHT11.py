import pyrebase
import time
from myDHT11 import dht11
config = {apiKey: "AIzaSyCTmSN8k4xQR6ZpUgmbwQS2cwB_HJQIsR0",
          authDomain: "rasppiweatherstation.firebaseapp.com",
          databaseURL: "https://rasppiweatherstation-default-rtdb.firebaseio.com",
          projectId: "rasppiweatherstation",
          storageBucket: "rasppiweatherstation.appspot.com",
          messagingSenderId: "1065055372685",
          appId: "1:1065055372685:web:fdcb5287da6844785aa9c4",
          measurementId: "G-TDGJ4Q6P9L"
          };
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
database = firebase.database()
a = dht11()
time.sleep(10)
print(a)
data = {"key1":a}
database.set(data)
print('hello')
