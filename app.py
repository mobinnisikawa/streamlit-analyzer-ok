import streamlit as st
import spacy
import subprocess
import sys

# SpaCyのモデルがなければインストール（Streamlit Cloud対応）
try:
    nlp = spacy.load("en_core_web_sm")
except:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

import pandas as pd

st.title("英文テキスト文法解析アプリ")

st.markdown("""
このアプリでは、英文テキストを透視的かつ文法的に詳細に分析することができます。  
たとえば、名詞・動詞・前置詞・構文構造などの文法情報を自動で抽出し、可視化します。  
**対応予定：カラマーゾフの兄弟、哲学論文、学術英文、など。**
""")

st.markdown("---")  # 区切り線（任意）

st.set_page_config(page_title="英文法解析", layout="centered")

st.title("📘 自然な英文法解析アプリ（スマホ対応）")

text = st.text_area(
    "英文を入力してください",
    height=120,
    placeholder="例：I saw a man with a telescope.",
    help="文法的に分析したい英語の文を入力してください（複数行もOK）"
)


if st.button("文法解析を実行"):
    if not text.strip():
        st.warning("英文を入力してください。")
    else:
import streamlit as st
import subprocess
import sys

# SpaCyのモデルがなければインストール（Streamlit Cloud対応）
try:
    import spacy
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "spacy==3.5.3"])
    import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

import pandas as pd


        import pandas as pd  # ←ファイルの一番上に import 済みなら不要

# 解析結果を表形式にする
results = []
for token in doc:
    results.append({
        "単語": token.text,
        "品詞": token.pos_,
        "詳細タグ": token.tag_,
        "係り先": token.head.text,
        "依存関係": token.dep_
    })

st.subheader("🔎 文法解析の表")
st.dataframe(pd.DataFrame(results), use_container_width=True)


        st.subheader("📎 構文依存関係")
        st.graphviz_chart(spacy.displacy.render(doc, style="dep", options={"compact": True}, jupyter=False))
