import os
'''
# 根据数据集路径改data_path, 其他参数不需要改
data_path = '210705'

sub_name = ['train', 'val', 'test']
formulas = '../data/' + data_path + '/formulas/'
#formulas = ../data/210705/formulas/
if not os.path.isdir('../data/' + data_path + '/matching/'):
    os.mkdir('../data/' + data_path + '/matching/')
#新建../data/210705/matching/
for sn in sub_name:
    match = '../data/' + data_path + '/matching/' + sn +'.matching.txt'
    #../data/210705/matching/train.matching.txt
    #../data/210705/formulas/train.formulas.norm.txt
    with open(formulas + sn + '.formulas.norm.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
    size = len(lines)
    for i in range(size):
        with open(match, 'a', encoding='utf-8') as f:
            fileName = str(i) + '.png'
            f.write(fileName + ' ' + str(i) + '\n')
'''
sub_name = ['train', 'dev']
formulas = './data/formulas/'
#E:\datasets_no_test\datasets_no_test\train.formulas.norm.txt
for sn in sub_name:
    #match = '../data/' + data_path + '/matching/' + sn + '.matching.txt'
    match = './data/matching/' + sn + '.matching.txt'
    with open(formulas + sn + '.formulas.norm.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    size = len(lines)
    for i in range(size):
        with open(match, 'a', encoding='utf-8') as f:
            fileName = str(i) + '.png'
            f.write(fileName + ' ' + str(i) + '\n')