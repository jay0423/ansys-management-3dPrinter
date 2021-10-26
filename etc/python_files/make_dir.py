"""
ipython make_dir.py
ディレクトリを自動的に作成する．
"""

import os
import sys

new_dir_path = input("フォルダを作成するパスを入力：")
if new_dir_path[-1] != "/":
    new_dir_path = new_dir_path + "/"
mother_name = input("フォルダの代表名を入力：")
son_name = input("数値を入力(カンマ','で分ける)：").replace(" ", "").replace("　", "").replace("，", ",").split(",")
dir_list = [new_dir_path + mother_name + son for son in son_name]

#確認
print("\n以下のフォルダを作成します．")
for dir in dir_list:
    print(dir)
a = input("実行:0，中断:1　：")
if a != "0":
    print("初めからやり直してください．")
    sys.exit()

for dir in dir_list:
    os.mkdir(dir)

print("作成しました．")