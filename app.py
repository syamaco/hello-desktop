import streamlit as st
import pandas as pd


@st.cache_data
def get_data(file) -> pd.DataFrame:
    # df = pd.read_excel(file)
    df = pd.read_csv(file)
    return df


def load_as_df(uploaded_file):
    df = get_data(uploaded_file)
    st.dataframe(df)

    x  = 'summary_month'
    y = 'participants'

    if x in df and y in df:
        import plotly.express as px

        fig = px.bar(df, x=x, y=y)
        st.plotly_chart(fig)
    else:
        st.write('グラフ描画カラム「summary_month」（形式:yyyy-MM）, 「participants」（形式:N） が見つかりません。')


def load_as_raw(uploaded_file):
    import os, csv, tempfile
    from pathlib import Path

    with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
        path = Path(tmp_file.name)
        path.write_bytes(uploaded_file.getvalue())

        st.write(tmp_file.name)

        # path = os.path.join(tempfile.mkdtemp(), uploaded_file.name)
        with open(path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                st.write(row)


st.title("CSVファイル読み込み＆グラフ描画")

# CSVファイルの読み込み
st.subheader("CSVファイルをアップロードしてください。")
uploaded_file = st.file_uploader("CSVファイル", type="csv")

if uploaded_file:
    st.write(uploaded_file.name)

    # load_as_raw(uploaded_file)
    load_as_df(uploaded_file)
