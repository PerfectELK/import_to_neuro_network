import json


class Base:

    data__arr = None
    train__data = []
    train__labels = []
    attrs = []

    types_convert = ['binary_array', 'division']
    types_convert_not_analise = ['not', 'relation']

    label__attr = {'attr': 'cost_full', 'type_convert': 'division', 'number': 1000000}

    def __init__(self):
        self.file_path = None

    def check__types_convert(self, name=''):
        for type in self.types_convert_not_analise:
            if name == type:
                return False
        return True

    def import_from_json(self, file_path='base.json'):
        self.file_path = file_path
        file_content = open(file_path, 'r').read()
        self.data__arr = json.loads(file_content)
        print('import from file ', file_path, ' success')

    def add_attribute(self, name=None, type_convert='division', meta=0):
        self.attrs.append({'name': name, 'type_convert': type_convert, 'meta': meta})
        return self

    def analise(self):
        for item in self.data__arr:
            for attr in self.attrs:
                if self.check__types_convert(name=attr['type_convert']):
                    try:
                        data = item[attr['name']]
                        if float(attr['meta']) < float(data):
                            attr['meta'] = float(data)
                    except:
                        data = item['metadata'][attr['name']]
                        if float(attr['meta']) < float(data):
                            attr['meta'] = float(data)

        print('Analise finished success')

    def get__attrs(self, slice=[]):
        data = []
        for attr in self.attrs:
            if attr['type_convert'] != 'not':
                func__name = getattr(self, 'convert__' + attr['type_convert'])

                if attr['type_convert'] == 'relation':
                    data.append(func__name(slice[attr['name']], slice[attr['meta']]))
                else:
                    data.append(func__name(slice[attr['name']], attr['meta']))

            else:
                data.append(float(slice[attr['name']]))
        return data

    def convert_values(self):
        self.analise()
        for item in self.data__arr:
            data = []
            func_name = getattr(self, 'convert__' + self.label__attr['type_convert'])
            label = func_name(number=item['cost_full'], denominator=self.label__attr['number'])
            data = self.get__attrs(slice=item)
            self.put_to_data(item=data, label=label)

    def convert__division(self, number, denominator):
        try:
            return float(number) / float(denominator)
        except:
            return 0

    def convert__binary_array(self):
        None

    def convert__relation(self, number, denominator):
        try:
            return float(number) / float(denominator)
        except:
            return 0

    def put_to_data(self, item=[], label=0.):
        self.train__data.append(item)
        self.train__labels.append(label)

    def train_to_json(self):
        data = json.dumps(self.train__data)
        labels = json.dumps(self.train__labels)

        data_file = open('./train-data.json', 'w')
        labels_file = open('./train-labels.json', 'w')

        data_file.write(data)
        labels_file.write(labels)
        data_file.close()
        labels_file.close()