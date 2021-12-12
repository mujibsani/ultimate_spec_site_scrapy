import scrapy
from ..items import BrandItem


class BrandCarUltimateSpecSpider(scrapy.Spider):
    name = 'ultimate_name_link'
    start_urls = [
        'https://www.ultimatespecs.com/car-specs/Toyota'
    ]

    def parse(self, response, **kwargs):
        items = BrandItem()
        car_lists = response.css('.somerow')
        for car_item in car_lists:
            car_series_name = car_item.css('h2::text').extract()  # .a-color-base.a-text-normal
            car_model_name = car_item.css('.someOtherRow a::text').extract()
            car_model_link = car_item.css('.someOtherRow a::attr(href)').extract()

            items['car_series_name'] = car_series_name
            items['car_model_name'] = car_model_name
            items['car_model_link'] = car_model_link

            yield items
