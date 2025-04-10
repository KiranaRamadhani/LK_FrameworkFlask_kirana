# Import Flask dan fungsi render_template untuk menampilkan file HTML
from flask import Flask, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Route utama (homepage) - hanya menampilkan teks biasa
@app.route("/")
def home():
    return "Hello, Flask!"

# Route halaman 'about' - menampilkan template about.html
@app.route("/about")
def about():
    return render_template('about.html')

# Route dengan parameter dinamis 'name' - menampilkan template profile.html dengan nama user
@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', username=name)

# Route untuk menampilkan data dictionary user ke dalam template data.html
@app.route('/data')
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('data.html', user=user)

# Route untuk menampilkan daftar user dengan peran/role ke dalam template users.html
@app.route('/users')
def users():
    user_list = [
        {"name": "Ali", "role": "admin"},
        {"name": "Budi", "role": "user"},
        {"name": "Citra", "role": "admin"},
        {"name": "Dewi", "role": "user"},
    ]
    return render_template('users.html', users=user_list)

# Route untuk menampilkan daftar user (string saja) menggunakan perulangan 'for' di template
@app.route('/users/for_statement')
def for_statement():
    user_list = ["Ali", "Budi", "Citra", "Dewi"]
    return render_template('users_for.html', users=user_list)

# Route untuk menampilkan data user dengan kondisi 'if' di template (misalnya cek role)
@app.route('/users/if_statement')
def if_statement():
    users = [
        {"name": "Ali", "role": "admin"},
        {"name": "Budi", "role": "user"},
        {"name": "Citra", "role": "admin"},
        {"name": "Dewi", "role": "user"},
    ]
    return render_template('users_if.html', users=users)

# Route untuk menampilkan daftar user dengan menampilkan indeks/urutan menggunakan loop.index
@app.route('/users/loop_index')
def loop_index():
    users = ["Ali", "Budi", "Citra", "Dewi"]
    return render_template('users_index.html', users=users)

# Route dengan parameter angka 'score' - digunakan untuk menampilkan nilai dan bisa diberi kondisi (misalnya A/B/C/D)
@app.route('/nilai/<int:score>')
def nilai(score):
    return render_template('nilai.html', score=score)

# Route untuk menampilkan daftar mahasiswa dan nilai mereka ke dalam template mahasiswa.html
@app.route('/mahasiswa')
def mahasiswa():
    daftar_mahasiswa = [
        {"nama": "Ali", "nilai": 92},
        {"nama": "Budi", "nilai": 80},
        {"nama": "Citra", "nilai": 65},
        {"nama": "Dewi", "nilai": 55},
    ]
    return render_template('mahasiswa.html', mahasiswa=daftar_mahasiswa)

# Menjalankan aplikasi Flask dalam mode debug (otomatis reload jika ada perubahan)
if __name__ == '__main__':
    app.run(debug=True)
