% Max Gong modified this code 
% GOAL: Signal processing to obtain usable PPG signal
% WHAT CODE DOES: Plot data, filtered data, FFT

%% Load Data
clear all
Directory = '/Users/999mg/Documents/I2BL/Data/5-7-19 PPG M H/';             % Import from xlsx
Sheet1 = 'RHPN3-M-1-middlefinger.xlsx';
xlRange1 = 'A1:A1000';
xlRange2 = 'C1:C1000';                                                     % IF CHANGE, MUST CHANGE L
L = 1000;                                                                  % L = length of data
fs = 104; 

Time = xlsread(strcat(Directory , Sheet1), xlRange1);  
LED1_R = xlsread(strcat(Directory , Sheet1), xlRange2);

mdates = datenum('30-Dec-1899')+Time;
t = datestr(mdates,'dd-mm-yyyy HH:MM:ss.FFF');
t = datetime(t, 'InputFormat', 'dd-MM-yyyy HH:mm:ss.SSS');
t.Format = 'dd-MM-yyyy HH:mm:ss.SSS';                                       % Convert dates to time format
y = LED1_R(:,1);                                                            % LED data
time = (datenum(t)-datenum(t(1)))*24*3600;
samples = 1:L; 

% convert analogRead to mV
y = y * (5*1000/1023);


% %% LPF & HPF data (LPF 4 Hz, HPF 0.5 Hz)
% figure(1)
% y_M = y - mean(y);                                                          % Remove DC offset for sake of finding frequency
% Wn = ([0.5, 3]) / (fs/2);                                                   % Normalized bandpass, input is cutoff frequencies
% [b,a] = butter(5, Wn);                                                      % 5th order Butterworth bandpass filter
% y_Filt = filter(b,a,y_M)+mean(y);
% plot(t,y)                                                                   % Plot raw data
% hold on
% plot(t,y_Filt,'LineWidth',2)                                                % Plot filtered data
% legend('Input Data','Filtered Data')
% xlabel('Time (HH:MM:SS.FFF)')
% ylabel('Photodetector (mV)')


%% Plot only samples, not time
figure
set(gcf, 'Units', 'Normalized', 'OuterPosition', [0.04, 0.04, 0.9, 0.9]);       % Enlarge figure to full screen.
y_M = y - mean(y);                                                          % Remove DC offset for sake of finding frequency
Wn = ([0.5, 3.5]) / (fs/2);                                                   % Normalized bandpass, input is cutoff frequencies
[b,a] = butter(5, Wn);                                                      % 5th order Butterworth bandpass filter
y_Filt = filter(b,a,y_M)+mean(y);

subplot(2,2,1)
plot(samples,y)  
% hold on
% plot(samples,y_Filt,'LineWidth',2)                                                % Plot filtered data
% legend('Input Data','Filtered Data')
ylabel('Photodetector (mV)')
xlabel('Samples')
title('Raw Signal')


%% Plot filtered data
subplot(2,2,2)
plot(samples,y_Filt-mean(y),'LineWidth',2)
title('Filtered Signal')
ylabel('Photodetector (mV)')
set(gca,'XTick',[])
a2 = axes('XAxisLocation','Bottom');
subplot(2,2,2,a2)
set(a2, 'color', 'none')
set(a2, 'YTick', [])
set(a2, 'XLim', [0 time(L)])
xlabel('Time (s)')


%% Plot FFT of data vs. filtered data 
y_M = y - mean(y);                                                          % Remove DC offset for sake of finding frequency
Y = fft(y_M);            
P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

y_Filt_M = y_Filt - mean(y_Filt);                                           % Remove DC offset for sake of finding frequency
Y_filt = fft(y_Filt_M);            
P2_f = abs(Y_filt/L);
P1_f = P2_f(1:L/2+1);
P1_f(2:end-1) = 2*P1_f(2:end-1);

f = fs*(0:(L/2))/L;

subplot(2,2,[3,4])
plot(f,P1) 
% hold on
% plot(f,P1_f,'LineWidth',2)
title('FFT of PPG signal')
% legend('Input Data','Filtered Data')
xlabel('f (Hz)')
ylabel('|FFT(y)|')


  





