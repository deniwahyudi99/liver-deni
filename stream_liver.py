import pickle
import streamlit as st

# membaca model
liver_model = pickle.load(open('indian_liver_patient_model.sav', 'rb'))

# Judul Web
st.title('Data Mining Prediksi liver')

age = st.text_input('Masukan usia')

gender = st.text_input('Masukan jenis kelamin')

tbn = st.text_input('Masukan Total senyawa kimia')

dbn = st.text_input('Masukan senyawa yang ada')

aph = st.text_input('Masukan Enzim')

aam = st.text_input('Masukan jumlah enzim dalam darah')

asm = st.text_input('Masukan enzim transaminase')

tps = st.text_input('Masukan jumlah protein')

agm = st.text_input('Masukan protein plasma darah')

ags = st.text_input('Masukan kadar protein yang tersisa dalam darah')

# code untuk kelompok jenis
liver_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    ane_prediction = liver_model.predict([[age, gender, tbn, dbn, aph, aam, asm, tps, agm, ags]])
    
    if(ane_prediction[0] == 1):
        liver_diagnosis = 'Pasien liver'
    else :
        liver_diagnosis = 'Pasien tidak liver'

    st.success(liver_diagnosis)
