## Face Detection Menggunakan Algoritma Haar Cascade Classifier

Algoritma Haar Cascade merupakan salah satu model machine learning yang kerap kali digunakan sebagai pondasi aplikasi object detection (terutama face recognition), dalam sebuah gambar maupun video. Algoritma ini lahir dari gagasan Paul Viola dan Michael Jones yang tertuang dalam paper berjudul “ Rapid Object Detection using a Boosted Cascade of Simple Features” (2001).
Berikut merupakan langkah - langkah untuk menggunakan algoritma Haar Cascade Classifier menggunakan bahasa pemrograman Python

### 1. Requirements
- Anaconda
&nbsp;&nbsp;<p>Anaconda adalah paket distribusi Python dari **Continuum Analytics** yang berisi paket Python ditambah beberapa paket tambahan untuk keperluan pemrograman data science, matematika   hingga teknik dalam satu distribusi platform yang user friendly. File instalasi Anaconda dapat diunduh di <a href="https://www.anaconda.com/products/individual">tautan ini</a>.</p> 
- OpenCV  
&nbsp;&nbsp;<p>OpenCV (Open Source Computer Vision Library), adalah sebuah library open source yang dikembangkan oleh intel  yang fokus untuk menyederhanakan programing terkait citra digital. Di dalam OpenCV sudah mempunyai banyak fitur, antara lain : pengenalan wajah, pelacakan wajah, deteksi wajah, Kalman filtering, dan berbagai jenis metode AI (Artificial Intellegence). Dan menyediakan berbagai algoritma sederhana terkait Computer Vision untuk low level API.Untuk bisa menggunakan algoritma Haar Cascade Classifier, anda harus menginstall library OpenCV di dalam environment yang anda buat terlebih dahulu. Untuk membuat environment dan menginstall library OpenCV silahkan pergunakan anaconda yang sudah di install</p>
- Visual Studio Code
&nbsp;&nbsp;<p>Visual Studio Code adalah editor source code yang dikembangkan oleh Microsoft untuk Windows, Linux dan MacOS. Ini termasuk dukungan untuk debugging, GIT Controlyang disematkan, penyorotan sintaks, penyelesaian kode cerdas, cuplikan, dan kode refactoring. Hal ini juga dapat disesuaikan, sehingga pengguna dapat mengubah tema editor, shortcut keyboard, dan preferensi.Visual Studio Code gratis dan open-source. File instalasi Visual Studio Code dapat diunduh di <a href="https://code.visualstudio.com/">tautan ini</a>.</p>
- File haarcascade_frontalface_default.xml
&nbsp;&nbsp;<p>File tersebut merupakan file yang berisi hasil training wajah</p>

### Test
- Test menggunakan gambar
