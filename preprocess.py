# -*- coding: UTF-8 -*-
import numpy as np
import os
import sys
import pandas as pd
import BeautifulSoup as soup

# read data
current_path = os.path.dirname(os.path.realpath(__file__))
print current_path
parent_path = os.path.dirname(current_path) 
train_file_en = parent_path + "/data/train/train/500train.en"
train_file_ch = parent_path + "/data/train/train/500train.ch"
eval_file_en = parent_path + "/data/eval/eval/500valid.en-zh.en.sgm"
eval_file_ch = parent_path + "/data/train/train/500valid.en-zh.zh.sgm"
# tf = "/etc/360/BDCI2017-360/evaluation_public.tsv"

def read_sgm(sgm_file):
    with open(sgm_file, 'r') as f:
        soup = soup(f)
        head = soup.find('srcset')
        print head


if __name__ == '__main__':
    gen_data_loader = Gen_Data_loader(64)
    gen_data_loader.create_batches('data/real_data.txt')


# lines = []
# with open(tf, 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         lines.append(line.strip().split('\t'))
#
# df = pd.DataFrame()
# tfdd = []
# ids = []
# one_temp = ""
#
# import jieba
#
# # jieba.enable_parallel(12)
# i = 1
# # preprocessing text
# for line in lines:
#     content = line[2].replace(r'[，。！《》（）“”：；？、——’‘]', '')
#     title = line[1].replace(r'[，。！《》（）“”：；？、——’‘]', '')
#     title = " ".join(jieba.cut(title))
#     one_temp += " ".join(jieba.cut(content))
#     one_temp = title + one_temp
#     tfdd.append(one_temp)
#     one_temp = ""
#     ids.append(line[0])
#     i += 1
#     if (i % 1000 == 0):
#         print (i)
#
# df['id'] = ids
# df['content'] = tfdd
#
# df.to_csv("/etc/360-5/data_temp/preprocess_completed_new_predict.tsv", encoding='utf-8', index=False, sep='\t')
#
#
