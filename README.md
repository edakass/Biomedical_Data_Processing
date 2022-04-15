# Biomedical_Data_Processing

> ## 11-03-2022

- Her şeyi kurallarla ifade etmek zor.

- CNN->Görüntü, RNN->video,ses vs

- Cyc Projesi?

Bilgi tabanlı yaklaşım.Mesela Fred isimli biri makineye dönüşecek mi? Sezgisel işlemlerde başarısızlık.

- Polar koordinatlarda daha kolaydır.

- Gösterim çok önemli.

- Her pixel girdimizdir.

- Hiperparametre->Kaç tane gizli katman olacağını ben belirleyeceğim,çok fazla nöron kullanılması iyi de değildir.

- Bilgiler ağırlıklarda taşınıyor.

- Kural Tabanlı -> Uzman sistemler

- Klasik Makine Öğrenme -> Elle tasarlanmış öznitelikler,ev satışı vb


> ## 18-03-2022

- YZ'yi bir matruşka olarak düşünebilirsin.(YZ->MÖ->DÖ)

- Ev tahmini satışı için -> regresyon problemi(sürekli)

- recommender sistemi -> bunu alan şunu da aldı gibi

- kategorilendirme->sınıflandırma

- Yaşı regresyondan sınıflandırmaya yönlendirmek için belli yaş grubunu seçmek için.Neden buna ihtiyaç duydum? Çünkü 0-100 arasında daha çok hata olacağı için,ama 0-18 yaş arasında hata olması daha iyi.

- Evlerin fiyatları sürekli olduğu için regresyon

- Denetimlide->direk çıktıya

- Denetimsiz->gruplara ayırıyor.

- Tek değişkenli linear regresyon

- Hiperparametre -> Araştırmacının kendisi tarafından geliştirilen değer,araştırmacı değiştirebiliyor.


> ## 24-03-2022

- csv->birbirinden virgül ile ayrılmış veriler.

- Girdiler x,çıktılar y

- iloc->belirlediğimiz satır ve sutundaki bilgileri okuyor. 0:3,0,1,2 olacak ama 3 olmayacak. İndex  0 dan başlıyor.

- sklearn -> bilimsel hesaplar için

- özellik ölçeklendirme feature scaling

> ## 01-04-2022

- CNN'e ihtiyç var çünkü YSA'da resim kullanmak zor oluyordu.

- 32x32x3 buradaki 3'ün anlamı RGB, eğer ki 1 olsaydı siyah beyaz demekti.Derinlikte demek.

- CNN'de ilk kısımda orjinal yani giriş katmanında kullanılıyor daha sonra ki kısımlarda aktivasyon haritasında kullanılıyor(orjinal resmi CNN ilk kısımda görüyor,sonraki katmanlarda aktivasyon haritalarındaki resmi kullanılıyor.

- Amacımız uygun filtreleri bulmak,ilk başta random daha sonra eğitim aşamasında değişiyor.

- CNN bize hız kazandırıyor,ortak filtreler kullanıyoruz,birbirine ait bağımlılıklar azaltılır.

- İlk aşamada ortak özellikler var.

- Transfer öğrenmeye olanak sağlayan ilk aşamadır.(Sabit şeyler, kol vs)

- Neden padding uyguluyoruz? Bir katmandan bir katmana küçülüyor.

- Kenardaki pixeller ortaya göre daha az bilgi alınıyor/kullanılıyor.

- Padding hem sağa hem de sola geliyor. 

- Pool uyguluyoruz küçülüyor diğeri büyüyor işlem hızı artıyor en önemli işlemi yapıyoruz.

- 2P : Hem sağa hem de sola ekleniliyor

- Hep tek sayılı mı olmalı filtreler ?

Çift olarak olabilir ama tek sayı daha kolay oluyor. Genelde çift filtre kullanılmıyor. Genelde kare 32x32,genelde kare olmaz günlük hayatta elimizde, CNN kaçlık istiyorsa ona çekmem gerekiyor. Makineler resmi bütün olarak görmüyor pixel pixel alıyor.

- CNN'de sadece ilk katmanda orjinal resim kullanılır daha sonra aktivasyon haritaları üzerinde işlem yapıp ilerliyoruz.

- Pooling Layer: Resmin büyüklüğünü azaltmaya yarıyor.

- Max Pooling: Aldığımız alanda en yüksek değeri alıyor.

- Avarage Pooling:Ortalamasını alıyor.

- Fully Connected Layer(FC): Tek boyutlu diziyi çeviriyoruz.

- RNN: Metin  CNN:Kan,MR görüntüsü vb için


> ## 08-04-2022

- binary class. : kedi=0 , köpek=1 

- Conv3D:videolarla işlem Conv2D:resimlerle işlemi gerçekleştiriyor

- Dense : Tek boyutlu vektöre çevirmemize yardımcı oluyor

- Neden padding kullanıyoruz,avantajı ne?
Bir layerdan diğer layera geç,nce değişmesin diye

- input shape:girdi büyüklüklerini belirtiyor.İnput shape sadece 1. katmanda bilgilerini giriyoruz. Daha sonra da keras bizim için yapıyor.

- Ara katmanlarda genel de ReLu kullanılıyor.

- Flattenle düzleştireceğiz.Tek boyuta geçirecek,tek boyutlu bir yer olacak.

- İkinci CNN katmanına eklerken input shape gerek yok.

- Elimdeki veri setini arttırma yöntemi için ImageDataGenerator

- Rescale: özellik ölçeklendirme


![image](https://user-images.githubusercontent.com/61595808/163446800-5b3370ba-0842-4b2b-802f-9afcfd509136.png)



![image](https://user-images.githubusercontent.com/61595808/163425632-dd53e0d0-daa4-4296-81e7-712b0b6a60f1.png)



![image](https://user-images.githubusercontent.com/61595808/163441039-3c2b52d2-a0d1-41ee-a6e3-d7cc5ecd63f6.png)



