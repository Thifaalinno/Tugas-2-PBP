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


--Tugas 3--

-- Terdapat setidaknya 5 komponen yang menjadi pembeda antara form POST dan form GET dalam Django, yaitu:
    - Dalam metode pengiriman data, form POST mengirim data sebagai bagian dari permintaan HTTP, sedangkan pada form GET, data dikirim sebagai query string dalam URL.
    - Dalam Keamanan, Post lebih aman untuk data yang sensitif, sedangkan pada Get, data terbuka dan kurang aman.
    - Batasan panjang data, Post tidak memiliki batasan yang bersifat baku tetapi terdapat batasan server, sedangkan Get memiliki batasan panjang URL.
    - Caching, Post tidak dicache oleh browser, sedangkan Get dapat dicache oleh browser.
    - Dalam Penggunaan, Post digunakan untuk mengirim data yang akan mengubah sumber daya di server, sedangkan Get digunakan untuk mengmbil informasi dari server tanpa mengubahnya.

-- Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data adalah:
    - XML memberi kita fleksibilitas untuk mendefinisikan struktur data yang kompleks, biasanya digunakan untuk pertukaran data antar aplikasi atau untuk mengatur data yang rumit seperti dokumen atau konfigurasi. 
    - JSON lebih sederhana dan ringkas dalam merepresentasikan data, sangat umum digunakan dalam pengembangan web, terutama untuk pertukaran data melalui API dan penyimpanan data yang mudah dimengerti.
    - HTML adalah bahasa yang digunakan untuk mengatur tampilan dan struktur halaman web, berfokus pada cara konten ditampilkan di peramban web pengguna.

-- JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kesederhanaan sintaksisnya yang mudah dibaca oleh manusia dan mudah diproses oleh mesin. JSON memiliki dukungan yang luas di berbagai bahasa pemrograman dan framework web, serta menjadi format standar dalam pengembangan RESTful APIs. Kemampuan JSON untuk mendukung beragam tipe data, mudah diuji, dan platform-agnostic membuatnya menjadi pilihan yang ideal untuk komunikasi antar aplikasi web yang berjalan pada berbagai lingkungan dan platform.

-- Langkah-langkah pengimplementasian cheklist pada Tugas 3:
1. Untuk membuat input form yang pertama dilakukan adalah membuat berkas baru pada direktori main yang digunakan untuk membuat struktur form yang dapat menerima data prouk baru. Membuat model dan menginisiasi fields dengan atribut yang akan digunakan. Selanjutnya membuat fungsi baru untuk menerima parameter request pada berkas views. Kemudian membuat berkas HTML yang akan digunakan untuk menampilkan input form tersebut pada peramban web pengguna.
2. Untuk menambahkan 5 fungsi views dengan kelima format yang di berikan yang pertama dilakukan adalah dengan mengembalikan data maupun mengembalikan data berdasarkan ID dalam bentuk format yang diberikan, yaitu XML, JSON, XML by ID, JSON by ID dan format HTML untuk menampilkan data pada peramban web. Dengan menambahkan fungsi baru yang digunakan untuk menerima parameter request pada tiap format pada berkas views.py dan me-return fungsi-fungsi tersebut serta menambahkan path url ke dalam berkas urls.py sehingga views dapat diakses dengan routing pada url.
3. Untuk membuat routing url untuk setiap views yang ada yaitu dengan menghilangkan path "main/" yang ada pada berkas urls.py pada root folder. Dengan demikian, setiap view dapat diakses dengan menambahkan "/" dan format views yang diinginkan pada url.

-- screenshot kelima url hasil akses pada Postman dalam bentuk link googledrive, berikut linknya: https://drive.google.com/drive/folders/1cVks04kNKf9oV-3PNkePU0SXtje7fAxX?usp=sharing


-- Tugas 4 --
-- Django UserCreationForm adalah sebuah formulir bawaan yang disediakan oleh Django untuk memudahkan pembuatan akun pengguna dalam aplikasi web. Formulir ini digunakan untuk mengumpulkan informasi yang diperlukan untuk membuat pengguna baru, seperti nama pengguna (username) dan kata sandi (password), serta informasi tambahan yang mungkin diperlukan sesuai dengan konfigurasi aplikasi Anda.
    Kelebihan:
    - Mudah Digunakan
    - Validasi Otomatis
    - Fleksibel

    Kekurangan:
    - Tidak dapat di Kustom
    - Penggunaan Default Template

-- Autentikasi adalah proses verifikasi identitas pengguna (misal, dengan username dan password), sementara otorisasi adalah pengaturan izin yang memutuskan apa yang dapat dilakukan oleh pengguna yang telah terautentikasi. Autentikasi memastikan pengguna sah, sementara otorisasi mengendalikan akses mereka ke fitur dan data. Keduanya penting dalam menjaga keamanan dan privasi serta mengendalikan akses dalam aplikasi. Django menyediakan alat untuk mengimplementasikan keduanya dengan efisien.

-- Cookies dalam konteks aplikasi web adalah data kecil yang disimpan di peramban pengguna untuk mengidentifikasi dan melacak penggunaan situs web. Django menggunakan cookies untuk mengelola data sesi pengguna dengan menyimpan informasi sesi seperti ID sesi atau preferensi pengguna secara aman pada peramban pengguna. Ini memungkinkan aplikasi untuk menjaga status pengguna selama mereka berinteraksi dengan situs web tanpa perlu masuk ulang. Django menyediakan dukungan bawaan untuk mengelola cookies sesi pengguna melalui modul django.contrib.sessions.

-- Penggunaan cookies dalam pengembangan web dapat aman secara default, tetapi ada risiko potensial seperti pelacakan pengguna dan kerentanannya terhadap serangan seperti perusakan cookie atau peretasan sesi. Pengembang perlu memahami risiko ini dan mengimplementasikan praktik keamanan seperti enkripsi dan kebijakan penggunaan cookies yang bijak untuk meminimalkan risiko tersebut.

-- Pengimplementasian checklist:
1. memodifikasi beberapa berkas diantaranya yaitu menambahkan fungsi-fungsi baru pada berkas views.py dan menghubungkan urls tersebut dengan menambahkan path url pada berkas urls.py dan menambahkan fitur-fitur yang dibutuhkan pada file html.
2. menambahkan fungsi baru pada fungsi show main dan meodifikasi fungsi-fungsi yang udah ada sebelumnya. Menambahkan import datetime untuk menambilkan last login.
3. Untuk menghubungkan  model Item dengan User, perlu mengimport User tsb pada berkas models.py dan menambahkan potongan kode pada model Product yang ada serta membuat fungsi baru.