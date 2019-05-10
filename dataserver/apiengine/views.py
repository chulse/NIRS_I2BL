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
# Include the `fusioncharts.py` file that contains functions to embed the charts.
from fusioncharts import FusionCharts
from rest_framework import generics

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
    renderer_classes = (AdminRenderer,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)


        print(request.data)
        #convert JSON data into a python dictionary
        data_dict = request.data
        '''filename = str(data_dict["date"]) + "_" + str(data_dict["time"]) + ".txt";'''
        filename = "infodata.txt"
        file=open("data/" + filename, "a+")
        file.write( str(data_dict["date"]) + ", "
                    + str(data_dict["time"]) + "," + str(data_dict["vinput"]) + "," 
                    + str(data_dict["voutunfiltered"]) + "," + str(data_dict["runfiltered"]) + "," 
                    + str(data_dict["voutfiltered"]) + "," + str(data_dict["rfiltered"]) + "," 
                    + str(data_dict["frequency"]) + "," + "\n") 
        file.close()
        return Response({})
    

    
class MessageList(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'message_list.html'

    def get(self, request):
        queryset = MessageModel.objects.all()
        return Response({'message': queryset})
 

####my func

def PD1R1(request):

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "PD1R1",
            "xAxisName": "Time",
            "yAxisName": "PD1R1(units)",
            "theme": "fusion",
            "showvalues": "0",
            "drawAnchors": "0"
        }
    dataSource['data'] = []

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key in MessageModel.objects.all():
        data = {}
        data["label"] = key.date
        data["value"] = key.pd1r1
        dataSource["data"].append(data)


# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
    pd1r1_line = FusionCharts("line", "PD1R1Chart", "1000", "800", "PD1R1-container", "json", dataSource)
    return render(request, 'index1.html', {
        'output_pd1r1': pd1r1_line.render()
    })

#####
def inputVoltage(request):

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Input Voltage",
            "xAxisName": "Time",
            "yAxisName": "Vin(V)",
            "theme": "fusion",
            "showvalues": "0",
            "drawAnchors": "0"
        }
    dataSource['data'] = []

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key in MessageModel.objects.all():
        data = {}
        data["label"] = key.time
        data["value"] = key.vinput
        dataSource["data"].append(data)


# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
    vin_line = FusionCharts("line", "inputVoltageChart", "1000", "800", "inputVoltageChart-container", "json", dataSource)
    return render(request, 'index1.html', {
        'output_vin': vin_line.render()
    })


def VoutUnfiltered(request):

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Unfiltered Output Voltage",
            "xAxisName": "Time",
            "yAxisName": "Vout(V)",
            "theme": "fusion",
            "drawAnchors": "0",
            "showvalues": "0"
        }
    dataSource['data'] = []

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key in MessageModel.objects.all():
        data = {}
        data["label"] = key.time
        data["value"] = key.voutunfiltered
        dataSource["data"].append(data)


# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
    voutun_line = FusionCharts("line", "outputVoltageUnChart", "1000", "800", "outputVoltageUnChart-container", "json", dataSource)
    return render(request, 'index2.html', {
        'output_voutun': voutun_line.render()
    })


def VoutFiltered(request):

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Filtered Output Voltage",
            "xAxisName": "Time",
            "yAxisName": "Vout(V)",
            "theme": "fusion",
            "drawAnchors": "0",
            "showvalues": "0"
        }
    dataSource['data'] = []

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key in MessageModel.objects.all():
        data = {}
        data["label"] = key.time
        data["value"] = key.voutfiltered
        dataSource["data"].append(data)


# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
    vout_line = FusionCharts("line", "outputVoltageChart", "1000", "800", "outputVoltageChart-container", "json", dataSource)
    return render(request, 'index3.html', {
       'output_vout': vout_line.render()
    })

def resistanceUnfiltered(request):

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Unfiltered Resistance",
            "xAxisName": "Time",
            "yAxisName": "Resistance(Ohm)",
            "theme": "fusion",
            "showvalues": "0",
            "drawAnchors": "0"
        }
    dataSource['data'] = []

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key in MessageModel.objects.all():
        data = {}
        data["label"] = key.time
        data["value"] = key.runfiltered
        dataSource["data"].append(data)


# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
    run_line = FusionCharts("line", "RUnChart", "1000", "800", "RUnChart-container", "json", dataSource)
    return render(request, 'index4.html', {
        'output_run': run_line.render()
    })




def resistanceFiltered(request):

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Filtered Resistance",
            "xAxisName": "Time",
            "yAxisName": "Resistance(Ohm)",
            "theme": "fusion",
            "showvalues": "0",
            "drawAnchors": "0"
        }
    dataSource['data'] = []

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key in MessageModel.objects.all():
        data = {}
        data["label"] = key.time
        data["value"] = key.rfiltered
        dataSource["data"].append(data)


# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
    r_line = FusionCharts("line", "RChart", "1000", "800", "RChart-container", "json", dataSource)
    return render(request, 'index5.html', {
        'output_r': r_line.render()
    })




