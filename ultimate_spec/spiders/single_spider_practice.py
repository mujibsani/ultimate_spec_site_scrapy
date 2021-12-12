import scrapy
from ..items import SingleCarSpecItem


class SingleItemScrap2(scrapy.Spider):
    name = 'single_prac'
    start_urls = [
        'https://www.ultimatespecs.com/car-specs/Toyota/122665/Toyota-Highlander-25-Hybrid-AWD.html'
    ]

    def parse(self, response, **kwargs):
        counter = 0
        items = SingleCarSpecItem()

        car_specs = response.css('.col-md-pull-4')

        for car_spec in car_specs:
            car_name = car_spec.css('.page_ficha_title_text span::text').extract()
            car_image = car_spec.css('.left_column_top_model_image::attr(src)').extract()
            car_description = car_spec.css('.resumo_ficha > .row .col-md-6+ .col-md-6::text').extract()
            car_single_specs = car_spec.css('.tabletd_right , .tabletd')

            items['car_name'] = car_name
            items['car_image'] = car_image
            items['car_description'] = car_description
            for car_single_spec in car_single_specs:
                car_left = car_single_spec.css('.tabletd::text').extract()
                car_right = car_single_spec.css('.tabletd_right::text').extract()
                if counter == 1:
                    items['car_name'] = ''
                    items['car_image'] = ''
                    items['car_description'] = ''
                    items['car_left'] = car_left
                    items['car_right'] = car_right
                else:
                    counter = 1
                    items['car_left'] = car_left
                    items['car_right'] = car_right

                yield items
        counter = 0
