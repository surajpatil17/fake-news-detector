import matplotlib.pyplot as plt

activities = ['Sleeping', 'Eating', 'Working', 'Playing']
slices = [7, 2, 2, 13]
colors = ['c', 'm', 'r', 'b']

plt.pie(slices, labels=activities, colors=colors,
        startangle=90, shadow=True,
        explode=(0, 0.1, 0, 0), autopct='%1.1f%%')

plt.title('Daily Activities')
plt.show()

