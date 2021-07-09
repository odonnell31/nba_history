# -*- coding: utf-8 -*-

from nba_history import player_data, team_data

draft_picks_df = player_data.scrape_draft_data(start_year = 2013,
                                               end_year = 2013,
                                               export = False)
print(draft_picks_df.head())

