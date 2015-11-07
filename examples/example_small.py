import yoshix
import random


class SmallExample(yoshix.YoshiExperiment):

    def setup(self):
        print("Hello!")
        self.setup_egg(("A", "B"))

    def single_run(self):
        self.partial_egg["A"] = random.randint(0, 100)
        self.partial_egg["B"] = random.randint(0, 100)
        print("Single Run {}".format(self.run_counter))

    def after_run(self):
        print(self.egg._data)
        print("Bye Bye")