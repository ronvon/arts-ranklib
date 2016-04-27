#!/usr/bin/python
# -*- coding: UTF-8 -*-

#desc integrate data
#author huabin.feng@dianping.com
#date 2015-05-21

import os

oriFile = 'train.txt';
oriFileHandler = open(oriFile, "r")
oriRecords = oriFileHandler.readlines()
oriFileHandler.close()
prevDocId = 'qid:0000'
for eachline in oriRecords:
    tmp = eachline.strip()
    loc = tmp.find('#')
    vecStr = tmp[0:loc]
    vec = vecStr.split(' ')
    newStr = ' '.join(vec[2:])
    currId = vec[1]
    if currId != prevDocId:
        prevDocId = currId
        print '##########'
    print newStr


