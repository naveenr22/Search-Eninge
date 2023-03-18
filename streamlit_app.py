import streamlit as st
import pandas as pd
from gensim.models import Word2Vec
model = Word2Vec.load("word2vec.model")
st.header("Unt edu Search engine")
text_input = st.text_input(
    "Enter some text 👇"
)
def make_clickable(val):
    # target _blank to open new window
    return '<a target="_blank" href="{}">{}</a>'.format(val, val)

df = pd.read_excel('final_unt.xlsx')
#df.style.format({'url': make_clickable})
# print(df)
match_term = ''
try:
    match_term = model.wv.most_similar(text_input)[0][0]
except:
    pass
# st.write(match_term)
data = pd.DataFrame()
if text_input:
    data = df[df['text'].str.contains(f'{text_input}|{match_term}',regex=True, na=False)]

# print(data)
if not data.empty:
    st.write(f"Total Results found {data.shape[0]}")
    for index,row in data.iterrows():
        st.header(f"[{row[1]}]({row[3]})")
        #st.markdown(row[3])
        st.text(row[2][0:100])