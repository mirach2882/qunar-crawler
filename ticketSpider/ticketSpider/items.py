# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from ticketSpider.elasticsearch_orm import qunarType



class TicketspiderItem(scrapy.Item):
    id = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    point = scrapy.Field()
    sight = scrapy.Field()
    level = scrapy.Field()
    price = scrapy.Field()
    count = scrapy.Field()
    intro = scrapy.Field()
    img_url = scrapy.Field()
    detail_url = scrapy.Field()
    score = scrapy.Field()
    desc = scrapy.Field()
    pic_url = scrapy.Field()

    def save_to_es(item):
        qunar = qunarType()
        qunar.id = item['id']
        qunar.area = item['area']
        qunar.address = item['address']
        qunar.point =item['point']
        qunar.sight = item['sight']
        qunar.level = item['level']
        qunar.price = item['price']
        qunar.count = item['count']
        qunar.img_url = item['img_url']
        qunar.detail_url = item['detail_url']
        qunar.score = item['score']
        qunar.desc = item['desc']
        qunar.save()
        return
    pass
