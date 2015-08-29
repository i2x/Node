#!/usr/bin/python
import random
import time 

var = 1
while var == 1 :
  f = open("/var/www/html/node/public/test.json", 'w')
  x =random.uniform(26.9,27.3);
  y =random.uniform(60.1,60.9);
  f.write('{\"temp\":'+str(x)+', \"hum\":'+str(y)+'}') 
  time.sleep(1)  # Delay for 1 minute (60 seconds)

