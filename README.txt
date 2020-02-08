Pertama dulu saya buat: 

1. different number of columns 
2. same number of columns 

Eksperimen menggunakan data diab versi besar jadi takes time! 

Akhirnya ya sudah ganti lah ke insights yang lain 

3. skewness_insights
4. kurtosis_insights
5. correlation_insights 

Tiga eksperimen ini menggunakan toy dataset diab dataset dari python 
Untuk eksperimen aggregate insights akhirnya pakai heart disease 

6. x_heart_dataset 

eksperimen no 6 ini cukup lengkap menggunakan heart disease

Setelah itu karena supervisor minta combination dalam satu plot akhinrya saya 
bikin folder lain 

7. combination_results 

Karena combination results masih dari data yg berbeda, beda k, beda percentage. 

Akhirnya saya putuskan buat folder lagi 

8. x_heart_insgihts. 

Nah folder ini berisi combination dg same dataset yakni heart disease dengan 
same subset juga yakni disease = Yes 


9. Sekarang ngerjain how to handle missing data jadi ada 3 cara. Lihat plot nya aja
saya juga ngerjain yg insight lain dengan 2 technique untuk handle missing


Kenapa di beberapa plot aggregate insight bisa sampaing missing 90 % dengan metode ignore cells? karena itu plot pakai missing on A + M yang mana tidak masalah 
Klo misal mau plot missing only on A atau only on M dg cara percentage dari value static total cells maka itu impossible. 


Klo mau lihat plot yg compare smua insight itu di x_heart_insight 

Tapi kalau mau lihat cumulative distance dari smua itu buka folder cumulative distance



10 Beda a heart dan heart random. 
heart random missing sampai 90 untuk a m 
kalau a heart hanya sampai 40 dan itu missing dimulai dari 5, bahkan klo yg drop rows hanya sampai 20 %. Intinya yang a heart itu untuk how to deal with missing 


11. Folder absolute correlation and skewness insight: correlation and skewness sudah pakai nilai abs 

12. small missing: mencoba dg missing percentage small 1 - 10 % missing 









Buat Code yang Lebih bagus lagi 
1. No missing on predicate column 
2. Same Column: A and M 
3. No Count aggregate insight, try min 
4. Missing settings: only A+M 0 - 90, A, M 0,5,10,15,20,25,30 
5. Create functions: Jaccard, RBO, c_d jadi satu semua, tinggal sekali calling
6. Correlation emang nilainya gitu, drop dia klo di c_d karena nilainya beda, mungkin krn effect missing 
7. Confirmation: AGF: SUM apakah hanya berefek pd k kecil? 
8. Plot How to handle missing values technique, dg 3 distance tadi

