
class YoshiEgg(object):
    """
    A YoshiEgg class is used to store results from experiments.
    """

    def __init__(self, recorded_data_idx):
        """
        Initialize an empty Egg.

        Data is stored in the form of a table.

        :param recorded_data_idx: The header of the data table.
        """
        self._records_header = recorded_data_idx

        # The data table is represented with a "list of dictionaries" [{}].
        self._data = []

    @property
    def header(self):
        """
        :return: The egg table header.
        """
        return self._records_header

    def add_row(self, row):
        """
        Add a row to the egg. The row must be of the same size of the header list.
        :param row:
        :return:
        """
        if len(row) != len(self._records_header):
            raise YoshiEggKeyException("Row is not the same size of the table.")
        self._data.append({k: v for k, v in zip(self._records_header, row)})

    def __setitem__(self, key, value):
        if isinstance(key, tuple) and len(key) == 2:
            i, k = key
        else:
            i, k = -1, key
        if k not in self._records_header:
            raise KeyError("Key is not a valid key for the egg.")
        self._data[i][k] = value

    def __getitem__(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            i, k = key
            return self._data[i][k]
        else:
            return self._data[key]

    def __contains__(self, item):
        return item in self._records_header


class YoshiEggKeyException(Exception):
    pass
