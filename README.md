# Sistem Pengenalan Citra Rambu-Rambu Lalu Lintas Menggunakan Algoritma YOLOv4

## Abstrak
Rambu-rambu lalu lintas merupakan alat pengendali lalu lintas untuk menyampaikan beberapa informasi berupa larangan, peringatan, perintah, atau petunjuk dengan tujuan untuk menertibkan pengendara. Pada rambu-rambu lalu lintas yang ditemui di jalan, banyak ditemukan rambu-rambu lalu lintas dengan kondisi yang jelek, sehingga susah untuk mengenali rambu-rambu tersebut. 

Dengan teknologi yang sedang berkembang pesat, pengimplementasian sebuah sistem yang dapat mengenali sebuah rambu-rambu lalu lintas dapat dilakukan. Namun, pendeteksian rambu-rambu lalu lintas bukan masalah yang mudah untuk dipecahkan. Rambu-rambu lalu lintas memiliki berbagai kondisi yang dapat mempengaruhi performa sistem. 

Pada penelitian ini akan dibuat sebuah sistem yang dapat mengenali sebuah rambu lalu lintas dengan berbagai kondisi secara real-time atau secara langsung pada saat itu juga. Jenis rambu-rambu lalu lintas yang digunakan adalah rambu peringatan, rambu larangan, dan rambu perintah yang berlaku di Indonesia. Total gambar yang digunakan sebanyak 300 gambar dengan kelas yang digunakan sebanyak 15 kelas yang akan diproses menggunakan data preprocessing dan data augmentation.

Proses pelatihan data menggunakan salah satu jenis algoritma YOLOv4 yaitu Scaled-YOLOv4 dan menggunakan framework PyTorch. Proses pelatihan data dilakukan dengan berbagai skema pelatihan, seperti dengan learning rate dan epoch yang berbeda-beda. Proses pelatihan data akan menghasilkan weight yang berguna untuk mendeteksi dan mengklasifikasikan rambu-rambu lalu lintas. 

Hasil pengujian terbaik menunjukkan bahwa sistem ini dapat mengenali rambu-rambu lalu lintas dengan tingkat akurasi F1-Score sebesar 99,3%, mAP 0,5 sebesar 99,5%, dan mAP 0,5:0,95 sebesar 89,4%.

## Tujuan
Membangun sebuah sistem pengenalan citra rambu-rambu lalu lintas yang dapat mengenali rambu-rambu lalu lintas dalam berbagai kondisi secara langsung (real-time) menggunakan algoritma Scaled-YOLOv4.

## Dataset
Data yang telah terkumpul berupa tiga jenis rambu yaitu rambu peringatan, rambu larangan, dan perintah. Setiap jenis rambu terdiri dari lima rambu yang berbeda dan setiap rambu tersebut terdiri dari 20 gambar yang berbeda. Total data yang digunakan adalah 300 gambar. 
Jumlah rambu lalu lintas pada dataset eksplorasi adalah sebanyak 15 jenis, yaitu:
  1.	Perintah memasuki salah satu jalur atau lajur yang ditunjuk.
  2.	Perintah memasuki jalur atau lajur yang ditunjuk (ke kiri).
  3.	Perintah memasuki jalur atau lajur yang ditunjuk (ke kanan).
  4.	Perintah mengikuti arah yang ditunjukkan saat memasuki bundaran.
  5.	Perintah mengikuti ke arah kiri.
  6.	Peringatan persimpangan tiga sisi kanan (ditempatkan pada lengan mayor).
  7.	Peringatan persimpangan tiga sisi kiri (ditempatkan pada lengan mayor).
  8.	Peringatan alat pemberi isyarat lalu lintas.
  9.	Peringatan simpang empat prioritas (ditempatkan pada lengan mayor).
  10.	Peringatan simpang empat prioritas (ditempatkan pada lengan minor).
  11.	Larangan menjalankan kendaraan dengan kecepatan lebih dari 40 km/jam.
  12.	Larangan menjalankan kendaraan dengan kecepatan lebih dari 60 km/jam.
  13.	Larangan berhenti.
  14.	Larangan parkir.
  15.	Larangan memutar balik.

## Alat
  1. Google Colaboratory
  2. Roboflow

## Hasil Implementasi
### Skema Pelatihan
Skema pelatihan yang akan digunakan adalah dataset pelatihan sebesar 70%, dataset validasi sebesar 10%, dan dataset pelatihan sebesar 20%.

### Data Preprocessing
Data preprocessing yang digunakan adalah resize untuk menyamakan ukuran gambar pada dataset yang memiliki ukuran berbeda-beda. 

### Data Augmentation
Data augmentation yang digunakan adalah
  1. Crop
  2. Rotation
  3. Hue
  4. Saturation
  5. Brightness
  6. Exposure
  7. Blur
  8. Cutout
  9. Mosaic
      
### Pelatihan
Proses pelatihan menggunakan lima varian learning rate, yaitu 0,1; 0,01; 0,001; 0,0013; dan 0,00261. Lima varian learning rate didapat dari nilai learning rate model YOLO versi lain. Epoch yang digunakan yaitu 100, 200, 300, 400, 500, dan 600. 
![image](https://github.com/randifajar/Traffic-Sign-Detection/assets/46032161/57cecc5f-3e48-4cc0-b365-fc4b54f8ef69)

Hasil dari pelatihan menggunakan learning rate 0,01 dan nilai epoch 500 adalah nilai F1-Score sebesar 99,3%, nilai mAP 0,5 sebesar 99,5% dan mAP 0,5:0,95 yang diperoleh adalah sebesar 0,894 atau 89,4%.

## Hasil Pelatihan
![image](https://github.com/randifajar/Traffic-Sign-Detection/assets/46032161/b33cd4cd-87c1-4462-8f1e-d31f976b9afd)
![image](https://github.com/randifajar/Traffic-Sign-Detection/assets/46032161/84653c63-fc2e-4cb7-a5b3-0f68f294c73e)

## Credits
  - [YOLOv4: Optimal Speed and Accuracy of Object Detection](https://arxiv.org/abs/2004.10934)
  - [YOLOv4 Repo](https://github.com/AlexeyAB/darknet)
  - [Scaled-YOLOv4: Scaling Cross Stage Partial Network](https://arxiv.org/abs/2011.08036)
  - [Scaled-YOLOv4 Repo](https://github.com/WongKinYiu/ScaledYOLOv4)
  - [Roboflow](https://roboflow.com/)
  - [Google Maps & Street View](https://www.google.com/maps)
