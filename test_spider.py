#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by betalun on 3/31/17

# from pyspider.libs.base_handler import *

import datetime
import click

# class Handler(BaseHandler):
#     crawl_config = {
#     }
#
#     @every(minutes=24 * 60)
#     def on_start(self):
#         self.crawl('http://scrapy.org/', callback=self.index_page)
#
#     @config(age=10 * 24 * 60 * 60)
#     def index_page(self, response):
#         for each in response.doc('a[href^="http"]').items():
#             self.crawl(each.attr.href, callback=self.detail_page)
#
#     @config(priority=2)
#     def detail_page(self, response):
#         return {
#             "url": response.url,
#             "title": response.doc('title').text(),
#         }


@click.command()
@click.option("--name",help="this is the name")
def test(name):
    click.echo(";;;;;;;")


if __name__ == '__main__':
    test()