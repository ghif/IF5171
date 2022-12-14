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


## Project #1: Census Income Prediction (Bobot: 70%)
Terdapat suatu dataset bernama Census Income, yang berisi personal profil dari beberapa sampel penduduk. 
Namun demikian, informasi mengenai pendapatan masih belum tersedia. Dataset Census Income dapat diakses di https://archive.ics.uci.edu/ml/datasets/census+income, yang sudah dibagi menjadi training (adult.data) dan test data (adult.test).

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
- Python notebook script (*.ipynb*)
- Stored model (dalam bentuk [persistent file](https://scikit-learn.org/stable/model_persistence.html))
- Predicted output dalam bentuk tabel dengan 2 kolom: 'Id' dan 'Prediction' (*.csv)

yang disimpan pada sebuah zip file dengan format __([NIM]-[NAMALENGKAP]-IF5171-DTLEM-1.zip)__ untuk disubmit ke platform Edunex.

## Project #2: Bank Customer Churn Prediction (Bobot: 30%)

Pada studi kasus perbankan, salah satu hal yang penting untuk dijaga adalah mempertahankan nasabah selama mungkin, i.e., [*customer lifetime value*](https://en.wikipedia.org/wiki/Customer_lifetime_value) yang tinggi. 
Semakin banyak nasabah yang menjadi tidak aktif atau tidak lagi menjadi nasabah (*churn*), maka semakin besar potensi kerugian yang dihasilkan.

Identifikasi dini apakah seorang nasabah berpotensi non-aktif (biasanya dalam kurun waktu 6 bulan ke depan) akan sangat bermanfaat bagi *account/sales officer* untuk menindaklanjuti dalam bentuk layanan ekstra atau penawaran produk sehingga dapat meningkatkan *customer experience*.


Sebagai seorang *data scientist*, Anda memiliki ide untuk mengimplementasikan sebuah model ML prediksi *churn* sehingga membantu para *account officer* dapat terbantu untuk melakukan tindak lanjut yang lebih terukur.
Di sini tersedia dataset *real world* [customer churns](https://1drv.ms/u/s!AgX5GEtworUahSBOjjue1xZEHri_?e=5mAEAc) dari salah satu bank besar di Indonesia, yang terdiri dari 2 file:
- churn_train.csv: 100.000 baris dan 126 atribut (125 kolom fitur dan 1 kolom target 'y')
- churn_test.csv: 25.000 baris

Atribut $x_0 - x_{124}$ merupakan info nasabah yang telah dinormalisasi dan dirahasiakan nama atributnya untuk menjaga *privacy* dan *security*.

Anda dipersilahkan untuk menggunakan algoritma DTL atau ensemble methods apapun yang menurut Anda mampu memberikan performa terbaik.

Deliverable yang perlu Anda hasilkan adalah:
- Python notebook implementation script (*.ipynb*)
- Stored model (dalam bentuk [persistent file](https://scikit-learn.org/stable/model_persistence.html))
- Predicted output dalam bentuk tabel dengan 2 kolom: 'Id' dan 'Prediction' (*.csv)

yang disimpan pada sebuah zip file dengan format __([NIM]-[NAMALENGKAP]-IF5171-DTLEM-2.zip)__ untuk disubmit ke platform Edunex.

Implementasi yang dilakukan, tertuang pada *.ipynb* script, sekurang-kurangnya meliputi:
1. *Data preparation*: __(15 poin)__
2. *Exploratory Data Analysis*: __(20 poin)__
3. *Feature Engineering*: __(30 poin)__
4. *Modeling*: __(20 poin)__
5. *Evaluation* yang menyertakan [skor-skor berikut](https://www.baeldung.com/cs/ml-accuracy-vs-auc): __(15 poin)__
	- Accuracy
	- Precision
	- Recall
	- False Positive Rate (FPR)
	- AUC
	- Grafik [Receiver Operating Characteristic (ROC) curve](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)

Sebagai tambahan konteks, telah dilakukan *first pass*/uji coba awal dengan menggunakan algoritma XGBoost dan proses *feature engineering* yang sangat sederhana. 
Hasil yang didapatkan sebagai berikut:
- Accuracy: 0.85
- Precision: 0.55
- Recall: 0.55
- FPR: 0.09
- AUC: 0.73

<img src="roc_init.png"  width=75% height=75%>
<!-- ![alt text](roc_init.png "ROC Curve"){width=50} -->

Anda diharapkan untuk bisa menghasilkan performa lebih baik dibandingkan *first pass* di atas.

Selamat bermain! :) 


## Submission
1. Dua (2) files yang di-submit via platform Edunex:
	- Project #1: __[NIM]-[NAMALENGKAP]-IF5171-DTLEM-1.zip__
	- Project #2: __[NIM]-[NAMALENGKAP]-IF5171-DTLEM-2.zip__
2. Deadline: __Jumat, 16 September 2022, pukul 23:59 WIB__