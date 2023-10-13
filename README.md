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

-- Tugas 5 --
-- berikut adalah manfaat dari setiap elemen selector dan kapan waktu yang tepat untuk menggunakannya:
 - Universal Selector (*):
Manfaat: Memengaruhi semua elemen dalam dokumen.
Kapan digunakan: Situasi khusus yang memerlukan pengaruh global pada semua elemen.
- ID Selector (#):
Manfaat: Memengaruhi elemen dengan id tertentu.
Kapan digunakan: Ketika Anda ingin memengaruhi elemen tunggal dengan id unik.
- Type Selector (Element Selector):
Manfaat: Memengaruhi semua elemen dengan jenis yang sama.
Kapan digunakan: Untuk gaya elemen umum dengan jenis yang sama, seperti paragraf atau heading.
- Class Selector (.):
Manfaat: Memengaruhi elemen dengan class tertentu.
Kapan digunakan: Untuk menerapkan gaya atau logika pada beberapa elemen dengan class yang sama, seperti tombol.
- Attribute Selector ([]):
Manfaat: Memengaruhi elemen berdasarkan atribut dan nilainya.
Kapan digunakan: Saat Anda ingin memilih elemen dengan atribut tertentu, seperti <a href="...">.
- Pseudo-class Selector (:):
Manfaat: Memengaruhi elemen berdasarkan keadaan atau interaksi pengguna.
Kapan digunakan: Untuk memberikan efek interaktif, seperti mengubah warna link saat kursor mengarah padanya.

--  berikut adalah beberapa tag HTML5 yang umum digunakan secara singkat:
<header>: Digunakan untuk bagian kepala dari suatu elemen atau dokumen, biasanya berisi judul atau logo.
<nav>: Mendefinisikan bagian navigasi dalam dokumen.
<main>: Menandakan konten utama dalam dokumen HTML.
<section>: Digunakan untuk mengelompokkan konten yang saling terkait dalam dokumen.
<article>: Digunakan untuk mengelompokkan konten yang independen, seperti postingan blog atau artikel berita.
<aside>: Mendefinisikan konten yang terkait, tetapi bukan bagian utama dari dokumen.
<footer>: Digunakan untuk bagian penutup atau kaki dari suatu elemen atau dokumen.
<div>: Kontainer generik untuk mengelompokkan dan mengatur elemen-elemen HTML.
<p>: Menandakan paragraf teks.
<a>: Membuat tautan atau hyperlink ke halaman lain atau sumber eksternal.
<img>: Menampilkan gambar di dalam dokumen.
<ul> dan <ol>: Digunakan untuk membuat daftar tak berurutan (unordered list) dan daftar berurutan (ordered list).
<li>: Mendefinisikan elemen dalam daftar, baik itu dalam <ul> atau <ol>.
<table>: Digunakan untuk membuat tabel dalam dokumen.
<form>: Membuat formulir yang memungkinkan pengguna untuk mengirimkan data.
<input>: Menambahkan berbagai jenis elemen input dalam formulir, seperti teks, kata sandi, atau tombol.
<textarea>: Membuat area teks besar yang memungkinkan pengguna memasukkan teks lebih dari satu baris.

-- Perbedaan antara margin dan padding:
Margin adalah jarak di luar batas elemen, yang mempengaruhi ruang antara elemen dan elemen-elemen lain di sekitarnya. Margin digunakan untuk mengatur jarak antara elemen dengan elemen lain di luarnya.

Padding adalah jarak di dalam batas elemen, yang mempengaruh ruang antara konten elemen dan batas elemen itu sendiri. Padding digunakan untuk mengatur jarak antara konten elemen dan batasnya.

-- Perbedaan antara framework CSS Tailwind dan Bootstrap:
- Tailwind CSS:
Pendekatan "utility-first" yang memungkinkan pengembang untuk membangun tampilan dengan menggunakan kelas-kelas kecil yang disesuaikan.
Menyediakan sejumlah besar kelas utilitas yang dapat diterapkan pada elemen HTML.
Lebih fleksibel dan memberikan kendali yang lebih besar dalam desain yang sangat disesuaikan.
Ukurannya lebih kecil dibandingkan dengan Bootstrap karena hanya menghasilkan kode CSS yang digunakan.

Gunakan Bootstrap jika ingin mengembangkan proyek dengan cepat dan memanfaatkan komponen-komponen bawaan, menginginkan tampilan yang seragam dan lebih tradisional, tidak memiliki banyak waktu atau sumber daya untuk menyesuaikan tampilan secara ekstensif.

- Bootstrap:
Terintegrasi dengan desain yang sudah ada dan menggunakan sejumlah besar komponen dan gaya bawaan.
Lebih cocok untuk pengembangan cepat dan prototyping karena komponen-komponen sudah siap digunakan.
Memiliki desain yang lebih konsisten secara default, cocok untuk proyek yang ingin tampil seragam.
Lebih cocok untuk pengembangan berbasis template dan proyek yang memerlukan tampilan yang sudah jadi.

Gunakan Tailwind CSS jika ingin desain yang sangat disesuaikan dan fleksibel, lebih suka pendekatan "utility-first" dalam pengembangan tampilan, ingin mengurangi ukuran file CSS yang dihasilkan, memiliki keterampilan CSS yang kuat atau memerlukan tampilan yang sangat khusus.

-- Pengimplementasian checklist:
1.  Menambahkan Bootstrap ke Aplikasi, CSS, JS dan lainnya
2. Menambahkan navbar pada halaman aplikasi, yaitu mengkustomisasi kode yg ada pada main.html
3. Menambahkan Fitur edit dan delete produk pada Aplikasi,
4. Melakukan kustomisasi kode pada halaman-halaman terkait sehingga tampilan menjadi lebih menarik dan berwarna.

-- Tugas 6 --
- Jelaskan perbedaan antara asynchronous programming dengan synchronous programming:
Perbedaan utama antara keduanya adalah bagaimana mereka menangani operasi yang memakan waktu. Synchronous programming menghentikan eksekusi sampai operasi selesai, sementara asynchronous programming memungkinkan eksekusi yang lebih fleksibel dengan melanjutkan ke tugas lain saat menunggu hasil operasi yang memakan waktu.

- Paradigma event-driven programming adalah pendekatan pemrograman di mana program merespon kejadian atau peristiwa yang terjadi, seperti interaksi pengguna, masukan data, atau peristiwa lainnya, dengan menjalankan fungsi atau tindakan tertentu. Dalam konteks JavaScript dan AJAX, ini mengacu pada cara program merespons peristiwa yang terjadi di dalam aplikasi web, seperti klik tombol, input pengguna, atau respon dari permintaan HTTP. Contohnya: Menampilkan Data Stok

- Pada AJAX, asynchronous programming memungkinkan pengiriman permintaan HTTP ke server tanpa menghentikan eksekusi kode JavaScript. Ini berarti kode JavaScript dapat terus berjalan, dan ketika respons dari server tiba, callback function akan dijalankan. Dengan demikian, aplikasi web tetap responsif, memungkinkan interaksi pengguna yang lebih halus dan dinamis.

- Fetch API merupakan pendekatan modern dan lebih ringan untuk mengelola permintaan HTTP di dalam aplikasi web, sementara jQuery adalah library yang lebih luas dalam cakupannya. Fetch API mendukung Promises, memberikan kontrol yang lebih besar, dan merupakan standar web, membuatnya menjadi pilihan yang lebih efisien untuk pengembangan proyek baru atau penggunaan AJAX yang sederhana.
