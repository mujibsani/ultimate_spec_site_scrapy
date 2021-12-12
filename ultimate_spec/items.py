# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UlimateSpecItem(scrapy.Item):
    # define the fields for your item here like:
    # car_series_name = scrapy.Field()
    pass


class BrandItem(scrapy.Item):
    car_series_name = scrapy.Field()
    car_model_name = scrapy.Field()
    car_model_link = scrapy.Field()


class SingleCarSpecItem(scrapy.Item):
    car_name = scrapy.Field()
    car_image = scrapy.Field()
    car_description = scrapy.Field()
    car_left = scrapy.Field()
    car_right = scrapy.Field()


class SingleCarSpecPracticeItem(scrapy.Item):
    car_name = scrapy.Field()
    car_image = scrapy.Field()
    car_description = scrapy.Field()

    car_num_of_cylinder = scrapy.Field()
    car_engine_code = scrapy.Field()
    car_fuel_type = scrapy.Field()
    car_fuel_system = scrapy.Field()
    car_engine_alighnment = scrapy.Field()
    car_rngine_position = scrapy.Field()
    car_engine_capacity = scrapy.Field()
    car_bore_x_stroke = scrapy.Field()
    car_number_of_velve = scrapy.Field()
    car_aspiration = scrapy.Field()
    car_compression_ratio = scrapy.Field()
    car_maximum_power_output_horsepower = scrapy.Field()
    car_maximum_torque = scrapy.Field()
    car_drive_wheel_traction_drivetrain = scrapy.Field()
    car_transmission_gearbox_number_of_speed = scrapy.Field()
    car_combined_power = scrapy.Field()
    car_combined_torque = scrapy.Field()
    car_number_of_electric_engine = scrapy.Field()
    car_electric_engine_type = scrapy.Field()
    car_fuel_low_wltp = scrapy.Field()
    car_fuel_medium_wltp = scrapy.Field()
    car_fuel_high_wltp = scrapy.Field()
    car_fuel_extra_high_wltp = scrapy.Field()
    car_fuel_combined_wltp = scrapy.Field()
    car_range_wltp = scrapy.Field()
    car_fuel_tank_capacity = scrapy.Field()
    car_co2_emission = scrapy.Field()
    car_co2_emission_wltp = scrapy.Field()
