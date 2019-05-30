from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import MessageModel
from .serializers import MessageSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.renderers import AdminRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
# Include the `fusioncharts.py` file that contains functions to embed the charts.
from fusioncharts import FusionCharts
from rest_framework import generics


import math
import os

    
def post(request, format='json'):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            token = Token.objects.create(user=user)
            json = serializer.data
            json['token'] = token.key
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
    #renderer_classes = (AdminRenderer,)
    renderer_classes = (JSONRenderer, )

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        data_dict = request.data
        pData1 = math.log10(float(data_dict["pd1r1"])/float(data_dict["pd1ir1"]))#LEDData0(i,1)= log10(JONPD1_RED1(i,1)/JONPD1_IR1(i,1));
        pData2 = math.log10(float(data_dict["pd2r2"])/float(data_dict["pd1ir2"]))#LEDData1(i,1)= log10(JONPD2_RED2(i,1)/JONPD1_IR2(i,1));
        pData3 = math.log10(float(data_dict["pd3r3"])/float(data_dict["pd1ir3"]))#LEDData2(i,1)= log10(JONPD3_RED1(i,1)/JONPD1_IR3(i,1));

        request.data["processedData1"]=pData1
        request.data["processedData2"]=pData2
        request.data["processedData3"]=pData3 # this willbe changed later but keep variable name the same to be used in StO2

        D2 = pData3-2*pData2+pData1 #D2(i,1)=(LEDData2(i,1)-2*LEDData1(i,1)+LEDData0(i,1));
        request.data["StO2"]=100*(-1.4*D2**3+4.82*D2**2-5.66*D2+2.38) #StO2(i,1)= 100*(-1.4*D2(i,1)^3+4.82*D2(i,1)^2-5.66*D2(i,1)+2.38);

        if serializer.is_valid():
            self.perform_create(serializer)
            #headers = self.get_success_headers(serializer.data)


            #print(request.data)
            #convert JSON data into a python dictionary
            filename = "infodata.txt"
            file=open("data/" + filename, "a+")
            file.write( str(data_dict) + "," + "\n") 
            file.close()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
class MessageList(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'message_list.html'

    def get(self, request):
        queryset = MessageModel.objects.all()
        return Response({'message': queryset})
 

####my func

def StO2(request):

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Tissue Oxygenation Visualization",
            "xAxisName": "Time", "labeldisplay": "rotate",
            "yAxisName": "StO2(units)",
            "theme": "fusion",
            "showvalues": "0",
            "drawAnchors": "0"
        }
    dataSource['data'] = []

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key in MessageModel.objects.all():
        data = {}
        data["label"] = key.date
        data["value"] = key.StO2
        dataSource["data"].append(data)


# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
    PPG_line = FusionCharts("line", "PPGChart", "1000", "800", "StO2-container", "json", dataSource)
    return render(request, 'index1.html', {
        'output_StO2': PPG_line.render()
    })

