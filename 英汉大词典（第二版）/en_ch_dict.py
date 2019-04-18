#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parser(text):
    # "派生"标记【卍】 和 "习语"标记【★】尚未处理
    outtext = text.replace("■", "").replace("ⓐ", ""). \
        replace("⏎", "").replace("▶", "").replace("➜", "")

    return outtext


def main():
    file_src = "/users/vivo/desktop/英汉大词典（第二版）.txt"
    file_dst = "/users/vivo/desktop/英汉大词典_edited.txt"

    all_entry = []

    with open(file_src, 'r') as f:
        full_text = f.read()

        entry_list = full_text.split("————————————")
        for entry in entry_list:
            if entry:
                row_list = []
                line_list = entry.splitlines()
                for line in line_list:
                    line_out = parser(line)
                    row_list.append(line_out)
                # row_list = [x for x in row_list if x != ""]
                new_entry = '\n'.join(row_list)  # 不分行显示则用空格代替"\n"
                new_entry = new_entry.strip()

            all_entry.append(new_entry)

    with open(file_dst, 'w') as f_out:
        for each in all_entry:
            # each = " ".join(each.splitlines())
            f_out.write('\n\n————————————\n' + each)


if __name__ == '__main__':
    main()
