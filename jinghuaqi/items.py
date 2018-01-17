# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JinghuaqiItem(scrapy.Item):
    # define the fields for your item here like:
    #商品名称
    p_Name = scrapy.Field()
    #店铺名称
    shop_name = scrapy.Field()
    #商品ID
    ProductID = scrapy.Field()
    #原价
    price = scrapy.Field()
    #折扣价
    PreferentialPrice = scrapy.Field()
    #评论总数
    CommentCount = scrapy.Field()
    #好评率
    GoodRateShow = scrapy.Field()
    #好评
    GoodCount = scrapy.Field()
    #中评
    GeneralCount = scrapy.Field()
    #差评
    PoorCount = scrapy.Field()
    #评论关键词
    keyword = scrapy.Field()
    #核心参数
    type = scrapy.Field()
    #品牌
    brand = scrapy.Field()
    #商品型号
    X_name = scrapy.Field()
    #商品类别
    X_type = scrapy.Field()
    #固体颗粒CADR
    solid_cadr = scrapy.Field()
    #气体CADR
    gas_cadr = scrapy.Field()
    #固体颗粒CCM
    solid_ccm = scrapy.Field()
    #气体CCM
    gas_ccm = scrapy.Field()
    #固体颗粒污染物能效等级
    solid_level = scrapy.Field()
    #气体污染物能效等级
    gas_level = scrapy.Field()
    #净化方式
    purify = scrapy.Field()
    #除菌功能
    sterilization = scrapy.Field()
    #滤网更新提示
    update = scrapy.Field()
    #睡眠模式
    sleep = scrapy.Field()
    #自动运转功能
    autorun = scrapy.Field()
    #定时功能
    time = scrapy.Field()
    #风速设定
    windspeed = scrapy.Field()
    #遥控功能
    telecontrol = scrapy.Field()
    #空气质量显示
    aqd = scrapy.Field()
    #颜色
    color = scrapy.Field()
    #商品链接
    product_url = scrapy.Field()
    #数据来源
    source = scrapy.Field()
    #爬取时间
    ProgramStarttime = scrapy.Field()
