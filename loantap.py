
import pandas as pd
import numpy as np
import json
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from flask import Flask,request

def preprocessing():
    df=pd.read_csv('loantap.csv')
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
# @app.route('/')
# def Title():
#     html_content = '''
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#       <meta charset="UTF-8">
#       <title>Loan Tap Predictor</title>
#       <style>
#         body {
#           font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#           background-color: #f0f8ff;
#           margin: 40px;
#           color: #333;
#         }
#         h1 {
#           color: #0066cc;
#           background-color: #e6f2ff;
#           padding: 15px;
#           border-radius: 8px;
#           text-align: center;
#           box-shadow: 0 0 8px rgba(0,0,0,0.1);
#         }
#         .content {
#           background-color: #ffffff;
#           padding: 20px;
#           border-radius: 10px;
#           box-shadow: 0 0 10px rgba(0,0,0,0.2);
#         }
#         .highlight {
#           color: #cc3300;
#           font-weight: bold;
#         }
#         ul {
#           margin-top: 10px;
#           padding-left: 20px;
#         }
#         ul li {
#           margin-bottom: 8px;
#           color: #007777;
#         }
#       </style>
#     </head>
#     <body>
#
#       <h1>🚀 LOAN TAP </h1>
#
#       <div class="content">
#         <p><span class="highlight">LoanTap</span> is an online platform committed to delivering customized loan products to millennials. They innovate in an otherwise dull loan segment, aiming to deliver <strong>instant, flexible loans</strong> on consumer-friendly terms to salaried professionals and businessmen.</p>
#
#         <p>The data science team at LoanTap is building an <em>underwriting layer</em> to determine the creditworthiness of <strong>MSMEs</strong> as well as individuals.</p>
#
#         <p>LoanTap deploys formal credit to salaried individuals and businesses through <strong>four main financial instruments:</strong></p>
#         <ul>
#           <li>💳 Personal Loan</li>
#           <li>🔁 EMI Free Loan</li>
#           <li>💼 Personal Overdraft</li>
#           <li>⏩ Advance Salary Loan</li>
#         </ul>
#
#         <p><span class="highlight">This case study</span> will focus on the underwriting process behind <strong>Personal Loan</strong> only.</p>
#       </div>
#
#     </body>
#     </html>
#     '''
#     return html_content

@app.route('/')
def home():
     render_template_string='''
        <html>
        <head>
            <title>LoanTap Predictor</title>
            <style>
                body { font-family: Arial; background-color: #f9f9f9; padding: 40px; }
                form { background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px #ccc; max-width: 400px; margin: auto; }
                h1 {color: #0066cc;background-color: #e6f2ff;padding: 15px;border-radius: 8px;text-align: center;box-shadow: 0 0 8px rgba(0,0,0,0.1);}
                h2 { text-align: center; color: #0066cc; }
                input[type=number] { width: 100%; padding: 8px; margin: 10px 0; border-radius: 4px; border: 1px solid #ccc; }
                input[type=submit] { background-color: #28a745; color: white; padding: 10px; border: none; width: 100%; border-radius: 4px; cursor: pointer; }
                .content { background-color: #ffffff; padding: 20px;border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.2);}
                .column {flex: 1;  padding: 15px; background-color: #f0f8ff;border: 1px solid #ccc;border-radius: 8px; }
                .container {display: flex;padding: 20px; gap: 20px;}
            </style>
        </head>
        <body>
        <div class="container">
            <div class="column">
                <h1>🚀 LOAN TAP </h1>
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
            <div class="column">

            <form action="/predict" method="POST">
                <h2>LoanTap Predictor</h2>
                <input type="number" name="loan_amt" placeholder="Loan Amount" required>
                <input type="number" name="term" placeholder="Term (months)" required>
                <input type="number" name="int_rate" placeholder="Interest Rate (%)" required>
                <input type="number" name="installment" placeholder="Installment Amount" required>
                <input type="number" name="income" placeholder="Monthly Income" required>
                <input type="submit" value="Predict">
            </form>
            </div>
        </div>
        </body>
        </html>
    '''
     return render_template_string


@app.route('/predict',methods =['POST'])
def loantap():
    # loan_req = json.loads(request.data)
    # loan_req=request.get_json()
    loan_req = request.form.to_dict()
    print(loan_req)
    a=list(loan_req.values())
    b = list(map(int, a))
    params = np.array(b).reshape(1,-1)
    df=preprocessing()
    model=model_build(df)
    y=np.round(prediction(model,params))
    result = "Loan Approved" if y[0] else "Loan Declined"
    return f"<h2 style='text-align:center; color:#333;'>{result}</h2>"

# if __name__ == '__main__':
#     app.run(debug=True)

