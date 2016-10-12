import os.path, re, numpy, matplotlib.pyplot

"""LINEAR REGRESSION"""
basepath = os.path.dirname(__file__)
filepath = os.path.abspath(os.path.join(basepath, "moore.csv"))
x_coord = []; y_coord = []
non_decimal = re.compile(r'[^\d]+')
for line in open(filepath, "r"):
    row = line.split('\t')
    x = int(non_decimal.sub('', row[2].split('[')[0]))
    y = int(non_decimal.sub('', row[1].split('[')[0]))
    x_coord.append(x)
    y_coord.append(y)

x_coord = numpy.array(x_coord); y_coord = numpy.array(y_coord)
y_coord = numpy.log(y_coord)

denominator = x_coord.dot(x_coord) - x_coord.mean() * x_coord.sum()
a = ( x_coord.dot(y_coord) - y_coord.mean() * x_coord.sum() ) / denominator
b = ( y_coord.mean() * x_coord.dot(x_coord) - x_coord.mean() * x_coord.dot(y_coord) ) / denominator
YHat = a * x_coord + b

d1 = y_coord - YHat
d2 = y_coord - y_coord.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
# print("Time to double: ", numpy.log(2) / a, "years")
# matplotlib.pyplot.scatter(x_coord, y_coord)
# matplotlib.pyplot.plot(x_coord, YHat)
# matplotlib.pyplot.show()

"""MULTIPLE LINEAR REGRESSION"""
