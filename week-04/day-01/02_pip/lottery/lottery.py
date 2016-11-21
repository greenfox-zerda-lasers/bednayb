# Create a method that returns the five most frequent lottery number in a pretty table format

def numbers_to_list():
    fr = open('otos.csv','r')
    result = f.read()
    fr.close()
    print(result)


data = "2015;48;2015.11.28.;0;0 Ft;21;2 670 505 Ft;2403;24 710 Ft;75831;1 525 Ft;9;50;72;76;89"

data = data.split()
data = data[8]
data = data[3:]

data2 = data.split(";")

data = []
for i in range(len(data2)):
    data.append(int(float(data2[i])))

print(data)


#
# def five_most_frequent(file_name):
#     result = ""
#     f = open(file_name,'r')
#     for line in f.readlines():
#
#
#     return result
#
# five_most_frequent()
