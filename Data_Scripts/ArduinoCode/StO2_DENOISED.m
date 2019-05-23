%Specifiy directory and worksheet you want to access
Directory = '/Users/sihan/Box Sync/I2BL Lab/IC PhD Project/PhD Proposal Content/CORELAB-Nature Biomed/NIRS/Experiments/3-29-2019 Corelab Oxy 1/';
Sheet1 = 'Jonathan RATN2.xlsx';

%Specify the excel sheet colums/ranges that you want to import 
xlRange1 = 'C1:C109';
xlRange2 = 'I1:I109';
xlRange3 = 'Q1:Q109';
xlRange4 = 'U1:U109';
xlRange5 = 'E1:E109';
xlRange6 = 'AG1:AG109';
xlRange7 = 'U1:U109';

JONPD1_RED1 = xlsread(strcat(Directory , Sheet1), xlRange1);
JONPD1_IR1 = xlsread(strcat(Directory , Sheet1), xlRange2);
JONPD2_RED2 = xlsread(strcat(Directory , Sheet1), xlRange3);
JONPD1_IR2 = xlsread(strcat(Directory , Sheet1), xlRange4);
JONPD3_RED1 = xlsread(strcat(Directory , Sheet1), xlRange5);
JONPD1_IR3 = xlsread(strcat(Directory , Sheet1), xlRange6);
JONPD2_IR2=xlsread(strcat(Directory , Sheet1), xlRange7);

%Initialize arrays
lenLEDData=length(JONPD1_RED1);
LEDData0=zeros(lenLEDData,1);
LEDData1=zeros(lenLEDData,1);
LEDData2=zeros(lenLEDData,1);
D2=zeros(lenLEDData,1);

%Calculate Tissue Attenuation (TA) as log of ratio between signal/reference
%intensity, then measure D2 array which is calculated with X660-2*X700+X740
i=1;
while i <=(lenLEDData)
    if i <= (lenLEDData)
        LEDData0(i,1)= log10(JONPD1_RED1(i,1)/JONPD1_IR1(i,1));
        LEDData1(i,1)= log10(JONPD2_RED2(i,1)/JONPD1_IR2(i,1));
        LEDData2(i,1)= log10(JONPD3_RED1(i,1)/JONPD1_IR3(i,1));
        D2(i,1)=(LEDData2(i,1)-2*LEDData1(i,1)+LEDData0(i,1));
        StO2(i,1)= 100*(-1.4*D2(i,1)^3+4.82*D2(i,1)^2-5.66*D2(i,1)+2.38);
    end
    i=i+1;
end

%Calculate StO2 using this formula
StO2 = wthresh(StO2,'s',2.6);

%Plot Values
figure;
x=1:length(JONPD2_RED2);
y1 = JONPD2_RED2; 
yyaxis left
plot(x,y1,'g')
yyaxis right
plot(x,StO2)
title('IR2 StO2')

[SIGDEN,~,thrParams,~,BestNbOfInt] = cmddenoise(StO2,'db3',12);
disp(StO2)
x=1:1:109;

%Plot Values
figure;
y1 = JONPD2_RED2; 
yyaxis left
plot(x,y1,'g')
yyaxis right
plot(x,SIGDEN)
title('IR2 StO2')


