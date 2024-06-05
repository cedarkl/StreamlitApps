import streamlit as st
import pandas as pd
# ßfrom io import StringIO
import string
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize


st.title("Text Process App")
st.write('''
Let's transform your text data to clean-and-clear for training!
''')

#uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
    # # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)
    #
    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)
    #
    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
st.subheader("Raw data")

data = pd.read_csv('/Users/kaylakim/Documents/cedarkl-Projects/learning-agency-lab-automated-essay-scoring-2/train.csv')
st.write(data.head())
st.write(data.shape)

st.subheader("Transform data")

def transform_data(data, col): # text column of the data
    # Count the sentences of each text
    data['sent_count'] = col.map(lambda x: len(sent_tokenize(x)))
    col = col.map(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
    col = col.map(lambda x: x.replace('\n', ' '))
    col = col.map(lambda x: x.lower())

    # Find the length of each text
    data['char_count'] = col.str.len()
    # Count the number of words in each text
    data['word_count'] = col.str.split().str.len()
    # Find the average length of word
    data['average_word_length'] = data['char_count'] / data['word_count']
    return data

data = transform_data(data, data['full_text'])
st.write(data.head())
st.write(data.shape)

st.subheader("Download data")
#data.to_csv("data_tranformed.csv", index=False)

#st.download_button('Download CSV', data)

# Different ways to use the API

# st.download_button('Download CSV', text_contents, 'text/csv')
# st.download_button('Download CSV', text_contents)  # Defaults to 'text/plain'

# with open('data_tranformed.csv') as f:
#     data = pd.read_csv(f)

#     st.write(data)
#     st.download_button('Download CSV', st.write(data))  # Defaults to 'text/plain'
# #    st.write('Thanks for downloading!')

# ---
# Binary files

# binary_contents = b'whatever'
#
# # Different ways to use the API
#
# st.download_button('Download file', binary_contents)  # Defaults to 'application/octet-stream'
#
# with open('myfile.zip', 'rb') as f:
#    st.download_button('Download Zip', f, file_name='archive.zip')  # Defaults to 'application/octet-stream'
#
# # You can also grab the return value of the button,
# # just like with any other button.
#
# if st.download_button(...):
#    st.write('Thanks for downloading!')







