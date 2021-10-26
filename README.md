# ansys-management

#### Ansys Mechanical APDL
Ansysのディレクトリ構成管理・自動解析・応力ーひずみ線図のエクセル生成を行います．
本ライブラリを使用すれば，ワンクリックで複数のansys解析から，応力ひずみ線図の生成まで自動的に行うことができ，ansys解析の効率を大幅に向上させることができます．

---

### ディレクトリ構成管理
  ここで定めるルールに従い，ディレクトリとファイルを自動生成します．特にansysファイルにおいては，変更したい数値の部分を自動で埋め込み，作成してくれます．


### 自動解析
  Ansys Mechanical APDLのAPIを利用し，解析を自動的に行います．ansysを実行する際，複数のパラメータを変更させて解析を行いたい場合があると思います．
  手動の場合，一つ一つのパラメータを変更させて解析を行うため，解析が終わるごとに解析の設定をし直さなければならず，とても非効率です．
  そこで，本ライブラリを用いることで，自動的に複数の解析を一気に行い，無駄な時間を省くことができます．


### 応力ーひずみ線図の生成
  解析結果のcsvファイルから，応力ひずみ線図を自動的に生成し，一つのエクセルファイルにまとめます．


## ソフトウェアバージョン ・ Pythonライブラリ
  - Visual Studio Code推奨（.ansys拡張子の拡張機能があるため）
  - Ansys Mechanical APDL 17.2以降
  - Python 3.8.8
  - IPython 7.22.0
  - [ansys-mapdl-core](https://mapdldocs.pyansys.com/getting_started/running_mapdl.html)
  - pandas
  - numpy


## Set Up
```bash
git clone "https://github.com/jay0423/ansys-management.git"
```
また，上記ソフトウェア，ライブラリをpipあるいはcondaによってインストールします．


## 実行手順
以下の手順により，処理を実行することができる．
  - ```settings.py```にて設定を完了させる．
  - 特定ディレクトリにbase.ansysを作成し，実行ansysを作成する．
  - 変更させたい部分を{% example %}というように書き換える．
  - 下記コマンドをコマンドプロンプトで実行する．
```bash
ipython ansys_managemet.py
```
詳しくはMANUAL.mdを参照してください．


## 注意点
Ansys Mechanical APDLを複数バージョンインストールしているとき，自動解析が行われずエラーが生じてしまう可能性があります．
複数インストールしている場合，コマンドプロンプトからipythonを起動し，以下コマンドを打ち込み，表示されるAnsysバージョンとライセンスを取得しているAnsysバージョンが一致していることを確認してください．

```ipython
from ansys.mapdl.core import launch_mapdl
mapdl = launch_mapdl()
print(mapdl.version)
```

ライセンスを取得しているものとバージョンが一致していない場合，そのAnsysはアンインストールしてください．