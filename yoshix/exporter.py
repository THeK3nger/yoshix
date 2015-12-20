import csv
import json

class YoshiEggExporter(object):

    def __init__(self, egg, output):
        self._egg = egg
        self._output = output

    def export(self):
        pass


class YoshiEggCSVExporter(YoshiEggExporter):

    def export(self):
        keys = self._egg._data[0].keys()
        with open(self._output, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self._egg._data)

class YoshiEggJSONExporter(YoshiEggExporter):

    def export(self):
        with open(self._output, 'w', newline='') as output_file:
            result = json.dumps(self._egg._data, separators=(',', ': '))
            output_file.write(result)
