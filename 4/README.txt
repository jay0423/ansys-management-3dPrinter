cfrp2本の時の有効な形状を模索する．
cfrpの先端を細くすることで応力集中を小さくするといった方法．


cfrp2=1
3/main=5と同じ
特に特別な方法は取られていない．

cfrp2=1.2
条件はcfrp2=1と同じだが，メッシュ分割方法は四面体．

cfrp2=1.3
エポキシ樹脂とplaの破断ひずみを小さくするため，ヤング率をどちらも半分にして解析を行う．


cfrp2=2
cfrpの先端が徐々に細くなる形状
cfrpが重なっている部分は細くならない．


cfrp2=3
cfrp=2の拡張版
cfrpの先端が徐々に細くなる形状
cfrpが重なっている部分も細くなる．
X_cf_small_fir = CF_len - (R_cf_small / (1 / CF_lap))/2 （cfrp2=2）
↓
X_cf_small_fir = CF_len - (R_cf_small / (1 / CF_lap)) （cfrp2=3）
