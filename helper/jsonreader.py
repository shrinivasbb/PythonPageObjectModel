import json;
import inspect;
import os;


class JsonReader:
    def read_from_file(filename):
            direct_path = os.path.dirname(os.path.realpath(__file__))
            direct_path = os.path.abspath(os.path.join(direct_path, '..'))
            filename = direct_path+'/resources/'+filename
            with open(filename, 'r') as f:
                data_items = json.load(f)
            datas_out = data_items[inspect.stack()[1][3]]
            return datas_out

    def read_from_file_and_element(filename, jsonelement):
            direct_path = os.path.dirname(os.path.realpath(__file__))
            direct_path = os.path.abspath(os.path.join(direct_path, '..'))
            filename = direct_path+'/resources/'+filename
            with open(filename, 'r') as f:
                data_items = json.load(f)
            datas_out = data_items[jsonelement]
            return datas_out


if __name__ == '__main__':
    js = JsonReader
    js.read_from_file()
