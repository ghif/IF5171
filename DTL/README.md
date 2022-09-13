# IF5171 Decision Tree and Ensemble Models

Selamat datang pada direktori belajar mandiri / praktikum untuk topik Decision Tree Learning (DTL) dan Ensemble Methods yang sudah kita bahas pada pertemuan ke-3 (Senin, 12 September 2022, 13:00 - 15:00) kuliah IF5171.
Di sini teman-teman akan melakukan eksplorasi bagaimana mengimplementasikan algoritma DTL dan ensemble methods dalam bahasa pemrograman Python dengan menggunakan Jupyter notebook.

## Main Dependencies

-- *Skip this part if your working environment has been ready* --

Apabila Anda mengerjakannya di PC/laptop masing-masing, pastikan working environment nya memiliki tools / libraries sebagai berikut:
- [Python 3.x.x](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn 1.x.x](https://scikit-learn.org/stable/)
- [Jupyter notebook](https://jupyter.org/)

## Warming Up
Implementasi kode dari problem __loan decision__ yang dibahas di kelas dapat Anda lihat pada file `loan.ipynb`. Silakan dipelajari sebagai *getting started* bagi yang belum familiar dengan Python dan [jupyter notebook](https://www.edureka.co/blog/wp-content/uploads/2018/10/Jupyter_Notebook_CheatSheet_Edureka.pdf). 

Untuk linux / mac user, jupyter notebook yang sudah ter-install dapat dijalankan pada *shell command*:

> jupyter notebook


## Project #1: Census Income Prediction
Terdapat suatu dataset bernama Census Income, yang berisi personal profil dari beberapa sampel penduduk. Namun demikian, informasi mengenai pendapatan masih belum tersedia. Dataset Census Income dapat diakses di https://archive.ics.uci.edu/ml/datasets/census+income, yang sudah dibagi menjadi training (adult.data) dan test data (adult.test).

Anda mendapatkan tantangan untuk menghasilkan model machine learning yang dapat memprediksi apakah pendapatan pertahun dari seseorang di atas atau di bawah $50k.
Performa yang diinginkan adalah akurasi >= 90% pada test data, karena dianggap cukup untuk bisa mengurangi pekerjaan manual yang mesti dilakukan.

Anda dipersilahkan untuk menggunakan algoritma DTL atau salah satu algoritma dari keluarga ensemble methods (e.g., AdaBoost) untuk menghasilkan model ML yang mencapai tujuan di atas.

Implementasi kode dan penjelasan deskriptif/reasoning mengenai implementasinya (boleh dalam bahasa Indonesia atau bahasa Inggris) dapat dituliskan pada *notebook script* yang Anda buat -- tidak perlu untuk menuliskan penjelasan deskriptif di dokumen/tempat terpisah. 

Dengan menyelesaikan tantangan tersebut, peluang skor yang Anda akan dapatkan adalah sebagai berikut:
1. Proses *data transformation* / *feature extraction* yang dilakukan, mencakup kode dan penjelasan deskriptif (__50 poin__)
2. Implementasi algoritma ML yang dilakukan, mencakup kode dan penjelasan deskriptif (__30 poin__)
3. Hasil akurasi pada test data:
	- 90 - 100: __(20 poin)__, atau
	- 80 - 90: __(10 poin)__, atau
	- 70 - 80: __(5 poin)__


Anda perlu mengumpulkan deliverables berikut:
- python notebook script (*.ipynb*)
- stored model (dalam bentuk file persistent)

yang disimpan pada sebuah zip file dengan format __([NIM]-[NAMA]-IF5171-DTLEM-1.zip)__ untuk disubmit ke platform Edunex.

## Project #2

??