import csv
import os
import math

class PPGdataPoint:
    size = -1 #dataset number of points
    meanR = 0
    meanIR = 0

    def __init__(self,time,pd1r1,pd1ir1):
        self.time = time
        self.pd1r1 = pd1r1
        self.pd1ir1 = pd1ir1
        PPGdataPoint.size += 1
        PPGdataPoint.meanR = (PPGdataPoint.meanR*PPGdataPoint.size + self.pd1r1)/(PPGdataPoint.size + 1)
        PPGdataPoint.meanIR = (PPGdataPoint.meanIR*PPGdataPoint.size + self.pd1ir1)/(PPGdataPoint.size + 1)

data = []

#path =  'C:\\....' # Set path of new directory here
#os.chdir(path) # changes the directory
#from apiengine.models import PPGModel # imports the model
with open('RHPN3-M-1-middlefinger.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    volt_const = 5*1000/1023
    for row in reader:
        data.insert(0,PPGdataPoint( float(row['time']) , volt_const*float(row['pd1r1']) , volt_const*float(row['pd1ir1']) ))
        print(PPGdataPoint.meanR)
        

    sampleRate = PPGdataPoint.size/(data[0].time-data[PPGdataPoint.size].time)
    print("===============")
    print(sampleRate)
    print(PPGdataPoint.size)
    print(PPGdataPoint.meanR)
    print(PPGdataPoint.meanIR)
        #p = MessageModel(time = val_time,
         #   pd1r1=val_pd1r1, pd1ir1=val_pd1ir1,
          #  processedData=(float(val_pd1r1)/float(val_pd1ir1))
           # )
        #p.save()


