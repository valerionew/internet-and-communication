#Would int be really cool if we could also plot the response times?

import requests   # http library
import matplotlib # Plot library

import matplotlib.pyplot as myplot # shorten the funciton name

measurements = []

for i in range(10):
    r = requests.get('https://www.google.com')
    measurements.append(r.elapsed.microseconds / 1000)

average = sum(measurements)/len(measurements)

# plot functions
myplot.figure()
myplot.plot(measurements)
myplot.axhline(y=average, color='r', linestyle='-')
myplot.ylim([0,max(measurements)])
myplot.xlabel("Measurement ID (order)")
myplot.ylabel("Response time [ms]")
myplot.title("Response time plot from google.com")
myplot.grid()
myplot.show()
