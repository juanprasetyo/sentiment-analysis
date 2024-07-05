import streamlit as st
import joblib
import numpy as np

# Fungsi untuk memuat model dan vectorizer
def load_model_and_vectorizer(dataset):
    model = joblib.load(f'{model_path}/{dataset}_model.pkl')
    vectorizer = joblib.load(f'{model_path}/{dataset}_vectorizer.pkl')
    return model, vectorizer

# Fungsi untuk memprediksi sentimen
def predict_sentiment(input_data, datasets):
    predictions = {}
    for dataset in datasets:
        model, vectorizer = load_model_and_vectorizer(dataset)

        # Transformasi input data menggunakan vectorizer
        input_vectorized = vectorizer.transform([input_data])

        # Lakukan prediksi menggunakan model
        prediction = model.predict(input_vectorized)

        if prediction[0] == 0:
            predictions[dataset] = "Negatif"
        else:
            predictions[dataset] = "Positif"
    return predictions

# Daftar dataset
datasets = [
    'BCA',
    'BRI',
    'Mandiri',
    'Combined'
]

# Path ke direktori model
model_path = 'models'

def show():
    st.title("Sentiment Analysis Prediction")

    # Input komentar dari pengguna
    input_data = st.text_area("Masukkan komentar Anda:")

    # Tombol untuk memprediksi
    if st.button("Prediksi Sentimen"):
        if input_data:
            predictions = predict_sentiment(input_data, datasets)

            # Tampilkan hasil prediksi
            st.write("Hasil Prediksi:")
            for dataset in datasets:
                st.write(f"Prediksi dari model {dataset}: {predictions[dataset]}")
        else:
            st.write("Silakan masukkan komentar terlebih dahulu.")
