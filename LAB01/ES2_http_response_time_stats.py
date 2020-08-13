# Making a single request and meausiring the time isn't very significant.
# Instead, we want to make multiple measurements

import requests # http library

measurements = [] # init the variable measurments

for i in range(10):
    r = requests.get('https://www.google.com')
    measurements.append(r.elapsed.microseconds / 1000)

print('Min time: ',min(measurements), 'ms')
print('Max time: ',max(measurements), 'ms')
print('Avg tine: ',round(sum(measurements)/len(measurements),3), 'ms')
