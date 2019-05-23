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
        request.data["processedData"]=int(request.data["pd1r1"])/int(request.data["pd2r2"])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)


        #print(request.data)
        #convert JSON data into a python dictionary
        data_dict = request.data
        '''filename = str(data_dict["date"]) + "_" + ".txt"''';#+ "_" + str(data_dict["time"]) + ".txt";
        filename = "infodata.txt"
        file=open("data/" + filename, "a+")
        file.write( str(data_dict["date"]) + ", "
                    + str(data_dict["pd1r1"]) + "," + str(data_dict["pd2r1"]) + "," 
                    + str(data_dict["pd3r1"]) + "," + str(data_dict["pd1ir1"]) + "," 
                    + str(data_dict["pd2ir1"]) + "," + str(data_dict["pd3ir1"]) + "," 
                    + str(data_dict["pd1r2"]) + "," + str(data_dict["pd2r2"]) + "," 
                    + str(data_dict["pd3r2"]) + "," + str(data_dict["pd1ir2"]) + "," 
                    + str(data_dict["pd2ir2"]) + "," + str(data_dict["pd3ir2"]) + ","
                    + str(data_dict["pd1r3"]) + "," + str(data_dict["pd2r3"]) + "," 
                    + str(data_dict["pd3r3"]) + "," + str(data_dict["pd1ir3"]) + "," 
                    + str(data_dict["pd2ir3"]) + "," + str(data_dict["pd3ir3"]) + ","
                    + str(data_dict["processedData"]) + "," + "\n") 
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

