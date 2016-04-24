#-*-coding: utf-8 -*-
from multiprocessing import Process
import sys
import time
from ear import Ear
from tongue import Tongue

class Android(object):

	alive = True

	def __init__(self, name = "Mr. Smith"):
		self.name = name
		self.ear = Ear()
		self.tongue = Tongue()
		self.brain = Brain()
		self.live()

	def live(self):
		while alive:
			time.sleep()
			dispatch = self.brain.main(dispatch)
			self.brain.state = dispach(self.brain.state)

class Brain(object):

 	frequency = 0.001
 	sub_systems = ["main","listen", "speak"]

 	def __init__(self):
 		self.data = None
 		self.dispatch = None
 		for system_name in sub_systems:
 			setattr(system_name, System(system_name).load())




class System(object):

	def __init__(self, name):
		self.data = []
		self.name = ""
		self.basic = []
		self.map = None

	def load(self):
		with open("self.name", "r") as f:
			pass

	def __call__(self, state):
		for neuron in state:
			neuron.process(self.data)
		for neuron in state:
			neuron.clean()
		return self.data


class Neuron(object):


	def __init__(self, data = None):
		self.data = None
		self.active = False
		self.synapses = []

	def __add__(self, neuron):
		self.synapses.append(neuron)

	def __sub__(self, neuron):
		self.synapses.remove(neuron)

	def __str__(self):
		return self.data

	def __enter__(self):
		pass

	def __close__(self):
		self.desactivate()

	def activate(self):
		self.active = True

	def desactivate(self):
		self.active = False

	def echo(self):
		return self.data

	def clean(self):
		self.data = None

	def process(self, data):
		if self.synapses == []:
			data.append(self.echo())
		for neuron in self.synapses:
			if neuron.active:
				neuron.train(data)
			else:
				neuron.activate()
	
	def clean(self):
		if self.active:
			for neuron in self.synapses:
				if neuron.active:
					neuron.clean()
		self.desactivate()
