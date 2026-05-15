Factory method nesne kurmayı istemciden ayırıp alt sınıflara devretmeye dayanan bir metoddur. Faz 0 daki kodda olan karmaşıklık nesne üretmeyi başka bir alt sınıfa atılarak çözüldü. Artık nesne yaratmak ve özellik eklemek daha az anlaşılır ve stabil.

LegacySoundLibrary nin metodları GameObject sistemine uymadığından SoundAdapter sınıfında adapter uygulandı bu sayede update/render bozulmadan harici kütüphaneler sisteme entegre edilebiliyor.

Nesne kod değişmeden ve çalışırken efekt eklemek için ShieldDecorator sınıfında Decorator kullanıldı bu sayede nesne hiyerarşisi bozulmadan; open/closed prensibine uygun şekilde yeni özellikler eklenebildi.