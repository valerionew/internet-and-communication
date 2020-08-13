# Now we want to compare different servers response time. We choose to compare 3 http servers (google, github and my website)

import requests
import matplotlib.pyplot as myplot # shorten the funciton name

websites = ['https://www.google.com', 'https://www.github.com', 'https://valerionappi.it']

myplot.figure()

for url in websites:
    print('We are testing: ', url)

    measurements = []
    for i in range(10):
        r = requests.get(url)
        measurements.append(r.elapsed.microseconds / 1000)

    myplot.plot(measurements, label=url)

    print('Min time: ',min(measurements), 'ms')
    print('Max time: ',max(measurements), 'ms')
    print('Avg tine: ',round(sum(measurements)/len(measurements),3), 'ms\n')



myplot.xlabel("Measurement ID (order)")
myplot.ylabel("Response time [ms]")
myplot.legend()
myplot.title("Response time plot from google.com")
myplot.grid()
myplot.show()
