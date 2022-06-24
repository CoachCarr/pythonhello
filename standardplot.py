import matplotlib.pyplot as plt #after the obligatory hello world, this is an ideal start
import numpy as np
#now gonna make my computer graphically display a  trig function
x = np.linspace(0, 20, 100)  # Create a nice list of evenly-spaced numbers over the range
plt.plot(x, np.cos(x))       # Simply plot the sine of each x point, later changed to tangent and cosine
plt.show()                   # gotta figure the word show means this will display the plot

#i think i still have a path issue with setting up a formatter and or virtual environment
#i could be better with the desktop git fiddle, so i plan to revision control experiments in python