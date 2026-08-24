TrollLens
Marka İtibarına Yönelik Koordineli Sahte Etkileşimlerin Davranışsal Tespiti

1. Literatür Taramasının Hazırlanması (Preparing Your Literature Review)

1. Giriş (Introduction)
Bu projenin odaklandığı temel pazarlama problemi "Marka Kimliği ve İtibar Sorunları (Brand Identity & Reputation Issues)" olarak belirlenmiştir. Sosyal medyada markalara yönelik yürütülen koordineli sahte hesap saldırıları ve haksız karalama kampanyaları (astroturfing), tüketicilerin marka güvenini zedelemekte ve markalar için sahte itibar krizlerine yol açmaktadır. Projemizin hedef kitlesi, sosyal medyadaki itibarlarını korumak isteyen markalar ile kriz yönetimi yürüten halkla ilişkiler (PR) ajanslarıdır. Bu bağlamda, temel proje sorumuz şudur: "Markalara saldıran koordineli bot ağları, değişken içeriklerden ziyade davranışsal imzaları (etkileşim ritimleri) üzerinden dilden bağımsız olarak nasıl tespit edilebilir?". Bu soruyu yanıtlamak ve B2B bir Pazarlama Teknolojisi (MarTech) çözümü geliştirmek için mevcut bot tespiti ve duygu analizi çalışmalarının sınırlarını literatür üzerinden incelemek büyük bir zorunluluktur.

2. Organizasyon (Organization)
Literatür taramamız, pazarlama problemimizi en iyi şekilde desteklemek amacıyla tematik olarak organize edilmiştir. İncelediğimiz ana temalar şu şekildedir:

* Temel Kavramlar: Sosyal medyada astroturfing (sahte kamuoyu oluşturma) ve bu durumun marka itibarı (brand reputation) üzerindeki etkileri. 

* Mevcut Yöntemler: Klasik duygu analizi (sentiment analysis) ve içerik filtreleme teknolojilerinin marka krizlerindeki yetersizlikleri. 

* Gelişmiş Teknolojiler: Davranışsal zaman serileri ve Çizge Sinir Ağları (Graph Neural Networks - GNN) ile ağ analizi tabanlı bot tespiti. 

3. Özet ve Sentez (Summary and Synthesis)
Literatürdeki çalışmalar, botların marka imajına olan yıkıcı etkilerini ve sahte müşteri kampanyalarının yapısal özelliklerini ele almaktadır. Örneğin, "Astroturfing Detection on Social Media" ve "Brand Reputation in the Age of Bots" gibi odak çalışmalar, bot ağlarının müşteri güvenini yapay bir şekilde nasıl manipüle ettiğini ortaya koymaktadır. Mevcut pazarlama teknolojisi literatürü incelendiğinde, geleneksel araçların çoğunlukla metin madenciliğine ve belirli anahtar kelimelere dayandığı görülmektedir. Ancak bu çalışmalar sentezlendiğinde; saldırganların aynı anda binlerce tweet atması veya eşzamanlı retweet yapması gibi "nasıl hareket ettiklerine" odaklanan davranışsal ritimlerin, sahte hesapları saptamada içerik analizinden çok daha güçlü bir yöntem olduğu anlaşılmaktadır.

4. Pazarlama Uygunluğu ve Boşluk (Marketing Relevance and Gap)
Meltwater veya Mention gibi mevcut duygu analizi araçları, markaya yönelik gelen tepkileri ölçmede sektörde yaygın olarak kullanılmaktadır. Ancak literatürde ve MarTech sektöründe çözülememiş en büyük boşluk, bu araçların gelen kitlesel tepkinin "organik bir müşteri şikayeti mi" yoksa "koordineli bir bot saldırısı mı" olduğunu ayırt edememesidir. İçerik filtreleme ve kelime bazlı yapay zeka yaklaşımları yetersizdir; çünkü anahtar kelimeler her markaya ve her yeni krize göre sürekli değişmektedir. Geliştirdiğimiz TrollLens projesi, ağlar arası ilişkiyi GNN (Çizge Sinir Ağları) modelleriyle çözerek ve botların "davranışsal proxy'sine" (ritim ve zamanlama) odaklanarak pazardaki bu teknolojik boşluğu doldurmaktadır.

5. Sonuç (Conclusion)
Literatürden elde edilen temel çıkarım, markaların koordineli sahte krizlerden korunması için içerik (ne söylendiği) analizinden ziyade yapısal ağ (nasıl söylendiği) analizine geçilmesi gerektiğidir. Bu durum, proje tasarımımızda derin öğrenme (GNN) ve davranışsal zaman serilerini kullanmamızı doğrudan şekillendirmektedir. Canlı kurumsal saldırı verisi toplamak zor ve maliyetli olduğundan, mevcut "Bilgi Operasyonları (Information Operations)" veri setleri, çalışma ritimlerinin benzerliği teziyle modelimiz için bir simülasyon (proxy) verisi olarak kullanılacaktır. TrollLens'in önereceği bu dilden bağımsız teknoloji; markaların gereksiz PR harcamalarını önlemesine, kriz yönetimini doğru verilerle yapmasına ve ölçülebilir marka güvenini (brand equity) korumasına doğrudan katkı sağlayacaktır.


6. Uygun Alıntılar (Proper Citations) Bu literatür taramasında, TrollLens projesinin temelini oluşturan marka itibarı sorunları, koordineli sahte etkileşimlerin (astroturfing) tespiti ve klasik duygu analizi yerine Çizge Sinir Ağları (GNN) kullanılarak davranışsal analiz yapılması yaklaşımlarını desteklemek amacıyla aşağıdaki akademik çalışmalardan faydalanılmıştır:
1. Rust, R. T., Rand, W., Huang, M. H., Stephen, A. T., Brooks, G., & Chabuk, T. (2021). Real-Time Brand Reputation Tracking Using Social Media. Journal of Marketing. (Bu çalışma, geleneksel metin madenciliğinin ve AI araçlarının marka itibarını ölçmedeki kullanımını ve mevcut sınırlarını anlamak için referans alınmıştır.)
2. Luceri, L., Salkar, T. V., Balasubramanian, A., Pinto, G., Sun, C., & Ferrara, E. (2026). Coordinated Inauthentic Behavior on TikTok: Challenges and Opportunities for Detection in a Video-First Ecosystem. Proceedings of the International AAAI Conference on Web and Social Media, 20(1), 1533-1550. (Sosyal medyada koordineli inotantik davranışların (CIB), içerikten bağımsız olarak senkronize paylaşımlar ve tekrarlanan davranışsal imzalar üzerinden nasıl tespit edilebileceğinin temellerini sağlar.)
3. Dang, Q.-V., Nguyen, P.-L., Le, D., & Dinh, M. N. (2026). XHBot: eXplainable Heterophily-aware Graph Neural Networks for Social Bot Detection. EAI Endorsed Transactions on AI and Robotics. (TrollLens'in temel yapay zeka yaklaşımı olan Çizge Sinir Ağları'nın (GNN) bot ağlarının tespit edilmekten kaçınma stratejilerini (davranışsal ritim ve ağ topolojisi) çözmedeki başarısını destekler.)
4. Elmas, T., Overdorf, R., Özkalay, A. F., & Aberer, K. (2021). Ephemeral Astroturfing Attacks: The Case of Fake Twitter Trends. 6th IEEE European Symposium on Security and Privacy (EuroS&P). (Koordineli sahte hesap ağlarının oluşturduğu geçici ama yıkıcı karalama ve manipülasyon kampanyalarının yapısını anlamak için kullanılmıştır.)



AI in Marketing Capstone — Bölüm 2: Veri Araştırması ve Bölüm 3: Teknoloji İncelemesi

2. Veri Araştırmasının Hazırlanması (Preparing Your Data Research)

2.1. Giriş (Introduction)

Bu projenin pazarlama hedefi, markaların sosyal medyada karşılaştığı olumsuz etkileşim dalgalarının organik müşteri tepkisi mi yoksa koordineli bir sahte hesap saldırısı mı olduğunu ayırt etmektir. Bu ayrımın doğru yapılması, kriz yönetimi kararlarının maliyetini doğrudan etkilemektedir: organik bir memnuniyetsizlik ürün veya hizmet düzeltmesi gerektirirken, koordineli bir astroturfing saldırısı platform bildirimi ve iletişim stratejisi gerektirmektedir. Yanlış teşhis, her iki yönde de kaynak israfına yol açmaktadır.

Bu hedefi ölçülebilir kılmak için belirlediğimiz temel performans göstergeleri (KPI) şunlardır: (i) koordineli kampanya tespitinde F1 skoru ve yanlış pozitif oranı, (ii) gerçek müşteri şikâyetlerinin yanlışlıkla bot olarak etiketlenme oranı (marka açısından en maliyetli hata türü), (iii) kriz tespit gecikmesi (saldırının başlangıcı ile uyarının üretilmesi arasındaki süre), ve (iv) marka etrafındaki konuşma hacminin ne kadarının inorganik olduğunu gösteren "kirlenmiş ses payı" (contaminated share of voice) oranı.

Bu göstergeleri hesaplayabilmek için ihtiyaç duyulan veri, metin içeriğinden ziyade hesaplar arası etkileşim ağı ve hesapların zamansal davranış örüntüleridir. Dolayısıyla aranan veri setinin üç özelliği taşıması gerekmektedir: hesap düzeyinde etkileşim grafiği (retweet, yanıt, alıntı), zaman damgalı aktivite kayıtları ve güvenilir bir "koordineli / organik" etiketi.

2.2. Veri Kaynağı ve Kapsamı (Data Source and Scope)

Projede üç kamuya açık (üçüncü taraf) veri seti kullanılacaktır. Birinci taraf marka verisine erişimimiz bulunmadığından, tüm veriler açık akademik kaynaklardan sağlanmaktadır. Bu durum hem bir kısıt hem de bir avantajdır: kısıttır, çünkü gerçek kurumsal saldırı verisi içermez; avantajdır, çünkü etiket kalitesi akademik olarak doğrulanmıştır ve tekrarlanabilirlik sağlar.

Birincil veri seti: LEN (Large Engagement Networks)
LEN, projemizin problemini birebir yansıtan tek veri setidir. Yazarlar, koordineli kampanyalar ile organik gündemleri ayırt etmek için bir sınıflandırma ölçütü oluşturmuş ve 179 kampanya ile 135 kampanya olmayan (organik) trendin etkileşim ağlarını yayınlamıştır. Ağlar kullanıcıları düğüm, retweet/yanıt/alıntı etkileşimlerini kenar olarak modellemektedir; ortalama bir grafik yaklaşık 11.000 düğüm ve 23.000 kenar içermektedir. Ayrıca kampanya ve kampanya olmayan türleri karakterize eden ince taneli etiketler de sunulmaktadır.

Pazarlama karşılığı: "Markam hakkında yükselen bu gündem organik bir müşteri tepkisi mi, yoksa merkezi olarak yönetilen bir kampanya mı?" sorusu, LEN'in çözmeye çalıştığı sınıflandırma probleminin doğrudan ticari karşılığıdır. Format: grafik (graph) veri seti. Erişim: kamuya açık.

İkincil veri seti: Ephemeral Astroturfing / "astrobots"
Elmas ve arkadaşlarının çalışması, Türk trendlerini hedef alan 212.000'den fazla botu tespit edip açık şekilde yayınlamıştır. Bu botlar koordineli biçimde tweet atıp kısa süre içinde silerek trend listesini manipüle etmektedir; bu davranış örüntüsü, botların güvenilir biçimde toplu olarak etiketlenmesini mümkün kılmakta ve veri setini bot araştırmaları için elverişli bir referans kaynağı hâline getirmektedir. Veri, ek açıklamalar ve kod ile birlikte açık bir depoda paylaşılmaktadır.

Bu veri setinin projemiz için kritik önemi: Buradaki manipülasyon siyasi değil, doğrudan ticaridir. İlgili çalışma, bu hizmeti sunan yapıların kendilerini sosyal medya ajansı olarak tanıttığını ve trend hizmetlerinin basit bir arama ile bulunabildiğini ortaya koymaktadır. Yani "bir markayı hedef alan ücretli koordineli kampanya" senaryosu varsayımsal bir tehdit değil, halihazırda işleyen bir pazardır. Bu, projemizin pazarlama gerekçesini akademik bir kaynağa dayandırmamızı sağlamaktadır.

Üçüncül veri seti: TwiBot-22
TwiBot-22, hesap düzeyinde bot tespiti için bugüne kadarki en büyük grafik tabanlı kıyaslama veri setidir; Twitter ağındaki çeşitlendirilmiş varlık ve ilişki türlerini sunmakta ve önceki veri setlerine kıyasla belirgin biçimde daha iyi etiket kalitesine sahiptir. Yazarlar 35 temsili bot tespit yöntemini yeniden uygulayarak dokuz veri seti üzerinde değerlendirmiştir. Bu veri seti projede kendi modelimizi kabul görmüş temel yöntemlerle kıyaslamak için kullanılacaktır.

Lisans uyarısı: TwiBot-22 veri seti CC BY-NC-ND 4.0 lisansı ile dağıtılmaktadır; değerlendirme çerçevesinin kodu MIT lisanslıdır. ND (türev üretilemez) koşulu, veri setini dönüştürüp yeniden dağıtmamızı engellemektedir — bu nedenle TwiBot-22 yalnızca kıyaslama amacıyla, yerel olarak kullanılacaktır.

Veri seti karşılaştırması
Veri seti
Birim
Ölçek
Etiket
Projedeki rolü
LEN
Kampanya / trend ağı
179 kampanya + 135 organik; ort. ~11.000 düğüm, ~23.000 kenar
Kampanya / organik
Ana eğitim ve değerlendirme seti
Astrobots (Ephemeral Astroturfing)
Hesap
212.000+ bot
Bot (kural tabanlı, yüksek güven)
Davranışsal öznitelik tasarımı; ticari astroturfing kanıtı
TwiBot-22
Hesap
Grafik tabanlı en büyük kıyaslama seti
Bot / insan (zayıf denetimli)
Temel yöntemlerle kıyaslama
 

2.3. Veri Kalitesi, Gizlilik ve Sınırlılıklar (Data Quality, Privacy, and Limitations)

Vekil (proxy) veri riski — en önemli sınırlılık
Projemizin en kritik metodolojik açığı şudur: elimizdeki hiçbir veri seti doğrudan bir markaya yönelik saldırı verisi içermemektedir. Tezimiz, bir markayı hedef alan koordineli ağ ile bir gündemi manipüle eden koordineli ağın davranışsal imzasının benzer olduğu yönündedir. Bu makul bir varsayımdır, ancak bu projede doğrulanmamış bir varsayımdır. Bu nedenle projenin çıktısı "markalara yönelik saldırıları tespit eden kanıtlanmış bir sistem" değil, "koordinasyon tespiti yönteminin marka koruma bağlamına aktarılabilirliğine dair bir fizibilite çalışması" olarak sunulmalıdır. Bu sınırın açıkça belirtilmesi, çalışmanın bilimsel dürüstlüğü açısından zorunludur.

Etiket üretiminden kaynaklanan döngüsellik riski
LEN'in referans etiketleri, geçici astroturfing saldırılarının kural tabanlı tespiti üzerinden üretilmiştir. Bu, etiketlerin güvenilirliğini artırırken bir risk de doğurmaktadır: modelimiz gerçek koordinasyon örüntüsünü değil, etiketi üreten kuralın izini öğrenebilir. Bu riski azaltmak için değerlendirme, farklı bir kaynaktan gelen organik trendlerle çapraz kontrol edilmelidir.

Diğer veri kalitesi sorunları
• Sınıf dengesi: LEN'de 179'a 135'lik dağılım kabul edilebilir düzeydedir. Buna karşılık astrobots veri setinde karşılaştırma için organik bir kontrol grubu bulunmamaktadır; bu grubun ayrıca oluşturulması gerekmektedir.
• Silinen içerik sorunu: Geçici astroturfing saldırılarında tweetler kısa süre içinde silindiğinden, bu içerikler geriye dönük anahtar kelime sorgularıyla toplanamamaktadır. Bu, veri toplamanın gerçek zamanlı yapılmasını zorunlu kılan yapısal bir kısıttır ve bizim gibi arşiv verisiyle çalışan ekipler için kapsam kaybı anlamına gelir.
• Tazelik (freshness): Veri setleri 2019–2025 aralığını kapsamaktadır. Manipülasyon taktikleri hızla evrildiğinden, güncel saldırı biçimleri bu verilerde temsil edilmiyor olabilir.
• Erişim kısıtı: X platformunun akademik araştırma API'si 2023 başında kapatılmıştır. Yeni veri toplama seçeneği pratikte bulunmadığından proje tamamen mevcut arşivlere bağımlıdır.
• Ölçek: LEN grafikleri geleneksel grafik sınıflandırma veri setlerinden belirgin biçimde büyüktür; bu, bellek ve hesaplama kaynağı planlamasını zorunlu kılar.
Gizlilik ve sorumlu kullanım
Veri setleri gerçek kullanıcı hesaplarına ait etkileşim kayıtları içermektedir. Bu nedenle: (i) analizler hesap düzeyinde değil, ağ örüntüsü düzeyinde raporlanacak, tekil kullanıcı kimlikleri yayımlanmayacaktır; (ii) KVKK ve GDPR kapsamında kişisel veri işleme ilkelerine uyulacak, veriler yalnızca akademik amaçla ve yerel ortamda saklanacaktır; (iii) veri setlerinin kendi lisans koşullarına (özellikle TwiBot-22'nin ND koşuluna) uyulacaktır; (iv) sistemin çıktısı hiçbir koşulda bir kullanıcıyı suçlayan nihai bir karar olarak değil, insan incelemesine sunulan bir aday listesi olarak konumlandırılacaktır.

Ticari bağlamda ek risk: Bir marka koruma aracının gerçek müşterileri "bot" olarak etiketlemesi, markanın kendisi için itibar riski doğurur. Bu nedenle projede yanlış pozitif oranı, genel doğruluktan daha öncelikli bir başarı ölçütü olarak ele alınmaktadır.

2.4. Keşifsel Analiz ve Pazarlama İçgörüleri (Exploratory Analysis and Marketing Insights)

Not: Bu bölümde sunulan analizler, veri setleri indirilip işlendikten sonra hesaplanacak betimleyici istatistikleri kapsamaktadır. Aşağıda planlanan analiz çerçevesi ve literatürün bu veri setleri hakkında halihazırda raporladığı bulgular yer almaktadır.

Literatürden gelen ilk bulgu: problem çözülmüş değil
LEN yazarları, güncel GNN yöntemlerinin kampanya / kampanya-olmayan ayrımında ve kampanya türü sınıflandırmasında yalnızca orta düzeyde sonuç verdiğini raporlamaktadır. Bu, projemiz açısından iki anlam taşımaktadır. Birincisi, seçtiğimiz problem çözülmüş bir problem değildir; ikincisi, mevcut yöntemleri doğrudan uygulamak yeterli olmayacak, model tasarımında koordinasyona özgü uyarlamalar gerekecektir. Pazarlama açısından bu bulgu, MarTech pazarındaki boşluğun teknik olarak da doğrulandığı anlamına gelmektedir: sorun yalnızca ürünleştirilmemiş değil, henüz tam olarak çözülmemiştir.

Hesaplanacak betimleyici istatistikler
1. Ağ yapısı: düğüm/kenar sayısı dağılımı, ortalama derece, yoğunluk, kümelenme katsayısı, bağlı bileşen sayısı — kampanya ve organik gruplar için ayrı ayrı.
2. Zamansal örüntü: etkileşimlerin saatlik dağılımı, en yoğun dakikadaki etkileşim yoğunluğu, koordinasyon penceresi genişliği (aynı içeriği paylaşan hesaplar arasındaki ortalama zaman farkı).
3. Hesap özellikleri: hesap yaşı dağılımı, takipçi/takip oranı, paylaşım sıklığı, hesap oluşturma tarihlerindeki yığılmalar.
4. Sınıf ayırt ediciliği: yukarıdaki özniteliklerin kampanya ve organik gruplar arasındaki dağılım farkları (etki büyüklüğü ile birlikte).
Beklenen örüntüler ve pazarlama metriklerine bağlanması
Veriden beklenen sinyal
Pazarlama karşılığı
Etkilenen KPI
Kısa pencerede eşzamanlı etkileşim yoğunluğu
Ani ve doğal olmayan bir kriz sinyali
Kriz tespit gecikmesi
Yüksek ağ yoğunluğu, düşük çeşitlilik
Konuşma az sayıda kaynaktan besleniyor
Kirlenmiş ses payı
Hesap oluşturma tarihlerinde yığılma
Amaca yönelik oluşturulmuş hesap ağı
Yanlış pozitif oranı (ayırt edici öznitelik)
Organik trendlerde geniş, seyrek ağ yapısı
Gerçek müşteri memnuniyetsizliği
Ürün/hizmet aksiyonu kararı
 

Bu bağlantı, projenin pazarlama değerinin somutlaştığı noktadır: aynı hacimdeki olumsuz konuşma, ağ yapısına göre tamamen farklı bir yönetimsel karar gerektirmektedir. Mevcut duygu analizi araçları bu iki durumu aynı sinyal olarak raporlamakta, dolayısıyla marka yöneticisini yanlış yönlendirebilmektedir.

2.5. Sonuç (Conclusion)

Seçilen veri setleri, projenin bir sonraki aşaması için uygundur. LEN doğrudan hedeflediğimiz sınıflandırma problemini, açık etiketlerle ve grafik formatında sunmaktadır; astrobots veri seti davranışsal öznitelik tasarımı için zengin bir kaynak ve aynı zamanda ticari astroturfing pazarının varlığına dair akademik kanıt sağlamaktadır; TwiBot-22 ise sonuçlarımızı kabul görmüş temel yöntemlerle karşılaştırma imkânı vermektedir.

Bununla birlikte, verinin en önemli sınırlılığı açıkça kabul edilmelidir: hiçbir veri seti doğrudan marka saldırısı verisi değildir ve bu nedenle proje, yöntemin marka koruma bağlamına aktarılabilirliğine dair bir fizibilite çalışması niteliğindedir. Bu sınırlılık, projenin geçerliliğini ortadan kaldırmamakta, ancak sonuçların yorumlanma biçimini belirlemektedir. Verinin grafik yapısı ve zamansal zenginliği, planlanan grafik tabanlı derin öğrenme yaklaşımını desteklemektedir.

2.6. Kaynaklar (Proper Citations)

Gopalakrishnan, A. A., Hossain, J., Elmas, T., & Sarıyüce, A. E. (2025). Large Engagement Networks for Classifying Coordinated Campaigns and Organic Twitter Trends. Proceedings of the International AAAI Conference on Web and Social Media (ICWSM). arXiv:2503.00599

Elmas, T., Overdorf, R., Özkalay, A. F., & Aberer, K. (2021). Ephemeral Astroturfing Attacks: The Case of Fake Twitter Trends. 2021 IEEE European Symposium on Security and Privacy (EuroS&P), 403–422.

Elmas, T. (2023). Analyzing Activity and Suspension Patterns of Twitter Bots Attacking Turkish Twitter Trends by a Longitudinal Dataset. Companion Proceedings of the ACM Web Conference 2023 (WWW '23 Companion). https://doi.org/10.1145/3543873.3587650

Feng, S., Tan, Z., Wan, H., Wang, N., Chen, Z., Zhang, B., Zheng, Q., Zhang, W., Lei, Z., Yang, S., Feng, X., Zhang, Q., Wang, H., Liu, Y., Bai, Y., Wang, H., Cai, Z., Wang, Y., Zheng, L., Ma, Z., Li, J., & Luo, M. (2022). TwiBot-22: Towards Graph-Based Twitter Bot Detection. Advances in Neural Information Processing Systems 35 (NeurIPS 2022), Datasets and Benchmarks Track.

Ephemeral Astroturfing & Fake Trends Bots veri deposu: https://github.com/tugrulz/EphemeralAstroturfing

TwiBot-22 kıyaslama çerçevesi: https://twibot22.github.io/

 
3. Teknoloji İncelemesinin Hazırlanması (Preparing Your Technology Review)

3.1. Giriş (Introduction)

Bu bölümde, TrollLens projesinin teknik temelini oluşturacak yaklaşım olan Çizge Sinir Ağları (Graph Neural Networks, GNN) ile bunların alternatifleri değerlendirilmektedir. İnceleme, dört teknoloji ailesini kapsamaktadır: sözlük ve kural tabanlı duygu analizi araçları, öznitelik tabanlı klasik makine öğrenmesi, metin tabanlı dönüştürücü (transformer) modeller ve grafik tabanlı derin öğrenme.

Teknoloji incelemesinin bu proje için özel bir önemi vardır: pazarlama ekiplerinin kullandığı sosyal dinleme araçları hâlihazırda mevcuttur ve yaygındır. Dolayısıyla soru "bir teknoloji seçmek" değil, "mevcut araçların yapamadığı işi hangi teknolojinin yapabileceğini" belirlemektir. Ayrıca seçilecek teknolojinin yalnızca teknik olarak başarılı değil, bir marka iletişim ekibinin günlük iş akışına entegre edilebilir ve kararları gerekçelendirilebilir olması gerekmektedir.

3.2. Teknoloji Genel Bakış (Technology Overview)

Duygu analizi ve sosyal dinleme platformları
Meltwater, Brandwatch ve benzeri platformlar marka etrafındaki konuşmayı toplayarak hacim, duygu tonu ve erişim metrikleri üretmektedir. Akademik literatürde de bu yaklaşımın olgunlaştığı görülmektedir: Rust ve arkadaşları, sosyal medya yorumlarının yapay zekâ tabanlı metin analiziyle işlenerek marka itibarının gerçek zamanlı izlenebileceğini göstermiş ve bu ölçümü müşteri değeri bileşenleriyle ilişkilendirmiştir. Bu teknolojiler ne söylendiğini ölçmekte başarılıdır.

Öznitelik tabanlı klasik makine öğrenmesi
Hesap yaşı, takipçi oranı, paylaşım sıklığı gibi el yapımı öznitelikler üzerinde çalışan rastgele orman ve gradyan artırma modelleri, bot tespitinde uzun süredir kullanılmaktadır. Hızlı, ucuz ve yorumlanabilir olmaları en büyük avantajlarıdır.

Grafik tabanlı derin öğrenme (GNN)
GNN'ler, hesapları düğüm ve etkileşimleri kenar olarak modelleyerek bir hesabın kendi özelliklerini değil, ağ içindeki konumunu öğrenmektedir. TwiBot-22 kıyaslama çalışması, bu yaklaşımın üstünlüğünü nicel olarak ortaya koymaktadır: grafik tabanlı yaklaşımlar genel olarak öznitelik veya metin tabanlı yöntemlerden daha etkilidir ve TwiBot-20 ile TwiBot-22 üzerindeki ilk beş modelin tamamı grafik tabanlıdır. Bu ilk beş model, tüm temel yöntemlerin ortalamasını TwiBot-20'de %13,8 ve TwiBot-22'de %8,2 oranında geçmektedir.

Koordinasyon tespiti yaklaşımları
Bot tespitinden ayrı bir literatür kolu, tekil hesapların otomatik olup olmadığından bağımsız olarak hesap gruplarının eşgüdümlü hareket edip etmediğine odaklanmaktadır. Luceri ve arkadaşları, koordineli sahte davranış tespitinin çevrimiçi etki operasyonları çalışmalarının merkezinde yer aldığını belirtmekte ve TikTok gibi video öncelikli platformlar için ağ tabanlı bir çerçeve geliştirmektedir. Bu ayrım projemiz için önemlidir: markaya saldıran hesaplar teknik olarak bot olmayabilir; gerçek insanlar tarafından yönetilen ancak eşgüdümlü hareket eden hesaplar da olabilir.

Açıklanabilirlik katmanı
GNN kararlarının gerekçelendirilmesi ayrı bir araştırma alanıdır. Bu alandaki güncel bir örnek olan XHBot, kamufle olmuş botların iyi niyetli kullanıcıları takip ederek tespitten kaçtığını ve bunun standart GNN toplayıcılarının performansını düşüren yapısal bir heterofili yarattığını belirtmekte; buna karşılık platform moderasyonu için şeffaf, çok düzeyli adli kanıt üreten bir çerçeve önermektedir. Bu, ticari bir üründe zorunlu olan "neden işaretlendi?" sorusunun cevabını sağlamaktadır.

3.3. Pazarlama Projesine İlgisi (Relevance to Your Marketing Project)

Seçilecek teknoloji, marka iletişim iş akışında mevcut sosyal dinleme katmanının hemen ardına, karar katmanının hemen öncesine yerleşmektedir:

Sosyal dinleme (mevcut araçlar) → Olumsuz hacim artışı tespiti → TrollLens koordinasyon filtresi → Kriz müdahale kararı

Bu konumlandırma iki nedenle önemlidir. Birincisi, TrollLens mevcut araçların yerini almamakta, onların çıktısını zenginleştirmektedir; bu, satış açısından entegrasyon direncini düşürmektedir. İkincisi, çıktı doğrudan bir yönetimsel karara bağlanmaktadır: koordineli saldırı tespit edilirse platform bildirimi ve kontrollü iletişim; organik memnuniyetsizlik tespit edilirse ürün veya hizmet düzeltmesi. Etkilenen KPI'lar kriz tespit gecikmesi, gereksiz PR harcaması ve yanlış teşhis oranıdır.

3.4. Karşılaştırma ve Değerlendirme (Comparison and Evaluation)

Değerlendirme ölçütleri, yalnızca teknik başarıyı değil pazarlama iş akışındaki uygulanabilirliği de içerecek şekilde seçilmiştir.

Ölçüt
Duygu analizi araçları
Klasik ML (öznitelik)
Metin tabanlı transformer
GNN (seçilen)
Koordinasyon tespiti
Yapamaz
Sınırlı
Sınırlı
Güçlü
Dil bağımsızlığı
Düşük
Yüksek
Düşük
Yüksek
Veri ihtiyacı
Düşük
Düşük
Orta
Yüksek (ağ verisi)
Yorumlanabilirlik
Yüksek
Yüksek
Düşük
Orta (ek katman gerekir)
Hesaplama maliyeti
Düşük
Düşük
Orta
Yüksek
Gecikme (gerçek zamanlılık)
Düşük
Düşük
Orta
Yüksek
Entegrasyon eforu
Hazır ürün
Düşük
Orta
Yüksek
Yeni taktiklere dayanıklılık
Düşük
Orta
Düşük
Yüksek
 

Tablo, GNN'in her ölçütte üstün olmadığını göstermektedir; hesaplama maliyeti, gecikme ve entegrasyon eforu açısından açıkça dezavantajlıdır. Seçimin gerekçesi tek bir satırda yatmaktadır: koordinasyon tespiti. Diğer üç teknoloji ailesi bu işi yapısal olarak yapamamaktadır, çünkü sinyal tekil hesabın özelliğinde değil hesaplar arasındaki ilişkidedir.

Ayrıca hibrit bir mimari benimsenmektedir: yorumlanabilir ve ucuz bir öznitelik tabanlı model (gradyan artırma) ilk eleme katmanı olarak çalışacak, yalnızca şüpheli görülen vakalar maliyetli GNN katmanına iletilecektir. Bu, gecikme ve maliyet dezavantajını pratikte önemli ölçüde azaltmaktadır.

Yine de gerçekçi olmak gerekmektedir: LEN yazarları, güncel GNN yöntemlerinin bu spesifik görevde yalnızca orta düzeyde sonuç verdiğini raporlamaktadır. Yani seçilen teknoloji doğru yöndedir ancak hazır bir çözüm değildir; ölçeklenebilirlik de ayrı bir kısıttır, zira bazı yöntemler daha küçük veri setlerinde iyi çalışırken TwiBot-22 ölçeğinde bellek kısıtları nedeniyle uygulanamamaktadır.

3.5. Kullanım Örnekleri (Use Cases and Examples)

5. Platform moderasyonu. Sosyal medya platformları koordineli hesap ağlarını tespit edip kaldırmaktadır. Öğrenilecek ders: tespit teknolojisi çalışmaktadır, ancak platform ölçeğinde ve platformun kendi takvimine göre işlemektedir — markalar bu sürecin sonucunu beklemek zorunda kalmaktadır. TrollLens'in ticari gerekçesi tam olarak bu gecikmedir.
6. Video öncelikli platformlarda koordinasyon tespiti. Luceri ve arkadaşları, metin merkezli platformlar için geliştirilen yöntemlerin TikTok'a uyarlanabildiğini göstermiştir. Öğrenilecek ders: davranışsal koordinasyon sinyali platformdan ve içerik biçiminden büyük ölçüde bağımsızdır — bu, projemizin dilden bağımsızlık iddiasını destekleyen en güçlü ampirik dayanaktır.
7. Ticari trend manipülasyonu hizmetleri. Türkiye'deki sahte trend saldırılarını inceleyen çalışma, bu hizmeti sunan yapıların kendilerini sosyal medya ajansı olarak tanıttığını ortaya koymaktadır. Öğrenilecek ders: hedef pazar teorik değildir; saldırı tarafı zaten ticarileşmiştir, savunma tarafı ise henüz ürünleşmemiştir.
8. Gerçek zamanlı marka itibarı izleme. Rust ve arkadaşlarının çalışması, sosyal medya verisinden marka itibarının izlenebileceğini ve bunun firmanın finansal değeriyle ilişkilendirilebileceğini göstermiştir. Öğrenilecek ders: itibar ölçümü marka değerine bağlanabildiği için, bu ölçümü kirleten sahte sinyalin ayıklanması da doğrudan finansal bir değer önermesidir.
3.6. Sınırlılıklar, Riskler ve Fırsatlar (Limitations, Risks, and Opportunities)

Riskler
• Yanlış pozitif — en kritik risk. Gerçek bir müşterinin bot olarak etiketlenmesi ve buna göre işlem yapılması, markanın kendisi için bir itibar krizine dönüşebilir. Bu nedenle sistem otomatik aksiyon almamalı, yalnızca insan incelemesine öneri sunmalıdır.
• Kamuflaj ve düşman uyumu. Modern botlar iyi niyetli kullanıcıları takip ederek tespitten kaçmakta ve standart GNN toplayıcılarının performansını düşüren yapısal heterofili yaratmaktadır. Saldırganlar savunmaya uyum sağlamaktadır; bu, tek seferlik değil sürekli güncellenen bir model gerektirir.
• Platform bağımlılığı. X'in araştırma API'sini kapatması, bu alandaki tüm çalışmaların veri erişimini kırılgan hâle getirmiştir. Ticari bir ürün için bu, tek bir tedarikçiye bağımlılık riskidir.
• Kötüye kullanım. Koordinasyon tespit eden bir aracın, meşru tüketici hareketlerini veya organize boykotları bastırmak için kullanılması mümkündür. Bu, teknik değil yönetişimsel bir risktir ve ürün tasarımında kullanım koşullarıyla sınırlandırılmalıdır.
• Ölçeklenebilirlik. Bazı yöntemler küçük veri setlerinde başarılıyken büyük ölçekte bellek kısıtları nedeniyle uygulanamamaktadır.
Fırsatlar
• Açıklanabilirlik bir farklılaştırıcıdır. Kararın gerekçesini gösteren çok düzeyli kanıt üretimi, hem kurumsal alıcının denetim ihtiyacını karşılamakta hem de ürünü rakiplerden ayırmaktadır.
• İnsan gözetimli tasarım. Sistemin nihai karar verici değil karar destek aracı olarak konumlanması, hem etik riski hem de yanlış pozitif maliyetini düşürmektedir.
• Dil bağımsızlığı ölçeklenme avantajıdır. Davranışsal sinyale dayanan bir modelin yeni bir pazara açılması için yeniden etiketleme ve yeniden eğitim maliyeti, metin tabanlı bir modele kıyasla belirgin şekilde düşüktür.
• Mevcut araçlarla tamamlayıcılık. Ürünün ikame değil eklenti olarak konumlanması, sosyal dinleme platformlarıyla ortaklık ve entegrasyon fırsatı yaratmaktadır.
3.7. Sonuç (Conclusion)

İnceleme sonucunda projenin teknik yaklaşımı olarak grafik tabanlı derin öğrenme, öznitelik tabanlı bir ön eleme katmanı ve açıklanabilirlik katmanı ile birlikte hibrit bir mimari içinde benimsenmiştir. Bu seçimin gerekçesi, GNN'in her ölçütte üstün olması değil, projenin temel sorusunu — koordinasyonun varlığını — yanıtlayabilen tek teknoloji ailesi olmasıdır. TwiBot-22 kıyaslama sonuçları bu tercihi nicel olarak desteklemektedir.

Pazarlama açısından yaratılacak pratik değer şudur: marka yöneticisi, olumsuz bir konuşma dalgasıyla karşılaştığında bunun gerçek müşteri memnuniyetsizliği mi yoksa satın alınmış bir saldırı mı olduğunu, gerekçesiyle birlikte görebilecektir. Bu ayrım, kriz iletişimi bütçesinin doğru yere yönlendirilmesini, gereksiz özür ve tazminat kampanyalarından kaçınılmasını ve gerçek müşteri şikâyetlerinin sahte gürültü içinde kaybolmamasını sağlamaktadır.

Bununla birlikte, literatürün bu görevde güncel yöntemlerin yalnızca orta düzeyde başarı gösterdiğini raporladığı unutulmamalıdır. Projenin gerçekçi hedefi, çözülmüş bir problemi ürünleştirmek değil, çözülmemiş bir problemde uygulanabilir bir ilk adım ortaya koymaktır.

3.8. Kaynaklar (Proper Citations)

Feng, S., Tan, Z., Wan, H., Wang, N., Chen, Z., Zhang, B., Zheng, Q., Zhang, W., Lei, Z., Yang, S., Feng, X., Zhang, Q., Wang, H., Liu, Y., Bai, Y., Wang, H., Cai, Z., Wang, Y., Zheng, L., Ma, Z., Li, J., & Luo, M. (2022). TwiBot-22: Towards Graph-Based Twitter Bot Detection. Advances in Neural Information Processing Systems 35 (NeurIPS 2022), Datasets and Benchmarks Track. arXiv:2206.04564

Luceri, L., Salkar, T. V., Balasubramanian, A., Pinto, G., Sun, C., & Ferrara, E. (2026). Coordinated Inauthentic Behavior on TikTok: Challenges and Opportunities for Detection in a Video-First Ecosystem. Proceedings of the International AAAI Conference on Web and Social Media, 20(1), 1533–1550. https://doi.org/10.1609/icwsm.v20i1.42711

Dang, Q.-V., Nguyen, P.-L., Le, D., & Dinh, M. N. (2026). XHBot: eXplainable Heterophily-aware Graph Neural Networks for Social Bot Detection. EAI Endorsed Transactions on AI and Robotics, 5.

Rust, R. T., Rand, W., Huang, M.-H., Stephen, A. T., Brooks, G., & Chabuk, T. (2021). Real-Time Brand Reputation Tracking Using Social Media. Journal of Marketing, 85(4), 21–43. https://doi.org/10.1177/0022242921995173

Gopalakrishnan, A. A., Hossain, J., Elmas, T., & Sarıyüce, A. E. (2025). Large Engagement Networks for Classifying Coordinated Campaigns and Organic Twitter Trends. Proceedings of the International AAAI Conference on Web and Social Media (ICWSM). arXiv:2503.00599

Elmas, T., Overdorf, R., Özkalay, A. F., & Aberer, K. (2021). Ephemeral Astroturfing Attacks: The Case of Fake Twitter Trends. 2021 IEEE European Symposium on Security and Privacy (EuroS&P), 403–422.