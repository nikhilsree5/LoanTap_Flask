
import pandas as pd
import numpy as np
import json
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from flask import Flask,request

def preprocessing():
    df=pd.read_csv('C:\\Users\\Aswathi Valsan\\Loantap\\LoanTap_Flask\\loanTap.csv')
    df['term']=df['term'].apply(lambda x:36 if x=='36 months' else 60)
    df['loan_status'] = df['loan_status'].apply(lambda x: 1 if x == 'Fully Paid' else 0)
    return df

def model_build(df):
    X = df.drop(columns=['loan_status'])
    y = df['loan_status']
    logreg = LogisticRegression()
    logreg.fit(X,y)
    return logreg

def prediction(model,x):
    y=model.predict(x)
    return y

app = Flask(__name__)
@app.route('/')
def Title():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Loan Tap Predictor</title>
      <style>
        body {
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          background-color: #f0f8ff;
          margin: 40px;
          color: #333;
        }
        h1 {
          color: #0066cc;
          background-color: #e6f2ff;
          padding: 15px;
          border-radius: 8px;
          text-align: center;
          box-shadow: 0 0 8px rgba(0,0,0,0.1);
        }
        .content {
          background-color: #ffffff;
          padding: 20px;
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }
        .highlight {
          color: #cc3300;
          font-weight: bold;
        }
        ul {
          margin-top: 10px;
          padding-left: 20px;
        }
        ul li {
          margin-bottom: 8px;
          color: #007777;
        }
      </style>
    </head>
    <body>

      <h1>🚀 LOAN TAP PREDICTOR</h1>

      <div class="content">
        <p><span class="highlight">LoanTap</span> is an online platform committed to delivering customized loan products to millennials. They innovate in an otherwise dull loan segment, aiming to deliver <strong>instant, flexible loans</strong> on consumer-friendly terms to salaried professionals and businessmen.</p>

        <p>The data science team at LoanTap is building an <em>underwriting layer</em> to determine the creditworthiness of <strong>MSMEs</strong> as well as individuals.</p>

        <p>LoanTap deploys formal credit to salaried individuals and businesses through <strong>four main financial instruments:</strong></p>
        <ul>
          <li>💳 Personal Loan</li>
          <li>🔁 EMI Free Loan</li>
          <li>💼 Personal Overdraft</li>
          <li>⏩ Advance Salary Loan</li>
        </ul>

        <p><span class="highlight">This case study</span> will focus on the underwriting process behind <strong>Personal Loan</strong> only.</p>
      </div>

    </body>
    </html>
    '''
    return html_content

@app.route('/predict',methods =['POST'])
def loantap():
    # loan_req = json.loads(request.data)
    loan_req=request.get_json()
    print(loan_req)
    params = np.array(list(loan_req.values())).reshape(1,-1)
    df=preprocessing()
    model=model_build(df)
    y=np.round(prediction(model,params))
    if(y[0]):
        return "Loan Sanctioned"
    else:
        return "Loan Declined"


# if __name__ == '__main__':
#     app.run(debug=True)

