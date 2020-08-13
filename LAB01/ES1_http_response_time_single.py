# We evaluate the response time of a server via http. We will use the Google server and the requests library.

import requests # http library

r = requests.get('https://www.google.com') # make a GET request to the server, puts in the r variabile some informations.

# which type r is?
print('The r variable is: ', type(r))

# Confirm the URL we contacted
print('We contacted: ', r.url)

# Status code classes:
# 2xx Success
#   200 = OK
# 4xx Client error
#   400 = Bad Request (syntax error?)
#   404 = Not Found
# 5xx Server error
print('We received status code: ', r.status_code)

# We want to get the response time. We convert the time in microseconds and divide by 1000 to get milliseconts
print('Response time:', r.elapsed.microseconds / 1000, 'ms')
