"""
../csv/に格納されたansysで解析実行後の出力ファイルを整理する．
TIMEとFXの列から歪みと応力を算出し，エクセルファイルで書き出す．
"""


import pandas as pd
import numpy as np
import sys
import openpyxl as px

# 入力値
FILE_NAME = input("csvファイル名を入力：")
FILE_NAME = FILE_NAME.replace(".csv","")
try:
    df = pd.read_csv("{}.csv".format(FILE_NAME))
except:
    print("そのファイルは存在しません．")
    sys.exit()
DETAIL = input("ファイルの詳細：")
if DETAIL == "":
    DETAIL = FILE_NAME.replace("_", ", ")
try:
    SPEED = float(input("試験速度[mm/s]：")) / 1000
except:
    SPEED = 0.001 #試験速度[m/s]
try:
    LENGTH = float(input("試験片長さ[mm]：")) / 1000
except:
    LENGTH = 0.12 #試験片長さ[m]
try:
    CROSS_SECTIONAL_AREA = float(input("断面積[mm2]："))
except:
    CROSS_SECTIONAL_AREA = 48.60 #[mm2]


# dataframeの整理
df = df.iloc[:,0].apply(lambda x: pd.Series(x.split()))
df = df.iloc[2:,:2]
df.columns = ["TIME", "FX"]

# 数値の文字型を小数型に変換し，文字をnanに変換し削除する．
def clean(x): # map用の関数を定義
    try:
        return float(x)
    except:
        return None
df.loc[:,"TIME"] = df.loc[:,"TIME"].map(clean)
df.loc[:,"FX"] = df.loc[:,"FX"].map(clean)
df = df.dropna(how="any")

df["strain"] = df.loc[:,"TIME"] * SPEED / LENGTH # 歪みの追加
df["FX"] = df.loc[:,"FX"] * (-1) # 荷重の変換
df["stress"] = df.loc[:,"FX"] / CROSS_SECTIONAL_AREA # 応力の追加
MAX_ROW = len(df)

# ヤング率の算出
x_ = df["strain"][:int((MAX_ROW-1)*0.2)]
y_ = df["stress"][:int((MAX_ROW-1)*0.2)]
a, b = np.polyfit(x_,y_,1)
print("ヤング率： {}".format(a))

# 最大応力の算出
max_stress = max(df["stress"])

#EXCELファイルへ書き出し
df.to_excel("{}.xlsx".format(FILE_NAME), index=False)


# エクセルファイルへ詳細を記載する．
book = px.load_workbook("{}.xlsx".format(FILE_NAME))
sheet = book['Sheet1']
# セルへ書き込む
sheet['F1'] = '詳細'
sheet['G1'] = DETAIL
sheet['F2'] = '最大応力'
sheet['G2'] = max_stress
sheet['F3'] = 'ヤング率'
sheet['G3'] = a


# 散布図の追加
# 散布図をグラフ変数:chartとして定義
chart=px.chart.ScatterChart()

# y,xデータの範囲を選択
x = px.chart.Reference(book["Sheet1"] ,min_col=3 ,max_col=3 ,min_row=2 ,max_row=MAX_ROW+1)
y = px.chart.Reference(book["Sheet1"] ,min_col=4 ,max_col=4 ,min_row=2 ,max_row=MAX_ROW+1)

#系列変数seriesをy,xを指定して定義する
series = px.chart.Series(y, x)
#散布図として定義したchartへデータを指定したseries変数を渡す
chart.series.append(series)
chart.title = FILE_NAME
chart.x_axis.title = 'Strain [-]'
chart.y_axis.title = 'Stress [MPa]'
#A6セルにグラフを表示
book["Sheet1"].add_chart(chart,"F5")


# ヤング率用散布図の追加
# 散布図をグラフ変数:chartとして定義
chart2=px.chart.ScatterChart()

# y,xデータの範囲を選択
x = px.chart.Reference(book["Sheet1"] ,min_col=3 ,max_col=3 ,min_row=2 ,max_row=int((MAX_ROW-1)*0.2))
y = px.chart.Reference(book["Sheet1"] ,min_col=4 ,max_col=4 ,min_row=2 ,max_row=int((MAX_ROW-1)*0.2))

#系列変数seriesをy,xを指定して定義する
series = px.chart.Series(y, x)
#散布図として定義したchartへデータを指定したseries変数を渡す
chart2.series.append(series)
chart2.x_axis.title = 'Strain [-]'
chart2.y_axis.title = 'Stress [MPa]'
#A6セルにグラフを表示
book["Sheet1"].add_chart(chart2,"F22")

# 保存する
book.save("{}.xlsx".format(FILE_NAME))



# # 記録テキストファイルへの記載
# path = "../excel/single/file_details.txt"
# with open(path, mode="a") as f:
#     f.write("\nstress_strain_{}.xlsx    {}".format(FILE_NAME, DETAIL))

