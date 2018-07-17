# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SoccerReferenceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #
    player = scrapy.Field()
    nationality = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()
    games = scrapy.Field()
    games_starts = scrapy.Field()
    games_subs = scrapy.Field()
    minutes = scrapy.Field()
    goals = scrapy.Field()
    assists = scrapy.Field()
    fouls = scrapy.Field()
    cards_yellow = scrapy.Field()
    cards_red = scrapy.Field()
    shots_on_target = scrapy.Field()
    goals_per90 = scrapy.Field()
    goals_assists_per90 = scrapy.Field()
    shots_on_target_per90 = scrapy.Field()
    fouls_per90 = scrapy.Field()
    cards_per90 = scrapy.Field()
    goals_against = scrapy.Field()
    goals_against_per90 = scrapy.Field()
    shots_on_target_against = scrapy.Field()
    save_perc = scrapy.Field()
    wins = scrapy.Field()
    draws = scrapy.Field()
    losses = scrapy.Field()
    clean_sheets = scrapy.Field()
    ilean_sheets_perc = scrapy.Field()

    squad_season = scrapy.Field()
    squad_name = scrapy.Field()
    squad_finished_ranking = scrapy.Field()
    squad_games = scrapy.Field()
    squad_points = scrapy.Field()
    squad_GD = scrapy.Field()
    squad_win = scrapy.Field()
    squad_draw = scrapy.Field()
    squad_lose = scrapy.Field()
    squad_GF = scrapy.Field()
    squad_top_scorer = scrapy.Field()
    squad_goalkeeper = scrapy.Field()
    squad_comp = scrapy.Field()
    squad_GA = scrapy.Field()
    squad_attendance = scrapy.Field()

    club_comp = scrapy.Field()
    club_squad_from = scrapy.Field()
    club_squad_to = scrapy.Field()
    club_country_name = scrapy.Field()
    club_squad_number = scrapy.Field()
    club_flag = scrapy.Field()
