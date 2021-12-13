################ settings_child.py ###################
"""
ファイル名の更新・ファイルの自動作成
    ・DIR_STRUCTURE
    ・BASE_PATH
自動解析・応力ひずみ線図の作成
    ・ANALYSIS_PATH
応力ひずみ線図の作成
    ・DISTANCE, TIME, LENGTH
"""



### ディレクトリ，ファイルの自動作成
"""
DIR_STRUCTURE = {
    'パス':[
        ('変更部分の名前', [数字, 数字, 数字]),
        ('変更部分の名前', [数字, 数字, 数字]),
    ],
    'パス':[
        ('変更部分の名前', [数字, 数字, 数字]),
    ]
}
例）
DIR_STRUCTURE = {
    '4\\': [
        ('cfrp2_lap', [10, 20, 30]),
        ('thickness', [0.5, 1.0, 1.5, 2.0]),
    ],
    '4\\cfrp2_lap=10\\thickness=0.5\\': [
        ('kasa', [1, 2, 3])
    ]
}
注意：
パス名はスラッシュをつける．
「変更部分の名前」は，ABBREVIATION内に含まれていなければならない．
"""
DIR_STRUCTURE = {
    '7\\mechanism\\': [
        ('pla_young', [1.39, 2.78]),
        ('epo_young', [0.4, 0.9, 1.5]),
        ('epo_hizumi', [0.02, 0.04, 0.1]),
    ],
}



# 応力ひずみ線図・自動解析
"""
・応力ひずみ線図の作成する際のパスの指定．
・自動解析を行うパスの指定．複数可．
・記入されたパス以降のansysファイルをもとに解析が行われる．
例）
ANALYSIS_PATH = [
    "4\\test1\\",
    "4\\test2\\"
]
"""
ANALYSIS_PATH = [
    "4\\cfrp2=1.3\\"
]



# 自動解析
"""
解析ファイルを削除するか．
膨大な量の解析を行う場合はバソコンのハードディスクがいっぱいになってしまうため，解析が終われば削除する．
DELETE_ANSYS_FILES = False（削除しない・推奨）
DELETE_ANSYS_FILES = True（削除する）
"""
DELETE_ANSYS_FILES = False



# 応力ひずみ線図の作成
"""
引張時間・引張距離・解析モデルの長さをansysファイルから探し出し，応力ひずみ線図を作成する．
全て変数が一致していることを確認．
例）
base.ansys
    ~~~
    X1 = 100E-3
    ~~~
    DISTANCE = 2.0E-3
    ~~~
    TIME1 = 2
    ~~~
↓
DISTANCE = "DISTANCE"
TIME = "TIME1"
LENGTH = "X1"
"""
DISTANCE = "DISTANCE"
TIME = "TIME1"
LENGTH = "X1"




# ファイルの自動生成（Ansysファイルへの書き込み）
"""
書き込みの元の対象ファイル
DIR_STRUCTURE直下に常に置く場合は，""に設定しておく．
例）
BASE_PATH = "sample/base.ansys"  <- 必ずしもbase.ansysでなくて良い．
"""
BASE_PATH = ""


########### settings/settings_core.py ##############
"""
ファイル名の更新・ファイルの自動作成
    ・DIR_IGNORE
    ・FILE_EXTENSION
    ・OMMISION
    ・BBASE_FILE_NAME
    ・WRITE_EXTENSION
    ・ABBREVIATION
    ・DEFAOLUT_REPLACE_WORD_DICT
応力ひずみ線図の作成
    ・PATH_FILE_NAME
自動解析
    ・PY_DIR_PATH
    ・CWD_PATH
"""


# 無視するディレクトリリスト
DIR_IGNORE = [
    'etc',
    '__pycache__',
    '.git',
    'py',
    '.VSCodeCounter'
]



### make_stress_strain.MakeStressStrain
PATH_FILE_NAME = "path.xlsx"



### Refresh
# ファイル名をルール通りに作成する対象ファイルの拡張子
FILE_EXTENSION = [
    "ansys",
    "csv"
]



# ファイル名を変更しないファイルリスト
OMISSION = [
    'base.ansys',
    'sample.ansys',
    'settings_memo.py',
    'README.md',
    'README.txt'
]



# WriteAnsysFile
# BASE_FILE_NAME + "." + WRITE_EXTENSION
# デフォルトの書き込みの元の対象ファイル名（BASE_PATH==""の時），特に変更する必要はない．
BASE_FILE_NAME = "base"

# 書き込み対象の拡張子
WRITE_EXTENSION = "ansys"




### auto_analysis
# 実行ディレクトリパス
# PY_DIR_PATH = "C:\\Users\\matlab\\Documents\\ansys\\ansys-management-3dPrinter\\" # 藤井windowsPC
PY_DIR_PATH = "C:\\Users\\matlab\\Documents\\ansys\\ansys-management-3dPrinter\\" # 梶本windowsPC
# PY_DIR_PATH = "/Users/jay0423/Documents/GitHub/ansys-management-3dPrinter/" # 梶本macPC


# ansysデータの保存先のディレクトリ(windows)のパス
# CWD_PATH = "C:\\Users\\matlab\\Documents\\ansys\\ansys_fujii\\" # 藤井windowsPC
CWD_PATH = "C:\\Users\\matlab\\Documents\\ansys\\ansys_kajimoto\\" # 梶本windowsPC


# TEMPのパス
# TEMP_PATH = "C:\\Users\\matlab\\AppData\\Local\\Temp\\" # 藤井windowsPC
TEMP_PATH = "C:\\Users\\matlab\\AppData\\Local\\Temp\\" # 梶本windowsPC


### auto_analysis
# CPUのコア数
NPROC = 4



# ディレクトリ名の略称の定義
"""
「=」がない場合はそのまま，ある場合は「=」より左側を入力する．
略称は他と被っては行けない．
大文字禁止
"""
import os
import json
ABBREVIATION_PATH = PY_DIR_PATH + os.path.join("abbreviation.json")
f = open(ABBREVIATION_PATH, "r")
ABBREVIATION = json.load(f)["ABBREVIATION"]
f.close()



# ファイルの自動生成（Ansysファイルへの書き込み）
"""
デフォルト値
base.ansysに埋め込む値がなかった場合，以下の値を入力する．
キーは，ABBREVIATION内に含まれていなければならない．
"""
f = open(ABBREVIATION_PATH, "r")
DEFAOLUT_REPLACE_WORD_DICT = json.load(f)["DEFAOLUT_REPLACE_WORD_DICT"]
f.close()