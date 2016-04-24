#-*-coding: utf-8 -*-
from multiprocessing import Process
import time

class Brain(object):

	alive = True
	frequency = 0.000001
	
	def __init__(self, memory = "memory"):
		pass

	def live(self):
		while self.alive:
			time.sleep(self.frequency)
			state = self.perception()
			data = self.cognition(state)
			p = Process(target=data[0], args=(data[1:]))
    		p.start()

	def perception(self):
		a = Neuron("1")
		b = Neuron("+")
		c = Neuron()
		d = Neuron()
		e = Neuron("2")
		a.synapses.append(c)
		a.synapses.append(d)
		b.synapses.append(d)
		c.synapses.append(e)
		d.synapses.append(e)

		state = [a, b, a]
		return state
	
	def shell(self, *args):
		print(args[0])
	
	def cognition(self, state):
		for neuron in state:
			data = neuron.process()

		return data

	def physical(self, *args):
		pass

	def memory(self, *args):
		pass




class Neuron(object):

	synapses = []
	data = None
	is_active = False

	def __init__(self, data = None):
		self.data = data

	def activate(self):
		self.is_active = True

	def desactivate(self):
		self.is_active = False

	def process(self):
		for neuron in self.synapses:
			if neuron.is_active == False:
				neuron.activate()
			else:
				if neuron.synapses == []:
					return neuron.data
				else:
					neuron.process()
		return None

	def clean(self):
		for neuron in self.synapses:
			neuron.desactivate()
			neuron.clean()




