django-metro
==============

Metro models for Django (for 2+, for django 1.x support use 0.4.2 version), plus the parser that fills
models with actual data from various data providers (primary - Wikipedia).
This is renamed django-russian-metro package (!).

All russian and cis parsers (like kiev or minsk) respects locale, that's why
for en locale they returns transliterated version of names.
Parsers for other cities takes only english names.

Parser downloads the following data:

- MetroLine: number, color and title
- Metro: line binding, title

Also you can run django command sometimes to get always actual data, or use celery task load_metro.


Installing
==============

1. For install django-metro, run on terminal:

        $ pip install django-metro

1. Then add this app to ``INSTALLED_APPS``:

        INSTALLED_APPS = (
            ...
            'metro',
            ...
        )

1. Apply migrations:

        ./manage.py migrate

1. Choose and specify data provider in `settings.py`:

        METRO_PROVIDER = 'moscow'

1. Finally, fill models with data:

        ./manage.py load_metro

1. Or:

        from metro.parser import provider
        provider.download_all()

1. Or use celery task `load_metro` (shared task in `tasks.py`)


Current available data providers
==============
##### (list updated)
Assign `METRO_PROVIDER` (in settings.py) one of the values below (source indicated in brackets):

##### Russia
- `'moscow'` -- Moscow (Wiki)
- `'spb'` -- Saint Petersburg (Wiki)
- `'novgorod'` -- Nizhny Novgorod (Wiki)
- `'novosib'` -- Novosibirsk (Wiki)
- `'ekat'` -- Yekaterinburg (Wiki/self)
- `'kazan'` -- Kazan (Wiki)
- `'samara'` -- Samara (Wiki)
- `'omsk'` -- Omsk (self) :)

##### CIS
- `'kiev'` -- Kiev (Wiki)
- `'minsk'` -- Minsk (Wiki)

##### World
- `'tokyo'` -- Tokyo (Wiki)
- `'london'` -- London (Wiki), very basic (without zones and branches)


Other stuff
==============
You can rename application title with `METRO_APP_TITLE` in your `settings.py`:

    METRO_APP_TITLE = u'Saint Petersrburg Metro'

Adopted for django-suit (SortableStackedInline).


License
==============
MIT probably.
