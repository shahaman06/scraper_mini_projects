# -*- coding: utf-8 -*-
import scrapy
from ..items import AmzScraperItem


class AmzSpiderSpider(scrapy.Spider):
    name = "amz_spider"
    page_number = 1
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.in/s?k=masala&i=pantry&srs=9574332031&ref=nb_sb_noss"
    ]

    def parse(self, response):

        items = AmzScraperItem()
        items["name"] = response.css("span.a-color-base.a-text-normal::text").extract()
        items["image"] = response.css(".s-image::attr(src)").extract()

        yield items
        self.page_number += 1
        next_page = (
            "https://www.amazon.in/s?k=masala&i=pantry&srs=9574332031&page="
            + str(self.page_number)
            + "&qid=1580090298&ref=sr_pg_"
            + str(self.page_number)
        )

        if self.page_number <= 3:
            yield response.follow(next_page, callback=self.parse)
