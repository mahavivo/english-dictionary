#!/usr/bin/env python
# -*- coding: utf-8 -*-

# csv数据转换成SQLite数据库格式，不直接放ecdict.db，是因为会膨胀很大。
# 此数据包含40万条记录，提取自共有770611条记录的ecdict.csv（出处 https://github.com/skywind3000/ECDICT）,
# 删除了所有短语和没有汉语释义的词条，只保留word、phonetic、translation三个字段。

import stardict

stardict.convert_dict('./minidict(400k).db', './minidict(400k).csv')
