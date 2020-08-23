import matplotlib.pyplot as plt 

from random import choice

class RandomWalk:
	"""Class for generating random walks."""

	def __init__(self, num_points=5000):
		self.num_points = num_points

		#X and Y start at 0 by default.
		self.x_values = [0]
		self.y_values = [0]


	#get_step determines the direction and distance the next point will take from the last.
	def get_step(self):
		direction = choice([1, -1])
		distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
		step = direction * distance
		return step
		

	def fill_walk(self):

		#While loop runs untill number of points set is met.
		while len(self.x_values) < self.num_points:
			x_step = self.get_step()
			y_step = self.get_step()

			#If checks to make sure new X and Y points dont just stay in the same place.
			if x_step == 0 and y_step == 0:
				continue

			#x and y are the last value in the value lists plus the current step.
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			#x and y are added to the list of values.
			self.x_values.append(x)
			self.y_values.append(y)



while True:
	rw = RandomWalk(5000)
	rw.fill_walk()

	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(19, 10))
	point_numbers = range(rw.num_points)
	
	ax.plot(rw.x_values, rw.y_values, linewidth=3)

	ax.scatter(0, 0, c='green', edgecolors='none', s=500)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=500)


	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break


PAGE 323