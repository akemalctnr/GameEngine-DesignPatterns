Oturum Süresi: 35 Dakika Katılımcılar: Ali Kemal (Junior Dev/Programcı) & Gemini (AI Pair Programmer)

Bu oturumda oyun motorunun davranışsal (behavioral) yeteneklerini artırmak ve sistemi gerçekten genişletilebilir (extensible) kılmak üzerine odaklandık. Ana hedefimiz, mevcut sınıfların koduna dokunmadan (Open/Closed Principle) yeni hareket ve bildirim özellikleri eklemekti.

Strategy Pattern: Hareket mantığını (Movement) sınıftan ayırmaya karar verdik. AI, if-else blokları yerine farklı strateji sınıfları (KeyboardMove, PatrolMove) kullanmamı önerdi. Bu sayede sınıfa dokunmadan yeni hareket tipleri eklenebilir hale geldi.  

Observer Pattern: Nesneler arası iletişim (Achievement/Log sistemi) için Observer örüntüsünü tartıştık. Bir olay gerçekleştiğinde (notify), başarı takipçisinin otomatik uyarılması sağlandı.Süre Tahmini: AI desteği olmasaydı, Strategy ve Observer örüntülerinin birbirine entegre edilmesi ve Python'daki abc modülü ile hatasız bir yapı kurulması en az 3-4 saatimi alırdı. AI ile bu süreci mimari tartışmalar dahil 30-40 dakikada tamamladık.  

AI başlangıçta her strateji için GameObject sınıfını miras alan devasa alt sınıflar önerdi. Ancak tartışmalar sonunda, "Composition over Inheritance" (Miras yerine Kompozisyon) prensibini kararlaştırarak stratejiyi ayrı bir bileşen olarak kurguladık.