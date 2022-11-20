import os
import random
import shutil


image_input_dir = 'E:/datasets_no_test/datasets_no_test/test/images/'
image_output_dir = 'E:/LaTeX_OCR_PRO-master/LaTeX_OCR_PRO-master/data/'
with open('E:/datasets_no_test/datasets_no_test/test_ids.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
size = len(lines)
'''改图片名字
for i in range(size):
    if i % 2000 == 0:
        print(i)
    image_origin_name = lines[i][:-1] + '.png'
    # image_name = str(i) + '.png'
    shutil.copy(image_input_dir + image_origin_name, image_output_dir + 'images_test/' + str(i) + '.png')
'''

match = 'E:/LaTeX_OCR_PRO-master/LaTeX_OCR_PRO-master/data/full/matching/test.matching.txt'
formula='E:/LaTeX_OCR_PRO-master/LaTeX_OCR_PRO-master/data/full/formulas/test.formulas.norm.txt'
for i in range(size):
      with open(match, 'a', encoding='utf-8') as f:
        fileName = lines[i][:-1] + '.png'
        f.write(fileName + ' ' + str(i) + '\n')
      with open(formula, 'a',encoding='utf-8') as f1:
        f1.write(lines[i][:-1] + '.formulas' + '\n')
