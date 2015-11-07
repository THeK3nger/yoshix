import examples.example_small

# MAIN
if __name__ == '__main__':
    ex = examples.example_small.SmallExample()
    ex.setup()
    ex.run_experiment()
    ex.after_run()
