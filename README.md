# Sesi9_PCd

Analisis Hasil
Operator Roberts:
Operator Roberts menggunakan dua kernel 2x2 untuk mendeteksi tepi. Metode Roberts ebih sensitif terhadap perubahan intensitas yang tajam dan memberikan hasil yang lebih halus dibandingkan dengan Sobel.
Hasil dari operator Roberts cenderung menghasilkan lebih banyak noise, terutama pada gambar dengan banyak detail halus.

Operator Sobel:
Operator Sobel menggunakan kernel 3x3 yang lebih besar, sehingga memberikan hasil yang lebih stabil dan mengurangi noise. Sobel lebih baik dalam mendeteksi tepi yang lebih halus dan lebih luas.
Hasil dari operator Sobel menunjukkan tepi dengan lebih jelas dan lebih sedikit noise dibandingkan dengan Roberts.
