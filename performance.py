import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Google Search', 'PyDoSc Search')
y_pos = np.arange(len(objects))
performance = [247, 20]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Search Results')
plt.title('Method Used')

plt.show()