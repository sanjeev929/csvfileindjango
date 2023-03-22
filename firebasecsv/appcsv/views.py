from django.shortcuts import render,redirect
import csv
import pandas as pd
import codecs
import pyrebase
Config = {
  "apiKey": "AIzaSyCSr25oefBynzz7dMyU1kllvcMzBiDhMGI",
  "authDomain": "test-50389.firebaseapp.com",
  "databaseURL": "https://test-50389-default-rtdb.firebaseio.com",
  "projectId": "test-50389",
  "storageBucket": "test-50389.appspot.com",
  "messagingSenderId": "940871427039",
  "appId": "1:940871427039:web:6bea61b95e28df01f91a6a",
  "measurementId": "G-VV9FMKCNB7"
}
firebase = pyrebase.initialize_app(Config)
db= firebase.database()
authe = firebase.auth()

def index(request):
    return render(request,'index.html')

def addfile(request):
    if request.method == 'POST':
        reader=request.FILES['myfile']
        read = csv.reader(codecs.iterdecode(reader, 'utf-8'))
        next(read)   
        for row in read:
            x=row[1]
            # name=len(row[0])
            # email=len([2])
            # city=len([3])
            # dob=len([4])
            # print("data length",name,email,city,dob)
            # if name and email and city and dob != 0: 
                # print("sucess")
            x = x.replace("p:","").replace("+91","").replace("+1","").replace("+78","").replace(" ","")
            try:
                numlen=len(x)
                print(numlen)
                if numlen < 10:
                    print('less than 10')
                    if numlen > 10:
                        x = x[1:]
                    y = {
                        "name":row[0],
                        "email":row[2],
                        "city":row[3],
                        "dob":row[4],
                        "phone-number":x
                        }
                    results = db.child("customer").child(x).update(y)             
            except Exception as e:
                print('Error issss ', e)
            # else:
            #     print("fail")
    return redirect(index)