import pickle
import streamlit as st
import pandas as pd

# Load model
with open("model.pkl", "rb") as file:
    model_load = pickle.load(file)

from sklearn.preprocessing import MinMaxScaler
minmaxscaler_load = MinMaxScaler()

# Daftar kolom fitur sesuai model
kolom_data = ['Marital_status', 'Displaced', 'Debtor', 'Tuition_fees_up_to_date',
              'Gender', 'Scholarship_holder', 'Age_at_enrollment',
              'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
              'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
              'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
              'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade']

# Konversi input ke numerik
def yesno_convert(option):
    return int(option == 'Yes')

def gender_convert(option):
    return int(option == 'Man')

def marital_convert(option):
    mapping = {
        'Single': 1,
        'Married': 2,
        'Widower': 3,
        'Divorced': 4,
        'Facto Union': 5,
        'Legally Separated': 6
    }
    return mapping.get(option, 0)

# Sidebar Input
with st.sidebar:
    st.header('Predict Machine 🎯', divider='rainbow')

    Gender = gender_convert(st.radio('Gender', ['Man', 'Woman'], horizontal=True))
    Marital_status = marital_convert(st.selectbox('Marital Status', 
                                                  ['Single', 'Married', 'Widower', 'Divorced', 'Facto Union', 'Legally Separated']))
    Age_at_enrollment = st.slider('Age at Enrollment', 10, 100)

    Debtor = yesno_convert(st.radio('Debtor', ['Yes', 'No'], horizontal=True))
    Tuition_fees_up_to_date = yesno_convert(st.radio('Tuition Fees Up to Date', ['Yes', 'No'], horizontal=True))
    Scholarship_holder = yesno_convert(st.radio('Scholarship Holder', ['Yes', 'No'], horizontal=True))
    Displaced = yesno_convert(st.radio('Displaced', ['Yes', 'No'], horizontal=True))

    col1, col2 = st.columns(2)
    with col1:
        Curricular_units_1st_sem_credited = st.number_input('1st Sem Credited', 0.0)
        Curricular_units_1st_sem_enrolled = st.number_input('1st Sem Enrolled', 0.0)
        Curricular_units_1st_sem_approved = st.number_input('1st Sem Approved', 0.0)
        Curricular_units_1st_sem_grade = st.number_input('1st Sem Grade', 0.0)
    with col2:
        Curricular_units_2nd_sem_credited = st.number_input('2nd Sem Credited', 0.0)
        Curricular_units_2nd_sem_enrolled = st.number_input('2nd Sem Enrolled', 0.0)
        Curricular_units_2nd_sem_approved = st.number_input('2nd Sem Approved', 0.0)
        Curricular_units_2nd_sem_grade = st.number_input('2nd Sem Grade', 0.0)

    # Buat DataFrame input
    input_data = pd.DataFrame([[Marital_status, Displaced, Debtor, Tuition_fees_up_to_date,
                                 Gender, Scholarship_holder, Age_at_enrollment,
                                 Curricular_units_1st_sem_credited, Curricular_units_1st_sem_enrolled,
                                 Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade,
                                 Curricular_units_2nd_sem_credited, Curricular_units_2nd_sem_enrolled,
                                 Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade]],
                               columns=kolom_data)

    if st.button('Predict'):
        try:
            result = model_load.predict(input_data)
            if result[0] == 0:
                st.success('✅ Siswa diprediksi **TIDAK** dropout.')
                st.balloons()
            else:
                st.error('⚠️ Siswa diprediksi **DROPOUT**.')
        except Exception as e:
            st.error(f"⚠️ Terjadi kesalahan saat prediksi: {e}")

# Tampilan Utama
st.title('🎓 Jaya Jaya Institut Dashboard')
st.subheader('Apa itu Jaya Jaya Institut?', divider='grey')
st.markdown('''**Jaya Jaya Institut** adalah sebuah lembaga pendidikan tinggi berbasis teknologi yang berkomitmen untuk mencetak lulusan berkualitas, adaptif, dan siap menghadapi tantangan global. 
            Dengan pendekatan pendidikan modern dan berbasis data, kami terus berinovasi untuk meningkatkan kualitas akademik dan pengalaman belajar mahasiswa.''')

st.subheader('Apa fungsi Predict Machine di samping?', divider='grey')
st.markdown('''**Predict Machine** merupakan fitur cerdas yang dikembangkan untuk memprediksi potensi siswa mengalami dropout (berhenti studi). Alat ini menggunakan model Machine Learning yang dilatih dari data historis mahasiswa untuk membantu pihak institusi dalam:

- Mengidentifikasi siswa yang berisiko tinggi mengalami dropout.
- Mengambil keputusan preventif dan intervensi tepat waktu.
- Meningkatkan retensi dan keberhasilan studi mahasiswa.''')

st.subheader('Bagaimana cara menggunakan Predict Machine?', divider='grey')
st.markdown('''Untuk menggunakan Predict Machine:

1. Klik ikon **panah (>)** di pojok kiri atas layar untuk membuka panel input.
2. Isi informasi siswa sesuai kondisi aktual, seperti status pernikahan, usia, status beasiswa, dan data akademik.
3. Klik tombol **Predict** untuk melihat hasil prediksi.
4. Sistem akan menampilkan apakah siswa tersebut diprediksi **dropout** atau **tetap melanjutkan studi**.

Fitur ini dirancang untuk menjadi alat bantu pengambilan keputusan berbasis data yang akurat dan mudah digunakan.''')
