# coding:utf8
import numpy as np
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
import jieba
reload(sys)
sys.setdefaultencoding('utf-8')

# read data
current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
train_file_en = parent_path + "/data/train/train/500train.en"
train_file_zh = parent_path + "/data/train/train/500train.zh"
eval_file_en_sgm = parent_path + "/data/eval/eval/500valid.en-zh.en.sgm"
eval_file_zh_sgm = parent_path + "/data/eval/eval/500valid.en-zh.zh.sgm"
eval_file_zh = eval_file_zh_sgm[:-4]
eval_file_en = eval_file_en_sgm[:-4]
train_file_jieba_zh = train_file_zh[:-3] + '_jieba.zh'
eval_file_jieba_zh = eval_file_zh[:-3] + '_jieba.zh'

#constant
TRAIN = 1
EVAL = 0


# parsing .sgm
def read_sgm(sgm_file):
    # a new file: delete ".sgm"
    filename = sgm_file[:-4]
    output = open(filename, 'w')
    with open(sgm_file, 'r') as f:
        for line in f.readlines():
            soup = BeautifulSoup(line, "html5lib")
            if soup.find('seg'):
                output.write(str(soup.seg.string) + '\n')


# split chinese with jieba
def split_chinese(zh_file):
    lines = []
    zh_jieba_file = zh_file[:-3] + '_jieba.zh'
    with open(zh_file, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip().split('\t'))

    with open(zh_jieba_file, 'w') as f2:
        for line in lines:
            content = line[0].replace(r'[，。！《》（）“”：；？、——’‘]','')
            content = " ".join(jieba.cut(content))
            f2.write(content + '\n')


# put the original and the translated sentences in one line
def joint_original_and_translate(zh_file, en_file, data_mode):
    if data_mode:   # train data
        filename = parent_path + '/data/train/train_file.csv'
    else:   # eval data
        filename = parent_path + '/data/eval/eval_file.csv'

    df = pd.DataFrame()
    original = []
    translated = []

    with open(zh_file, 'r') as zf:
        for zhline in zf.readlines():
            original.append(zhline.strip().split('\n'))

    with open(en_file, 'r') as ef:
        for enline in ef.readlines():
            translated.append(enline.strip().split('\n'))

    df['original'] = original
    df['translated'] = translated

    df.to_csv(filename, index=False, encoding='utf-8', sep='\t')




if __name__ == '__main__':
    # read_sgm(eval_file_zh_sgm)
    # read_sgm(eval_file_en_sgm)
    # print eval_file_zh
    # print eval_file_en
    # split_chinese(train_file_zh)
    # split_chinese(eval_file_zh)
    joint_original_and_translate(train_file_jieba_zh, train_file_en, TRAIN)
    joint_original_and_translate(eval_file_jieba_zh, eval_file_en, EVAL)




