nba_history
=======

.. image:: https://badge.fury.io/py/nba-history.svg
    :target: PyPI_
    :alt: nba_history page on the Python Package Index
.. image:: https://img.shields.io/badge/nba__history-100%25-brightgreen
    :target: https://shields.io/category/coverage
    :alt: Code coverage from coveralls.io

nba_history is a python package for dynamically scraping NBA player, team, and draft data.

nba_history returns all scraped data as a pandas dataframe with an option to also export results as a CSV.

A short example of the nba_history function scrape_draft_data is below:

.. code:: python

    from nba_history import player_data, team_data

	# scrape 2013 NBA draft picks
    df = player_data.scrape_draft_data(start_year = 2013,
		end_year = 2013,
		export = False)
	print(draft_picks_df.head())

.. image:: https://github.com/odonnell31/nba_history/blob/main/docs/img/draft_picks_example.png
    :alt: [logo]
    :align: center

	
Installation
------------

nba_history depends on the Python modules requests_, beautifulsoup_, and pandas_

**Installation with pip:** if you have ``pip`` installed, just type this in a terminal:

.. code:: bash

    $ pip install nba_history

**Installation by hand:** download the sources, either from PyPI_ or, if you want the development version, from GitHub_, unzip everything into one folder, open a terminal and type:

.. code:: bash

    $ (sudo) python setup.py install


Documentation
-------------

The nba_history package has 2 modules, player_data and team_data

Inside the player_data module are the following scraping functions


Contribute
----------

nba_history is open-source library originally written by odonnell31_ and released under the MIT licence. The project is hosted on GitHub_, where everyone is welcome to contribute, ask for help or simply give feedback. Please read the `Contributing Guidelines`_ for more information about how to contribute!

You can also discuss the project on Reddit_. This is preferred over GitHub issues for usage questions and examples.


Maintainers
-----------

- odonnell31_ (owner)

.. MoviePy links
.. _gallery: https://zulko.github.io/moviepy/gallery.html
.. _documentation: https://zulko.github.io/moviepy/
.. _`download MoviePy`: https://github.com/Zulko/moviepy
.. _`Label Wiki`: https://github.com/Zulko/moviepy/wiki/Label-Wiki
.. _Contributing Guidelines: https://github.com/Zulko/moviepy/blob/master/CONTRIBUTING.md

.. Websites, Platforms
.. _Reddit: https://www.reddit.com/r/moviepy/
.. _PyPI: https://pypi.python.org/pypi/moviepy
.. _GitHub: https://github.com/Zulko/moviepy
.. _Gitter: https://gitter.im/movie-py/Lobby

.. Software, Tools, Libraries
.. _Pillow: https://pillow.readthedocs.org/en/latest/
.. _Scipy: https://www.scipy.org/
.. _`OpenCV 2.4.6`: https://github.com/skvark/opencv-python
.. _Pygame: https://www.pygame.org/download.shtml
.. _Numpy: https://www.scipy.org/install.html
.. _imageio: https://imageio.github.io/
.. _`Scikit Image`: https://scikit-image.org/docs/stable/install.html
.. _Decorator: https://pypi.python.org/pypi/decorator
.. _proglog: https://github.com/Edinburgh-Genome-Foundry/Proglog
.. _ffmpeg: https://www.ffmpeg.org/download.html
.. _ImageMagick: https://www.imagemagick.org/script/index.php
.. _`Matplotlib`: https://matplotlib.org/
.. _`Sphinx`: https://www.sphinx-doc.org/en/master/setuptools.html

.. People
.. _Zulko: https://github.com/Zulko
.. _`@mgaitan`: https://github.com/mgaitan
.. _`@tburrows13`: https://github.com/tburrows13
.. _`@earney`: https://github.com/earney
.. _`@mbeacom`: https://github.com/mbeacom
.. _`@overdrivr`: https://github.com/overdrivr
.. _`@keikoro`: https://github.com/keikoro
.. _`@ryanfox`: https://github.com/ryanfox
.. _`@mondeja`: https://github.com/mondeja
