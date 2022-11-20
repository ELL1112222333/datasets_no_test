from model.utils import *
import json

path='./data/'
v1,d1=get_latex_ocrdata(path,'dev')
print('dev finish')
v2,d2=get_latex_ocrdata(path,'train')
print('train finish')

json_str_v1 = json.dumps(v1)
json_str_d1 = json.dumps(d1)
json_str_v2 = json.dumps(v2)
json_str_d2 = json.dumps(d2)

with open('vocab1.json', 'w') as json_file:
    json_file.write(json_str_v1)

with open('data/dev.json', 'w') as json_file:
    json_file.write(json_str_d1)

with open('data/vocab2.json', 'w') as json_file:
    json_file.write(json_str_v2)

with open('data/train.json', 'w') as json_file:
    json_file.write(json_str_d2)




