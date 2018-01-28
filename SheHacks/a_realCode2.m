% DELETE ANY OLD SERIAL DATA
% ***************************
upperLpath='C:\Users\julia\Google Drive\SheHacks';
lowerLpath='C:\Users\julia\Google Drive\SheHacks\audio';

cd(upperLpath);
a = instrfindall;
delete(a)
clc

% SET UP CONNECTIONS, VARIABLES, OBJECTS
% **************************************
x=0.1:0.1:45;
iLast=0;
counter = 0;
recObj=audiorecorder;

arduino=serial('COM3','BaudRate',9600);
fopen(arduino);

% CONSTANTLY LOOK FOR SOUND, RECORD IF SOUND DETECTED
% ***************************************************
for i=1:length(x)
    
    % print current clock timer
    clc
    time=i/10;
    fprintf('Timer: %f\n',time)
    
    % read sensor
    y(i)=fscanf(arduino,'%d');
    
    % record me maybe?
    if y(i) > 750 && i-iLast>40
        
        % prepare to record
        
        iLast=i;
        disp('Audio detected!');
        disp('Recording in 2 seconds.');
        pause(2);
        cd(lowerLpath);
        counter = counter + 1;
        fileName={strcat('file',num2str(counter),'.flac')};
        fileNames(counter,1)=fileName;
        blueLED=1;
        fprintf(arduino,blueLED);
        disp('Recording now.')
        
        % record for 5 seconds
        recordblocking(recObj,5);
        
        % write audio data
        audiodata=getaudiodata(recObj);
        audiowrite(fileName{1},audiodata,8192);
        
        % end recording phase
        disp('Audio recorded successfully.')
        blueLED=0;
        fprintf(arduino,blueLED);
        cd(upperLpath);
        
    end
        
    % a check to prevent an excessive number of recordings per session    
    if counter > 4
        break
    end
    
end


% DISCONNECT, PLOT, SHOW FILE NAMES
% *********************************

fclose(arduino);

h=max(size(y));
x=x(1:h);

plot(app.UIAxes,x,y);
app.UITable.Data=fileNames;

delete(arduino);
clear arduino

% end

