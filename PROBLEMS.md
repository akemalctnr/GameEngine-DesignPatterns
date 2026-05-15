Faz 0 

1- Tüm nesneler bir sınıfa bağlı
2- Yeni nesne eklemek için mevcut metodlar değiştirilmeli
3- Yeni nesne ve davranış eklemek kodu okunamaz hale getirebilir
4- Mevut kodda farklı özelliklere sahip özellikler eklemek imkansız 
5- Item sınıfının health değerine ihtiyacı yok ama "GameObject" sınıfı yüzünden bu değeri taşımak zorunda kalıyor

Ai Ne Gördü:
Open/Closed ihlali, Single responsibility ihlali, Type-Based Dispatch Anti-Pattern, Kod Tekrarı (DRY İhlali) ni gördü. Bunlardan genel olarak mantığı aynı olsa da Type-Based'i ve kod tekrarını görememiştim ben Enemy yerine enemy yazınca çalışmayacağını söylüyor ve update/render aynı if else zincirlerini içeriyor.

Eksikleri
Kodun ileri safhada çok karmaşıklaşağı konusunda beni uyarmadı veya Item sınıfında gereksiz özellikler olduğunu söylemedi.


Faz 1 Çözülen Sorunlar

*Nesne yaratma karmaşası Factory Method ile çözüldü

Faz 2 Çözülen Sorunlar
Adapter ve Decorator kullanılarak sisteme yeni özellik eklemek için mevcut sınıfların değiştirilmesine olan gereklilik giderildi(OCP ihlali). Ve uyumsuz kütüphaneler sisteme dahil edildi. 
