Factory method nesne kurmayı istemciden ayırıp alt sınıflara devretmeye dayanan bir metoddur. Faz 0 daki kodda olan karmaşıklık nesne üretmeyi başka bir alt sınıfa atılarak çözüldü. Artık nesne yaratmak ve özellik eklemek daha az anlaşılır ve stabil.

LegacySoundLibrary nin metodları GameObject sistemine uymadığından SoundAdapter sınıfında adapter uygulandı bu sayede update/render bozulmadan harici kütüphaneler sisteme entegre edilebiliyor.

Nesne kod değişmeden ve çalışırken efekt eklemek için ShieldDecorator sınıfında Decorator kullanıldı bu sayede nesne hiyerarşisi bozulmadan; open/closed prensibine uygun şekilde yeni özellikler eklenebildi.

Strategy Pattern ile hareket mantığı (Movement) gibi sürekli değişebilen veya yeni tipleri eklenebilecek davranışların nesne sınıflarının içine gömülmesi, kodun şişmesine ve esnekliğini yitirmesi sorunu kaldırıldı ve Open/Closed Prensibi (OCP) en üst seviyede uygulandı. Mevcut Player sınıfını değiştirmeden sisteme "Uçma" veya "Işınlanma" gibi yeni hareket yetenekleri eklenebilir hale geldi.  
 
Observer Pattern sayesinde artık oyunda bir olay gerçekleştiğinde (örn: bir başarının kazanılması) nesnenin bu durumdan haberdar olması gereken diğer sistemlerle sıkı bir bağ kurması gerekmiyor. Nesnelerin kendi durum değişikliklerini, kendisini dinleyen sistemlere otomatik olarak bildirmesi sağlandı.