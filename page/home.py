import streamlit as st

def show():
    st.title("Sentiment Analysis Application")
    st.write("Author: Martinus Juan Prasetyo")
    
    st.subheader("Penjelasan Aplikasi")
    st.write("""
        Aplikasi ini dirancang untuk memprediksi sentimen dari komentar yang diinputkan pengguna menggunakan beberapa model yang telah dilatih pada dataset berbeda. 
        Pengguna dapat memasukkan teks komentar, dan aplikasi akan memproses teks tersebut untuk menentukan sentimennya berdasarkan model-model tersebut.
        
        Cara Kerja Aplikasi:
        1. **Input Komentar**: Pengguna memasukkan teks komentar ke dalam aplikasi.
        2. **Prediksi Sentimen**: Teks yang sudah diproses kemudian dianalisis menggunakan beberapa model SVM yang sudah dilatih sebelumnya pada dataset yang berbeda (BCA, BRI, Mandiri, dan Combined) untuk memprediksi sentimen.
        3. **Output Sentimen**: Hasil prediksi dari masing-masing model (positif, negatif) ditampilkan kepada pengguna.
    """)

    st.subheader("Analisis Sentimen")
    st.write("""
        Analisis sentimen adalah proses menggunakan pemrosesan bahasa alami (NLP), analisis teks, dan linguistik komputasional 
        untuk mengidentifikasi dan mengklasifikasikan opini yang dinyatakan dalam teks. Ini sering digunakan dalam berbagai 
        aplikasi seperti layanan pelanggan, analisis media sosial, dan analisis umpan balik produk.
    """)

    st.subheader("Algoritma yang Digunakan: SVM")
    st.write("""
        Support Vector Machine (SVM) adalah salah satu algoritma pembelajaran mesin yang paling populer dan kuat yang digunakan untuk klasifikasi dan regresi. 
        Dalam konteks analisis sentimen, SVM digunakan untuk mengklasifikasikan teks ke dalam kategori sentimen positif, negatif, atau netral. 
        Algoritma SVM bekerja dengan mencari hyperplane optimal yang memisahkan kelas-kelas dalam ruang fitur yang memiliki margin terbesar.
        
        Kelebihan SVM:
        - **Efektif dalam ruang berdimensi tinggi**: SVM sangat efektif dalam menangani data dengan banyak fitur.
        - **Hemat memori**: Hanya sebagian dari poin data yang digunakan dalam menentukan hyperplane (vektor pendukung).
        - **Fleksibilitas**: Dapat menggunakan kernel trick untuk menangani data yang tidak linear.

        Kelemahan SVM:
        - **Kinerja lambat pada dataset besar**: Pada dataset yang sangat besar, SVM bisa menjadi lambat.
        - **Pemilihan kernel**: Memilih kernel yang tepat bisa menjadi kompleks dan memerlukan penyesuaian yang tepat untuk mendapatkan hasil terbaik.
    """)

    st.subheader("Daftar Dataset yang Digunakan")
    st.write("""
        Berikut adalah daftar dataset yang digunakan dalam analisis sentimen ini:
        - **BCA Mobile** [Link download](https://data.mendeley.com/datasets/mvshyj7g67/1)
        - **BRI Mobile** [Link download](https://data.mendeley.com/datasets/8cnzj9h72v/1)
        - **Livin Mandiri** [Link download](https://data.mendeley.com/datasets/h8p5v6r6dn/1)
    """)
