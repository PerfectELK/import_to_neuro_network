from import_to_network.offer import Offer

b = Offer()
b.start()
b.train_to_json()

print(b.train__data)
print(b.train__labels)
print(len(b.train__data))
print(len(b.train__labels))