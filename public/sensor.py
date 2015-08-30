#!/usr/bin/env python
import os
import random
import time 

var = 1
while var == 1 :

  f = open(os.path.dirname(os.path.abspath(__file__))+"/test.json", 'w')
  x =random.uniform(27,27.5);
  y =random.uniform(60.1,60.9);
  f.write('{\"temp\":'+str(x)+', \"hum\":'+str(y)+'}') 
  time.sleep(3)  # Delay for 1 minute (60 seconds)

