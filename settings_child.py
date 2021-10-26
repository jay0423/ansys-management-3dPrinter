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
    '\\': [
        ('', []),
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


