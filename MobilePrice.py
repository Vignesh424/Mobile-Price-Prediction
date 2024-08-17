import streamlit as st
import pickle

model = pickle.load(open('mobile.pkl', 'rb'), encoding='latin1')

def run():
    st.title("Mobile Prediction using Machine Learning")


     ## Ratings
    ratings = st.number_input('Enter Ratings')

    ## RAM
    ram = st.number_input('Enter RAM')

    ## ROM
    rom = st.number_input('Enter ROM')
    
    ## Mobile_Size
    mob_size = st.number_input('Enter Mobile Size', value=0)

    ## Number of pixels of the Back camera
    backcam = st.number_input("Enter Pixels in Back Camera",value=0)

    ## Number of pixels of the Selfi camera
    selficam = st.number_input("Enter Pixels in Selfi Camera",value=0)

    ## Battery
    battery= st.number_input("Enter Battery",value=0)




    if st.button("Submit"):
        features = [[ratings,ram,rom,mob_size,backcam,selficam,battery]]
        print(features)
        prediction = model.predict(features)
        weight = [str(i) for i in prediction]
        ans = ', '.join(weight)
        if ans == 0:
            st.error("Error in the Inputs: Please Try Again")

        else:
            st.success("The predicted Price of the Phone is:"+" "+ans)
            

run()
