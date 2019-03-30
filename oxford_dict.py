#!/usr/bin/env python
# -*- coding: UTF-8 -*-


file_src = "/users/vivo/desktop/oxford_dict_english.txt"

file_dst = "/users/vivo/desktop/dict_result.txt"


def parser(text):
    if text.startswith("★☆☆"):
        if "▶" in text:
            text = text.replace("▶", "\n▶")
            outtext = text[6:].strip()
        else:
            outtext = text[6:].strip()
    elif text.startswith(" /"):
        outtext = text.strip()

    elif text.startswith("1."):
        outtext = "1." + text.partition("•")[2]
    elif text.startswith("2."):
        outtext = "2." + text.partition("•")[2]
    elif text.startswith("3."):
        outtext = "3." + text.partition("•")[2]
    elif text.startswith("4."):
        outtext = "4." + text.partition("•")[2]
    elif text.startswith("5."):
        outtext = "5." + text.partition("•")[2]
    elif text.startswith("6."):
        outtext = "6." + text.partition("•")[2]
    elif text.startswith("7."):
        outtext = "7." + text.partition("•")[2]
    elif text.startswith("8."):
        outtext = "8." + text.partition("•")[2]
    elif text.startswith("9."):
        outtext = "9." + text.partition("•")[2]
    elif text.startswith("10."):
        outtext = "10." + text.partition("•")[2]
    elif text.startswith("11."):
        outtext = "11." + text.partition("•")[2]
    elif text.startswith("12."):
        outtext = "12." + text.partition("•")[2]
    elif text.startswith("13."):
        outtext = "13." + text.partition("•")[2]
    elif text.startswith("14."):
        outtext = "14." + text.partition("•")[2]
    elif text.startswith("15."):
        outtext = "15." + text.partition("•")[2]
    elif text.startswith("16."):
        outtext = "16." + text.partition("•")[2]
    elif text.startswith("17."):
        outtext = "17." + text.partition("•")[2]
    elif text.startswith("18."):
        outtext = "18." + text.partition("•")[2]
    elif text.startswith("▶"):
        outtext = text.strip()
    elif text.startswith("【IDIOMS】"):
        outtext = text.strip()
    elif text.startswith(" --›"):
        outtext = text.strip()
    elif text.startswith("◘"):
        outtext = text.strip()
    elif text.startswith("【派生】"):
        outtext = text.strip()
    elif text.startswith("♦"):
        outtext = text.strip()
    elif text.startswith("【PHR V】"):
        outtext = text.strip()
    elif text.startswith("•"):
        outtext = text.strip()
    else:
        outtext = ""

    return outtext


all_entry = []

with open(file_src, 'r') as f:
    full_text = f.read()
    full_text = full_text.replace("/▶", "/\n▶")


    entry_list = full_text.split("————————————")
    for entry in entry_list:
        if entry:
            row_list = []
            line_list = entry.splitlines()
            for line in line_list:
                line_out = parser(line)
                row_list.append(line_out)
            row_list = [x for x in row_list if x != ""]
            new_entry = '\n'.join(row_list)
            new_entry = new_entry.strip()

        all_entry.append(new_entry)

with open(file_dst, 'w') as f_out:
    for each in all_entry:
        # each = " ".join(each.splitlines())
        f_out.write('\n\n' + each)