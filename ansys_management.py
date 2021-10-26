"""
ansys_management.py
読み込み時，settings_child.pyとpy/settings/settings_core.pyをpy/settings/settings.pyへコピーする．

関数一覧
    設定の管理
        ・settings_copy_to_child
        ・settings_memo
    更新・自動生成・応力ひずみ線図・自動解析
        ・refresh_main
        ・write_ansys_file_main
        ・path_multiple_stress_strain_main
        ・auto_analysis
        ・all
"""


import sys
import os
import time

# ファイル自動作成または自動解析が実行されたとき，py/のsettings.pyへsettings_child.pyとpy/settings/settings_core.pyをコピペする．
with open(os.path.normcase("py/settings/settings_core.py"), encoding="utf-8_sig") as f: # 読み取り
    data_lines_core = f.readlines()
with open(os.path.normcase("settings_child.py"), encoding="utf-8_sig") as f: # 読み取り
    data_lines_child = f.readlines()
with open(os.path.normcase("py/settings/settings.py"), mode="w", encoding="utf-8_sig") as f: # 書き込み
    f.writelines(data_lines_child + data_lines_core)

# 初期チェック
from py.settings.settings_check import FIRST_CHECK
FIRST_CHECK().check_first_all()

from py.settings.settings_check import FIRST_PATH_CHECK
from py.settings import settings
from py.core.get_path import GetPath
from py.core.files_management import Refresh, WriteAnsysFile
from py.core.make_stress_strain import MakeStressStrain, MakeStressStrainFromAnsysFile
from py.core.auto_analysis import AutoAnalysis


SLASH = os.path.normcase("a/")[-1]



################ 設定の管理 ###################

def settings_copy_to_child():
    """
    ファイル自動作成または自動解析が終了したとき，settings_child.pyへ
    py/settings/settings_copy_base.pyをコピペする．
    """
    with open(os.path.normcase("py/settings/settings_copy_base.py"), encoding="utf-8_sig") as f: # 読み取り
        data_lines_copy_base = f.readlines()
    with open(os.path.normcase("settings_child.py"), mode="w", encoding="utf-8_sig") as f: # 書き込み
        f.writelines(data_lines_copy_base)



def settings_memo(first_path):
    with open(os.path.normcase("py/settings/settings_core.py"), encoding="utf-8_sig") as f: # 読み取り
        data_lines_core = f.readlines()
    with open(os.path.normcase("settings_child.py"), encoding="utf-8_sig") as f: # 読み取り
        data_lines_child = f.readlines()
    with open(os.path.normcase(first_path + "settings_memo.py"), mode="w", encoding="utf-8_sig") as f: # 書き込み
        f.writelines(data_lines_child + data_lines_core)


def _check_first_path(first_path):
    if first_path[-1] != SLASH:
        first_path += SLASH
    return first_path


################ 更新・自動生成・応力ひずみ線図・自動解析 ###################

def refresh_main():
    # ファイル名の修正
    # ファーストパスの選択
    files_dir = [f for f in os.listdir() if os.path.isdir(os.path.join(f))]
    files_dir = [f for f in sorted(files_dir) if f not in settings.DIR_IGNORE]
    for i, l in enumerate(files_dir):
        print("{}： {}{}".format(i+1, l, SLASH))
    first_path = int(input("入力してください："))
    try:
        first_path = files_dir[first_path-1] + SLASH
    except:
        print("やり直してください．")
        sys.exit()

    a = Refresh(first_path)
    a.refresh()




def write_ansys_file_main():
    # ファイルの自動生成とbase.ansysの書き込み
    key_list = list(settings.DIR_STRUCTURE.keys())
    for i, first_path in enumerate(key_list):
        print(first_path)
        if i == 0:
            settings_memo(first_path)
        FIRST_PATH_CHECK(first_path).check_write_ansys_file_main() # 設定の確認
        a = WriteAnsysFile(_check_first_path(first_path))
        if i != 0:
            # 重複するファイルを削除する．
            a.delete_files()
        a.make_files()
    print("ファイルの作成完了．Ansysファイルに変数が埋め込まれているか必ず確認してください．")




def path_multiple_stress_strain_main():
    # 応力ひずみ線図の生成
    p = input("\n入力方法を選択\n0: path.xlsx\n1: settings_child.ANALYSIS_PATH\n入力してください：")
    if p == "0":
        a = MakeStressStrain()
        a.make_stress_strain()
    elif p == "1":
        if settings.ANALYSIS_PATH != []:
            CROSS_SECTIONAL_AREA = float(input("\n断面積[mm2]を入力してください．\n入力してください："))
            for first_path in settings.ANALYSIS_PATH:
                FIRST_PATH_CHECK(first_path).check_path_multiple_stress_strain_main()
            for first_path in settings.ANALYSIS_PATH:
                d = MakeStressStrainFromAnsysFile(first_path)
                d.CROSS_SECTIONAL_AREA = CROSS_SECTIONAL_AREA
                d.make_stress_strain()
        else:
            print("settings_child.ANALYSIS_PATHにパスを入力してください．")
            sys.exit()
    else:
        print("やり直してください．")
        sys.exit()




def auto_analysis():
    # 自動解析の実行
    if settings.DELETE_ANSYS_FILES:
        p = input("\nsettings_child.pyのDELETE_ANSYS_FILESがTrueとなっています．本当にAnsysデータベースファイルなどを削除しますか？\n0: はい\n1: いいえ（ディレクトリ名を設定していない場合）\n入力してください：")
        if p != "0":
            print("やり直してください．")
            sys.exit()

    # ファーストパスの選択
    if settings.ANALYSIS_PATH == []:
        print("Error: 解析を行うパスが指定されていません．settings_child.pyのANALYSIIS_PATHでパスを指定してください．")
        sys.exit()

    dir_name = input("\nプロジェクト名（ansysファイル格納ディレクトリ名）を入力：")
    # csvファイルへ時間と力の出力を実装するかの選択．
    output_csv = input("\ncsvファイルへ出力しますか？\n0: はい\n1: いいえ（ディレクトリ名を設定していない場合）\n入力してください：")
    if output_csv == "0":
        output_csv = True
    elif output_csv == "1":
        output_csv = False
    else:
        print("やり直してください．")
        sys.exit()
    if settings.DELETE_ANSYS_FILES == True and output_csv == False:
        print("csvに出力しないのであれば，settings_child.pyのDELETE_ANSYS_FILESはFalseにしてください．")
        sys.exit()

    if output_csv:
        excel_perm = input("\n応力ひずみ線図のエクセルファイルを作成しますか？（全ての解析モデルで断面積が同じ必要があります．）\n0: はい\n1: いいえ\n入力してください：")
        if excel_perm == "0":
            excel_perm = True
        else:
            excel_perm = False
        if excel_perm:
            CROSS_SECTIONAL_AREA = float(input("\n断面積[mm2]を入力してください．\n入力してください："))

    # 実行ファイルのパスを取得
    ansys_path_list = []
    for first_path in settings.ANALYSIS_PATH:
        a = GetPath(first_path=_check_first_path(first_path), slash=SLASH)
        ansys_path_list += a.get_list("ansys", omission_files=settings.OMISSION)
    print("\n実行ファイルの確認")
    for i, path in enumerate(ansys_path_list):
        print("{}: {}".format(i+1, path))
    analysis_num = int(input("解析をしたい番号を入力．\n0: 全て解析実行\n1 - {}：これ以降の番号を解析\n入力してください：".format(len(ansys_path_list))))
    if analysis_num == 0:
        pass
    elif analysis_num >= 1 and analysis_num <= len(ansys_path_list):
        ansys_path_list = ansys_path_list[analysis_num-1:]
    else:
        print("やり直してください．")
        sys.exit()

    # 解析実行
    print("解析開始")
    dir_name = settings.CWD_PATH + SLASH + dir_name
    os.mkdir(dir_name)
    b = AutoAnalysis(output_csv=output_csv)
    b.dir_name = dir_name
    t1 = time.time()
    b.multiple_auto_analysis(ansys_path_list)
    t2 = time.time()
    elapsed_time = t2-t1
    print(f"経過時間：{elapsed_time}s")

# 応力ひずみ線図のエクセルファイルの生成
    print("\n応力ひずみ線図作成の開始")
    if excel_perm == True and output_csv == True:
        for first_path in settings.ANALYSIS_PATH:
            d = MakeStressStrainFromAnsysFile(_check_first_path(first_path))
            d.CROSS_SECTIONAL_AREA = CROSS_SECTIONAL_AREA
            d.dir_name = dir_name
            print()
            d.make_stress_strain()
        print("応力ひずみ線図作成の完了\n")



def all():
    ### ファイルの自動生成，自動解析，応力ひずみ線図の生成
    # 初期設定
    dir_name = input("\nプロジェクト名（ansysファイル格納ディレクトリ名）を入力：")
    os.mkdir(settings.CWD_PATH + SLASH + dir_name)
    CROSS_SECTIONAL_AREA = float(input("\n断面積[mm2]を入力してください．\n入力してください："))

    # ファイルの自動生成とbase.ansysの書き込み
    for i, first_path in enumerate(settings.DIR_STRUCTURE):
        if i == 0:
            settings_memo(first_path)
        FIRST_PATH_CHECK(first_path).check_all() # 設定の確認
        a = WriteAnsysFile(first_path)
        # 重複するファイルを削除する．
        a.delete_files()
        a.make_files()
    print("ファイル作成完了\n")
    time.sleep(1)

    # 自動解析
    completion = input("0: 解析実行, 1: やりなおす\n入力してください：")
    if completion != "0":
        print("やり直してください．")
        sys.exit()
    print("解析開始")
    # all()の場合，settings.pyのDIR_STRUCTUREからパスを取得し，その部分のみの解析を行う．
    def get_first_path_list():
        # パスのリストを取得する．
        DIR_STRUCTURE = sorted(settings.DIR_STRUCTURE)
        dir0 = DIR_STRUCTURE[0]
        first_path_list = [dir0]
        for dir in DIR_STRUCTURE[1:]:
            if dir0 not in dir:
                first_path_list.append(dir)
        return first_path_list
    first_path_list = get_first_path_list() # 解析するファーストパスのリストを取得する．
    # 実行ファイルのパスを取得
    ansys_path_list = []
    for first_path in first_path_list:
        b = GetPath(first_path=first_path, slash=SLASH)
        ansys_path_list += b.get_list("ansys", omission_files=settings.OMISSION)
    # 自動解析の実行
    c = AutoAnalysis(output_csv=True)
    c.dir_name = dir_name
    t1 = time.time()
    c.multiple_auto_analysis(ansys_path_list)
    t2 = time.time()
    elapsed_time = t2-t1
    print(f"総解析時間：{elapsed_time}s")
    print("解析完了\n")

    # 応力ひずみ線図のエクセルファイルの生成
    for first_path in first_path_list:
        d = MakeStressStrainFromAnsysFile(_check_first_path(first_path))
        d.CROSS_SECTIONAL_AREA = CROSS_SECTIONAL_AREA
        d.make_stress_strain()
    print("応力ひずみ線図作成の完了")





################ 呼び出しの実行 ###################

if __name__ == '__main__':
    print("\n!!!　実行する作業の選択　!!!")
    print("-----------------------------")
    print("1： ファイルの自動生成")
    print("2： 自動解析")
    print("3： 応力ひずみ線図の作成")
    print("4： All")
    print("-----------------------------")
    print("5： ファイル名の更新")
    print("6： settings_childの初期化")
    print("-----------------------------")
    a = input("入力してください：")
    if a == "1":
        write_ansys_file_main()
    elif a == "2":
        auto_analysis()
    elif a == "3":
        path_multiple_stress_strain_main()
        sys.exit()
    elif a == "4":
        all()
    elif a == "5":
        refresh_main()
        sys.exit()
    elif a == "6":
        settings_copy_to_child()
        sys.exit()
    else:
        print("やり直してください．")
        sys.exit()
    # 最終処理
    permission = input("settings_child.pyを初期化しますか？\n0: はい\n1: いいえ\n入力してください：")
    if permission == "0":
        settings_copy_to_child()
