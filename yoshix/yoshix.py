from yoshix.yoshiegg import YoshiEgg, YoshiEggKeyException


class YoshiExperiment(object):
    """
    `YoshiExperiment` is the base class for every user created experiment.

    The class provide the basic interface and infrastructure to register data,
    run single experiments, generate input data and so on.

    The class should never be initialized by its own. This should be always
    extended by a child class.
    """

    def __init__(self):
        self.name = self.__class__.__name__
        self._generators = {}
        self.__egg = None
        self._egg_is_ready = False  # Egg is ready only after the experiment.
        self.__empty_row = None
        self.__run_counter = 0

    def setup(self):
        """
        This function is called before the experiment is started. This can be
        used to initialize variables, generators and every other detail.
        :return: None
        """
        pass

    def single_run(self):
        """
        This represent the atomic experiment run.
        :return: None
        """
        pass

    def run_experiment(self):
        """
        The wrapping experiment loop. This function invokes single_run for
        every combination of **variable parameters** provided by the generators.
        :return: None
        """
        self.__run_counter = 0
        for i in range(3):  # TODO: Temporary
            self.__egg.add_row(self.__empty_row)
            self.__run_counter += 1
            self.single_run()
        self._egg_is_ready = True

    def after_run(self):
        """
        This method is invoked after the experiment is completed.

        Can be used to package the result Egg, clean up the disk and more.
        :return:
        """
        pass

    @property
    def partial_egg(self):
        if self.__egg is None:
            raise EggNotReady("Try to access an egg that is None")
        else:
            return self.__egg

    @property
    def egg(self):
        if self._egg_is_ready:
            return self.__egg
        if self.__egg is None:
            raise EggNotReady("Try to access an egg that is None")
        elif not self._egg_is_ready:
            raise EggNotReady("The egg is there but the experiment is not completed yet!")
        else:
            raise Exception("Something is really wrong there!")

    @property
    def run_counter(self):
        return self.__run_counter

    def setup_egg(self, data_headers, row_initialization=None):
        self.__egg = YoshiEgg(data_headers)
        # If row_init is None we assume all zeroes.
        if row_initialization is None:
            row_initialization = tuple((0 for _ in data_headers))
        if len(row_initialization) == len(data_headers):
            self.__empty_row = row_initialization
        else:
            raise YoshiEggKeyException("Initialization vector does not match the header.")


class EggNotReady(Exception):
    pass