import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data = requests.get(url).text
# print(data)

# l1 = data.split("\n")
# print(l1)

# l2 = [item.split(",") for item in l1 if len(item)!=0]
# print(l2)

# with open("66_iris.pkl", "wb") as f:
#     pickle.dump(l2, f)
#
# with open("66_iris.pkl", "rb") as f:
#     print(pickle.load(f))