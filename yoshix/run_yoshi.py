import sys
import os
import glob
import importlib
import importlib.util
import yoshix


def import_module_from_file(full_path_to_module):
    """
    Import a module given the full path/filename of the .py file

    Python 3.4

    """

    module = None

    try:

        # Get module name and path from full path
        module_dir, module_file = os.path.split(full_path_to_module)
        module_name, module_ext = os.path.splitext(module_file)

        # Get module "spec" from filename
        spec = importlib.util.spec_from_file_location(module_name, full_path_to_module)

        module = spec.loader.load_module()

    except Exception as ec:
        # Simple error printing
        # Insert "sophisticated" stuff here
        print(ec)

    finally:
        return module


def print_header():
    print("Welcome to Yoshi eXperiment!")
    print("{} experiment(s) found...".format(len(modules)))


def print_usage():
    print("USAGE:")
    print("python -m yoshix.run_yoshi EXPERIMENTS_PATH")

# MAIN
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(-1)
        
    folder = sys.argv[1]
    modules = glob.glob(folder + "/*.py")
    experiments_modules = []

    print_header()

    # Load a module for each file in the folder.
    for f in modules:
        experiments_modules.append(import_module_from_file(f))

    # Find all the subclasses of YoshiExperiment so far.
    experiments_classes = [v.__name__ for v in yoshix.YoshiExperiment.__subclasses__()]

    # Try to load every subclasses and run the experiment.
    for exp_cls in experiments_classes:
        for m in experiments_modules:
            ex = getattr(m, exp_cls, None)
            if ex is None:
                continue
            print("EXECUTION OF EXPERIMENT {}".format(exp_cls))
            ex().run()
