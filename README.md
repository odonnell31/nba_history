# nba_history

**nba_history** is a python package for dynamically scraping NBA player, team, and draft data.

nba_history returns all scraped data as a pandas dataframe with an option to also export results as a CSV.

[![Version](https://badge.fury.io/py/nba-history.svg)](https://badge.fury.io/py/nba-history.svg)
[![Downloads](https://pepy.tech/badge/nba-history)](https://pepy.tech/project/nba-history)
[![Coverage](https://img.shields.io/badge/nba__history-100%25-brightgreen)](https://img.shields.io/badge/nba__history-100%25-brightgreen)

## example

A short example for scaping NBA draft information is below:

```python
from nba_history import player_data, team_data

# scrape 2013 NBA draft picks
df = player_data.scrape_draft_data(start_year = 2013,
	end_year = 2013,
	export = False)
print(draft_picks_df.head())
```

![Alt text](docs/img/draft_picks_example.png)


## Installation

nba_history depends on the Python modules requests, beautifulsoup, and pandas

**Installation with pip:** if you have ``pip`` installed, type this in a terminal:

```console
$ python -m pip install nba_history
```

**Installation by hand:** download the sources, either from PyPI or, if you want the development version, from GitHub, unzip everything into one folder, open a terminal and type:

```console
$ (sudo) python setup.py install
```

## Documentation

The nba_history package has 2 modules, player_data and team_data

### player_data functions

### team_data functions

##Contribute

nba_history is open-source library originally written by odonnell31_ and released under the MIT licence. The project is hosted on GitHub_, where everyone is welcome to contribute, ask for help or simply give feedback. Please read the `Contributing Guidelines`_ for more information about how to contribute!

You can also discuss the project on Reddit. This is preferred over GitHub issues for usage questions and examples.


## Maintainers

odonnell31 (owner)