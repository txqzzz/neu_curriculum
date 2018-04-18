# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 02/04/2018 21:14
    @Name: preprocess
    @Project: neu_curriculum
"""
import re
import jieba
import config

def _preprocess(in_filename, out_filename):
    in_file = open(config.DATA_DIR+in_filename, 'r')
    out_file = open(config.DATA_DIR+out_filename, 'w')

    while True:
        line = in_file.readline().strip()
        cut_result = jieba.lcut(line)
    result = ''.join(cut_result) + '\n'

    out_file.write(result)


if __name__ == "__main__":
    print("Pre-processing data now...")
    _preprocess("corpus.sentence.txt", "corpus.cut")
    
