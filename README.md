# YoshiX

![YoshiX](/images/yoshi.png)

**YoshiX** (_Yoshi E**X**periment_) is a library for collecting and processing experimental data such as benchmarks results. This is particularly suited for experiment who require to run an algorithm several time with different parameters combinations.

YoshiX is directly inspired by Unit Testing but provide also functionality to store, process and export heterogeneous data coming from algorithms and experiments.

## Features

The slowly increasing list of features includes:

 * Runs experiments in a replicable way.
 * Modular experiment specification! Each experiment is a python file, YoshiX will automatically find every experiment in a folder and will run each one of them!
 * Automatically iterates over the parameter space according your own generators (any generator can be used as a source, from the `range` function to a custom generator!).
 * Collects the experiment results in a synthetic way (the **YoshiX Egg**).
 * Export the eggs into different formats (_CSV_, _JSON_ and many other to come).

## Usage

### Collecting Data

This is the basic structure for a Youshi experiment.

```python
class SmallExample(yoshix.YoshiExperiment):

    def setup(self):
        # Setup the "egg" and the experiment.
        self.setup_egg(("Data1", "Data2"))

    def single_run(self):
        # Run the actual experiment.

        print("Single Run {}".format(self.run_counter))
        # ... Do some computation...
        self.partial_egg["Data1"] = random.randint(0, 100)
        self.partial_egg["Data2"] = random.randint(0, 100)
        # ... Do some other thing...

    def after_run(self):
        # Clean up...
```

The `setup` method is used to initialize the experiment and, in particular the "egg" that will be used to collect the data.

The `single_run` method is where the actual experiment is computed. This method will be called several times with different parameters (see **generators**) collecting each run results in a table.

The `after_run` method is where the experiment can perform some kind of global clean up (e.g., deleting files) or processing and exporting the collected data.

### Generators and Fixed Parameters

Yoshi's Generators are exactly like standard Python generators. They are linked to particulars parameters and are used by Yoshi in order to generate the input parameters. Any Python generator can be used as a generator.

In the following example we can see how to assign a fixed parameter and a variable parameters using a generator. In the example the `Min` parameter will be 0 for every experiment run. Otherwise the `Max` parameters use the `range` builtin generator in order to variate the Max parameter from 1 to 10.

```python
def setup(self):
    self.setup_egg(("Min", "Max", "A", "B"))
    self.assign_fixed_parameter("Min", 0)
    self.assign_generators("Max", range(1, 10))
```

### Exporting

Once the experiment is completed and the egg is ready we can decide to export the egg in some other format. For instance we can decide to export the egg in CSV.

```python
def after_run(self):
    YoshiEggCSVExporter(self.egg, "test.csv").export()
    print("Bye Bye")
```

In this example we use the `YoshiEggCSVExporter` exporter in order to export the egg into a csv file.

### Command line usage

Once you have a set of experiments in a folder (for instance, "examples") you can use

```
yoshi_run ./examples
```

in order to run all the experiments in the folder.
