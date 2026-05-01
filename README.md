# Advanced Google Dork Generator v3.0

> **Yetkili Guvenlik Arastirmasi ve Bug Bounty Programlari icin Profesyonel Google Dork Ureteci**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/Lisans-MIT-green)
![Purpose](https://img.shields.io/badge/Amac-Egitim%20%26%20Arastirma-orange)
![Status](https://img.shields.io/badge/Durum-Aktif-brightgreen)

---

## ONEMLI YASAL UYARI

> **BU ARAC YALNIZCA EGITIM VE YETKILI GUVENLIK ARASTIRMASI AMACIYLA SUNULMAKTADIR.**

Bu araci indirerek, yukleyerek veya kullanarak asagidaki sartlari kabul etmis sayilirsiniz:

1. **Yalnizca Yetkili Kullanim**: Bu arac yalnizca **yetkili guvenlik degerlendirmeleri**, **bug bounty programlari** ve **egitim arastirmalari** icin tasarlanmistir. Herhangi bir guvenlik testi yapmadan once hedef kurulustan **acik yazili izin** almaniz gerekmektedir.

2. **Yasadisi Faaliyet Yasagi**: Bu arac hicbir yasadisi, yetkisiz veya etik disi faaliyet icin kullanilamaz. Bilgisayar sistemlerine yetkisiz erisim, dunya genelinde bir cok ulkede **suctur**:
   - **Turkiye**: TCK Madde 243-245 (Bilisim Suclari) - 1 ila 8 yil hapis cezasi
   - **ABD**: Computer Fraud and Abuse Act (CFAA)
   - **AB**: 2013/40/EU sayili Direktif
   - **Ingiltere**: Computer Misuse Act 1990
   - **Almanya**: StGB 202a-202c

3. **Kullanici Sorumlulugu**: Bu aracin gelistiricileri, aracin kotuye kullanimi, hasar veya yasal sonuclar icin **HICBIR sorumluluk** kabul etmez. Kullaniminizin tum yururlukteki yasa ve yonetmeliklere uygun olmasini saglamak **tamamen sizin sorumlulugunuzdadir**.

4. **Google Dorking Kamuya Acik Bilgidir**: Google dorklari, kamuya acik sekilde indekslenmis bilgileri bulan gelismis arama sorgularidir. Ancak bu aramalarla bulunan sistemlere **yetkisiz erisim, istismar veya gizliligini ihlal etme YASADISIDIR**.

5. **Bug Bounty Programlari**: Bu araci bug bounty programlari icin kullaniyorsaniz:
   - Hedefin programin **kapsami** dahilinde oldugunu dogrulayin
   - Programin **katilim kurallarini** takip edin
   - Acikliklari sorumlu bir sekilde uygun kanallardan **raporlayin**
   - Hicbir veriye **erismeyin, degistirmeyin veya kopyalamayin**

**BU SARTLARI KABUL ETMIYORSANIZ BU ARACI KULLANMAYINIZ.**

---

## Google Dorking Nedir?

Google Dorking (Google Hacking olarak da bilinir), Google'da gelismis arama operatorleri kullanarak kamuya acik sekilde indekslenmis belirli bilgileri bulma pratigidir. Asagidaki alanlarda **mevsru bir kesif teknigi** olarak yaygin sekilde kullanilir:

- **Guvenlik arastirmacilari** - yetkili sizma testlerinde
- **Bug bounty avcilari** - HackerOne, Bugcrowd, Intigriti gibi platformlarda
- **Sistem yoneticileri** - kendi kuruluslarinin maruziyetini kontrol etmek icin
- **OSINT analistleri** - acik kaynak istihbarat toplama icin
- **SEO uzmanlari** - rekabet analizi icin

Bu arac bu arama sorgularinin **uretimini otomatiklestirir**. Hicbir hedef sistemle **etkilesime girmez**, hedeflere **istek gondermez** ve hicbir acikligi **istismar etmez**.

---

## Ozellikler

### CMS'e Ozel Dork Sablonlari (147 sablon)

| CMS | Sablon | Aciklama |
|-----|--------|----------|
| WordPress | 39 | Plugin yollari, config dosyalari, debug loglari, REST API, XML-RPC |
| Joomla | 21 | Admin panelleri, bilesenler, yapilandirma dosyalari, API endpointleri |
| Drupal | 16 | Changelog, ayarlar, moduller, JSON API, node yollari |
| Magento | 10 | Config XML, admin panelleri, REST API, log dosyalari |
| PrestaShop | 7 | Admin panelleri, moduller, config dosyalari |
| OpenCart | 5 | Admin panelleri, config dosyalari, sistem loglari |
| Laravel | 8 | .env dosyalari, debug bar, Telescope, Horizon |
| Generic | 41 | Dizin listeleri, phpMyAdmin, .git, yedekler, API'ler, Swagger |

### Keyword Ureteci Sistemi

| Kategori | Adet | Aciklama |
|----------|------|----------|
| Ulkeler | 57 | Otomatik uretilen ulke isimleri |
| Sehirler | 666 | 57 ulkeden buyuk sehirler |
| TLD'ler | 66 | Ulkeye ozel ve genel alan adi uzantilari |
| Sektorler | 50 | Hastane, banka, universite, otel vb. |
| Zafiyet Anahtar Kelimeleri | 29 | login, admin, config, backup, debug vb. |

### Desteklenen Ulkeler (57)

<details>
<summary>Tam ulke listesini gormek icin tiklayiniz</summary>

| Kod | Ulke | TLD | Sehir |
|-----|------|-----|-------|
| TR | Turkiye | .tr | 20 |
| US | ABD | .us | 20 |
| DE | Almanya | .de | 15 |
| FR | Fransa | .fr | 15 |
| GB | Ingiltere | .uk | 15 |
| ES | Ispanya | .es | 15 |
| IT | Italya | .it | 15 |
| IN | Hindistan | .in | 15 |
| BR | Brezilya | .br | 14 |
| RU | Rusya | .ru | 14 |
| JP | Japonya | .jp | 14 |
| CN | Cin | .cn | 14 |
| AU | Avustralya | .au | 14 |
| CA | Kanada | .ca | 14 |
| MX | Meksika | .mx | 14 |
| NL | Hollanda | .nl | 13 |
| PL | Polonya | .pl | 13 |
| AR | Arjantin | .ar | 12 |
| CO | Kolombiya | .co | 12 |
| EG | Misir | .eg | 12 |
| IR | Iran | .ir | 12 |
| NO | Norvec | .no | 12 |
| PT | Portekiz | .pt | 12 |
| SA | Suudi Arabistan | .sa | 12 |
| SE | Isvec | .se | 12 |
| UA | Ukrayna | .ua | 12 |
| IQ | Irak | .iq | 11 |
| KR | Guney Kore | .kr | 11 |
| NG | Nijerya | .ng | 11 |
| VN | Vietnam | .vn | 11 |
| AT | Avusturya | .at | 10 |
| BD | Banglades | .bd | 10 |
| BE | Belcika | .be | 10 |
| CH | Isvicre | .ch | 10 |
| CL | Sili | .cl | 10 |
| CZ | Cek Cumhuriyeti | .cz | 10 |
| DK | Danimarka | .dk | 10 |
| FI | Finlandiya | .fi | 10 |
| GH | Gana | .gh | 10 |
| GR | Yunanistan | .gr | 10 |
| HU | Macaristan | .hu | 9 |
| IE | Irlanda | .ie | 10 |
| IL | Israil | .il | 10 |
| KE | Kenya | .ke | 10 |
| MA | Fas | .ma | 10 |
| MY | Malezya | .my | 10 |
| NZ | Yeni Zelanda | .nz | 10 |
| PE | Peru | .pe | 10 |
| PH | Filipinler | .ph | 10 |
| PK | Pakistan | .pk | 10 |
| RO | Romanya | .ro | 10 |
| TH | Tayland | .th | 10 |
| TN | Tunus | .tn | 10 |
| ZA | Guney Afrika | .za | 10 |
| AE | BAE | .ae | 8 |
| ID | Endonezya | .id | 12 |
| SG | Singapur | .sg | 1 |

</details>

---

## Kurulum

### Gereksinimler

- Python 3.8 veya daha yeni
- Harici bagimliligi yoktur (sadece standart kutuphane)

### Kurulum Adimlari

```bash
git clone https://github.com/KULLANICI_ADINIZ/google-dork-generator.git
cd google-dork-generator
```

`pip install` gerekmez - arac yalnizca Python standart kutuphane modullerini kullanir.

---

## Kullanim

### Hizli Baslangic

```bash
# Interaktif mod (yeni baslayanlar icin onerilir)
python dork_generator.py -i

# Turkiye icin WordPress dorklari uret
python dork_generator.py --cms wordpress --country TR

# Birden fazla ulke icin tum CMS dorklari
python dork_generator.py --cms all --country TR,DE,FR

# Desteklenen tum ulkeleri listele
python dork_generator.py --list-countries
```

### Komut Satiri Secenekleri

| Secenek | Aciklama | Varsayilan |
|---------|----------|------------|
| `-i`, `--interactive` | Interaktif modda calistir | - |
| `--cms` | CMS platformlari (virgullerle ayrilmis) | `all` |
| `--country` | Ulke kodlari (virgullerle ayrilmis veya `all`) | - |
| `--cats` | Anahtar kelime kategorileri | - |
| `--keywords` | Ozel anahtar kelimeler | - |
| `--list-countries` | Desteklenen tum ulkeleri goster | - |
| `--limit` | Maksimum dork sayisi | `0` (sinirsiz) |
| `--shuffle` | Ciktiyi karistir | `false` |
| `--format` | Cikti formati (`txt` veya `json`) | `txt` |
| `-o`, `--output` | Cikti dosya adi | otomatik |

### Kullanilabilir CMS Degerleri

```
wordpress, joomla, drupal, magento, prestashop, opencart, laravel, generic, all
```

### Kullanilabilir Anahtar Kelime Kategorileri

```
countries, tlds, industries, vuln_keywords, all_cities
```

### Ornekler

```bash
# Turkiye icin WordPress dorklari (sehir bazli)
python dork_generator.py --cms wordpress --country TR

# Avrupa ulkeleri icin Joomla + Drupal dorklari
python dork_generator.py --cms joomla,drupal --country DE,FR,GB,ES,IT,NL

# Sektor anahtar kelimeleriyle tum CMS dorklari, JSON olarak kaydet
python dork_generator.py --cms all --cats industries --format json -o sektor_dorklari.json

# ABD icin ozel anahtar kelimelerle WordPress dorklari
python dork_generator.py --cms wordpress --country US --keywords hospital,university

# TUM ulkeler icin dork uret (buyuk cikti)
python dork_generator.py --cms wordpress --country all --limit 1000 --shuffle

# Laravel .env dosyasi dorklari (global)
python dork_generator.py --cms laravel --cats tlds

# Genel zafiyet dorklari
python dork_generator.py --cms generic --cats vuln_keywords
```

### Interaktif Mod

Interaktif mod sizi adim adim yonlendirir:

```
$ python dork_generator.py -i

  +==================================================+
  |     ADVANCED GOOGLE DORK GENERATOR v3.0          |
  |     Bug Bounty & Security Research Tool          |
  |     All CMS Platforms Supported                  |
  +==================================================+

[?] List supported countries? (y/n): y
[?] Country codes (e.g. TR,US,DE or 'all'): TR
[?] CMS (comma-separated, or 'all'): wordpress
[?] Extra keyword categories (comma-separated, optional):
[?] Custom keywords (comma-separated, optional):
[?] Limit (0 = no limit): 100
[?] Shuffle results? (y/n): y
[?] Output format (txt/json): txt
[?] Output filename (Enter = auto):

[*] Generating dorks...
[+] 100 dorks saved to: dorks_20260501_230354.txt
```

---

## Cikti Formatlari

### Metin Formati (`.txt`)

```
# Google Dorks - Generated 20260501_230354
# Total: 858

inurl:"/wp-content/plugins/" turkey
inurl:"/wp-content/plugins/" site:.tr
inurl:"/wp-content/plugins/" istanbul
inurl:"/wp-content/plugins/" ankara
...
```

### JSON Formati (`.json`)

```json
{
  "generated_at": "20260501_230354",
  "total": 858,
  "dorks": [
    "inurl:\"/wp-content/plugins/\" turkey",
    "inurl:\"/wp-content/plugins/\" site:.tr",
    "inurl:\"/wp-content/plugins/\" istanbul"
  ]
}
```

---

## Kullanim Alanlari (YALNIZCA YASAL)

### 1. Bug Bounty Kesfi

Uretilen dorklari yetkili bug bounty platformlarindaki kapsam dahili hedefleri bulmak icin kullanin:
- [HackerOne](https://www.hackerone.com/)
- [Bugcrowd](https://www.bugcrowd.com/)
- [Intigriti](https://www.intigriti.com/)
- [YesWeHack](https://www.yeswehack.com/)

### 2. Kendi Altyapinizi Denetleme

Kendi kurulusunuzun hassas dosyalarinin Google tarafindan kamuya acik sekilde indekslenip indekslenmedigini kontrol edin:
- Yapilandirma dosyalari acikta mi?
- Debug loglari herkese acik mi?
- Admin panelleri indekslenmis mi?
- Yedek dosyalari gorunur mu?

### 3. Guvenlik Egitimi

Yaygin web uygulamasi yapilandirma hatalarini ve bunlarin arama motorlari araciligiyla nasil kesiflenebildigini ogrenin.

### 4. OSINT Arastirmasi

Yetkili arastirmalar icin acik kaynak istihbarat toplama calismalari yurutin.

---

## Sorumlu Aciklama (Responsible Disclosure)

Bu aracla uretilen dorklari kullanarak bir zafiyet kesifederseniz:

1. Acikligi istismar etmeye **CALISMAYINIZ**
2. Hicbir veriye **erismeyin, degistirmeyin veya indirmeyin**
3. Bulguyu kurulusun sorumlu aciklama programi araciligiyla **RAPORLAYIN**
4. Aciklama programi yoksa `security@domain.com` uzerinden dogrudan iletisime gecin
5. [ISO 29147](https://www.iso.org/standard/72311.html) zafiyet aciklama yonergelerine uyun

---

## Proje Yapisi

```
google-dork-generator/
|-- dork_generator.py    # Ana script (tek dosya, bagimliligi yok)
|-- README.md            # Bu dosya
|-- LICENSE              # MIT Lisansi
```

---

## Katki Saglama

Katkilasiniz memnuniyetle karsilanir! Lutfen sunlari saglayin:

1. Tum katkilar **mesru guvenlik arastirmasi** amaclarina yonelik olsun
2. Exploit kodu veya zararli veri yukleri **dahil edilmesin**
3. Yeni dork sablonlari istismar degil **tespit** odakli olsun
4. Sorumlu aciklama uygulamalarina uyun

---

## Lisans

Bu proje MIT Lisansi altinda lisanslanmistir. Detaylar icin [LICENSE](LICENSE) dosyasina bakiniz.

---

## Sorumluluk Reddi (Son Kez Tekrar)

```
BU YAZILIM "OLDUGU GIBI" SUNULUR, HICBIR GARANTI VERILMEZ.

YAZARLAR VE KATKILCILAR, BU ARACIN KOTUYE KULLANIMINDAN
DOLAYI HICBIR SORUMLULUK KABUL ETMEZ. BU ARAC YALNIZCA
YETKILI GUVENLIK ARASTIRMASI, BUG BOUNTY PROGRAMLARI VE
EGITIM AMACLARINA YONELIKTIR.

BILGISAYAR SISTEMLERINE YETKISIZ ERISIM YASADISIDIR VE
CEZAI KOVUSTURMA, PARA CEZASI VE HAPIS CEZASI ILE
SONUCLANABILIR.

BU ARACI KULLANARAK, EYLEMLERINIZIN TAM SORUMLULUGUNUN
SIZDE OLDUGUNU ANLADIGINIZI VE KABUL ETTIGINIZI BEYAN
ETMIS OLURSUNUZ.

SORUMLU KULLANIN. YASAL HACKLEYIN.
```

---

**Guvenlik arastirma toplulugu icin ozenle yapilmistir.**
