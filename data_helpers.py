#!/usr/bin/env python
# coding=utf-8

import numpy as np
import re
import itertools
from collections import Counter

def clean_str_4_json(string):
    string = re.sub(r"true", '"True"', string)
    string = re.sub(r"false", '"False"', string)
    string = re.sub(r"none", '"None"', string)
    string = re.sub(r"\\", r'\\\\', string)
    return string

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """    
    #add by qin haining 170405
    #for del the /r/n with nothing 
    #string = re.sub(r"^$\r\n", "", string)
    #end
#    string = re.sub(r"[^\u4e00-\u9fa5]", " ", string)
    string = re.sub(r"[A-Za-z0-9(),!?]", " ", string)
    string = re.sub(r"[\'\`\{\}\:\"\[\]\.\-\;\*\/\=]", " ", string)
    string = re.sub(r"[%\~\^\_\\]", " ", string)
    string = re.sub(r"  ", " ", string)
    string = re.sub("[、？，。！～]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
#    print(string.strip().lower())
    return string.strip().lower()


def load_data_and_labels(positive_data_file, negative_data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    positive_examples = list(open(positive_data_file, encoding='utf8').readlines())
    positive_examples = [s.strip() for s in positive_examples]
    negative_examples = list(open(negative_data_file, encoding='utf8').readlines())
    negative_examples = [s.strip() for s in negative_examples]
    # Split by words
    x_text = positive_examples + negative_examples
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    positive_labels = [[0, 1] for _ in positive_examples]
    negative_labels = [[1, 0] for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    #打印出清洗后的数据 x_text==数据 y==标签
#    print("x_text=%s\n"% (x_text))
#    print("y=%s\n"% (y))
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=False):
    """
    Generates a batch iterator for a dataset.
    """
    
    print('=====')
    print('\n')
#    print(data)
    print('\n')
#    print(batch_size)
    print('\n')
#    print(num_epochs)
    print('\n')

    data = np.array(data) 
    # np.array 把数据转型为数组
    #[[...]
    #[...]
    #[...]]
#    print(data)
    data_size = len(data)
#    print(data_size)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    print(num_batches_per_epoch)
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
            print(shuffled_data)

        else:
            shuffled_data = data
            print(data)

        for batch_num in range(num_batches_per_epoch):
            print(batch_num)
            start_index = batch_num * batch_size
            print(start_index)
            end_index = min((batch_num + 1) * batch_size, data_size)
            print(end_index)
            yield shuffled_data[start_index:end_index]
