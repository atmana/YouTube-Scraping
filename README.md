Melakukan scraping video trick Internet gratis/murah yang paling update dan memiliki jumlah View yang terbanyak di YouTube. 
Dari informasi text comment pada video, dilakukan analisis secara otomatis berdasarkan model data yang sudah ditraining menggunakan Naive Bayes Classifier, sehingga dapat disimpulkan diawal trick video tersebut working atau tidak.

Script utama yang dirunning untuk manjalankan seluruh fungsi --> Youtube_by_Keyword.py 

Menjalankan fungi untuk sentiment analis dari comment di video --> sentimentYouTube.py

Mengambil text comment dari video --> comment_extract.py

Proses model training untuk menjalankan analisa sentimen dari comment di video --> training_classifier.py

Data set training --> emoji.txt, negative.txt, positive.txt

Hasil model training --> classifier.pickle


Sample Output :

Title	viewCount	commentCount	likeCount	dislikeCount	URL	positive (%)	negative (%)

TELKOMSEL OPOK LANCAR JAYA TERBARU DESEMBER AKTIF SAMPAI 2020	3620	173	34	4	https://www.youtube.com/watch?v=2C7lYB7slow	31	68

Cara Baru Tembak Kuota OMG 5 gb Rp 10.000 + Kuota 1 GB Rp 10 Rupiah	5492	109	130	4	https://www.youtube.com/watch?v=vantJjBXuks	58	41

Paket internet murah Telkomsel	72629	702	1977	129	https://www.youtube.com/watch?v=7hmtK_02ok8	86	14

Paket internet murah Telkomsel 10gb	45140	425	1261	88	https://www.youtube.com/watch?v=NpahSYCJl-g	76	24

Paket internet murah Telkomsel 30gb	26135	744	1202	71	https://www.youtube.com/watch?v=zC1LNq3Nq90	93	7

Paket Internet Telkomsel Murah 10Ribu 10Giga Dan Aktif 30 Hari ðŸ‘‰ OMG âœ“ Terbaru	13610	480	203	18	https://www.youtube.com/watch?v=Aw7qy0f6GHI	50	50
