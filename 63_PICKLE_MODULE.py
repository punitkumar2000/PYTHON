#PICKING
import pickle
cars = ["audi", "bmw", "maruti suzuki"]
print(type(cars))
file = "mycar.pkl"
fileobj = open(file, "wb")
pickle.dump(cars, fileobj)
fileobj.close()


#UNPICKLING
file = "mycar.pkl"
fileobj = open(file, "rb")
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
