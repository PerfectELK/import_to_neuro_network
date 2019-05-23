from import_to_network.base import Base


class Offer(Base):

        def __init__(self):
                super().__init__()

        def start(self):
                self.add_attribute(name='area_kitchen')\
                        .add_attribute(name='is_newbie', type_convert='not')\
                        .add_attribute(name='level', type_convert='relation', meta='levels')\
                        .add_attribute(name='levels')\
                        .add_attribute(name='room_amount')\
                        .add_attribute(name='area_living')\
                        .add_attribute(name='area_full')\
                        .add_attribute(name='area_bathroom')
                self.import_from_json(file_path='./offers.json')
                self.convert_values()









