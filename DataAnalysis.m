clc
clear
data = readtable('Gen_Data/log1.csv');
h = zeros(3, 1);


% Finding 2 second limit in data
time = data.time;
i = 1;
while time(i)-time(1) < 2
    i = i + 1;
end


X = data.rpm(1:i); % If using readtable
Y = data.time(1:i) - time(1); % If using readtable

% Rise peak
Peak = [0 0];
for i = 1:length(X)
    if Peak(1) < X(i)
        Peak(1) = X(i);
        Peak(2) = Y(i);
    end
end

% Settling time
lastVal = X(end);

overRange = lastVal*1.02;
underRange = lastVal*0.98;
settlingVal = [0 0];
count = length(X);
%for i = length(X):1
%    if underRange >= X(count) && X(count) >= overRange
        
    settlingVal = [X(count) Y(count)];
while count > 0 && underRange < X(count) && X(count) < overRange
    settlingVal = [X(count) Y(count)];
    count = count - 1;
end


color1 = [0.3010 0.7450 0.9330];
h(1) = plot(Y, X, 'Color', color1);
xlabel('X-axis Time (s)');
ylabel('Y-axis RPM');
title('RPM from 5V step');

hold on
p = plot(Peak(2), Peak(1), 'o', 'MarkerFaceColor', 'red', 'MarkerEdgeColor', 'black');

% Add label to the point
label_peak = sprintf('Peak value: %.2f RPM', Peak(1));
text(Peak(2), Peak(1), label_peak, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');

hold on
p2 = plot(settlingVal(2), settlingVal(1), 'o', 'MarkerFaceColor', 'cyan', 'MarkerEdgeColor', 'black');

label_settle = sprintf('Settling time: %.2f s', settlingVal(2));
text(settlingVal(2), settlingVal(1), label_settle, 'VerticalAlignment', 'top', 'HorizontalAlignment','left');


%%

data = readtable('Gen_Data/log2.csv');

% Finding 2 second limit in data
time = data.time;
i = 1;
while time(i)-time(1) < 2
    i = i + 1;
end


X = data.rpm(1:i); % If using readtable
Y = data.time(1:i) - time(1); % If using readtable

% Rise peak
Peak = [0 0];
for i = 1:length(X)
    if Peak(1) < X(i)
        Peak(1) = X(i);
        Peak(2) = Y(i);
    end
end

% Settling time
lastVal = X(end);

overRange = lastVal*1.02;
underRange = lastVal*0.98;
settlingVal = [0 0];
count = length(X);
%for i = length(X):1
%    if underRange >= X(count) && X(count) >= overRange
        
    settlingVal = [X(count) Y(count)];
while count > 0 && underRange < X(count) && X(count) < overRange
    settlingVal = [X(count) Y(count)];
    count = count - 1;
end


color2 = [0 0.4470 0.7410];
h(2) = plot(Y, X, 'Color', color2);
xlabel('X-axis Time (s)');
ylabel('Y-axis RPM');
title('RPM from 5V step');

hold on
p = plot(Peak(2), Peak(1), 'o', 'MarkerFaceColor', 'red', 'MarkerEdgeColor', 'black');

% Add label to the point
label_peak = sprintf('Peak value: %.2f RPM', Peak(1));
text(Peak(2), Peak(1), label_peak, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');

hold on
p2 = plot(settlingVal(2), settlingVal(1), 'o', 'MarkerFaceColor', 'cyan', 'MarkerEdgeColor', 'black');

label_settle = sprintf('Settling time: %.2f s', settlingVal(2));
text(settlingVal(2), settlingVal(1), label_settle, 'VerticalAlignment', 'top', 'HorizontalAlignment','left');

%%

data = readtable('Gen_Data/log4.csv');

% Finding 2 second limit in data
time = data.time;
i = 1;
while time(i)-time(1) < 2
    i = i + 1;
end


X = data.rpm(1:i); % If using readtable
Y = data.time(1:i) - time(1); % If using readtable

% Rise peak
Peak = [0 0];
for i = 1:length(X)
    if Peak(1) < X(i)
        Peak(1) = X(i);
        Peak(2) = Y(i);
    end
end

% Settling time
lastVal = X(end);

overRange = lastVal*1.02;
underRange = lastVal*0.98;
settlingVal = [0 0];
count = length(X);
%for i = length(X):1
%    if underRange >= X(count) && X(count) >= overRange
        
    settlingVal = [X(count) Y(count)];
while count > 0 && underRange < X(count) && X(count) < overRange
    settlingVal = [X(count) Y(count)];
    count = count - 1;
end


color3 = [0.4940 0.1840 0.5560];
h(3) = plot(Y, X, 'Color', color3);
xlabel('X-axis Time (s)');
ylabel('Y-axis RPM');
title('RPM response from Voltage step');

hold on
p = plot(Peak(2), Peak(1), 'o', 'MarkerFaceColor', 'red', 'MarkerEdgeColor', 'black');

% Add label to the point
label_peak = sprintf('Peak value: %.2f RPM', Peak(1));
text(Peak(2), Peak(1), label_peak, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');

hold on
p2 = plot(settlingVal(2), settlingVal(1), 'o', 'MarkerFaceColor', 'cyan', 'MarkerEdgeColor', 'black');

label_settle = sprintf('Settling time: %.2f s', settlingVal(2));
text(settlingVal(2), settlingVal(1), label_settle, 'VerticalAlignment', 'top', 'HorizontalAlignment','left');
hold off;


legend(h, {'5V', '10V', '15V'}, 'Location', 'southeast');

xlim([min(Y) 2]);
