import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

st.title("Loan Prediction App")
st.write('''
Let's consider what condition can match yours!
''')

train = pd.read_csv(https://raw.githubusercontent.com/cedarkl/StreamlitApps/main/LoanPredictionApp/train.csv)
train_sub = train[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                   'Loan_Amount_Term', 'Credit_History']]
train_sub = train_sub.dropna()

min_max_scaler = MinMaxScaler()
train_sub_mmscaled = min_max_scaler.fit_transform(train_sub)
df_train_sub_mmscaled = pd.DataFrame(train_sub_mmscaled, columns=['ApplicantIncome',
                                                                  'CoapplicantIncome',
                                                                  'LoanAmount',
                                                                  'Loan_Amount_Term',
                                                                  'Credit_History'])

y = df_train_sub_mmscaled.Credit_History
X = df_train_sub_mmscaled.drop(['Credit_History'], axis=1)

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.3, random_state=1)

clf = LogisticRegression()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_valid)

acc = accuracy_score(y_valid, y_pred)*100
st.write(f'Accuracy: {round(acc,1)} %')

st.write('Put your info. please!')
try:
    income = int(st.text_input('Your income per month:'))
    coincome = float(st.text_input('Your spouse income per month:'))
    loanamount = float(st.text_input('How much would you like to loan?'))
    loanterm = float(st.text_input('Which term (months) would you like to tend?'))

    X_input = [[income, coincome, loanamount, loanterm]]
    X_input_scaled = min_max_scaler.fit_transform(X_input)

    diagnosis = ''
    if st.button("Your Test Result"):
        prediction = clf.predict(X_input_scaled)
        if prediction[0] == 0:
            diagnosis = 'Disapproval!'
        else:
            diagnosis = 'Approval.'
    st.success(diagnosis)

except:
    st.write("Please enter to continue...")









