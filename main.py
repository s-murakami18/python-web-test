import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Python Web テスト')

st.write('プログレスバーの表示')
# st.sidebar.write('Interactive Widgets')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

# チェックボックスによるメディアの表示可否
# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='Mizuki', use_column_width=True)

# セレクトボックスによる値の動的変更
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい。',
#     list(range(1, 11))
# )
#
# 'あたなの好きな数字は、', option, 'です。'

# テキスト入力による値の動的変更
# text = st.text_input('あなたの趣味を教えて下さい。')
# 'あなたの趣味は：', text

# スライダーによる値の動的変更
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

# レイアウトを整える
# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
#
# 'あなたの趣味は：', text
# 'コンディション：', condition

# ２カラムレイアウトにする
# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expanderの追加
expander = st.beta_expander('問い合せ')
expander.write('問合せ内容を書く')

# img = Image.open('sample.jpg')
# # use_column_width → 実際のレイアウトの横幅に合わせて表示する
# st.image(img, caption='Mizuki', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# df = pd.DataFrame({
#    '１列目': [1, 2, 3, 4],
#    '２列目': [10, 20, 30, 40]
# })

# write() → 表の細かい設定はできない
# st.write(df)

# dataframe() → 表の縦横の長さを指定できる
# axis(行=1, 列=0)
# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))

# table() = static(静的)なテーブルを作りたい時に使用する(sortはできない)
# st.table(df.style.highlight_max(axis=0))

# マジックコマンドを使用（マークダウン）
# """
# # 章
# ## 節
# ### 項
#
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# 折れ線グラフを描く
# st.line_chart(df)

# エリアチャート
# st.area_chart(df)

# 棒グラフ
# st.bar_chart(df)

# map
# st.map(df)


