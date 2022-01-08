#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" 《21世纪英汉词典》纯文本文件提取 """

import re

file_src = r'C:\Users\vivo\Desktop\21世纪英汉词典.txt'

file_dst = r'C:\Users\vivo\Desktop\21世纪英汉词典-Plain.txt'


def main():
    with open(file_src, 'r', encoding='UTF-8') as f:
        full_text = f.read()
        modified_text = re.sub(r'</>\n.*?\n<link href=', '</>\n<link href=', full_text)     #删除索引词头
        entry_list = modified_text.split('</>')

        temp_list = []

        for entry in entry_list:
            clean_txt = re.sub(r'<[^>]*>', '', entry)      #删除所有html标签
            del_blank_txt = ' '.join([s for s in clean_txt.splitlines() if s])     #去除空行
            temp_list.append(del_blank_txt)

        whole_text = '\n'.join(temp_list)


        with open(file_dst, 'w', encoding='UTF-8') as f_out:
            f_out.write(whole_text)


if __name__ == '__main__':
    main()