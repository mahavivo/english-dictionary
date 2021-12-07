#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" 从牛津高阶双解英汉词典（第8版）mdx文件中提取中文释义 """

import csv
from bs4 import BeautifulSoup


file_src = r'C:\Users\vivo\Desktop\OxfordAdvanced.txt'

file_dst = r'C:\Users\vivo\Desktop\OxfordAdvanced_extractor.txt'
file_csv = r'C:\Users\vivo\Desktop\OxfordAdvanced_extractor.csv'


def make_pos(soup):
    pos = soup.find(class_='pos')
    if pos:
        pos = pos.get_text()
    else:
        pos = ''

    return pos


def make_z_n(soup):
    z_n_soup = soup.find(class_='z_n')
    if z_n_soup:
        z_n = z_n_soup.get_text()
    else:
        z_n = ''

    return z_n


def make_sense_g(soup):
    sense = soup.find(class_='sense-g')
    if sense:
        if sense.find(class_='chn'):
            sense = sense.find(class_='chn').get_text()
            sense =   '(' + sense + ')'
        else:
            sense = soup.find(class_='sense-g').get_text()
    else:
        sense = ''

    return sense


def make_label_g(soup):
    label = soup.find(class_='label-g')
    if label:
        if label.find(class_='schn'):
            label = label.find(class_='schn').get_text()
            label =  '(' + label + ')'
        elif label.find(class_='chn'):
            label = label.find(class_='chn').get_text()
            label =  '(' + label + ')'
        else:
            label = soup.find(class_='label-g').get_text()
    else:
        label = ''

    return label


def make_dc(soup):
    dc = soup.find(class_='dc')
    if dc:
        if dc.find(class_='chn'):
            dc = dc.find(class_='chn').get_text()
            dc =   '(' + dc + ')'
        else:
            dc = soup.find(class_='dc').get_text()
    else:
        dc = ''

    return dc


def make_def_g(soup):
    def_soup = soup.find(class_='def-g')
    if def_soup:
        d_soup = def_soup.find(class_='d')
        if d_soup:
            definition = d_soup.find(class_='chn')
            if definition:
                definition = definition.get_text()
            else:
                definition = ''
        else:
            definition = def_soup.find(class_='chn')
            if definition:
                definition = definition.get_text()
            else:
                definition = ''
    else:
        definition = ''

    return definition


def make_full_def(soup):
    def_soup = soup.find(class_='def-g')

    if def_soup:
        dr_g_soup = soup.find_all(class_='dr-g')
        if dr_g_soup:
            for x in dr_g_soup:
                x.decompose()

        ids_g_soup = soup.find_all(class_='ids-g')
        if ids_g_soup:
            for x in ids_g_soup:
                x.decompose()

        pvs_g_soup = soup.find_all(class_='pvs-g')
        if pvs_g_soup:
            for x in pvs_g_soup:
                x.decompose()


    if soup.find(class_='label-g') and soup.find(class_='sense-g'):

        label = make_label_g(soup)
        sense = make_sense_g(soup)

        definition = make_def_g(soup)

        full_def = label + sense + definition


    elif soup.find(class_='label-g'):

        label = make_label_g(soup)
        definition = make_def_g(soup)

        full_def = label + definition


    elif soup.find(class_='sense-g'):

        sense = make_sense_g(soup)
        definition = make_def_g(soup)

        full_def = sense + definition

    elif soup.find(class_='dc'):

        dc = make_dc(soup)
        definition = make_def_g(soup)

        full_def = dc + definition

    else:

        definition = soup.find(class_='chn')
        if definition:
            full_def = definition.get_text()
        else:
            full_def = ''


    return full_def


def make_definition(soup):
    ng_trans = soup.find_all(class_='n-g')

    if ng_trans:           # 处理一词多个义项
        def_text = []

        for trans_item in ng_trans:

            zn = make_z_n(trans_item)
            definition = make_full_def(trans_item)
            each_trans = zn + definition

            def_text.append(each_trans)

        full_def = ' '.join(def_text)

    else:
        full_def = make_full_def(soup)

    return full_def


def main():
    with open(file_src, 'r', encoding='UTF-8') as f:
        full_text = f.read()
        headwords = full_text.split('</>')

        for headword in headwords:
            soup = BeautifulSoup(headword, 'lxml')

            if soup.find('link'):

                trans_list = []

                entry = soup.find(class_='no-dot-h')
                if entry:
                    entry = entry.get_text()
                else:
                    entry = ''
                trans_list.append(entry)

                phone_us = soup.find(class_='phon-us')
                if phone_us:
                    phone_us = phone_us.get_text()
                    if phone_us:
                        phone_us = '[' + phone_us + ']'
                else:
                    phone_us = ''
                trans_list.append(phone_us)

                p_g = soup.find_all(class_='p-g')
                def_list = []

                if p_g:                # 处理一词多个词性的状况
                    for p_g_item in p_g:
                        p_g_pos = make_pos(p_g_item)
                        p_g_def = make_definition(p_g_item)
                        def_list.append(p_g_pos + ' ' + p_g_def)
                    definition = ' '.join(def_list)

                    trans_list.append(definition)
                else:
                    pos = make_pos(soup)
                    definition = make_definition(soup)
                    definition = pos + ' ' + definition

                    trans_list.append(definition)


                with open(file_dst, 'a+', encoding='UTF-8') as f_out:
                    trans_text = ' '.join(trans_list)
                    f_out.write(trans_text + '\n')

                # with open(file_csv, 'a+', newline='', encoding='UTF-8') as f_csv:
                #     writer = csv.writer(f_csv)
                #     writer.writerow(trans_list)


if __name__ == '__main__':
    main()