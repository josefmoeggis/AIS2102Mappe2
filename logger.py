import csv
import os
import time

LOGGING = False

fieldnames = [
    "time",
    "motor_angle",
    "motor_setpoint",
    "pendulum_angle",
    "pendulum_setpoint",
    "rpm",
    "voltage",
    "current",
    "error",
    "x_hat1",
]

files = 0
directory = os.path.join(os.curdir, "Gen_Data")

output_dir = 'CSV_sourcecodePos/OurData'
filename = f'{output_dir}/saved_dataposObserver2.csv'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Check if the directory exists
"""if os.path.exists(directory) and os.path.isdir(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            files += 1

    print(f"Number of files in 'Gen_Data': {files}")
else:
    print("The 'Gen_Data' directory does not exist.")

filename = f"Gen_Data/log{files}.csv"
"""

counter = 0
startTime = time.time()


def enableLogging():
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    global LOGGING
    LOGGING = True


def save_data(data, error, x_hat1):
    if not LOGGING:
        return
    global counter
    global filename
    elapsedTime = round(time.time() - startTime, 3)

    with open(filename, "a", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info = {
            "time": elapsedTime,
            "motor_angle": data[0],
            "motor_setpoint": data[1],
            "pendulum_angle": data[2],
            "pendulum_setpoint": data[3],
            "rpm": data[4],
            "voltage": data[5],
            "current": data[6],
            "error" : error,
            "x_hat1" : x_hat1,
        }
        csv_writer.writerow(info)
