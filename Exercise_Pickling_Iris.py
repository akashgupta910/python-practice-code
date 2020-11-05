import requests, pickle

# Get iris.data

get_data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
iris_dataset = get_data.text

# Split iris.data

split_iris_data = iris_dataset.split("\n")
data_list=[]
i = 0
while i<len(split_iris_data):
  data_list.append(split_iris_data[i:i+1])
  i+=1

#Pickling a Python Object

wb_file = "iris.data.pik"
wb_file_object = open(wb_file, "wb")
pickle.dump(data_list, wb_file_object)
wb_file_object.close()

# De-pickling a Python Object

rb_file = "iris.data.pik"
rb_file_object = open(rb_file, "rb")
data = pickle.load(rb_file_object)
print(data)