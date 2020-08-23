from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


die_1 = Die()
die_2 = Die()

#making rolls and storing them in a list with comprehension
results = [ die_1.roll() * die_2.roll() for result in range(10_000)]

#Analyzing the results with comprehension.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [ results.count(value) for value in range(1, max_result+1)]

#Visualize the results as a histogram 
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of rolling multiply two d6 10,000 times', 
					xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_times_d6.html')

