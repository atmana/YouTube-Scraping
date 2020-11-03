Melakukan scraping video trick Internet gratis/murah yang paling update dan memiliki jumlah View yang terbanyak di YouTube. 
Dari informasi text comment pada video, dilakukan analisis secara otomatis berdasarkan model data yang sudah ditraining menggunakan Naive Bayes Classifier, sehingga dapat disimpulkan diawal trick video tersebut working atau tidak.

Script utama yang dirunning untuk manjalankan seluruh fungsi --> Youtube_by_Keyword.py 
Menjalankan fungi untuk sentiment analis dari comment di video --> sentimentYouTube.py
Mengambil text comment dari video --> comment_extract.py
Proses model training untuk menjalankan analisa sentimen dari comment di video --> training_classifier.py
Data set training --> emoji.txt, negative.txt, positive.txt
Hasil model training --> classifier.pickle


Sample Output :
Title	viewCount	commentCount	likeCount	dislikeCount	favoriteCount	videoId	channelId	categoryId	URL	positive (%)	negative (%)
TELKOMSEL OPOK,HTTP INJECTOR TES LIMIT ALL TKP..!!!	3300	69	32	3	0	9amVk5ISI1M	UCxEyBff9TVgXPH_F9W9h3fQ	28	https://www.youtube.com/watch?v=9amVk5ISI1M	55	44
TELKOMSEL OPOK LANCAR JAYA TERBARU DESEMBER AKTIF SAMPAI 2020	3620	173	34	4	0	2C7lYB7slow	UCogULQdQ7btpKWn6hNGpLyg	27	https://www.youtube.com/watch?v=2C7lYB7slow	31	68
30 GB 10rb - Paket Internet Murah Telkomsel	13182	98	545	74	0	djRU4I1mHFU	UC7M1uQ8jyaw80a_3LSSsQow	24	https://www.youtube.com/watch?v=djRU4I1mHFU	87	12
Cara Baru Tembak Kuota OMG 5 gb Rp 10.000 + Kuota 1 GB Rp 10 Rupiah	5492	109	130	4	0	vantJjBXuks	UCQncgrC8SUXDBavN4KtUQ0g	26	https://www.youtube.com/watch?v=vantJjBXuks	58	41
