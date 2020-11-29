def predict(data):
    # Inisiasi Nilai Weight dari file .ipynb
    weight = [  0.46855066420800107, 
                0.33255066420800095, 
                0.21255066420800084, 
                -0.09144933579199932, 
                0.22055066420800085, 
                0.404550664208001, 
                -0.0754493357919993, 
                0.14855066420800078, 
                0.06855066420800071, 
                0.44455066420800105, 
                0.14055066420800078, 
                0.22855066420800085, 
                0.2605506642080009, 
                0.2765506642080009, 
                0.34055066420800095, 
                0.412550664208001, 
                0.364550664208001, 
                0.46855066420800107, 
                0.4845506642080011, 
                0.46855066420800107, 
                -0.09944933579199933, 
                0.46855066420800107, 
                0.21255066420800084, 
                0.46855066420800107, 
                0.2845506642080009, 
                0.1725506642080008, 
                0.5085506642080011, 
                -0.16344933579199938, 
                -0.16344933579199938, 
                0.02855066420800071, 
                0.34055066420800095, 
                -0.22744933579199944, 
                -0.23544933579199945, 
                -0.09144933579199932, 
                0.42855066420800103, 
                0.1645506642080008, 
                0.01255066420800071, 
                0.22855066420800085, 
                0.24455066420800087, 
                -0.1874493357919994, 
                -0.13944933579199936 
            ]
    #weight = [ 0.36206383542652043, 0.08206383542652018, 0.0980638354265202, 0.08206383542652018, 0.14606383542652024, 0.29006383542652037, -0.10193616457347987, 0.1060638354265202, -0.02993616457347984]
    
    # Inisiasi Nilai Bias dari file .ipynb
    bias = -0.264000000000001
    #bias = -0.11200000000000088
    
    # Deklarasi Nilai Prediksi
    predict = ""

    # Inisiasi variabel yang menyimpan hasil perkalian Weight dan Nilai Value
    multiply = 0

    # Menghitung Nilai setiap baris dengan looping 
    for i, value in enumerate(data):
        # Menjumlahkan hasil perkalian setiap feature
        multiply += weight[i] * value
    
    # Menjumlahkan hasil perkalian dengann Nilai Bias
    Y_in = bias + multiply

    if (Y_in >= 0) :
        # Jika positif, maka berisiko terkena Kanker Payudara
        predict = "Maaf, anda berisiko tinggi kanker payudara!"
    else :
        # Jika negatif, maka berisiko rendah Kanker Payudara
        predict = "Selamat, anda berisiko rendah :)"
    return predict # Mengembalikan Nilai agar ditampilkan pada Web (CLient-Side)
