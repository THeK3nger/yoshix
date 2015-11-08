# YoshiX

![YoshiX](/images/yoshi.png)

**YoshiX** (_Yoshi Experiment_) is a library for collecting and processing experimental data such as benchmarks results. This is particularly suited for experiment who require to run an algorithm several time with different parameters combinations.

YoshiX is directly inspired by Unit Testing but provide also functionality to store, process and export heterogeneous data coming from algorithms and experiments.

## Examples

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
        self.partial_egg["A"] = random.randint(0, 100)
        self.partial_egg["B"] = random.randint(0, 100)
        # ... Do some other thing...

    def after_run(self):
        # Clean up...
```

The `setup` method is used to initialize the experiment and, in particular the "egg" that will be used to collect the data.

The `single_run` method is where the actual experiment is computed. This method will be called several times with different parameters (see **generators**) collecting each run results in a table.

The `after_run` method is where the experiment can perform some kind of global clean up (e.g., deleting files) or processing and exporting the collected data.

### Generators

Yoshi's Generators are exactly like standard Python generators. They are linked to particulars parameters and are used by Yoshi in order to generate the input parameters.

TODO
