import yoshix
from yoshix.exporter import YoshiEggCSVExporter

import random


class SmallExample(yoshix.YoshiExperiment):

    def setup(self):
        print("Hello!")
        self.setup_egg(("Min", "Max", "A", "B"))
        self.assign_fixed_parameter("Min", 0)
        self.assign_generators("Max", range(1, 10))

    def single_run(self, params):
        print(params)
        self.partial_egg["A"] = random.randint(params["Min"], params["Max"])
        self.partial_egg["B"] = random.randint(0, 100)
        print("Single Run {}".format(self.run_counter))

    def after_run(self):
        YoshiEggCSVExporter(self.egg, "test.csv").export()
        print("Bye Bye")
