################ settings_child.py ###################
"""
ファイル名の更新・ファイルの自動作成
    ・ABBREVIATION
    ・DIR_STRUCTURE
    ・BASE_PATH
応力ひずみ線図の作成
    ・DEFAOLUT_REPLACE_WORD_DICT, DISTANCE, TIME, LENGTH, CROSS_SECTIONAL_AREA
自動解析
    ・ANALYSIS_PATH
"""



# ディレクトリ名の略称の定義
"""
「=」がない場合はそのまま，ある場合は「=」より左側を入力する．
略称は他と被っては行けない．
大文字禁止
"""
ABBREVIATION = {
    'cfrp0': 'c0', # CFRPなし
    'cfrp1': 'c1', # CFRP1本
    'cfrp2_lap': 'c2_l', # CFRP2本，重ね継ぎ手長さ
    'thickness': 'th', # CFRPの太さ
    'gap': 'g', # CFRP間の距離
    'div': 'd', # メッシュ分割の細かさ
    'kasa': 'kasa', # 傘形状
    'cf_tensile': 'cft',
    ###########################################
    'time_distance': 't', # 引張速度と引張距離
    'correction': 'cor', # 修正バージョン
    'length': 'len', # 試験片長さ
    'solid185': 's185', # solid185
    'solid186': 's186', # solid186
    'cfrp_tensile': 'cfr', # CFRPの強度
    'epo_tensile': 'epo', # epoxyの強度
    'super': 'sup', # その他改良
    'cfrp': 'cfrp',
    'epoxy': 'epoxy',
    'pla': 'pla',
}



### ディレクトリ，ファイルの自動作成
"""
ディレクトリ構成．
DIR_STRUCTURE = {
    'パス':[
        ('変更部分の名前', [数字, 数字, 数字]),
        ('変更部分の名前', [数字, 数字, 数字]),
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
    ],
    '4\\cfrp2_lap=20\\thickness=0.5\\': [
        ('div', [0.5, 1.0, 2.0])
    ],
}

注意：
パス名はスラッシュをつける．
「変更部分の名前」は，ABBREVIATION内に含まれていなければならない．
"""
DIR_STRUCTURE = {
    '4\\cfrp1\\': [
        ('cf_tensile', [500, 600, 700, 1000, 1500]),
    ],
    '4\\cfrp2\\': [
        ('cfrp2_lap', [10, 20, 30]),
    ],
}



# ファイルの自動生成（Ansysファイルへの書き込み）
"""
デフォルト値
base.ansysに埋め込む値がなかった場合，以下の値を入力する．
キーは，ABBREVIATION内に含まれていなければならない．
"""
DEFAOLUT_REPLACE_WORD_DICT = {
    'cfrp2_lap': '20', # CFRP2本，重ね継ぎ手長さ
    'thickness': '2.0', # CFRPの太さ
    'gap': '0.5', # CFRP間の距離
    'div': '1.0', # メッシュ分割の細かさ
}


# ファイルの自動生成（Ansysファイルへの書き込み）
DISTANCE = "DISTANCE"
TIME = "TIME1"
LENGTH = "X1"
CROSS_SECTIONAL_AREA = 50 # 数値



# ファイルの自動生成（Ansysファイルへの書き込み）
"""
書き込みの元の対象ファイル
DIR_STRUCTURE直下に常に置く場合は，""に設定しておく．
例）
BASE_PATH = "sample/base.ansys"  <- 必ずしもbase.ansysでなくて良い．
"""
BASE_PATH = ""



# 自動解析
"""
自動解析を行うパスの指定．複数可．
例）
ANALYSIS_PATH = [
    "4\\test1\\",
    "4\\test2\\"
]
"""
ANALYSIS_PATH = [
    "4\\cfrp2\\",
]


########### settings/settings_core.py ##############
"""
ファイル名の更新・ファイルの自動作成
    ・DIR_IGNORE
    ・FILE_EXTENSION
    ・OMMISION
    ・BBASE_FILE_NAME
    ・WRITE_EXTENSION
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
    'py'
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
PY_DIR_PATH = "C:\\Users\\matlab\\Documents\\ansys-management\\"

# ansysデータの保存先のディレクトリ(windows)
CWD_PATH = "C:\\Users\\matlab\\ansys_kajimoto\\"
