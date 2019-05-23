import csv
import os
import math

#path =  'C:\\....' # Set path of new directory here
#os.chdir(path) # changes the directory
from apiengine.models import MessageModel # imports the model
with open('Jonathan_RATN2.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
            val_pd1r1=row['pd1r1']
            val_pd2r1=row['pd2r1']
            val_pd3r1=row['pd3r1']

            val_pd1ir1=row['pd1ir1']
            val_pd2ir1=row['pd2ir1']
            val_pd3ir1=row['pd3ir1']

            val_pd1r2=row['pd1r2']
            val_pd2r2=row['pd2r2']
            val_pd3r2=row['pd3r2']

            val_pd1ir2=row['pd1ir2']
            val_pd2ir2=row['pd2ir2']
            val_pd3ir2=row['pd3ir2']

            val_pd1r3=row['pd1r3']
            val_pd2r3=row['pd2r3']
            val_pd3r3=row['pd3r3']

            val_pd1ir3=row['pd1ir3']
            val_pd2ir3=row['pd2ir3']
            val_pd3ir3=row['pd3ir3']

            #ratio_1 = math.log(float(val_pd1r1)/float(val_pd1ir1))
            #ratio_2 = math.log(float(val_pd2r2)/float(val_pd1ir2))
            #ratio_3 = math.log(float(val_pd3r3)/float(val_pd1ir3))
            ####TBD need the algorithm updated

            p = MessageModel(date = row['date'],
                pd1r1=val_pd1r1, pd2r1=val_pd2r1,
                pd3r1=val_pd3r1,pd1ir1=val_pd1ir1,
                pd2ir1=val_pd2ir1, pd3ir1=val_pd3ir1,
                pd1r2=val_pd1r2, pd2r2=val_pd2r2,
                pd3r2=val_pd3r2,pd1ir2=val_pd1ir2,
                pd2ir2=val_pd2ir2, pd3ir2=val_pd3ir2,
                pd1r3=val_pd1r3, pd2r3=val_pd2r3,
                pd3r3=val_pd3r3,pd1ir3=val_pd1ir3,
                pd2ir3=val_pd2ir3, pd3ir3=val_pd3ir3,
                processedData=(float(val_pd1r1)/float(val_pd1ir1))
                )
            p.save()


