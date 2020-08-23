
import matplotlib.pyplot as plt 
import plotly.graph_objects as go 
import numpy as np

"""
#Taken and edited from https://plotly.com/python/random-walk/
l = 1000
x_steps = np.random.choice([-1,1], size=l) + 0.2 * np.random.randn(l)
y_steps = np.random.choice([-1,1], size=l) + 0.2 * np.random.randn(l)
x_position = np.cumsum(x_steps)
y_position = np.cumsum(y_steps * x_steps)

fig = go.Figure(data=go.Scatter(
    x=x_position,
    y=y_position,
    mode='markers',
    name='Random Walk',
    marker=dict(

        color=np.arange(l),
        size=8,
        colorscale='Reds',
        showscale=True
    )
))

fig.show()
"""

"""
===================================================================
"""

from die import Die


die_1 = Die()
die_2 = Die()

#making rolls and storing them in a list with comprehension
results = [ die_1.roll() + die_2.roll() for result in range(5000)]

#Analyzing the results with comprehension.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [ results.count(value) for value in range(2, max_result+1)]



plt.bins = []
x_max = die_1.num_sides + die_2.num_sides
for label in range(2, x_max+1):
    plt.bins.append(label)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(plt.bins, frequencies, linewidth=3)

ax.set_title("Frequencies of two d6 being rolled.", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()