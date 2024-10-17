import pickle
import streamlit as st

# Load the model
pickle_in = open("rf_model.pkl", "rb")
classifier = pickle.load(pickle_in)

# Prediction function
def predict_risk(age, systolicbp, diastolicbp, bs, bodytemp):
    prediction = classifier.predict([[age, systolicbp, diastolicbp, bs, bodytemp]])
    return prediction

# Main function for the app
def main():
    st.title("Maternal Health Risk Prediction")

    # Input fields for user to enter data
    age = st.text_input("Age")
    systolicbp = st.text_input("SystolicBP")
    diastolicbp = st.text_input("DiastolicBP")
    bs = st.text_input("BS")
    bodytemp = st.text_input("BodyTemp")
    
    result = ""
    
    # When the Predict button is clicked
    if st.button("Predict"):
        result = predict_risk(age, systolicbp, diastolicbp, bs, bodytemp)
        
        if result == [2.0]:
            result = "High"
        elif result == [1.0]:
            result = "Mid"
        elif result == [0.0]:
            result = "Low"
        
        # st.success(f'The risk level is {result}')
        st.markdown(f"<h2 style='color: black;'>Predicted Risk Level: {result}</h2>", unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
