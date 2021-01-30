import matplotlib.pyplot as plt
from random import choice


class random_walk:
    def __init__(self, num_points=5000):
        # all walks start at (0,0)
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # caculate all the points in the walk
        # keep taking steps until the walks reaches desired length
        while len(self.x_values) < self.num_points:
            x_direction = choice([-1, 1])
            x_distance = choice([1, 2, 3, 4, 5])
            x_step = x_direction * x_distance
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)


rw = random_walk()
rw.fill_walk()
plt.style.use('seaborn')
fg, ax = plt.subplots(figsize=(16, 9), dpi=128)
num_points = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, c=(0.4, 0.7, 0.3), linewidth=0.8)
# ax.scatter(rw.x_values, rw.y_values, s = 0.1, c = num_points, edgecolors = 'none', cmap = plt.cm.gist_rainbow)
# ax.scatter(0, 0, c = (0, 0.1, 0), edgecolors = 'none', s = 50)
# ax.scatter(rw.x_values[-1], rw.y_values[-1], edgecolors = 'none', c = (0, 0, 0.1), s = 50)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
# plt.savefig('randomwalks.png')
