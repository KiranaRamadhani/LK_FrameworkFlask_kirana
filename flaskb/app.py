# Import Flask dan modul pendukung: render_template untuk menampilkan HTML, request untuk menangani form
from flask import Flask, render_template, request

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Route untuk halaman utama, menerima metode GET dan POST
@app.route("/", methods=["GET", "POST"])
def index():
    # Jika user mengirim form (POST)
    if request.method == "POST":
        # Mengambil input dari form (konversi ke float karena akan dihitung sebagai angka)
        principal = float(request.form["principal"])  # Modal awal
        rate = float(request.form["rate"])            # Suku bunga (% per tahun)
        time = float(request.form["time"])            # Lama waktu (dalam tahun)

        # Menghitung bunga sederhana (Simple Interest)
        interest = (principal * rate * time) / 100

        # Menghitung total tabungan setelah bunga
        total_amount = principal + interest

        # Menampilkan hasil pada template 'result.html' dengan data total dan bunga
        return render_template("result.html", total=total_amount, interest=interest)

    # Jika metode GET, tampilkan form input di 'index.html'
    return render_template("index.html")

# Menjalankan aplikasi jika file ini dijalankan langsung
if __name__ == "__main__":
    app.run(debug=True)
