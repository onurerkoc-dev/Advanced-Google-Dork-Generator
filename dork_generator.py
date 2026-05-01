#!/usr/bin/env python3
"""
Advanced Google Dork Generator v3.0
CMS-based dork generation for security research & bug bounty
Author: Onur Erkoç
"""

import itertools
import random
import argparse
import json
import os
from datetime import datetime

# ============================================================
# DORK TEMPLATES - CMS SPECIFIC
# ============================================================

WORDPRESS_DORKS = [
    'inurl:"/wp-content/plugins/" {keyword}',
    'inurl:"/wp-content/themes/" {keyword}',
    'inurl:"/wp-admin/" {keyword}',
    'inurl:"/wp-includes/" {keyword}',
    'inurl:"xmlrpc.php" {keyword}',
    'inurl:"wp-login.php" {keyword}',
    'inurl:"wp-config.php" {keyword}',
    'inurl:"wp-config.php.bak" {keyword}',
    'inurl:"wp-config.php.old" {keyword}',
    'inurl:"wp-config.php.save" {keyword}',
    'inurl:"wp-config.php.swp" {keyword}',
    'inurl:"wp-config.php~" {keyword}',
    'inurl:"/wp-json/wp/v2/users" {keyword}',
    'inurl:"/wp-json/wp/v2/posts" {keyword}',
    'inurl:"/wp-content/uploads/" {keyword}',
    'inurl:"/wp-content/debug.log" {keyword}',
    'inurl:"/?author=1" {keyword} site:.com',
    'intitle:"WordPress" inurl:"/readme.html" {keyword}',
    'inurl:"/wp-content/plugins/revslider/" {keyword}',
    'inurl:"/wp-content/plugins/contact-form-7/" {keyword}',
    'inurl:"/wp-content/plugins/elementor/" {keyword}',
    'inurl:"/wp-content/plugins/woocommerce/" {keyword}',
    'inurl:"/wp-content/plugins/jetpack/" {keyword}',
    'inurl:"/wp-content/plugins/akismet/" {keyword}',
    'inurl:"/wp-content/plugins/wordfence/" {keyword}',
    'inurl:"/wp-content/plugins/yoast/" {keyword}',
    'intext:"WordPress" inurl:"/license.txt" {keyword}',
    'inurl:"/wp-content/uploads/" ext:sql {keyword}',
    'inurl:"/wp-content/uploads/" ext:txt {keyword}',
    'inurl:"/wp-content/uploads/" ext:log {keyword}',
    'inurl:"/wp-content/backup-db/" {keyword}',
    'inurl:"/wp-content/backups/" {keyword}',
    'intitle:"Index of" "wp-content" {keyword}',
    'intitle:"Index of" "wp-admin" {keyword}',
    'inurl:"/wp-content/plugins/wp-file-manager/" {keyword}',
    'inurl:"/wp-content/plugins/easy-wp-smtp/" {keyword}',
    'inurl:"/wp-content/plugins/duplicator/" {keyword}',
    'inurl:"/wp-content/plugins/wp-symposium/" {keyword}',
    'inurl:"/?rest_route=/wp/v2/users" {keyword}',
]

JOOMLA_DORKS = [
    'inurl:"/administrator/" intitle:"Joomla" {keyword}',
    'inurl:"/components/com_" {keyword}',
    'inurl:"/components/com_users/" {keyword}',
    'inurl:"/components/com_content/" {keyword}',
    'inurl:"/components/com_contact/" {keyword}',
    'inurl:"/components/com_fields/" {keyword}',
    'inurl:"/components/com_media/" {keyword}',
    'inurl:"/media/jui/" {keyword}',
    'inurl:"/configuration.php" {keyword}',
    'inurl:"/configuration.php.bak" {keyword}',
    'inurl:"/configuration.php~" {keyword}',
    'inurl:"/configuration.php.old" {keyword}',
    'intitle:"Joomla" inurl:"/README.txt" {keyword}',
    'inurl:"/administrator/manifests/" {keyword}',
    'inurl:"/libraries/joomla/" {keyword}',
    'inurl:"/plugins/system/" site:*.com {keyword}',
    'intitle:"Index of" "com_" {keyword}',
    'inurl:"/api/index.php/v1" {keyword}',
    'inurl:"/administrator/help/" {keyword}',
    'inurl:"/tmp/" intitle:"Joomla" {keyword}',
    'inurl:"/logs/" intitle:"Joomla" {keyword}',
]

DRUPAL_DORKS = [
    'inurl:"/sites/default/files/" {keyword}',
    'inurl:"/sites/all/modules/" {keyword}',
    'inurl:"/sites/all/themes/" {keyword}',
    'inurl:"/node/" intitle:"Drupal" {keyword}',
    'inurl:"/user/login" intitle:"Drupal" {keyword}',
    'inurl:"/CHANGELOG.txt" intitle:"Drupal" {keyword}',
    'inurl:"/INSTALL.txt" intitle:"Drupal" {keyword}',
    'inurl:"/UPDATE.txt" intitle:"Drupal" {keyword}',
    'inurl:"/sites/default/settings.php" {keyword}',
    'inurl:"/misc/drupal.js" {keyword}',
    'inurl:"/core/CHANGELOG.txt" {keyword}',
    'inurl:"/modules/system/" {keyword}',
    'inurl:"/profiles/standard/" {keyword}',
    'intitle:"Index of" "sites/default" {keyword}',
    'inurl:"/jsonapi/node/" {keyword}',
    'inurl:"/admin/config" intitle:"Drupal" {keyword}',
]

MAGENTO_DORKS = [
    'inurl:"/app/etc/local.xml" {keyword}',
    'inurl:"/app/etc/env.php" {keyword}',
    'inurl:"/admin" intitle:"Magento" {keyword}',
    'inurl:"/downloader/" intitle:"Magento" {keyword}',
    'inurl:"/skin/frontend/" {keyword}',
    'inurl:"/media/catalog/" {keyword}',
    'intitle:"Magento" inurl:"/RELEASE_NOTES.txt" {keyword}',
    'inurl:"/var/log/" intitle:"Magento" {keyword}',
    'inurl:"/var/report/" intitle:"Magento" {keyword}',
    'inurl:"/rest/V1/" intitle:"Magento" {keyword}',
]

PRESTASHOP_DORKS = [
    'inurl:"/admin" intitle:"PrestaShop" {keyword}',
    'inurl:"/modules/" intitle:"PrestaShop" {keyword}',
    'inurl:"/themes/" intitle:"PrestaShop" {keyword}',
    'inurl:"/config/settings.inc.php" {keyword}',
    'inurl:"/config/settings.inc.php.bak" {keyword}',
    'inurl:"/docs/CHANGELOG.txt" intitle:"PrestaShop" {keyword}',
    'intitle:"PrestaShop" inurl:"/install/" {keyword}',
]

OPENCART_DORKS = [
    'inurl:"/admin/" intitle:"OpenCart" {keyword}',
    'inurl:"/catalog/" intitle:"OpenCart" {keyword}',
    'inurl:"/config.php" intitle:"OpenCart" {keyword}',
    'inurl:"/admin/config.php" intitle:"OpenCart" {keyword}',
    'intitle:"OpenCart" inurl:"/system/logs/" {keyword}',
]

LARAVEL_DORKS = [
    'inurl:"/.env" "DB_PASSWORD" {keyword}',
    'inurl:"/.env" "APP_KEY" {keyword}',
    'inurl:"/storage/logs/laravel.log" {keyword}',
    'intitle:"Laravel" inurl:"/telescope" {keyword}',
    'intitle:"Laravel" inurl:"/horizon" {keyword}',
    'inurl:"/vendor/phpunit/" {keyword}',
    'intitle:"Whoops" "Laravel" {keyword}',
    'inurl:"/_debugbar/" {keyword}',
]

GENERIC_DORKS = [
    'intitle:"Index of /" {keyword}',
    'intitle:"Index of" "parent directory" {keyword}',
    'inurl:"/phpmyadmin/" {keyword}',
    'inurl:"/adminer.php" {keyword}',
    'inurl:"/phpinfo.php" {keyword}',
    'inurl:"/.git/" {keyword}',
    'inurl:"/.svn/" {keyword}',
    'inurl:"/.env" {keyword}',
    'inurl:"/.htaccess" {keyword}',
    'inurl:"/.htpasswd" {keyword}',
    'inurl:"/server-status" {keyword}',
    'inurl:"/server-info" {keyword}',
    'inurl:"/web.config" {keyword}',
    'inurl:"/crossdomain.xml" {keyword}',
    'inurl:"/robots.txt" "Disallow" {keyword}',
    'inurl:"/sitemap.xml" {keyword}',
    'inurl:"/backup/" ext:sql {keyword}',
    'inurl:"/backup/" ext:zip {keyword}',
    'inurl:"/backup/" ext:tar.gz {keyword}',
    'inurl:"/db/" ext:sql {keyword}',
    'ext:sql "INSERT INTO" {keyword}',
    'ext:log "password" {keyword}',
    'ext:cfg "password" {keyword}',
    'ext:ini "password" {keyword}',
    'ext:env "DB_PASSWORD" {keyword}',
    'ext:yml "password:" {keyword}',
    'ext:json "api_key" {keyword}',
    'ext:json "secret" {keyword}',
    'inurl:"/api/v1/" {keyword}',
    'inurl:"/api/v2/" {keyword}',
    'inurl:"/swagger-ui.html" {keyword}',
    'inurl:"/api-docs" {keyword}',
    'intitle:"Dashboard" inurl:"/login" {keyword}',
    'intitle:"Admin" inurl:"/login" {keyword}',
    'inurl:"/debug/" {keyword}',
    'inurl:"/trace/" {keyword}',
    'inurl:"/console/" {keyword}',
    'inurl:"/cgi-bin/" {keyword}',
    'inurl:"/shell" ext:php {keyword}',
    'inurl:"/filemanager/" {keyword}',
    'inurl:"/uploads/" ext:php {keyword}',
]

# ============================================================
# KEYWORD GENERATOR - COUNTRY-BASED AUTO GENERATION
# ============================================================

COUNTRY_DB = {
    "TR": {"name": "Turkey", "tld": ".tr", "cities": ["istanbul","ankara","izmir","bursa","antalya","adana","konya","gaziantep","mersin","diyarbakir","kayseri","eskisehir","trabzon","samsun","denizli","malatya","erzurum","van","elazig","manisa"]},
    "US": {"name": "USA", "tld": ".us", "cities": ["newyork","losangeles","chicago","houston","phoenix","philadelphia","sanantonio","sandiego","dallas","austin","seattle","denver","boston","miami","atlanta","detroit","portland","lasvegas","memphis","baltimore"]},
    "DE": {"name": "Germany", "tld": ".de", "cities": ["berlin","hamburg","munich","cologne","frankfurt","stuttgart","dusseldorf","leipzig","dortmund","essen","bremen","dresden","hannover","nuremberg","duisburg"]},
    "FR": {"name": "France", "tld": ".fr", "cities": ["paris","marseille","lyon","toulouse","nice","nantes","strasbourg","montpellier","bordeaux","lille","rennes","reims","toulon","grenoble","dijon"]},
    "GB": {"name": "UK", "tld": ".uk", "cities": ["london","manchester","birmingham","leeds","glasgow","liverpool","edinburgh","bristol","sheffield","cardiff","belfast","nottingham","leicester","coventry","bradford"]},
    "ES": {"name": "Spain", "tld": ".es", "cities": ["madrid","barcelona","valencia","seville","zaragoza","malaga","murcia","palma","bilbao","alicante","cordoba","valladolid","vigo","gijon","granada"]},
    "IT": {"name": "Italy", "tld": ".it", "cities": ["rome","milan","naples","turin","palermo","genoa","bologna","florence","catania","bari","venice","verona","messina","padua","trieste"]},
    "BR": {"name": "Brazil", "tld": ".br", "cities": ["saopaulo","riodejaneiro","brasilia","salvador","fortaleza","belohorizonte","manaus","curitiba","recife","goiania","belem","portoalegre","guarulhos","campinas"]},
    "IN": {"name": "India", "tld": ".in", "cities": ["mumbai","delhi","bangalore","hyderabad","ahmedabad","chennai","kolkata","pune","jaipur","lucknow","kanpur","nagpur","indore","thane","bhopal"]},
    "RU": {"name": "Russia", "tld": ".ru", "cities": ["moscow","saintpetersburg","novosibirsk","yekaterinburg","kazan","nizhnynovgorod","chelyabinsk","samara","omsk","rostov","ufa","krasnoyarsk","voronezh","perm"]},
    "JP": {"name": "Japan", "tld": ".jp", "cities": ["tokyo","yokohama","osaka","nagoya","sapporo","fukuoka","kobe","kyoto","kawasaki","saitama","hiroshima","sendai","chiba","kitakyushu"]},
    "CN": {"name": "China", "tld": ".cn", "cities": ["beijing","shanghai","guangzhou","shenzhen","chengdu","wuhan","hangzhou","xian","nanjing","chongqing","tianjin","suzhou","zhengzhou","changsha"]},
    "AU": {"name": "Australia", "tld": ".au", "cities": ["sydney","melbourne","brisbane","perth","adelaide","canberra","hobart","darwin","goldcoast","newcastle","wollongong","geelong","cairns","townsville"]},
    "CA": {"name": "Canada", "tld": ".ca", "cities": ["toronto","montreal","vancouver","calgary","edmonton","ottawa","winnipeg","quebec","hamilton","kitchener","london","victoria","halifax","saskatoon"]},
    "MX": {"name": "Mexico", "tld": ".mx", "cities": ["mexicocity","guadalajara","monterrey","puebla","tijuana","leon","juarez","zapopan","merida","cancun","queretaro","chihuahua","saltillo","morelia"]},
    "NL": {"name": "Netherlands", "tld": ".nl", "cities": ["amsterdam","rotterdam","thehague","utrecht","eindhoven","groningen","tilburg","almere","breda","nijmegen","haarlem","arnhem","leiden"]},
    "SE": {"name": "Sweden", "tld": ".se", "cities": ["stockholm","gothenburg","malmo","uppsala","vasteras","orebro","linkoping","helsingborg","norrkoping","jonkoping","lund","umea"]},
    "NO": {"name": "Norway", "tld": ".no", "cities": ["oslo","bergen","trondheim","stavanger","drammen","fredrikstad","kristiansand","tromso","sandnes","sarpsborg","skien","bodo"]},
    "PT": {"name": "Portugal", "tld": ".pt", "cities": ["lisbon","porto","amadora","braga","funchal","coimbra","setubal","almada","aveiro","evora","faro","guimaraes"]},
    "PL": {"name": "Poland", "tld": ".pl", "cities": ["warsaw","krakow","lodz","wroclaw","poznan","gdansk","szczecin","bydgoszcz","lublin","bialystok","katowice","gdynia","czestochowa"]},
    "UA": {"name": "Ukraine", "tld": ".ua", "cities": ["kyiv","kharkiv","odesa","dnipro","donetsk","zaporizhzhia","lviv","kryvyirih","mykolaiv","mariupol","luhansk","vinnytsia"]},
    "AR": {"name": "Argentina", "tld": ".ar", "cities": ["buenosaires","cordoba","rosario","mendoza","tucuman","laplata","mardelplata","salta","santafe","sanjuan","resistencia","neuquen"]},
    "CO": {"name": "Colombia", "tld": ".co", "cities": ["bogota","medellin","cali","barranquilla","cartagena","cucuta","bucaramanga","pereira","santamarta","ibague","manizales","pasto"]},
    "EG": {"name": "Egypt", "tld": ".eg", "cities": ["cairo","alexandria","giza","shubra","portunsaid","suez","luxor","aswan","tanta","mansoura","ismailia","faiyum"]},
    "ZA": {"name": "South Africa", "tld": ".za", "cities": ["johannesburg","capetown","durban","pretoria","portelizabeth","bloemfontein","nelspruit","polokwane","kimberley","pietermaritzburg"]},
    "ID": {"name": "Indonesia", "tld": ".id", "cities": ["jakarta","surabaya","bandung","medan","semarang","makassar","palembang","tangerang","depok","bekasi","malang","bogor"]},
    "TH": {"name": "Thailand", "tld": ".th", "cities": ["bangkok","chiangmai","pattaya","phuket","hatyai","nakhonratchasima","khonkaen","udonthani","suratthani","chiangrai"]},
    "VN": {"name": "Vietnam", "tld": ".vn", "cities": ["hanoi","hochiminh","danang","haiphong","cantho","nhatrang","hue","dalat","vungtau","quynhon","buonmathuot"]},
    "PK": {"name": "Pakistan", "tld": ".pk", "cities": ["karachi","lahore","islamabad","rawalpindi","faisalabad","multan","peshawar","quetta","sialkot","gujranwala"]},
    "BD": {"name": "Bangladesh", "tld": ".bd", "cities": ["dhaka","chittagong","khulna","rajshahi","sylhet","rangpur","comilla","gazipur","narayanganj","mymensingh"]},
    "IR": {"name": "Iran", "tld": ".ir", "cities": ["tehran","mashhad","isfahan","karaj","shiraz","tabriz","qom","ahvaz","kermanshah","urmia","rasht","zahedan"]},
    "IQ": {"name": "Iraq", "tld": ".iq", "cities": ["baghdad","basra","erbil","mosul","sulaymaniyah","najaf","karbala","kirkuk","nasiriyah","amarah","diwaniyah"]},
    "SA": {"name": "Saudi Arabia", "tld": ".sa", "cities": ["riyadh","jeddah","mecca","medina","dammam","khobar","tabuk","buraidah","khamismushait","hofuf","jubail","yanbu"]},
    "AE": {"name": "UAE", "tld": ".ae", "cities": ["dubai","abudhabi","sharjah","ajman","alain","rasalkhaimah","fujairah","ummalquwain"]},
    "KR": {"name": "South Korea", "tld": ".kr", "cities": ["seoul","busan","incheon","daegu","daejeon","gwangju","suwon","ulsan","changwon","goyang","seongnam"]},
    "PH": {"name": "Philippines", "tld": ".ph", "cities": ["manila","quezoncity","davao","cebu","zamboanga","taguig","antipolo","pasig","cagayandeoro","paranaque"]},
    "MY": {"name": "Malaysia", "tld": ".my", "cities": ["kualalumpur","georgtown","johor","ipoh","kuching","kotakinabalu","shah alam","malacca","seremban","miri"]},
    "SG": {"name": "Singapore", "tld": ".sg", "cities": ["singapore"]},
    "GR": {"name": "Greece", "tld": ".gr", "cities": ["athens","thessaloniki","patras","heraklion","larissa","volos","ioannina","kavala","chania","rhodes"]},
    "CZ": {"name": "Czech Republic", "tld": ".cz", "cities": ["prague","brno","ostrava","plzen","liberec","olomouc","budejovice","hradeckralove","pardubice","zlin"]},
    "RO": {"name": "Romania", "tld": ".ro", "cities": ["bucharest","clujnapoca","timisoara","iasi","constanta","craiova","brasov","galati","ploiesti","oradea"]},
    "HU": {"name": "Hungary", "tld": ".hu", "cities": ["budapest","debrecen","szeged","miskolc","pecs","gyor","nyiregyhaza","kecskemet","szekesfehervar"]},
    "AT": {"name": "Austria", "tld": ".at", "cities": ["vienna","graz","linz","salzburg","innsbruck","klagenfurt","villach","wels","sanktpolten","dornbirn"]},
    "CH": {"name": "Switzerland", "tld": ".ch", "cities": ["zurich","geneva","basel","bern","lausanne","winterthur","lucerne","stgallen","lugano","biel"]},
    "BE": {"name": "Belgium", "tld": ".be", "cities": ["brussels","antwerp","ghent","charleroi","liege","bruges","namur","leuven","mons","aalst"]},
    "DK": {"name": "Denmark", "tld": ".dk", "cities": ["copenhagen","aarhus","odense","aalborg","esbjerg","randers","kolding","horsens","vejle","roskilde"]},
    "FI": {"name": "Finland", "tld": ".fi", "cities": ["helsinki","espoo","tampere","vantaa","oulu","turku","jyvaskyla","lahti","kuopio","kouvola"]},
    "IE": {"name": "Ireland", "tld": ".ie", "cities": ["dublin","cork","limerick","galway","waterford","drogheda","kilkenny","sligo","wexford","athlone"]},
    "IL": {"name": "Israel", "tld": ".il", "cities": ["telaviv","jerusalem","haifa","rishonlezion","petahtikva","ashdod","netanya","beersheva","holon","bneibrak"]},
    "CL": {"name": "Chile", "tld": ".cl", "cities": ["santiago","valparaiso","concepcion","antofagasta","vina","temuco","rancagua","talca","arica","iquique"]},
    "PE": {"name": "Peru", "tld": ".pe", "cities": ["lima","arequipa","trujillo","chiclayo","piura","cusco","iquitos","huancayo","tacna","juliaca"]},
    "NG": {"name": "Nigeria", "tld": ".ng", "cities": ["lagos","kano","ibadan","abuja","portuharcourt","benin","maiduguri","zaria","aba","jos","ilorin"]},
    "KE": {"name": "Kenya", "tld": ".ke", "cities": ["nairobi","mombasa","kisumu","nakuru","eldoret","thika","malindi","kitale","garissa","nyeri"]},
    "GH": {"name": "Ghana", "tld": ".gh", "cities": ["accra","kumasi","tamale","takoradi","ashaiman","sunyani","capetown","obuasi","tema","teshie"]},
    "MA": {"name": "Morocco", "tld": ".ma", "cities": ["casablanca","rabat","fes","marrakech","tangier","meknes","oujda","kenitra","agadir","tetouan"]},
    "TN": {"name": "Tunisia", "tld": ".tn", "cities": ["tunis","sfax","sousse","kairouan","bizerte","gabes","ariana","gafsa","monastir","benarous"]},
    "NZ": {"name": "New Zealand", "tld": ".nz", "cities": ["auckland","wellington","christchurch","hamilton","tauranga","napier","dunedin","palmerston","nelson","rotorua"]},
}

INDUSTRIES = [
    "hospital", "university", "school", "bank", "hotel", "shop", "store",
    "market", "news", "blog", "forum", "government", "military", "police",
    "court", "library", "museum", "church", "mosque", "restaurant", "clinic",
    "pharmacy", "insurance", "travel", "airline", "shipping", "logistics",
    "factory", "mining", "energy", "telecom", "media", "entertainment",
    "sports", "fashion", "beauty", "automotive", "realestate", "construction",
    "agriculture", "finance", "consulting", "education", "healthcare",
    "technology", "startup", "ecommerce", "nonprofit", "legal", "accounting",
]

VULN_KEYWORDS = [
    "login", "admin", "dashboard", "panel", "upload", "register", "signup",
    "password", "config", "setup", "install", "backup", "database", "debug",
    "error", "test", "dev", "staging", "beta", "demo", "api", "token",
    "secret", "private", "internal", "legacy", "old", "temp", "tmp",
]


class KeywordGenerator:
    """Auto-generates keywords per country"""

    def __init__(self):
        self.db = COUNTRY_DB

    def get_country_codes(self):
        return list(self.db.keys())

    def get_country_names(self):
        return [v["name"] for v in self.db.values()]

    def generate_for_country(self, code, include_cities=True, include_tld=True, include_industries=True):
        """Generate all keywords for a single country"""
        code = code.upper()
        if code not in self.db:
            return []
        country = self.db[code]
        keywords = []
        keywords.append(country["name"].lower())
        if include_tld:
            keywords.append(f"site:{country['tld']}")
        if include_cities:
            keywords.extend(country["cities"])
        if include_industries:
            for ind in INDUSTRIES:
                keywords.append(f"site:{country['tld']} {ind}")
        return keywords

    def generate_all_countries(self, include_cities=True, include_tld=True, include_industries=False):
        """Generate keywords for ALL countries"""
        all_kw = []
        for code in self.db:
            all_kw.extend(self.generate_for_country(code, include_cities, include_tld, include_industries))
        return list(dict.fromkeys(all_kw))  # dedupe preserving order

    def generate_tlds_only(self):
        """Get all TLDs"""
        tlds = set()
        for v in self.db.values():
            tlds.add(f"site:{v['tld']}")
        tlds.update(["site:.com","site:.net","site:.org","site:.edu","site:.gov","site:.io","site:.info","site:.biz","site:.xyz"])
        return sorted(tlds)

    def generate_cities_only(self, country_code=None):
        """Get cities, optionally filtered by country"""
        cities = []
        if country_code:
            code = country_code.upper()
            if code in self.db:
                cities = self.db[code]["cities"]
        else:
            for v in self.db.values():
                cities.extend(v["cities"])
        return cities

    def list_countries(self):
        """Print all supported countries"""
        print(f"\n  {'Code':<6}{'Country':<20}{'TLD':<8}{'Cities'}")
        print(f"  {'-'*50}")
        for code, data in sorted(self.db.items()):
            print(f"  {code:<6}{data['name']:<20}{data['tld']:<8}{len(data['cities'])}")
        print(f"\n  Total: {len(self.db)} countries\n")


# Build KEYWORDS dict dynamically for backward compat
_kg = KeywordGenerator()
KEYWORDS = {
    "countries": [v["name"].lower() for v in COUNTRY_DB.values()],
    "tlds": _kg.generate_tlds_only(),
    "industries": INDUSTRIES,
    "vuln_keywords": VULN_KEYWORDS,
    "all_cities": _kg.generate_cities_only(),
}

# ============================================================
# DORK GENERATOR CLASS
# ============================================================

class DorkGenerator:
    """Professional Google Dork Generator for Bug Bounty Research"""

    def __init__(self):
        self.cms_templates = {
            "wordpress": WORDPRESS_DORKS,
            "joomla": JOOMLA_DORKS,
            "drupal": DRUPAL_DORKS,
            "magento": MAGENTO_DORKS,
            "prestashop": PRESTASHOP_DORKS,
            "opencart": OPENCART_DORKS,
            "laravel": LARAVEL_DORKS,
            "generic": GENERIC_DORKS,
        }
        self.generated = []

    def generate(self, cms_list=None, keyword_cats=None, custom_keywords=None, limit=0, shuffle=False):
        """Generate dorks with given parameters"""
        self.generated = []

        # Select CMS templates
        if not cms_list or "all" in cms_list:
            cms_list = list(self.cms_templates.keys())

        # Build keyword list
        keywords = []
        if custom_keywords:
            keywords.extend(custom_keywords)
        if keyword_cats:
            for cat in keyword_cats:
                if cat in KEYWORDS:
                    keywords.extend(KEYWORDS[cat])
        if not keywords:
            keywords = [""]  # Empty = no keyword appended

        # Generate combinations
        for cms in cms_list:
            templates = self.cms_templates.get(cms, [])
            for template in templates:
                for kw in keywords:
                    dork = template.replace("{keyword}", kw).strip()
                    if dork not in self.generated:
                        self.generated.append(dork)

        if shuffle:
            random.shuffle(self.generated)

        if limit > 0:
            self.generated = self.generated[:limit]

        return self.generated

    def save(self, filename, fmt="txt"):
        """Save generated dorks to file"""
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        if not filename:
            filename = f"dorks_{ts}.{fmt}"

        if fmt == "json":
            data = {
                "generated_at": ts,
                "total": len(self.generated),
                "dorks": self.generated,
            }
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# Google Dorks - Generated {ts}\n")
                f.write(f"# Total: {len(self.generated)}\n\n")
                for dork in self.generated:
                    f.write(dork + "\n")

        print(f"[+] {len(self.generated)} dorks saved to: {filename}")
        return filename

    def stats(self):
        """Print generation statistics"""
        cms_counts = {}
        for cms, templates in self.cms_templates.items():
            cms_counts[cms] = len(templates)

        print(f"\n{'='*55}")
        print(f"  DORK GENERATOR STATISTICS")
        print(f"{'='*55}")
        print(f"  Generated dorks : {len(self.generated)}")
        print(f"  CMS Templates   :")
        for cms, count in cms_counts.items():
            print(f"    {cms:15s}: {count} templates")
        print(f"  Keyword categories: {len(KEYWORDS)}")
        for cat, kws in KEYWORDS.items():
            print(f"    {cat:15s}: {len(kws)} keywords")
        print(f"{'='*55}\n")


# ============================================================
# BANNER & CLI
# ============================================================

BANNER = """
  +==================================================+
  |     ADVANCED GOOGLE DORK GENERATOR v3.0          |
  |     Bug Bounty & Security Research Tool          |
  |     All CMS Platforms Supported                  |
  +==================================================+
"""

def interactive_mode():
    """Run in interactive mode"""
    gen = DorkGenerator()
    kg = KeywordGenerator()

    print(BANNER)
    print("  Available CMS: wordpress, joomla, drupal, magento,")
    print("                  prestashop, opencart, laravel, generic, all")
    print("  Keyword cats : countries, tlds, industries, vuln_keywords, all_cities")
    print(f"{'='*55}\n")

    # List countries?
    show = input("[?] List supported countries? (y/n): ").strip().lower()
    if show == "y":
        kg.list_countries()

    # Country selection
    country_input = input("[?] Country codes (e.g. TR,US,DE or 'all'): ").strip()
    country_keywords = []
    if country_input:
        if country_input.lower() == "all":
            country_keywords = kg.generate_all_countries()
        else:
            codes = [c.strip().upper() for c in country_input.split(",") if c.strip()]
            for code in codes:
                country_keywords.extend(kg.generate_for_country(code))

    # CMS selection
    cms_input = input("[?] CMS (comma-separated, or 'all'): ").strip()
    cms_list = [c.strip().lower() for c in cms_input.split(",") if c.strip()]
    if not cms_list:
        cms_list = ["all"]

    # Additional keyword categories
    cat_input = input("[?] Extra keyword categories (comma-separated, optional): ").strip()
    keyword_cats = []
    if cat_input:
        if cat_input.lower() == "all":
            keyword_cats = list(KEYWORDS.keys())
        else:
            keyword_cats = [c.strip().lower() for c in cat_input.split(",") if c.strip()]

    # Custom keywords
    custom_input = input("[?] Custom keywords (comma-separated, optional): ").strip()
    custom_kw = list(country_keywords)  # start with country keywords
    if custom_input:
        custom_kw.extend([c.strip() for c in custom_input.split(",") if c.strip()])

    # Limit
    limit_input = input("[?] Limit (0 = no limit): ").strip()
    limit = int(limit_input) if limit_input.isdigit() else 0

    # Shuffle
    shuffle = input("[?] Shuffle results? (y/n): ").strip().lower() == "y"

    # Output format
    fmt = input("[?] Output format (txt/json): ").strip().lower()
    if fmt not in ("txt", "json"):
        fmt = "txt"

    # Output file
    out_file = input("[?] Output filename (Enter = auto): ").strip()
    if not out_file:
        out_file = None

    # Generate
    print("\n[*] Generating dorks...")
    cats_to_use = keyword_cats if keyword_cats else None
    custom_to_use = custom_kw if custom_kw else None
    dorks = gen.generate(cms_list, cats_to_use, custom_to_use, limit, shuffle)
    gen.stats()
    gen.save(out_file, fmt)

    # Preview
    print(f"\n[*] Preview (first 15):")
    for i, d in enumerate(dorks[:15], 1):
        print(f"  {i:3d}. {d}")
    if len(dorks) > 15:
        print(f"  ... and {len(dorks)-15} more")


def main():
    parser = argparse.ArgumentParser(
        description="Advanced Google Dork Generator v3.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python dork_generator.py -i
  python dork_generator.py --cms wordpress --country TR
  python dork_generator.py --cms all --country all
  python dork_generator.py --cms joomla --country TR,DE,FR
  python dork_generator.py --cms wordpress --cats tlds --keywords hotel,bank
  python dork_generator.py --list-countries
        """,
    )
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("--cms", default="all", help="CMS list (comma-separated)")
    parser.add_argument("--cats", default="", help="Keyword categories (comma-separated)")
    parser.add_argument("--keywords", default="", help="Custom keywords (comma-separated)")
    parser.add_argument("--country", default="", help="Country codes (e.g. TR,US,DE or 'all')")
    parser.add_argument("--list-countries", action="store_true", help="List all supported countries")
    parser.add_argument("--limit", type=int, default=0, help="Max dork count")
    parser.add_argument("--shuffle", action="store_true", help="Shuffle output")
    parser.add_argument("--format", choices=["txt", "json"], default="txt", help="Output format")
    parser.add_argument("-o", "--output", default="", help="Output file")

    args = parser.parse_args()

    if args.list_countries:
        print(BANNER)
        KeywordGenerator().list_countries()
        return

    if args.interactive:
        interactive_mode()
        return

    print(BANNER)

    gen = DorkGenerator()
    kg = KeywordGenerator()

    cms_list = [c.strip() for c in args.cms.split(",") if c.strip()]
    cats = [c.strip() for c in args.cats.split(",") if c.strip()] if args.cats else None

    # Build custom keywords from country + manual keywords
    custom = []
    if args.country:
        if args.country.lower() == "all":
            custom.extend(kg.generate_all_countries())
        else:
            codes = [c.strip().upper() for c in args.country.split(",") if c.strip()]
            for code in codes:
                custom.extend(kg.generate_for_country(code))

    if args.keywords:
        custom.extend([c.strip() for c in args.keywords.split(",") if c.strip()])

    custom = custom if custom else None

    dorks = gen.generate(cms_list, cats, custom, args.limit, args.shuffle)
    gen.stats()
    gen.save(args.output or None, args.format)

    print(f"\n[*] Preview (first 10):")
    for i, d in enumerate(dorks[:10], 1):
        print(f"  {i:3d}. {d}")
    if len(dorks) > 10:
        print(f"  ... and {len(dorks)-10} more")


if __name__ == "__main__":
    main()

