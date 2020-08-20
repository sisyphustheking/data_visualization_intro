import matplotlib.pyplot as plt 

from random_walk import RandomWalk 


while True:
	rw = RandomWalk(5000)
	rw.fill_walk()

	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(19, 10))
	point_numbers = range(rw.num_points)
	
	ax.plot(rw.x_values, rw.y_values, linewidth=3)

	ax.scatter(0, 0, c='green', edgecolors='none', s=500)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=500)


	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break