# --- when run, will begin logging moisture data from IoT
# --- at 5 min intervals, then upload the data to Amazon S3
# --- bucket hourly.
from datetime import datetime
from time import sleep
import numpy as np
import random

def datapoint():
  """create data point and add it to value_log and time_log"""
  ts = datetime.now()

  value = random.uniform(0,10)
  t = np.array([ts.year,ts.month,ts.day,ts.hour,ts.minute, ts.second])

  value_log[datapoint.count] = value
  time_log[datapoint.count] = t

  print('count is: ' + str(datapoint.count))
  datapoint.count += 1

def upload_s3():
  """adding value_log and time_log values accumulated
  over last hour to Amazon s3 bucket"""
  print('uploading to S3')


datapoint.count = 0
interval = 5
total_points = 30
value_log = np.empty(total_points, dtype=float)
time_log = np.empty((total_points,6), dtype=int)

def main():
  for i in range(total_points):
    if (datapoint.count % 5 == 0 and not datapoint.count == 0):
      upload_s3()

    datapoint()
    print('value log is: ')
    print(value_log[:datapoint.count])
    print('latest time is: ')
    print(time_log[datapoint.count-1])
    print('')
    sleep(interval)    

#  print('value log is: ')
#  print(value_log)
#  print('time log is: ')
#  print(time_log)


if __name__ == '__main__':

  main()

