# MongoDB incremental backup

## backup

 => Backup mekanizması
 * Yedekleme config dosyasında belirten sayıda full ve inc backup almaktadır.
 * ilk yedek full olacaktır.
 * Config dosyasında belirtildiği üzere dizine yedekleri zaman damgası ile kayıt edecektir.
 * Yedek alma işlemi başarılı olursa sistem bunu sqlite tablosuna kayıt edecektir.
 * Full yedeklemeden sonra kayıt olunan zaman damgasından sonraki değişikler inc backup olarak kayıt altına alınacaktır.
 * Inc backup sayısı mod ile kontrol edilip daha sonra tekrar full yedek alma işlemine başlamaktadır.
 
## restore

=> Restore mekanizması
* Yedekleten geri dönmek için dialog sayesinde tablodan okunan tüm değerler gösterilir.
* Inc backupdan dönülmek istenilirse; önce full backup a geri dönülür daha sonra sırası ile inc backuplar yüklenir.
* Yükleme işlemleri bittikten sonra(Her bir parti); kontrolün manuel olmasını sağlamak için,  geçişlerde enter tuşuna basması beklenir.
* Tuşa basıldıktan sonra sırası itibariyle diğer inc backup'lar yüklenir.
* ``` mongostat ``` aracı ile restore işlemi gerçek zamanlı izlenebilmektedir.


## Video
* Restore işlemi kısaca gösterilmiştir.

[![MongoDB Restore](https://img.youtube.com/vi/EJQs6vlcBLk/0.jpg)](https://www.youtube.com/watch?v=EJQs6vlcBLk)


[mongoInc-backup-0.1-1.fc34.x86_64.rpm](https://github.com/OEntegrasyon/MongoDB_incremental_backup/releases/download/mongoInc-backup/mongoInc-backup-0.1-1.fc34.x86_64.rpm)




