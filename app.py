from flask import Flask, render_template, request
import perceptron

# Inisiasi Library Flask untuk tampilan Web
app = Flask(__name__)

# Inisiasi Feature
features = ['age', 
            'menopauseStatus', 
            'tumorSize',
            'axillaryLymphNode', 
            'nodeCapsPenetration', 
            'malignancy',
            'breastSide', 
            'breastQuad',
            'irradiation']

# Halaman Awal
@app.route("/")
def index():
    # Menampilkan Opsi pada halaman awal sebanyak jumlah pertanyaan, yaitu 9
    option = [0] * 9
    # Menampilkan halaman awal
    return render_template(
        "index.html", template="Flask",
        option = option,
        data = "Hasil prediksi akan muncul disini !"
    )

# Dieksekusi jika form sudah disubmit
@app.route("/result", methods=['POST'])
def form_value():
    # Looping untuk mendapat jawaban setiap baris dari pengguna
    option = [float(request.form.get(feature)) for feature in features]
    
    # Prediksi dengan function Perceptron yang sudah dibuat pada 'perceptron.py'
    predict = perceptron.predict(option)
    
    # Menampilkan Nilai (hasil prediksi) dari fungsi Perceptron ke Web/Pengguna
    return render_template(
        "index.html", template="Flask",
        option = option,
        data = predict
    )

# Dieksekusi jika dijalankan : 'flask run'
if __name__ == '__main__':
    app.run(port=5000, debug=True)
