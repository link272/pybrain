import csv
from itertools import count
import pickle

class Brain(object):

    def __init__(self, name = "Android"):
        self.name = name
        self.cortex = System("cortex", System)
        self.emotion = System("emotion")
        self.listen = System("listen")
        self.speak = System("speak")
        self.read = System("read")
        self.write = System("write")
        self.logical = System("logical")

    def add_system(self, name, ntype):
        setattr(name, System(name, ntype))

    def save(self):
        pickle.dump(self, open("brain.db", "wb" ))

    def load(self):
        self = pickle.load(self, open("brain.db", "rb" ))




class Neuron(object):

    def __init__(self, nid = 0, data = None):
        self.nid = nid
        self.data = data
        self.active = False
        self.synapses = []
        print('neuron initialised')

    def __add__(self, neuron):
        self.synapses.append(neuron)

    def __sub__(self, neuron):
        self.synapses.remove(neuron)

    def __str__(self):
        return self.data.__str__()

    def activate(self):
        print("-->activate")
        self.active = True

    def desactivate(self):
        print("-->desactivate")
        self.active = False

    def echo(self, meaning):
        if self.data != None:
            meaning.append(self)

    def register(self, path):
        path.append(self)

    def clean(self):
        self.data = None
        self.synapses = []

    def switch(self):
        if self.active:
            self.desactivate()
        else:
            self.activate()

    def light_up(self, path, meaning):
        print("-->sending up")
        self.switch()
        for i in self.synapses:
            i.switch()
            if i.active != self.active:
                i.register(path)
                i.echo(meaning)
                i.light_up(path, meaning)


    def turn_off(self):
        self.desactivate()
        for i in self.synapses:
            i.desactivate()


class System(object):

    def __init__(self, name = "", ntype = str):
        self.ntype = ntype
        self.name = name
        self.path = []
        self.meaning = []
        self.data = []
        self.base = []
        self.net = []

    def __str__(self):
        return self.name

    def __enter__(self):
        return self
        print("-> initialise system")
        if self.base == []:
            with open(self.name, 'r') as f:
                parser = csv.reader(f, delimiter="\t")
                nid = count(1)
                for i in parser:
                    if i[0] == "":
                        self.net.append(Neuron(nid.next()))
                    else:
                        tmp = Neuron(nid.next(), self.kind(i[1]))
                        self.net.append(tmp)
                        self.base.append(tmp)
                for i in parser:
                    j = 0
                    tab = map(int, i[2].split(","))
                    for k in tab:
                        self.net[j] + self.net[k]
                    j += 1

                    
    def kind(self, string):
        return self.ntype(string)

    def learn(self, nnew, nmid, nlast):
        nnew+nmid
        nmid+nlast
        nnew+nlast

    def forget(self, n):
        n.clean()

    def __exit__(self, exception_type, exception_value, traceback):
        print("-> exit system")
        self.clean_up()
        self.path = []
        self.meaning = []

    def process(self, data):
        self.path += data
        for i in data:
            if i in self.base:
                i.light_up(self.path, self.meaning)

    def clean_up(self):
        for i in self.path:
            i.turn_off()

    def save(self):
        with open(self.name, 'w') as f:
            parser = csv.writer(f, delimiter="\t")
            for i in self.net:
                depend = [j.nid for j in i.synapses]
                depend = ",".join(depend)
                parser.writerow([i.nid, i.__str__(), depend])

    def export(self):
        return [i.data for i in self.meaning if i.active]