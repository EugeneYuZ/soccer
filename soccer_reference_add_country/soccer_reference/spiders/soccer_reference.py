import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from soccer_reference.items import SoccerReferenceItem


class Myspider(scrapy.Spider):
    allowed_domains = ['fbref.com']
    name = 'soccer_reference'
    url = 'https://fbref.com/en/squads/index.html'
    domain = 'https://fbref.com'
    barshurl = 'index.html'

    def start_requests(self):
        yield Request(self.url, self.parse)

    def parse(self, response):
        ths = BeautifulSoup(response.text, 'lxml').find_all('tr')
        for j in ths:
            i = j.find('th', {"data-stat": "country"})
            i1 = j.find('td', {"data-stat": "flag"})
            if i1 is not None:
                club_flag = i1.get_text()
            if i.find('a') is not None:
                y = self.domain + str(i.find('a')['href']) + '/' + self.barshurl
                club_country_name = i.find('a').get_text()
                yield Request(y, callback=self.get_squad, meta={'club_country_name': club_country_name, 'club_flag': club_flag})

    def get_squad(self, response):
        ths = BeautifulSoup(response.text, 'lxml').find_all('tr')
        club_country_name = response.meta['club_country_name']
        club_flag = response.meta['club_flag']
        for j in ths:
            i = j.find('th', {"data-stat": "squad"})
            i1 = j.find('td', {"data-stat": "comp"})
            i2 = j.find('td', {"data-stat": "max_season"})
            i3 = j.find('td', {"data-stat": "min_season"})
            i4 = j.find('td', {"data-stat": "num_comps"})
            if i1 is not None:
                club_comp = i1.get_text()
            else:
                club_comp = "None"

            if i2 is not None:
                club_squad_to = i2.get_text()
            else:
                club_squad_to = "None"

            if i3 is not None:
                club_squad_from = i3.get_text()
            else:
                club_squad_from = "None"

            if i4 is not None:
                club_squad_number = i4.get_text()
            else:
                club_squad_number = "None"

            if i.find('a') is not None:
                y = self.domain + str(i.find('a')['href']) + '/' + self.barshurl
                squad_name = i.find('a').get_text()
                yield Request(y, callback=self.get_season_squads, meta={'club_country_name': club_country_name, 'club_flag': club_flag, 'club_squad_number': club_squad_number, 'club_comp': club_comp, 'club_squad_from': club_squad_from, 'club_squad_to': club_squad_to,
                                                                        'squad_name': squad_name})

    def get_season_squads(self, response):
        squad_name = response.meta['squad_name']
        club_flag = response.meta['club_flag']
        club_country_name = response.meta['club_country_name']
        club_squad_number = response.meta['club_squad_number']
        club_comp = response.meta['club_comp']
        club_squad_from = response.meta['club_squad_from']
        club_squad_to = response.meta['club_squad_to']
        ths = BeautifulSoup(response.text, 'lxml').find_all('tr')

        for j in ths:
            i0 = j.find('td', {"data-stat": "squad"})
            i = j.find('th', {"data-stat": "season"})
            i1 = j.find('td', {"data-stat": "comp_level"})
            i2 = j.find('td', {"data-stat": "lg_finish"})
            i3 = j.find('td', {"data-stat": "games"})
            i4 = j.find('td', {"data-stat": "goal_diff"})
            i5 = j.find('td', {"data-stat": "wins"})
            i6 = j.find('td', {"data-stat": "draws"})
            i7 = j.find('td', {"data-stat": "losses"})
            i8 = j.find('td', {"data-stat": "goals_for"})
            i9 = j.find('td', {"data-stat": "goals_against"})
            i10 = j.find('td', {"data-stat": "attendance_per_g"})
            i11 = j.find('td', {"data-stat": "top_team_scorers"})
            i12 = j.find('td', {"data-stat": "top_keeper"})
            i13 = j.find('td', {"data-stat": "points"})

            if i is not None:
                squad_season = i.get_text()
            else:
                squad_season = "None"

            if i1 is not None:
                squad_comp = i1.get_text()
            else:
                squad_comp = "None"

            if i2 is not None:
                squad_finished_ranking = i2.get_text()
            else:
                squad_games = "None"

            if i3 is not None:
                squad_games = i3.get_text()
            else:
                squad_games = "None"

            if i4 is not None:
                squad_GD = i4.get_text()
            else:
                squad_GD = "None"

            if i5 is not None:
                squad_win = i5.get_text()
            else:
                squad_win = "None"
            if i6 is not None:
                squad_draw = i6.get_text()
            else:
                squad_draw = "None"
            if i7 is not None:
                squad_lose = i7.get_text()
            else:
                squad_lose = "None"
            if i8 is not None:
                squad_GF = i8.get_text()
            else:
                squad_GF = "None"

            if i9 is not None:
                squad_GA = i9.get_text()
            else:
                squad_GA = "None"

            if i10 is not None:
                squad_attendance = i10.get_text()
            else:
                squad_attendance = "None"

            if i11 is not None:
                squad_top_scorer = i11.get_text()
            else:
                squad_top_scorer = "None"

            if i12 is not None:
                squad_goalkeeper = i12.get_text()
            else:
                squad_goalkeeper = "None"

            if i13 is not None:
                squad_points = i13.get_text()
            else:
                squad_points = "None"
            # print(squad_points)
            if i0 is not None:
                if i0.find('a') is not None:
                    y = self.domain + str(i0.find('a')['href']) + '/' + self.barshurl
                    squad_name = i0.find('a').get_text()
                    yield Request(y, callback=self.get_players, meta={'club_country_name': club_country_name, 'club_flag': club_flag, 'club_squad_number': club_squad_number, 'club_comp': club_comp, 'club_squad_from': club_squad_from, 'club_squad_to': club_squad_to, 'squad_name': squad_name, 'squad_season': squad_season, 'squad_finished_ranking': squad_finished_ranking, 'squad_games': squad_games, 'squad_points': squad_points, 'squad_GD': squad_GD, 'squad_win': squad_win, 'squad_draw': squad_draw, 'squad_lose': squad_lose, 'squad_GF': squad_GF, 'squad_top_scorer': squad_top_scorer, 'squad_goalkeeper': squad_goalkeeper, 'squad_comp': squad_comp, 'squad_GA': squad_GA, 'squad_attendance': squad_attendance})

    def get_players(self, response):
        items = SoccerReferenceItem()
        squad_name = response.meta['squad_name']
        club_flag = response.meta['club_flag']
        club_country_name = response.meta['club_country_name']
        club_squad_number = response.meta['club_squad_number']
        club_comp = response.meta['club_comp']
        club_squad_from = response.meta['club_squad_from']
        club_squad_to = response.meta['club_squad_to']
        squad_season = response.meta['squad_season']
        squad_name = response.meta['squad_name']
        squad_finished_ranking = response.meta['squad_finished_ranking']
        squad_games = response.meta['squad_games']
        squad_points = response.meta['squad_points']
        squad_GD = response.meta['squad_GD']
        squad_win = response.meta['squad_win']
        squad_draw = response.meta['squad_draw']
        squad_lose = response.meta['squad_lose']
        squad_GF = response.meta['squad_GF']
        squad_top_scorer = response.meta['squad_top_scorer']
        squad_goalkeeper = response.meta['squad_goalkeeper']
        squad_comp = response.meta['squad_comp']
        squad_GA = response.meta['squad_GA']
        squad_attendance = response.meta['squad_attendance']
        print(squad_GA)
        stats_player_names = BeautifulSoup(response.text, 'lxml').find_all('tr')
        for j in stats_player_names:
            i0 = j.find('th', {"data-stat": "player", "scope": "row"})
            i = j.find('td', {"data-stat": "nationality"})
            i1 = j.find('td', {"data-stat": "position"})
            i2 = j.find('td', {"data-stat": "age"})
            i3 = j.find('td', {"data-stat": "games"})
            i4 = j.find('td', {"data-stat": "games_starts"})
            i5 = j.find('td', {"data-stat": "games_subs"})
            i6 = j.find('td', {"data-stat": "minutes"})
            i7 = j.find('td', {"data-stat": "goals"})
            i8 = j.find('td', {"data-stat": "assists"})
            i9 = j.find('td', {"data-stat": "fouls"})
            i10 = j.find('td', {"data-stat": "cards_yellow"})
            i11 = j.find('td', {"data-stat": "cards_red"})
            i12 = j.find('td', {"data-stat": "shots_on_target"})
            i13 = j.find('td', {"data-stat": "goals_per90"})
            i14 = j.find('td', {"data-stat": "goals_assists_per90"})
            i15 = j.find('td', {"data-stat": "shots_on_target_per90"})
            i16 = j.find('td', {"data-stat": "fouls_per90"})
            i17 = j.find('td', {"data-stat": "cards_per90"})
            i18 = j.find('td', {"data-stat": "goals_against"})
            i19 = j.find('td', {"data-stat": "goals_against_per90"})
            i20 = j.find('td', {"data-stat": "shots_on_target_against"})
            i21 = j.find('td', {"data-stat": "save_perc"})
            i22 = j.find('td', {"data-stat": "wins"})
            i23 = j.find('td', {"data-stat": "draws"})
            i24 = j.find('td', {"data-stat": "losses"})
            i25 = j.find('td', {"data-stat": "clean_sheets"})
            i26 = j.find('td', {"data-stat": "clean_sheets_perc"})

            if i0 is not None:
                player = i0.get_text()

                if i is not None:
                    nationality = i.get_text()
                else:
                    nationality = "None"

                if i1 is not None:
                    position = i1.get_text()
                else:
                    position = "None"

                if i2 is not None:
                    age = i2.get_text()
                else:
                    age = "None"

                if i3 is not None:
                    games = i3.get_text()
                else:
                    games = "None"

                if i4 is not None:
                    games_starts = i4.get_text()
                else:
                    games_starts = "None"

                if i5 is not None:
                    games_subs = i5.get_text()
                else:
                    games_subs = "None"
                if i6 is not None:
                    minutes = i6.get_text()
                else:
                    minutes = "None"
                if i7 is not None:
                    goals = i7.get_text()
                else:
                    goals = "None"
                if i8 is not None:
                    assists = i8.get_text()
                else:
                    assists = "None"

                if i9 is not None:
                    fouls = i9.get_text()
                else:
                    fouls = "None"

                if i10 is not None:
                    cards_yellow = i10.get_text()
                else:
                    cards_yellow = "None"

                if i11 is not None:
                    cards_red = i11.get_text()
                else:
                    cards_red = "None"

                if i12 is not None:
                    shots_on_target = i12.get_text()
                else:
                    shots_on_target = "None"

                if i13 is not None:
                    goals_per90 = i13.get_text()
                else:
                    goals_per90 = "None"
                if i14 is not None:
                    goals_assists_per90 = i14.get_text()
                else:
                    goals_assists_per90 = "None"

                if i15 is not None:
                    shots_on_target_per90 = i15.get_text()
                else:
                    shots_on_target_per90 = "None"
                if i16 is not None:
                    fouls_per90 = i16.get_text()
                else:
                    fouls_per90 = "None"

                if i17 is not None:
                    cards_per90 = i17.get_text()
                else:
                    cards_per90 = "None"

                if i18 is not None:
                    goals_against = i18.get_text()
                else:
                    goals_against = "None"

                if i19 is not None:
                    goals_against_per90 = i19.get_text()
                else:
                    goals_against_per90 = "None"
                if i20 is not None:
                    shots_on_target_against = i20.get_text()
                else:
                    shots_on_target_against = "None"
                if i21 is not None:
                    save_perc = i21.get_text()
                else:
                    save_perc = "None"
                if i22 is not None:
                    wins = i22.get_text()
                else:
                    wins = "None"

                if i23 is not None:
                    draws = i23.get_text()
                else:
                    draws = "None"

                if i24 is not None:
                    losses = i24.get_text()
                else:
                    losses = "None"

                if i25 is not None:
                    clean_sheets = i25.get_text()
                else:
                    clean_sheets = "None"

                if i26 is not None:
                    ilean_sheets_perc = i26.get_text()
                else:
                    ilean_sheets_perc = "None"

                items['player'] = player
                items['nationality'] = nationality
                items['position'] = position
                items['age'] = age
                items['games'] = games
                items['games_starts'] = games_starts
                items['games_subs'] = games_subs
                items['minutes'] = minutes
                items['goals'] = goals
                items['assists'] = assists
                items['fouls'] = fouls
                items['cards_yellow'] = cards_yellow
                items['cards_red'] = cards_red
                items['shots_on_target'] = shots_on_target
                items['goals_per90'] = goals_per90
                items['goals_assists_per90'] = goals_assists_per90
                items['shots_on_target_per90'] = shots_on_target_per90
                items['fouls_per90'] = fouls_per90
                items['cards_per90'] = cards_per90
                items['goals_against'] = goals_against
                items['goals_against_per90'] = goals_against_per90
                items['shots_on_target_against'] = shots_on_target_against
                items['save_perc'] = save_perc
                items['wins'] = wins
                items['draws'] = draws
                items['losses'] = losses
                items['clean_sheets'] = clean_sheets
                items['ilean_sheets_perc'] = ilean_sheets_perc
                items['squad_season'] = squad_season
                items['squad_name'] = squad_name
                items['squad_finished_ranking'] = squad_finished_ranking
                items['squad_games'] = squad_games
                items['squad_points'] = squad_points
                items['squad_GD'] = squad_GD
                items['squad_win'] = squad_win
                items['squad_draw'] = squad_draw
                items['squad_lose'] = squad_lose
                items['squad_GF'] = squad_GF
                items['squad_top_scorer'] = squad_top_scorer
                items['squad_goalkeeper'] = squad_goalkeeper
                items['squad_comp'] = squad_comp
                items['squad_GA'] = squad_GA
                items['squad_attendance'] = squad_attendance
                items['club_comp'] = club_comp
                items['club_squad_from'] = club_squad_from
                items['club_squad_to'] = club_squad_to
                items['club_country_name'] = club_country_name
                items['club_squad_number'] = club_squad_number
                items['club_flag'] = club_flag

                yield items

        # for i in player_name:
        #     if i.find('a') is not None:
        #         player_name = i.find('a').get_text()
        #         print(player_name)
        #         items['player_name'] = player_name
        #         items['club_country_name'] = club_country_name
        #         items['squad_name'] = squad_name
        #         items['squads_seasons'] = squads_seasons
        #         yield items
