link Repositori: https://github.com/Thifaalinno/Tugas-2-PBP.git

-- Langkah-langkah pengimplementasian cheklist:
1. Untuk membuat sebuah proyek Django baru, langkah pertama yang dilakukan adalah dengan membuat direktori baru dan mengaktifkan virtual environment.
2. Menyiapkan Dependencis dan membuat proyek Django. Dependencis berguna untuk memungkinkan pengembang memanfaatkan kode yang telah ada dan mempercepat pengembangan, dengan membuat berkas requirements.txt yang berisi beberapa dependencis. Selanjutnya membuat proyek Django dengan perintah 'django-admin startproject <nama proyek> .' pada cmd.
3. Konfigurasi proyek dan menjalankan server. Menambahkan '*' pada ALLOWED_HOSTS di settings.py untuk keperluan deployment. Kemudian menjalankan server Django dengan perintah 'python manage.py runserver'.
4. Menghentikan server dan menonaktifkan virtual environment. 
5. Mengunggah proyek ke repositori GitHub, dengan membuat repositori baru pada GitHub kemudian menginisiasi direktori utama sebagai repositori Git. Kemudian menambahkan berkas konfigurasi yang saya namankan '.gitignore'. Selanjutnya melakukan add, commit, push dari direktori repositori lokal.
6. Deployment pada Adaptable.io (Mengalami masalah pada saat deployment pada Adaptable.io karna akun dinonaktifkan oleh Adaptable.io)
7. Membuat aplikasi main pada proyek, dengan menjalankan perintah 'python manage.py startapp main' dan mendaftarkan aplikasi main ke dalam proyek dengan menambahkan 'main' pada berkas settings.py yang ada pada direktori utama.
8. Membuat dan mengisi berkas main.html untuk routing proyek main, dengan membuat direktori baru bernama templates pada direktori aplikasi main yang berisi berkas main.html yang berguna untuk menampilkan halaman main pada client.
9. Membuat model dasar dengan mengubah berkas models.py dengan atribut wajib yang ada pada deskripsi tugas yaitu name sebagai nama item dengan tipe CharField, amount sebagai jumlah item dengan tipe IntegerField,
description sebagai deskripsi item dengan tipe TextField. Selanjutnya melakukan migrasi model.
10. Menghubungkan view dengan template dengan mengintegrasi komponen MVT dan selanjutnya memodifikasi kode pada berkas views.py.
11. Mengonfigurasi routing URL dengan membuat berkas urls.py pada direktori main dan melengkapi kodenya. 
12. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat.
13. Mebuat README.md berisi tautan 


-- Bagan yang berisi request client ke web aplikasi berbasis Django:
    1. Client(Browser), Pengguna membuka browser dan mengirimkan permintaan ke aplikasi Django.
    2. DNS Resolution, Browser mencari alamat IP aplikasi melalui DNS.
    3. HTTP Request, Browser mengirimkan permintaan HTTP ke server web Django.
    4. Django URL Routing (urls.py), Django mencocokkan URL dengan view yang sesuai berdasarkan konfigurasi urls.py.
    5. View (views.py), View memproses permintaan, berinteraksi dengan model jika perlu, dan mengembalikan data.
    6. Model (models.py), Model digunakan untuk berkomunikasi dengan database jika diperlukan.
    7. Response Building, Data dari view digabungkan dengan template HTML untuk membuat halaman HTML.
    8. HTTP Response, Halaman HTML dikirim kembali ke browser dengan status HTTP.
    9. Browser pengguna, Browser menerima dan merender halaman HTML untuk ditampilkan kepada pengguna.

Hubungan antar komponen:
Request dari client seperti browser dari user, pertama kali diterima oleh Django yang kemudian mengarahkan request tersebut menuju view yang sesuai berdasarkan konfigurasi pada 'urls.py'.
urls.py menghubungkan URL yang diterima dengan fungsi view pada views.py yang akan menghandle request tersebut. Ini merupakan langkah awal dalam pemrosesan request client. Kemudian view akan memproses request yang diterima, hal ini mencakup berbagai tindakan seperti mengambil data dari model, melakukan perhitungan, atau mengembalikan respon berdasarkan logika aplikasi. Selanjutnya jika view memerlukan akses ke database, models.py digunakan untuk berinteraksi dengan database. Model digunakan untuk mengambil atau menyimpan data yang diperlukan oleh view.
Terakhir, ketika view telah memiliki semua data yang diperlukan, templates digunakan untuk menghasilkan halaman HTML yang akan dikirimkan kembali ke client sebagai respon. Data dari view dimasukkan ke dalam template untuk menampilkan informasi kepada pengguna. Django mengirimkan halaman ini sebagai respon kembali ke client, yang akan ditampilkan di browser pengguna.


-- Pada dasarnya virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada perangkat yang digunakan. Menggunakan  virtual environment memumngkinkan untuk menjaga kebersihan dan keteraturan proyek yang dibangun. Selain itu, penggunakan virtual environment memudahkan pengguna lain untuk dengan mudah membuat virtual environment yang sama dan menjalankan proyek tersebut tanpa adanya masalah kompatibilitas. Dengan keunggulan yang diberikan terhadap penggunaan virtual environment maka kita menggunakannya dalam pembuatan aplikasi web berbasis Django ini.
Ya, kita tetap dapat melakukannya tetapi penggunaan virtual environment sangat direkomendasikan untuk alasan-alasan yang telah saya jelaskan di atas. Penggunaan Django sebagai media dalam pembuatan aplikasi web ini bahkan memiliki dukungan bawaan untuk virtual environment melalui alat pernama 'venv'. Sehingga, sebaiknya kita memanfaatkan virtual environment untuk membangun aplikasi web berbasis Django ini.


-- MVC (Model View Controller), MVT (Model View Template), dan MVVM (Model View ViewModel) adalah tiga pola arsitektur perangkat lunak yang digunakan dalam pengembangan perangkat lunak untuk memisahkan komponen-komponen yang berbeda dalam aplikasi dan mengorganisasi logika bisnis, tampilan, dan kontrol dengan cara yang terstruktur.
Perbedaan utama ketiganya:
    -MVC umumnya digunakan dalam aplikasi desktop dan web tradisional.
    -MVT adalah pola arsitektur spesifik untuk Django dengan Template   menggantikan Controller.
    -MVVM digunakan dalam aplikasi berbasis klien, dengan ViewModel mengatur komunikasi antara Model dan View.