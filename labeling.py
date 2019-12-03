#@title
from multi_label_pigeon import multi_label_annotate
from IPython.display import display, Image

image_path = "/content/SkripsiGan/Dap/"
annotations = multi_label_annotate(
  [
    '/content/SkripsiGan/Dap/42_3.jpg',
    '/content/SkripsiGan/Dap/43_3.jpg',
    '/content/SkripsiGan/Dap/44_3.jpg',
    '/content/SkripsiGan/Dap/45_3.jpg',
    '/content/SkripsiGan/Dap/46_3.jpg',
    '/content/SkripsiGan/Dap/47_3.jpg',
    '/content/SkripsiGan/Dap/48_3.jpg',
    '/content/SkripsiGan/Dap/49_3.jpg',
    '/content/SkripsiGan/Dap/50_3.jpg',
    '/content/SkripsiGan/Dap/51_3.jpg',
    '/content/SkripsiGan/Dap/52_3.jpg',
    '/content/SkripsiGan/Dap/53_3.jpg',
    '/content/SkripsiGan/Dap/54_3.jpg',
    '/content/SkripsiGan/Dap/55_3.jpg',
    '/content/SkripsiGan/Dap/56_3.jpg',
    '/content/SkripsiGan/Dap/57_3.jpg',
    '/content/SkripsiGan/Dap/58_3.jpg',
    '/content/SkripsiGan/Dap/59_3.jpg',
   '/content/SkripsiGan/Dap/60_3.jpg',
    '/content/SkripsiGan/Dap/61_3.jpg',
    '/content/SkripsiGan/Dap/62_3.jpg',
    '/content/SkripsiGan/Dap/63_3.jpg',
    '/content/SkripsiGan/Dap/64_3.jpg',
    '/content/SkripsiGan/Dap/65_3.jpg',
    '/content/SkripsiGan/Dap/66_3.jpg',
    '/content/SkripsiGan/Dap/67_3.jpg',
    '/content/SkripsiGan/Dap/68_3.jpg',
    '/content/SkripsiGan/Dap/69_3.jpg',
    '/content/SkripsiGan/Dap/70_3.jpg',
    '/content/SkripsiGan/Dap/71_3.jpg',
   '/content/SkripsiGan/Dap/72_3.jpg',
 '/content/SkripsiGan/Dap/73_3.jpg',
    '/content/SkripsiGan/Dap/74_3.jpg',
    '/content/SkripsiGan/Dap/75_3.jpg',
    '/content/SkripsiGan/Dap/76_3.jpg',
    '/content/SkripsiGan/Dap/77_3.jpg',
    '/content/SkripsiGan/Dap/78_3.jpg',
    '/content/SkripsiGan/Dap/79_3.jpg',
    '/content/SkripsiGan/Dap/80_3.jpg',
    '/content/SkripsiGan/Dap/81_3.jpg',
    '/content/SkripsiGan/Dap/82_3.jpg',
    '/content/SkripsiGan/Dap/83_3.jpg',
   '/content/SkripsiGan/Dap/84_3.jpg',      
    '/content/SkripsiGan/Dap/85_3.jpg',
    '/content/SkripsiGan/Dap/86_3.jpg',
    '/content/SkripsiGan/Dap/87_3.jpg',
    '/content/SkripsiGan/Dap/88_3.jpg',
    '/content/SkripsiGan/Dap/89_3.jpg',
    '/content/SkripsiGan/Dap/90_3.jpg',
    '/content/SkripsiGan/Dap/91_3.jpg',
    '/content/SkripsiGan/Dap/92_3.jpg',
    '/content/SkripsiGan/Dap/93_3.jpg',
    '/content/SkripsiGan/Dap/94_3.jpg',
    '/content/SkripsiGan/Dap/95_3.jpg',
   '/content/SkripsiGan/Dap/96_3.jpg', 
  '/content/SkripsiGan/Dap/97_3.jpg',
    '/content/SkripsiGan/Dap/98_3.jpg',
    '/content/SkripsiGan/Dap/99_3.jpg',
   '/content/SkripsiGan/Dap/100_3.jpg', 
   ],
  options={'Lengkap/Tidak':['Lengkap = Kecenderungan ekshibisionis, merasa mampu diterima secara sosial, ketergantungan sosial.','Tidak = Depresif, tidak mengakui kenyataan, tertekan secraa neurotis, kurang dorongan berprestasi'], 
           'sedih/gembira':['Perasaan sedih /tertekan','Bersemangat dan motivasi berprestasi'],
           'lokasi':[
                      'Atas = Kurang kuat pegangan, kurang mantap, berfantasi untuk nampak kuat. Mungkin takabur atau tak mau tahu, mungkin optimis terhadap kerjanya, memandang rendah terhadap orang lain, tendensi kurang yakin akan dirinya.',
                     'tengah = Memiliki adaptasi yang cukup baik, bersifat egosentris, insecure dan rigid, berusaha kontrol secara cermat.',
                     'bawah = 	Perasaan insecure dan tak pasti, berpikir  pada hal-hal konkrit/ berpijak pada realita. Kebutuhan akan kepastian/depresif, kurang usaha, mudah menyerah, di dominasi oleh asadar, kebutuhan keseimbangan, kontrol, menunjukkan keseimbangan, ketenangan kestabilan (secara demonstratif)',
                     'kanan = Kontrol emosionil, berusaha keras untuk sukses, orientasi lingkungan/dunia luar, ekstrofert, orientasi masa yang akan datang',
                     'kananAtas = Negativisme pada diri sendiri, agresif, memberontak.',
                     'kiri = Dikuasai emosi, menekankan masa yang lalu, tendensi impulsif, self oriented, depresif tapi banyak frustasi, introfert, bayak dikendalikan ketaksadaran',
                     'bawahKiri = Dikuasai emosi, menekankan masa lalu, tendensi impulsif, self-oriented, intro-vert, banyak dikendalikan ketidaksa-daran, depresif'
                     ],
          'Garis':[
                  'konsisten = Penyesuaian diri baik',
		              'kabur = Kurang berani tampil dan menyatakan diri, cemas, insecure, ragu, takut, tidak pasti, kontrol yang rigid yang didasari oleh rasa tertekan dan kurang mampu berkarya, depresif, kurang mampu dan kurang gairah, intelektual dan introversive, spirituil',
                  'Tebal = Penuntut, menguasai, menentang keku-asaan, dorongan bermusuhan, yakin diri, anxiety, tegang, kerusakan otak organis, manic',
                  'Tipis = Ada hambatan berhubungan dengan lingkungan, biasa nampak pada tendebsi skizoid',
                  ],
          ' KEPALA':[
                          'TakLengkap = Tendensi hambatan dalam hubungan sosial, neourotis',
                          'Agakbesar = Ada kemungkinan gangguan organis (misalnya, orang sering sakit, kerusakan otak, kemunduran, tendensi hipokondriasis, intelegensi kurang, pikirannya melayang (over) pada paranoid, terlalu membanggakan intelek, penekanan pada fantasi (pada anak-anak) aspirasi intelektuil (mungkin disertai orandiosity), kurang masak dalam instropeksi atau fantasi, simptom-simptom pada kepala',
                          'TerlaluBesar = Tendensi aspirasi lebih besar dari pada kemampuan' ,
                          ],
          ' RAMBUT ':[
                          'Botak = Merasa kurang jantan',
                          'DiUlang2 = Suka menyerang',
                          'RambutWanitaYgTakAdadiPria = Regresi',
                          'PenempatanTepat = Tekanan/ tuntutan kejantanan',
                          'RambutTipis = Kurang jantan / tidak pasti',
                          'RambutMenyolokDanKacau = Sifat kekacauan pada individu',
                          'Gundul/SedikitSekali = Tendensi castrasi kompleks',
                          'RambutGondrong = Erotis protes/ kemungkinan ada konflik',
                          'Jambang/Kumis/rambutLain = Keraguan pada kejantanan sehingga kompensasinya jadi sok jantan ,ketidak pastian seksuil',
                          'RambutPadaRahang = Skizoid',
                          'JenggotKambing = Ingin menunjukkan kejantanan dengan cara tak wajar/ kurang wajar,indikasi artistik, anti sosial, atau ada unsur-unsur skizoid',
                          'Jenggot/JambangDitekankan = Perhatian berlebihan pada kejantanan',
                          ],
		      ' Alis':[
                          'Tebal = Wajar, normal ',
                          'Teratur = Sebagai hiasan, refleksi sikap kritis namun tidak menentang,kecenderungan kehalusan budi pekerti, kesopanan, cenderung menjaga, memelihara',
                          ],	
            ' MATA ':[
                          'MenekankanPupil Mata = Paranoia dan menampakkan fantasi, angan-angan',
                          'matabulatan = Egosentris histeris, tidak masak, egosentris, regresi ',
                          'MatabulatanTerkatup =  Pertautan ide-ide, paranoid ',
                          ' MataTerkatup = Paranoidd',
                          'Mataterlalukecil = Ingin mencampakkan dunia luar (tak acuh), self absorption ',
                          ' Tidakmelihat = Emotional immaturity dan egosentris, kekanak-kanakan, cacat mental tingkat ringan, biasa unutk anak-naak yang masih muda, tergantung,emosi datar, hambatan dalam membedakan sesuatu',
                          'Buta, terutup, tertutup topi,cekung = Tanda keengganann memperhatikan sekitar, mungkin suka bertengakar. Tendensi menolak keadaan yang tidak menyenangkan ,tendensi menyatakan ketidaksenangan ',
                          'Tebal,diberintekanan = Bermusuhan dan mengancam, bersemnagat, indikasi pamer terutama pada gadis, hoimoseksual. Histeris egoistik ',
                          'Tajam,besar, disertai kepala besar = Paranoid, unsur agresif, sadisme, ingin berkuasa besar sekali ',
                          'SetengahTertutup = Introfert, kurang kontak dengan dunia luar, kontak sosila sangat kurang, terlebih bila tidak digambar ',
                          'Mata tanpa variasi = Kekanak-kanakan dalam perasaan Kurang masak (mis:egosentris)  ',
                          'Diberi kacamata = Kompensasi dalam pergaulan karena merasa mau terhadap konflik yang dialami ',
                          ' Mata sipit =  Kepicikan pandangan',
                          'Mata membelalak =  Rangsangan /gairah seksuil ',
                          'Mata juling = Pikiran kacau ',
                          'Lingkaran bola mata besar,tetapi mata kecil = Rasa ingin tau hal dosa, konflik voyourism ',

                          ],                    			 
                          
            ' MULUT/BIBIR ':[
                          'Cekung = Menerima dan membutuhkan ketergan-tungan, pasif',
                          'Melengkung ke atas Psikosomatik pada pernafasan, memak-sakan diri, berpura-pura sebagai kom-pensasi perasan tidak menerima, ten-densi menunjukkan senyum ',
                          'Mulut besar (ditonjolkan) =  Biasa pada anak kecil, regresi, infantilisme (pada dewasa) ',
                          'Mulut tebal dan lurus =  oral agresif, .mengkritik terus dapat dikatakan sadisme ',
                          'Giginya kelihatan = Oral agresif (suka mengkritik) tendensi menyerang secara oral, sinisme ',
                          'Tetawa lebar =  Tendensi orang depresif dengan kompensasi tertawa lebar ',
                          ' Sangat kecil =  Menentang oral dependency, independent',
                          'Mulut tidak digambar/dihilangkan =  Penolakan terhadap kebutuhan afektif, guilty feeling, depresi, kontak verbal yang terganggu(dengan lingkungan) ',
                          ],
          
                          
            ' TELINGA ':[
                          'Penekanan/pembesaran pada telinga = Jika berlebihan mungkin halusinasi pendengaran, tendensi gangguan pengakit telinga, paranoid, skizoid, tuna rungu, ketidaks tabilan rungu,ideas of reference/keingintahuan yang besar, daya kritik kurang, peka terhadap kritik/sikap orang lan kerena neurotik ekstrim, paranoid, tendensi konfik homoseksual pasif ',
                          ' Teliga besar, mulut lurus dan tebal  = Tendensi oposisi terhadap otoritas/atasannya',
                          'Telinga lebar =  Peka terhadap kritik ',
                          'Telinga kabur/tidak jelas =  Kesadaran pribadi goncang, keraguan ',
                          'Telinga digambar akhir = Konflik dengan hubungan manusiawi, mungkin ada kesulitan bicara. Penolakan terhadap kritik ',
                          'Kurang tekanan =  Penolakan terhadap kritik, menolak pendapat orang lain, menghindari halusianasi pendengaran, lebih umum pada orang lanjut usia dari pada orang muda ',
      
                          ],  

            ' DAGU ':[
                          'ditekankan =  Kompensasi ketidak pastian , tak bisa mengambil keputusan takut bertanggung jawab, fantasi',
                          'Melebih-leboiihkan dagu  = Kompensasi dari perasan tak mampu tak dapat mengambil keputusan ',
                          'Perluasan dagu  = Adanya dorongan agresif ',
                          'Tekanan pada dagu (pada ganbar seks lain) =  Ketergantungan pada jenis lain ',
                          'Jakun =  Menunjukkan sifat kejantanan 9tak disadari), wajar pada remaja ',
                         
                          
                          ], 
              ' LEHER ':[
                          'Panjang dan tipis (kurus)  = Kurang mampun mengontrol dorongan , mungkin permusuhan',
                          'Besar dan gemuk  = mungkin rigid, penggabungan impils yang baik ',
                          'Menghilangkan pangkal leher =  Sering membiarkan dorongan-dorongan dengan kobtrol yang tidak cermat ',
                          'Ditutup dengan dasi dan krah  = Melakukan Kontrol intelektual terhadap impuls-impuls atau dorongannya ',
                         
                          ],              
              ' BAHU ':[
                          'Lebar & besar =  Dorongan kekuatan fisik, merasa mampu',
                          'Pundak yang sempit/kecil = Perasaan inferior, kurang mampu mencoba mencari kompensasi ',
                          'Persegi  = Kaku dan bermusuhan, defensif terhadap permusuhan',
                          'Pundak satu sisi tal seimbang = dengan bagian lain Ketidakseimbangan emosi, konflik peran seksualnya ',
                          'Pundak sering dihapus dan diualang =  Kurang yakin pada kemampuan dan perkembanga dirinya ',
                          'Proporsi dan bentuk pundak yang bagus = Lancar , felksibel, seimbang dan merasa mampu ',
                        
                          
                          ],  
              ' LENGAN ':[
                          'Lengan dan tangan yang dihilangkan  = Pandangan tidak pasti, scizoprenic depressi, aktiviyas, rpoduktif, guilty feelings berhubungan dengan permusuhan seksuil',
                          'tidak digambar sama sekali = Gangguan otak yang berhubungan dengan motorik ',
                          'Digambar tidak seuai dengan tangan  = Konflik dalam kontak dengan orang lian, sifat agresi, terlebih bila hal ini terdapat pada anak umur belasan tahun, tendensi psikopat (pada orang dewasa)',
                          'dilipat (sedekap) =  Ambivalensi, usaha nampak kuat, bermusuhan dan seksualitas',
                          'Dilipat di belakang  = Menolak dunia luar karena rasa curiga dan bermusuhan ',
                          'pendek sekali =  Ambisi, kemauan lemah, merasa lemah, loyo ',
                          'yang kecil dan tipis =  Merasa lemah dan sia-sia /tidak berguna ',
                          'seperti sayap =  Lemah, ada hambatan kontak sosial ',
                          'di belakang  = Guilty feeling, ingin menghukum tangan, kebutuhan mengontrol agresi ',
                          'dengan garis tebal =  Perasaan menghukum ',
                          'luas/tebal =  Mengutamakan kekautan , mementingkan otot daripada otak ',
                          'panjang  = Ambisius, usaha untuk sukses, mengharapkan perhatian dan kasih sayang ',
                          'sangat panjang = Ambisi dan mencari kompensasi dari perasaan tidak pasti ',
                          'nampak meraih =  Melaksanakan interaksi sosial ',
                          'Garis yang langsung dan lancar =  Siap berhubungan dengan lingkungan',
                          ' Lengan nampak terulur =  Butuh dorongan emosionil',
                          
                          ],                
              ' TANGAN/JARI ':[
                          ' besar dan luas =  Usaha untuk kuat, ingin memperbaiki hubungan sosial karena merasa tak pasti dan mantap, biasa(nornal)unutk remaja dan orang muda',
                          ' dihilangkan =  Perasaan tidak pasti dalam kontak sosial, perasaan tidak mampu, permusuhan dan seksuil, guilty feeling dari sikap agresif ',
                          ' digambar akhir =  Kesulitan dan ketidak sediaan dalam kontak sosiaL',
                          ' saku/dibelakang =  Menolak atau ketidaksediaan berhubungna dengan sosial. Psikopat, ingin berhubungan sosail tapi merasa kurang mampu, inferior, takut, dll. (pasif). (biasanya ada kombinasi dengan yang ada kancinya)',
                          ' bergaris tebal = Rasa bersalah, masturbasi, curang, merampas ',
                          'dekat genital =  Perhatian pada seksual, guilty feeling seksuil, menolak terhadap rangsangan seksual ',
                          ' jari-jari yang jelas =  Cenderung ke arah paranoid',
                          ' senjata (pisau, dll) = Agresi terhadap/ sebagai penutupan terhadap kelemahan atau kekuarangan terhadap dirinya (biasanya disertai dengan gambar kancing baju yang jelas) ',
                          'Jari yang disertai dengan kuku =  Agresif dalam bentuk motorik, seperti robot, keahlian pekerjaan dengan lemah, pada anak wajar, pada dewasa , kekanak-kanakan ',
                        
                          
                          ],  
              ' TUBUH ':[
                          ' dihilangkan =  Penolakan terhadap impuls fisik, kehilangan kebanggaan fisik, biasa digambar oleh anak-anak',
                          ' sangat kecil = Menghindari dorongan fisik, perasaan inferior, merasa kurangs ehat/kuat ',
                          ' sangat besar(lebar) = Kurang merasakan kepauasan fisik, mencoba menunjukkan kekuatan fisik',
                          ' shading tebal  pada jenis kelamin lain  = Menentang /nermusuhan dengan jenis kelamin lain',
                       
                          
                          ],  
              ' PAHA ':[
                          'Tanpa kaki =  Perasaan tertekan dan tergantung yang bersifat patologis, tidak mampu, perasaan kastrasi, kesulitan dalam menanggapi adanya dorongan seksuil',
                          'Panjang besar = Berusaha mencapai otoritas, ambivalensi ',
                          'Pendek =  Merasa kurang lincah.kurang mampu ',
                          'Terpentang  = Menentang kekuasaan, bersiap sedia.kewaspadaan perasaan tidak aman yang terpendam, kebutuhan untuk mendapatkan keseimbangan ',
                      
                          
                          ],  
              ' KAKI ':[
                          'Gambar kaki secara simbol  = Traumatis, kontrol diri secara impulsif',
                          'Kaki dihilangkan  = Perasan tidak mampu, kurang efektif, sakit-sakitan, tertekan ',
                          'Sangat kecil = Tertekan, kontrol kaku terhadap seksualitas, ketergantungan pada orang lain ',
                          'Sangat besar =  Kebutuhan yang besar akan rasa aman, butuh banyak dorongan ',
                          'Kaki panjang =  Berhubungan dengan seksualitas pria, mengaharapkan kebebasan, depresif ',
                          'Kaki dipentingkan digambar = Permusuhan yang ditekan,atau di kontrol munculnya ',
                          'Kaki  terlalu pendek =  Sifat kepala batu ',
                          'Kaki  memaki sepatu =  Wajar bagi anak kecil, Tendesi infantil (bagi orang dewasa) ',
                          'Kaki belums eslsai =  Vitalitas lemah ',
                          'Ruas kaki jelas =  Skizoid ',
                      
                          
                          ],
              ' PAKAIAN ':[
                          'Digambar  = normal',
                          'Terlalu lengkap =  Narsistis (pemujaan terhadap pakaian) ',
                          'Pakaian minim sekali =  Pemujaan terhadap fisik, introfert, self absorbed, pemujaan terhadap perkembangan fisik, tendensi suka berfantasi di dalam pergaulan sosial, kurang berpastisipasi sosilal ',
                          'Tidak jelas antara berpakaian atau tidak = Kurang mantap pada kekautan fisiknya ',
                          'Ada tambahan ornamen (dasi, alung dlll) =  Kompulsif ',
                      
                          
                          ],
              ' PERHIASAN/ORNAMEN ':[
                          'Perhiasan Ada secara mencolok  = Mencari perhatian, menunjukkan penyesuaian yang bersifat psikopatik (kurang wajar) (bila digambar wanita muda, lebih –lebih bila ditekankan bagian seksuilnya)',
                          'Ada Dasi yang dikenakan  = Sering dihubungkan dengan agresi seksuil yang dimunculkan, kurang masak seksuil ',
                          'Saku pada baju/celana  = Deprifasi afeksi, ketergantungan pada ibu ',
                          'Ikat pinggang Ada Ketergantungan ',
                          'Saku digambar ditekankan Infantil, etrgantung dependent, kikir, suka minta, kehausan kasih sayang dan perlindungan, usaha mengatasi ketergantungan secara jantan, ketergantungan oral, menekan kebebasan sendiri (terutama pada wanita) ',
                          'Kancing  di bawah garis tengah Ketergantungan pada ibu (egosentris) ',
                          'Kancing  sangat jelas, menonjol, ditekankan. = Ketergantungan, tidak masak , tidak pasti',
                          'Kancing  dalam manset =  Sangat teliti, formil ',
                          'Sabuk ditekankan shading kuat =  Kontrol kuat terhadap nafsu ',
                          'Tanpa ikat pinggang = Biasa, mudah menyatakan dorongan, tanpa hambatan, sebaliknya mungkin menyatakan kefleksbelan terhadap kontrolm seksuil ',
                          'Talis sepatu dan baju kusut, detil yang tidak perlu Obsesif kompulsif ',

                      
                          
                          ],                                                    
                           },
  display_fn=lambda filename: display(Image(filename))
)