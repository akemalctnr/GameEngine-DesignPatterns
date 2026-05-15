Konu: Mini Oyun Motoru
Oyun motoru senaryosu, farklı nesne tiplerinin davranışlarını yönetmek için tasarım örüntülerinin nasıl kullanıldığını görmek açısından çok zengin bir alan sunuyor. if-else karmaşasından kurtulup daha esnek bir yapı kurmak için bu konuyu seçtim.

## 🏗 Mimari Yapı (Faz 1)
Başlangıçtaki karmaşık `if-else` yapısı, **Factory Method** kullanılarak aşağıdaki gibi modernize edilmiştir:

![Phase 1 UML Diagram](docs/diagrams/phase1.png)

## 🛠 Yapısal (Structural) Geliştirmeler (Faz 2)
Bu aşamada sisteme mevcut kodu bozmadan yeni yetenekler kazandırıldı:
**Adapter:** Harici ses kütüphanesi sisteme entegre edildi.
**Decorator:** Nesnelere dinamik görsel efekt (kalkan) özelliği eklendi.

![Architectural Diagram - Phase 2](docs/diagrams/phase2.png)