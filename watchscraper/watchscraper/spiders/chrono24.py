import datetime
import re
import scrapy
from ..items import WatchscraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class WatchSpiderChrono24(CrawlSpider):
    custom_settings = {
        'CONCURRENT_REQUESTS': 32
    }
    name = "chrono24"
    allowed_domains = ["chrono24.de"]
    start_urls = {
        "https://www.chrono24.de"
    }
    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.RFPDupeFilter'
    }

    # response.css("#main-content a::text").extract() für die namen
    uhrenmarken_roh = ['/rolex/index.htm', '/omega/index.htm', '/iwc/index.htm', '/breitling/index.htm', '/hublot/index.htm', '/panerai/index.htm', '/tagheuer/index.htm', '/cartier/index.htm', '/zenith/index. htm', '/patekphilippe/index.htm', '/audemarspiguet/index.htm', '/jaegerlecoultre/index.htm', '/alangesoehne/index.htm', '/tudor/index.htm', '/longines/index.htm', '/sinn/index.htm', '/chopard/index.htm', '/blancpain/index.htm', '/franckmuller/index.htm', '/glashuetteoriginal/index.htm', '/bellross/index.htm', '/girardperregaux/index.htm', '/mauricelacroix/index.htm', '/ chronoswiss/index.htm', '/alangesoehne/index.htm', '/abpparis/index.htm', '/aerowatch/index.htm', '/aigle/index.htm', '/aigner/index.htm', '/alainsilberstein/index.htm', '/alexandershorokhoff/index.htm', '/alfreddunhill/index.htm', '/alfredrochatfils/index.htm', '/alpina/index.htm', '/andersengenve/index.htm', '/angelus/index.htm', '/angularmomentum/index.htm', '/anonimo/index.htm', '/apple/index.htm', '/aquanautic/index.htm', '/aquastar/index.htm', '/aristo/index.htm', '/armandnicolet/index.htm', '/armani/index.htm', '/arminstrom/index.htm', '/arnoldson/index.htm', '/artisanal/index.htm', '/artya/index.htm', '/askania/index.htm', '/ateliersdemonaco/index.htm', '/atlantic/index.htm', '/audemarspiguet/index.htm', '/augustereymond/index .htm', '/auricoste/index.htm', '/avier/index.htm', '/azimuth/index.htm', '/azzaro/index.htm', '/brm/index.htm', '/ball/index.htm', '/balmain/index.htm', '/barington/index.htm', '/baumemercier/index.htm', '/bedatco/index.htm', '/behrens/index.htm', '/bellross/index.htm', '/benrus/index.htm', '/benzinger/index.htm', '/bertolucci/index.htm', '/beuchat/index.htm', '/bifora/index.htm', '/blackoutconcept/index.htm', '/blancpain/index.htm', '/blu/index.htm', '/boegli/index.htm', '/bognertime/index.htm', '/boldr/index.htm', '/bomberg/index.htm', '/boucheron/index.htm', '/bovet/index.htm', '/breguet/index.htm', '/breil/index.htm', '/breitling/index.htm', '/bremont/index.htm', '/brunosoehnle/index.htm', '/bulgari/index.htm', '/bulova/index.htm', '/bunz/index.htm', '/burberry/index.htm', '/bwcswiss/index.htm', '/chwolf/index.htm', '/cabestan/index.htm', '/cadetchronostar/index.htm', '/camelactive/index.htm', '/camillefournet/index.htm', '/candino/index.htm', '/carlfbucherer/index.htm', '/carloferrara/index.htm', '/cartier/index.htm', '/casio/index.htm', '/catena/index.htm', '/catorex/index.htm', '/cattin/index .htm', '/century/index.htm', '/cerruti/index.htm', '/certina/index.htm', '/chanel/index.htm', '/charmex/index.htm', '/charriol/index.htm', '/chasedurer/index.htm', '/chaumet/index.htm',  '/chopard/index.htm', '/chrisbenz/index.htm', '/christiaanvdklaauw/index.htm', '/christofle/index.htm', '/christopheclaret/index.htm', '/christopherward/index.htm', '/chronographesuissec ie/index.htm', '/chronoswiss/index.htm', '/churpfaelzischeuhrenmanufaktur/index.htm', '/citizen/index.htm', '/ckcalvinklein/index.htm', '/claudebernard/index.htm', '/claudemeylan/index.htm', '/clerc/index.htm', '/concord/index.htm', '/condor/index.htm', '/cornehl/index.htm', '/cortebert/index.htm', '/corum/index.htm', '/cronus/index.htm', '/cuervoysobrinos/index.htm', ' /cvstos/index.htm', '/cwc/index.htm', '/cyclos/index.htm', '/cyma/index.htm', '/cyrus/index.htm', '/ddornbluethsohn/index.htm', '/damasko/index.htm', '/danielroth/index.htm', '/davidoff/index.htm', '/davosa/index.htm', '/debethune/index.htm', '/degrisogono/index.htm', '/decade/index.htm', '/deepblue/index.htm', '/delacour/index.htm', '/delaneau/index.htm', '/delma/index.htm', '/devon/index.htm', '/dewitt/index.htm', '/diesel/index.htm', '/dietrich/index.htm', '/dior/index.htm', '/dodane/index.htm', '/dolcegabbana/index.htm', '/dombaizinternational/index.htm', '/doxa/index.htm', '/dubeyschaldenbrand/index.htm', '/dubois1785/index.htm', '/duboisetfils/index.htm', '/dufeau/index.htm', '/dugena/index.htm', '/ebel/index.htm', '/eberhardco/index.htm', '/edox/index.htm', '/eichmueller/index.htm', '/election/index.htm', '/elgin/index.htm', '/elysee/index.htm', '/engelhardt/index.htm', '/enicar/index.htm', '/ennebi/index.htm', '/epos/index.htm', '/ernestborel/index.htm', '/ernstbenz/index.htm', '/erwinsattler/index.htm', '/esprit/index.htm', '/eterna/index.htm', '/eulit/index.htm', '/eulux/index.htm', '/fpjourne/index.htm', '/faberge/index.htm', '/favreleuba/index.htm', '/feldo/index.htm', '/fendi/index.htm', '/festina/index.htm', '/fluco/index.htm', '/fludo/index.htm', '/formex/index.htm',  '/fortis/index.htm', '/forum/index.htm', '/fossil/index.htm', '/francvila/index.htm', '/franckdubarry/index.htm', '/franckmuller/index.htm', '/frederiqueconstant/index.htm', '/gagamilano/index.htm', '/gallet/index.htm', '/gant/index.htm', '/garde/index.htm', '/garmin/index.htm', '/germanowalter/index.htm', '/gevril/index.htm', '/gigandet/index.htm', '/girardperregaux/index.htm', '/giulianomazzuoli/index.htm', '/glashuetteoriginal/index.htm', '/glycine/index.htm', '/graf/index.htm', '/graham/index.htm', '/grandseiko/index.htm', '/greubelforsey/index.htm', '/grovana/index.htm', '/gruen/index.htm', '/groenefeld/index.htm', '/gubglashuette/index.htm', '/gucci/index.htm', '/guess/index.htm', '/geraldgenta/index.htm', '/guebelin/index.htm', '/hidwatch/index.htm', '/hmosercie/index.htm', '/habring/index.htm', '/hacher/index.htm', '/haemmer/index.htm', '/hagal/index.htm', '/hamilton/index.htm', '/hanhart/index.htm', '/harrywinston/index.htm', '/hautlence/index.htm', '/hd3/index.htm', '/hebdomas/index.htm', '/helvetia/index.htm', '/hentschelhamburg/index.htm', '/herms/index.htm', '/herzog/index.htm', '/heuer/index.htm', '/hirsch/index.htm', '/hublot/index.htm', '/hugoboss/index.htm', '/hyt/index.htm', '/icewatch/index.htm', '/ikepod/index.htm', '/illinois/index.htm', '/ingersoll/index.htm', '/invicta/index.htm', '/ironannie/index.htm', '/itaynoy/index.htm', '/iwc/index.htm', '/jacobco/index.htm', '/jacquesetoile/index.htm', '/jacqueslemans/index.htm', '/jaegerlecoultre/index.htm', '/jaermannstuebi/index.htm', '/jaquetdroz/index.htm', '/jbgioacchino/index.htm', '/jeandeve/index.htm', '/jeanlassale/index.htm', '/jeanmarcel/index.htm', '/jeanrichard/index.htm', '/joop/index.htm', '/jorghysek/index.htm', '/julesjuergensen/index.htm', '/junghans/index.htm', '/junkers/index.htm', '/juvenia/index.htm', '/kelek/index.htm', '/khs/index.htm', '/kienzle/index.htm', '/kobold/index.htm', '/konstantinchaykin/index.htm', '/korloff/index.htm', '/krieger/index.htm', '/kronsegler/index.htm', '/lepee/index.htm', '/lleroy/index.htm', '/laco/index.htm', '/lacoste/index.htm', '/lancaster/index.htm', '/lanco/index.htm', '/langheyne/index.htm', '/laurentferrier/index.htm', '/lebeaucourally/index.htm', '/leinfelder/index.htm', '/lemania/index.htm', '/leonidas/index.htm', '/limes/index.htm', '/lindewerdelin/index.htm', '/lip/index.htm', '/livwatches/index.htm', '/locman/index.htm', '/longines/index.htm', '/longio/index.htm', '/lorenz/index.htm', '/lorus/index.htm', '/louiserard/index.htm', '/louismoinet/index.htm', '/louisvuitton/index.htm', '/louisxvi/index.htm', '/lucienrochat/index.htm',  '/ludovicballouard/index.htm', '/luminox/index.htm', '/luemtec/index.htm', '/mmswisswatch/index.htm', '/madeditions/index.htm', '/marcelloc/index.htm', '/margi/index.htm', '/marlboro/index.htm', '/martinbraun/index.htm', '/marvin/index.htm', '/maserati/index.htm', '/matheytissot/index.htm', '/mauboussin/index.htm', '/mauriceblum/index.htm', '/mauricedemauriac/index.htm', '/mauricelacroix/index.htm', '/mbf/index.htm', '/meccanicheveloci/index.htm', '/meistersinger/index.htm', '/mercure/index.htm', '/mercury/index.htm', '/meva/index.htm', '/meyers/index.htm', '/michaelkors/index.htm', '/michelherbelin/index.htm', '/micheljordi/index.htm', '/michele/index.htm', '/mido/index.htm', '/milleret/index.htm', '/milus/index.htm', '/minerva/index.htm', '/momentum/index.htm', '/momodesign/index.htm', '/mondaine/index.htm', '/mondia/index.htm', '/montblanc/index.htm', '/montega/index.htm', '/morellato/index.htm', '/moritzgrossmann/index.htm', '/movado/index.htm', '/muehleglashuette/index.htm', '/nbyaeeger/index.htm', '/noa/index.htm', '/nautica/index.htm', '/nauticfish/index.htm', '/nethuns/index.htm', '/nike/index.htm', '/ninaricci/index.htm', '/nivada/index.htm', '/nivrel/index.htm', '/nixon/index.htm', '/nomos/index.htm', '/nouvellehorlogeriecalabresenhc/index.htm', '/officinadeltempo/index.h tm', '/ollechwajs/index.htm', '/omega/index.htm', '/orator/index.htm', '/orbita/index.htm', '/orfina/index.htm', '/orient/index.htm', '/oris/index.htm', '/outoforder/index.htm', '/pacardt/index.htm', '/panerai/index.htm', '/parmigianifleurier/index.htm', '/patekphilippe/index.htm', '/paulpicot/index.htm', '/pequignet/index.htm', '/perigaum/index.htm', '/perrelet/index.htm', '/perseo/index.htm', '/phantoms/index.htm', '/philipstein/index.htm', '/philipwatch/index.htm', '/piaget/index.htm', '/pierrebalmain/index.htm', '/pierrecardin/index.htm', '/pierredn/eco-drive-one--mod2930.htm', '/panerai/luminor-submersible--mod134.htm', '/panerai/radiomir-1940-3-days--mod1970.htm', '/cartier/tank--mod186.htm', '/cartier/santos--mod180.htm']
    uhrenmarken = []
    for item in uhrenmarken_roh:
        new_item = item.split('/')[1]
        uhrenmarken.append('/' + new_item)

    print(uhrenmarken)
    # uhrenmarken = ('/rolex')

    rules = (
        Rule(LinkExtractor(allow=r"watches", deny=uhrenmarken)),
        Rule(LinkExtractor(allow=uhrenmarken), callback="parse_item", follow=True)
    )

    def parse_item(self, response):
        items = WatchscraperItem()

        # response.css("td span::text").extract()
        # response.css("td a::text").extract()
        # response.css("td::text").extract()

        main_facts = response.css("td a::text").extract()

        facts_array = response.css(".col-md-12 td::text, .p-r-2 strong::text").extract()

        print(main_facts)
        # values = response.css("td::text").extract()
        # print(values)

        if len(main_facts) > 0 and len(main_facts) > 3 and main_facts[2] is not None and not main_facts[0].startswith("\n"):
            try:
                brand = main_facts[0]
            except:
                brand = None
            try:
                model = main_facts[1]
            except:
                model = None
            try:
                reference = main_facts[2]
            except:
                reference = None
            try:
                movement_type = facts_array[facts_array.index("Aufzug") + 1]
            except:
                movement_type = None
            try:
                size = response.css("#detail-page-dealer .col-md-12 span::text").extract()[0]
            except:
                size = None
            try:
                gender = main_facts[3]
            except:
                gender = None
            try:
                SKU = facts_array[facts_array.index("Inseratscode") + 1]
            except:
                SKU = None
            try:
                price = response.css(".js-price-shipping-country::text").extract()[0]
            except:
                price = None
            try:
                scope_of_delivery = response.css(".col-md-12 .justify-content-between::text").extract()[0]
            except:
                scope_of_delivery = None
            try:
                production_date = facts_array[facts_array.index("Herstellungsjahr") + 1]
            except:
                production_date = None
            try:
                availability = facts_array[facts_array.index("Verfügbarkeit") + 1]
            except:
                availability = None
            try:
                location = facts_array[facts_array.index("Standort") + 1]
            except:
                location = None
            try:
                condition = response.css(".text-link.js-conditions::text").extract()[0]
            except:
                condition = None
            try:
                case_material = facts_array[facts_array.index("Material Gehäuse") + 1]
            except:
                case_material = None
            try:
                strap_material = facts_array[facts_array.index("Material Armband") + 1]
            except:
                strap_material = None
            try:
                bezel_material = facts_array[facts_array.index("Material Lünette") + 1]
            except:
                bezel_material = None
            try:
                glas = facts_array[facts_array.index("Glas") + 1]
            except:
                glas = None
            try:
                dial = facts_array[facts_array.index("Zifferblatt") + 1]
            except:
                dial = None
            try:
                strap_colour = facts_array[facts_array.index("Farbe Armband") + 1]
            except:
                strap_colour = None
            try:
                clasp = facts_array[facts_array.index("Schließe") + 1]
            except:
                clasp = None
            try:
                clasp_material = facts_array[facts_array.index("Material Schließe") + 1]
            except:
                clasp_material = None
            try:
                movement = facts_array[facts_array.index("Kaliber/Werk") + 1]
            except:
                movement = None
            try:
                extra = facts_array
            except:
                extra = None
            try:
                features = response.css("tbody:nth-child(5) tr+ tr .p-r-2::text").extract()[0]
            except:
                features = None
            try:
                delivery_cost = response.css(".js-delivery-cost::text").extract()[0]
            except:
                delivery_cost = None
            try:
                seller_type = response.css(".p-a-0.text-link::text").extract()[0]
            except:
                seller_type = None


            items["price"] = price
            items["brand"] = brand
            items["model"] = model
            items["reference"] = reference
            items["movement_type"] = movement_type
            items["size"] = size
            items["gender"] = gender
            items["SKU"] = SKU
            items["time"] = datetime.datetime.now()
            items["source"] = "chrono24"
            items["scope_of_delivery"] = scope_of_delivery
            items["production_date"] = production_date
            items["availability"] = availability
            items["location"] = location
            items["condition"] = condition
            items["case_material"] = case_material
            items["strap_material"] = strap_material
            items["bezel_material"] = bezel_material
            items["glas"] = glas
            items["dial"] = dial
            items["strap_colour"] = strap_colour
            items["clasp"] = clasp
            items["clasp_material"] = clasp_material
            items["movement"] = movement
            items["extra"] = extra
            items["features"] = features
            items["delivery_cost"] = delivery_cost
            items["seller_type"] = seller_type


            if brand is not None:
                yield items
