import random
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


dice1 = Dice(6)
dice2 = Dice(10)

results = [dice1.roll() + dice2.roll() for i in range(500)]
max_result = dice1.sides + dice2.sides
frq = [results.count(i) for i in range(2, max_result + 1)]

x_values = list(range(2, max_result + 1))
data = [Bar(x = x_values, y = frq)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency'}
my_layout = Layout(title = 'Results of rolling Dice', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'dice.html')
