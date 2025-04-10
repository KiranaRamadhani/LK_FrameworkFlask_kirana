# 🚀 Getting Started Flask Py

**Flask** adalah framework Python yang ringan dan sederhana untuk membuat web application. Cocok banget buat pemula maupun yang udah berpengalaman.

---

## 1. Instalasi Flask

Sebelum mulai, pastikan Python sudah terinstal. Lalu, install Flask via pip:

```bash
pip install flask
```

---

## 2. Struktur Folder Project

```
project/
│
├── static/
│   └── style.css
├── templates/
│   ├── about.html
│   ├── data.html
│   ├── mahasiswa.html
│   ├── nilai.html
│   ├── profile.html
│   ├── users.html
│
├── app.py
└── requirements.txt
```

---

## 3. Membuat Aplikasi Flask

File utama: `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 4. HTML Template dengan `render_template`

### 4.1 `about.html`

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>About</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Ini Halaman About</h1>
    <p>Selamat datang di halaman About!</p>
</body>
</html>
```

### 4.2 Route Flask

```python
@app.route("/about")
def about():
    return render_template('about.html')
```

---

## 5. Menambahkan CSS

### 5.1 File `static/style.css`

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    text-align: center;
    padding: 50px;
}

h1 {
    color: #333;
}

p {
    font-size: 18px;
    color: #666;
}
```

---

## 6. Routing Dinamis

### 6.1 Mengirim Parameter ke URL

```python
@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', username=name)
```

### 6.2 Template `profile.html`

```html
<h1>Selamat datang, {{ username }}!</h1>
```

---

## 7. Mengirim Dictionary ke Template

### Route

```python
@app.route('/data')
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('data.html', user=user)
```

### Template `data.html`

```html
<h1>Nama: {{ user.name }}</h1>
<p>Umur: {{ user.age }}</p>
<p>Kota: {{ user.city }}</p>
```

---

## 8. Menggunakan `for` dan `if` di Template

### 8.1. `for` Loop

```python
@app.route('/users')
def users():
    user_list = [
        {"name": "Ali", "role": "admin"},
        {"name": "Budi", "role": "user"},
        {"name": "Citra", "role": "admin"},
        {"name": "Dewi", "role": "user"},
    ]
    return render_template('users.html', users=user_list)
```

#### Template `users.html` (Potongan)

```html
<ul>
{% for user in users %}
    {% if user.role == "admin" %}
        <li><strong>{{ user.name }} (Admin)</strong></li>
    {% else %}
        <li>{{ user.name }}</li>
    {% endif %}
{% endfor %}
</ul>
```

---

## 9. Menampilkan Index Loop

```html
<ul>
{% for user in users %}
    <li>{{ loop.index }}. {{ user.name }}</li>
{% endfor %}
</ul>
```

---

## 10. Template Kondisional (`if`, `elif`, `else`)

### Route

```python
@app.route('/nilai/<int:score>')
def nilai(score):
    return render_template('nilai.html', score=score)
```

### Template `nilai.html`

```html
{% if score >= 90 %}
    <p>Nilai Anda: {{ score }} - Sangat Baik! 🎉</p>
{% elif score >= 75 %}
    <p>Nilai Anda: {{ score }} - Baik 👍</p>
{% elif score >= 60 %}
    <p>Nilai Anda: {{ score }} - Cukup 😊</p>
{% else %}
    <p>Nilai Anda: {{ score }} - Perlu Perbaikan 😢</p>
{% endif %}
```

---

## 11. Loop dengan Kondisi dan Nilai

### Route

```python
@app.route('/mahasiswa')
def mahasiswa():
    daftar_mahasiswa = [
        {"nama": "Ali", "nilai": 92},
        {"nama": "Budi", "nilai": 80},
        {"nama": "Citra", "nilai": 65},
        {"nama": "Dewi", "nilai": 55},
    ]
    return render_template('mahasiswa.html', mahasiswa=daftar_mahasiswa)
```

### Template `mahasiswa.html`

```html
<ul>
{% for mhs in mahasiswa %}
    <li>
        {{ mhs.nama }} - Nilai: {{ mhs.nilai }} - 
        {% if mhs.nilai >= 90 %}
            Lulus dengan Pujian 🎓
        {% elif mhs.nilai >= 75 %}
            Lulus 👍
        {% elif mhs.nilai >= 60 %}
            Lulus Bersyarat 😊
        {% else %}
            Tidak Lulus 😢
        {% endif %}
    </li>
{% endfor %}
</ul>
```

---

## 12. Interaktif Konten di HTML + JS

### Template `users.html` Interaktif

```html
<a href="javascript:void(0)" onclick="showContent('for_statement')">
    <button>7.1. For Statement dalam Template Flask</button>
</a>

<script>
function showContent(id) {
    document.querySelectorAll('.content').forEach((el) => el.style.display = 'none');
    document.getElementById('main_content').style.display = 'none';
    document.getElementById(id).style.display = 'block';
}
</script>
```

---

## 13. Menjalankan Aplikasi

Setelah semua siap, jalankan aplikasi dengan:

```bash
python app.py
```

Akses di browser:

```bash
http://127.0.0.1:5000/
```

---

## 🌐 Daftar URL Route

| URL | Keterangan |
|-----|------------|
| `/` | Halaman utama |
| `/about` | Halaman about |
| `/profile/<nama>` | Halaman profil dinamis berdasarkan nama |
| `/data` | Menampilkan data user dari dictionary |
| `/users` | Menampilkan daftar user dengan `for` dan `if` |
| `/mahasiswa` | Menampilkan status nilai mahasiswa |
| `/nilai/<angka>` | Menampilkan hasil penilaian berdasarkan nilai |

---

## ✅ Kebutuhan Dependensi

File `requirements.txt`:

```
Flask==2.1.1
Werkzeug==2.0.3
```

Instal semua dependensi:

```bash
pip install -r requirements.txt
```

---

# 🧮 Kalkulator Bunga Tabungan dengan Flask

Aplikasi web sederhana menggunakan Flask untuk menghitung **bunga tabungan** berdasarkan input pengguna: modal awal, suku bunga, dan lama waktu menabung. Desainnya modern dan responsif, cocok buat latihan *form handling* dan *perhitungan dinamis* di sisi server.

---

## 📁 Struktur Project

```
project/
│
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
└── requirements.txt
```

---

## 🔧 1. Instalasi

Install semua dependensi terlebih dahulu:

```bash
pip install -r requirements.txt
```

Isi file `requirements.txt`:

```
Flask==2.1.1
Werkzeug==2.0.3
```

---

## 🧠 2. Fungsi Aplikasi

Aplikasi ini menghitung **bunga sederhana (Simple Interest)** menggunakan rumus:

```
Bunga = (Modal × Suku Bunga × Waktu) / 100
Total = Modal + Bunga
```

---

## 🌐 3. Routing

| URL | Metode | Keterangan |
|-----|--------|------------|
| `/` | GET / POST | Menampilkan form kalkulator dan memproses perhitungan |
| `/result` | POST (via render) | Menampilkan hasil perhitungan bunga |

---

## 📄 4. `app.py` - Logika Utama

```python
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        principal = float(request.form["principal"])
        rate = float(request.form["rate"])
        time = float(request.form["time"])

        interest = (principal * rate * time) / 100
        total_amount = principal + interest

        return render_template("result.html", total=total_amount, interest=interest)

    return render_template("index.html")
```

---

## 🖥️ 5. Template `index.html` – Form Input

```html
<h2>Kalkulator Bunga Tabungan</h2>
<form method="POST">
    Modal Awal:
    <input type="number" name="principal" required><br>
    Suku Bunga (% per tahun):
    <input type="number" name="rate" required><br>
    Waktu (tahun):
    <input type="number" name="time" required><br>
    <button type="submit">Hitung</button>
</form>
```

---

## 📊 6. Template `result.html` – Hasil Perhitungan

```html
<h2>Hasil Perhitungan</h2>
<p id="total" data-value="{{ total }}">{{ total }}</p>
<p id="interest" data-value="{{ interest }}">{{ interest }}</p>
<a href="/">Hitung Lagi</a>
```

Disertai script JavaScript untuk **format mata uang Rupiah (Rp)**:

```javascript
function formatCurrency(value) {
    let formattedValue = value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return "Rp " + formattedValue;
}
```

---

## 🎨 7. CSS (style.css)

File `static/style.css` memberikan tampilan modern:

- Container dengan *shadow*, *rounded corners*
- Responsif & clean
- Input dan tombol dengan style menarik
- Format hasil perhitungan agar lebih rapi

Contoh:

```css
.container {
    max-width: 600px;
    margin: 40px auto;
    padding: 20px;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
```

---

## 🚀 Menjalankan Aplikasi

Jalankan aplikasi dengan:

```bash
python app.py
```

Buka browser:

```
http://127.0.0.1:5000/
```

---

## ✅ Contoh Penggunaan

**Input:**

- Modal Awal: 1.000.000
- Suku Bunga: 5
- Waktu: 2 tahun

**Hasil:**

- Bunga: Rp 100.000
- Total Tabungan: Rp 1.100.000

---