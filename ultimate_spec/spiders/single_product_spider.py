import scrapy
import csv

from ..items import BrandItem


class SingleCarUltimateSpecSpider(scrapy.Spider):

    name = 'ultimate_single_car'

    # def get_link(self):
    #     str_link = None
    #     with open('link.csv', encoding='utf-8-sig') as csvFile:
    #         reader = csv.reader(csvFile)
    #         count = 0
    #
    #         for row in reader:
    #             count = count + 1
    #             if count > 2:
    #                 if str_link is None:
    #                     print('mujib la sani')
    #                     str_link = row[0]
    #
    #                 else:
    #                     str_link = str_link + ',' + row[0]
    #     return str_link
    #
    # link_lists = get_link().split(',')
    # with open('single.csv', 'w', newline='') as file:
    #     custom_writer = csv.writer(file)
    #     for link in link_lists:
    #         custom_writer.writerow(['https://www.ultimatespecs.com' + link])
    #
    # with open('single.csv') as csvFile:
    #     start_urls = [line.strip() for line in csvFile]
    #
    #     def parse(self, response, **kwargs):
    #         items = BrandItem()
    #         car_lists = response.css('.somerow')
    #         for car_item in car_lists:
    #             car_series_name = car_item.css('h2::text').extract()  # .a-color-base.a-text-normal
    #             car_model_name = car_item.css('.someOtherRow a::text').extract()
    #             car_model_link = car_item.css('.someOtherRow a::attr(href)').extract()
    #
    #             items['car_series_name'] = car_series_name
    #             items['car_model_name'] = car_model_name
    #             items['car_model_link'] = car_model_link
    #
    #             yield items
    pass
