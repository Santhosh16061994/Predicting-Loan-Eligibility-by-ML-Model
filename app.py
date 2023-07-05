import streamlit as st
import pickle

# Function to set custom CSS styles
def set_custom_style():
    # Add custom CSS styles to change the appearance of the app
    st.markdown(
        """
        <style>
        /* Add your custom styles here */
        body {
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 600px;
            padding: 20px;
            margin: 0 auto;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .btn-predict {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
        .btn-predict:hover {
            background-color: #0056b3;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    # Set custom styles
    set_custom_style()

    # Header section
    st.markdown("<h1>Streamlit Loan Eligibility Prediction App</h1>", unsafe_allow_html=True)

    # Input fields
    st.markdown("### Personal Information")
    col1, col2 = st.columns(2)
    gender = col1.selectbox('Gender', ('Male', 'Female'))
    married = col2.selectbox('Married', ('Yes', 'No'))
    dependents = col1.selectbox('Dependents', ('None', 'One', 'Two', 'Three'))
    education = col2.selectbox('Education', ('Graduate', 'Not Graduate'))
    self_employed = col1.selectbox('Self-Employed', ('Yes', 'No'))

    st.markdown("### Financial Information")
    col3, col4 = st.columns(2)
    applicant_income = col3.number_input('Applicant Income')
    coapplicant_income = col4.number_input('Coapplicant Income')
    loan_amount = col3.number_input('Loan Amount')
    loan_amount_term = col4.number_input('Loan Tenure (in months)')

    st.markdown("### Additional Information")
    credit_history = st.number_input('Credit History', 0.0, 1.0)
    property_area = st.selectbox('Property Area', ('Semiurban', 'Urban', 'Rural'))

    # Predict button
    if st.button('Predict', key='predict_button'):
        # Make prediction
        result = predict(
            gender, married, dependents, education, self_employed,
            applicant_income, coapplicant_income, loan_amount,
            loan_amount_term, credit_history, property_area
        )

        # Display prediction result
        st.success(f'You are {result} for the loan')

# Load the trained model
with open('train_model.pkl', 'rb') as pkl:
    train_model = pickle.load(pkl)

# Function to preprocess user input and make predictions
def predict(gender, married, dependent, education, self_employed, applicant_income,
           coapplicant_income, loan_amount, loan_amount_term, credit_history, propertyI apologize for the confusion. It seems there was a mistake in the code provided. The correct method to create multiple columns in Streamlit is `st.columns()` instead of `st.beta_columns()`. Here's the corrected version of the code:

```python
import streamlit as st
import pickle

def main():
    bg = """<div style='background-color:black; padding:13px'>
              <h1 style='color:white'>Streamlit Loan Eligibility Prediction App</h1>
           </div>"""
    st.markdown(bg, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    gender = col1.selectbox('Gender', ('Male', 'Female'))
    married = col2.selectbox('Married', ('Yes', 'No'))
    dependents = col1.selectbox('Dependents', ('None', 'One', 'Two', 'Three'))
    education = col2.selectbox('Education', ('Graduate', 'Not Graduate'))

    col3, col4 = st.columns(2)
    self_employed = col3.selectbox('Self-Employed', ('Yes', 'No'))
    applicant_income = col4.number_input('Applicant Income')

    col5, col6 = st.columns(2)
    coapplicant_income = col5.number_input('Coapplicant Income')
    loan_amount = col6.number_input('Loan Amount')

    col7, col8 = st.columns(2)
    loan_amount_term = col7.number_input('Loan Tenure (in months)')
    credit_history = col8.number_input('Credit History', 0.0, 1.0)

    property_area = st.selectbox('Property Area', ('Semiurban', 'Urban', 'Rural'))
    button = st.button('Predict')

    if button:
        result = predict(gender, married, dependents, education, self_employed, applicant_income,
                        coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area)
        st.success(f'You are {result} for the loan')

def predict(gender, married, dependent, education, self_employed, applicant_income,
           coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area):
    gen = 0 if gender == 'Male' else 1
    mar = 0 if married == 'Yes' else 1
    dep = float(0 if dependent == 'None' else 1 if dependent == 'One' else 2 if dependent == 'Two' else 3)
    edu = 0 if education == 'Graduate' else 1
    sem = 0 if self_employed == 'Yes' else 1
    pro = 0 if property_area == 'Semiurban' else 1 if property_area == 'Urban' else 2
    Lam = loan_amount / 1000
    cap = coapplicant_income / 1000

    prediction = train_model.predict([[gen, mar, dep, edu, sem, applicant_income, cap,
                                      Lam, loan_amount_term, credit_history, pro]])
    verdict = 'Not Eligible' if prediction == 0 else 'Eligible'
    return verdict

if __name__ == '__main__':
    main()
