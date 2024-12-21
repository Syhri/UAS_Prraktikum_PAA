# Solusi dengan Algoritma Greedy
Algoritma greedy memilih titik terdekat yang belum dikunjungi pada setiap langkah. Meskipun ini tidak selalu menghasilkan solusi optimal, algoritma ini jauh lebih cepat.

***Kompleksitas Waktu dan Ruang***   
1. Time Complexity: (O(n^2))  
Algoritma greedy mengunjungi setiap kota satu kali dan pada setiap langkah mencari kota terdekat yang belum dikunjungi, sehingga kompleksitasnya adalah (O(n^2)).
2. Space Complexity: (O(n^2))  
Algoritma ini menggunakan ruang untuk menyimpan matriks jarak, yang berukuran (n \times n).

# Solusi dengan Algoritma Brute Force
Algoritma brute force mencoba semua permutasi dari urutan kota untuk menemukan rute dengan jarak total terpendek.

***Kompleksitas Waktu dan Ruang***
1. Time Complexity: (O(n!)):  
Algoritma brute force mencoba semua permutasi dari urutan kota. Ada (n-1)! permutasi yang harus diperiksa, di mana (n) adalah jumlah kota.
2. Space Complexity: (O(n)):  
Algoritma ini menggunakan ruang untuk menyimpan rute optimal dan jarak total.

***Kesimpulan***  
- Algoritma Brute Force: Memberikan solusi optimal tetapi tidak efisien untuk jumlah kota yang besar karena kompleksitas waktu yang eksponensial.
- Algoritma Greedy: Lebih efisien untuk jumlah kota yang besar, meskipun hasilnya mungkin tidak selalu optimal.

Pemilihan algoritma bergantung pada ukuran masalah dan kebutuhan spesifik Anda. Jika jumlah kota kecil, algoritma brute force bisa digunakan untuk mendapatkan solusi optimal. Untuk jumlah kota yang lebih besar, algoritma greedy lebih praktis digunakan.
