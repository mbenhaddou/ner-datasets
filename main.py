import entities_data


e=entities_data.read_conll('CONLL02-nl', split='train')


for s in e:
    print(s)