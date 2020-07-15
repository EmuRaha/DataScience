from matplotlib import pyplot as plt
from matplotlib import style

# style.use('ggplot')

plt.plot([15,138,93],[47,85,106],label='Firts',linewidth= 4)
# plt.show()

a = [12,23,56,78,95]
b = [34,56,26,78,97]
plt.plot(a,b,label='Second',linewidth= 4)
plt.legend()
plt.title("My plot")
plt.xlabel("This is X axis")
plt.ylabel("This is Y axis")
plt.show()

######################################################################
######################################################################

style.use('ggplot')

plt.plot([15,138,93],[47,85,106],label='Firts',linewidth= 4)
# plt.show()

a = [12,23,56,78,95]
b = [34,56,26,78,97]
plt.plot(a,b,label='Second',linewidth= 4)
plt.legend()
plt.title("My plot")
plt.xlabel("This is X axis")
plt.ylabel("This is Y axis")
plt.show()

######################################################################
######################################################################

plt.scatter([15,138,93],[47,85,106],label='Firts',linewidth= 4)
# plt.show()
a = [12,23,56,78,95]
b = [34,56,26,78,97]
plt.scatter(a,b,label='Second',linewidth= 4)
plt.legend()
plt.title("My plot")
plt.xlabel("This is X axis")
plt.ylabel("This is Y axis")
plt.show()

######################################################################
######################################################################

plt.hist([15,38,93],[47,85,106],label='Firts',linewidth= 4)
# plt.show()
a = [12,23,56,78,95]
b = [34,56,62,87,97]
plt.hist(a,b,label='Second',linewidth= 4)
plt.legend()
plt.title("My plot")
plt.xlabel("This is X axis")
plt.ylabel("This is Y axis")
plt.show()

# above code gives error(histogram)


















