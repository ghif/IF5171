## Soal UTS (25 poin)
Implementasikan sebuah model deep learning dengan menggunakan PyTorch yang mampu memprediksi objek pada dataset CIFAR-100: https://pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR100.html.

#### Deliverables
- Notebook scripts yang mengimplementasikan algoritma *training* (ipynb / py)
- 1 grafik/*line chart* yang menggambarkan progress akurasi terhadap waktu/epoch: sumbu x menunjukkan epoch, sumbu y menggambarkan skor akurasi (png / jpg)

#### Skor
- (20 poin) Deliverables di atas dalam kondisi lengkap serta proses training berjalan dengan benar / tidak ada *runtime error* pada *training scripts*.
- (+5 poin) Apabila mampu mencapai *test/validation accuracy* mencapai akurasi di atas 40%.

#### Referensi/*Hints*
* Manfaatkan `dropout` atau `batch normalization` untuk mendapatkan akurasi prediksi yang lebih baik.
	* nn.Dropout: https://pytorch.org/docs/stable/generated/torch.nn.Dropout.html
	* nn.Dropout2d: https://pytorch.org/docs/stable/generated/torch.nn.Dropout2d.html
	* nn.BatchNorm1d: https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html#torch.nn.BatchNorm1d
	* nn.BatchNorm2d: https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d


