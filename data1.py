import matplotlib.pyplot as plt

x_axis = list(range(-100, 101))
y_axis = [x**2 for x in x_axis]
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(x_axis, y_axis, linewidth = 2, c = (0.8, 0.1, 0.2))
ax.scatter(x_axis, y_axis, s=2, cmap=plt.cm.gist_rainbow)
ax.set_title("Graph", fontsize=24)
ax.set_xlabel("X - axis", fontsize=14)
ax.set_ylabel("Y - axis", fontsize=14)
ax.tick_params(axis='both', labelsize=10)
plt.show()
# plt.savefig('Images/graph.png', bbox_inches = 'tight')
