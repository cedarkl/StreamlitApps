import streamlit as st
import pandas as pd
import string
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize


st.title("Text Process App")
st.write('''
Let's transform your text data to clean-and-clear for training!
''')

try:
   uploaded_file = st.file_uploader("Choose a file", type=['csv'])
   if uploaded_file is not None:
       st.subheader("Raw data")
       data = pd.read_csv(uploaded_file)
       st.write(data.head())
       st.write(data.shape)

       st.subheader("Transform data")
       def clean_data(text_col):
           text_col = text_col.map(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
           text_col = text_col.map(lambda x: x.replace('\n', ' '))
           text_col = text_col.map(lambda x: x.lower())
           return text_col

       # data['full_text'] = clean_data(data['full_text'])
       # st.write(data.head())

       def transform_data(data, text_col):  # text column of the data
           # Count the sentences of each text
           data['sent_count'] = text_col.map(lambda x: len(sent_tokenize(x)))
           text_col = clean_data(text_col)

           # Find the length of each text
           data['char_count'] = text_col.str.len()
           # Count the number of words in each text
           data['word_count'] = text_col.str.split().str.len()
           # Find the average length of word
           data['average_word_length'] = data['char_count'] / data['word_count']
           data['full_text_cleaned'] = text_col
           data = data.drop(data.columns[[1]], axis=1)
           return data

       data = transform_data(data, data['full_text'])
       st.write(data.head())
       st.write(data.shape)

       # @st.cache_data
       # def convert_data(data):
       #     return data.to_csv(index=False).encode('utf-8')

       # data_csv = convert_data(data)

       # # with open("data_tranformed.csv") as f:
       # #     st.download_button(label="Download Full CSV", data=f, mime='text/csv')

       # st.download_button("Download Full CSV", data_csv,
       #                    "file.csv",
       #                    "text/csv",
       #                    key='download-csv')

except:
   st.write("Please load a file to continue...")









