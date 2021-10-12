import requests
url = "https://www.geeksforgeeks.org/python-reversed-split-strings/"

data = requests.get(url).text
print(data)