import streamlit as st
import spacy

st.set_page_config(page_title="英文法解析", layout="centered")

st.title("📘 自然な英文法解析アプリ（スマホ対応）")

text = st.text_area("英文を入力してください：", height=150, placeholder="例：I saw a man with a telescope.")

if st.button("文法解析を実行"):
    if not text.strip():
        st.warning("英文を入力してください。")
    else:
        try:
            nlp = spacy.load("en_core_web_sm")
        except:
            st.error("SpaCyモデルが読み込めません。requirements.txtに `en_core_web_sm` を追加してください。")

        doc = nlp(text)

        st.subheader("📌 単語と品詞")
        for token in doc:
            st.write(f"{token.text} → {token.pos_}（{token.tag_}） | 係り先: {token.head.text}")

        st.subheader("📎 構文依存関係")
        st.graphviz_chart(spacy.displacy.render(doc, style="dep", options={"compact": True}, jupyter=False))
