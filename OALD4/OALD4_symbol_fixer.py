#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OALD4原始文档音标使用了"Kingsoft Phonetic Plain"字体，导致不安装该字体的电脑会出现乱码，在此批量替换修正。
# 金山词霸音标字体编码表可参见 http://www.fmddlmyy.cn/text66.html

import re


file_src = "/users/vivo/desktop/OALD4_INIT.txt"

file_dst = "/users/vivo/desktop/OALD4_edited.txt"


def converter(match):
    phonetic_string = match.group()
    correct_symbol = phonetic_string.replace("5", "ˈ").replace("7", "ˌ").replace("9", "ˌ") \
        .replace("A", "æ").replace("B", "ɑ").replace("C", "ɔ").replace("E", "ə").replace("F", "ʃ") \
        .replace("I", "ɪ").replace("J", "ʊ").replace("N", "ŋ").replace("Q", "ʌ") \
        .replace("R", "ɔ").replace("T", "ð").replace("U", "u").replace("V", "ʒ") \
        .replace("W", "θ").replace("Z", "ɛ").replace(r"\\\\", "ɜ").replace("^", "ɡ") \
        .replace(":", "ː").replace("[", "ɜːr").replace("L", "ər").replace("?@", "US")

    return correct_symbol



with open(file_src, 'r') as f:
    text = f.read()

    p = re.compile("/.*?; .*?/")

    result = re.sub(p, converter, text)


with open(file_dst, 'w') as fo:
    fo.write(result)