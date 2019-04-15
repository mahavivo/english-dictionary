#!/usr/bin/env python
# -*- coding: utf-8 -*-

# csv数据转换成SQLite数据库格式，不直接放ecdict.db，是因为会膨胀很大。
# 此数据包含770611条记录，来自 https://github.com/skywind3000/ECDICT

import stardict

stardict.convert_dict('./ecdict.db', './ecdict.csv')
