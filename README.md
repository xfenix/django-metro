django-russian-metro
===================

Russian metro models for django (only for 1.7+), plus the parser that fills models with actual data from various data providers (primary - Wikipedia).

Parser downloads the following data:
- MetroLine: number, color and title
- Metro: line binding, title

Also you can run django command sometimes to get always actual data.


Installing
===================

1. For install django-russian-metro, run on terminal:

        $ pip install django-russian-metro

1. Then add this app to ``INSTALLED_APPS``:

        INSTALLED_APPS = (
            ...
            'russian_metro',
            ...
        )

1. Apply migrations:
  
        ./manage.py migrate

1. Choose and specify data provider in `settings.py`:
        
        RUMETRO_PROVIDER = 'moscow'

1. Finally, fill models with data:
        
        ./manage.py load_metro
   
   Or:

        from russian_metro.parser import provider
        provider.download_all()


Current available data providers
===================
Set `RUMETRO_PROVIDER` to one of the following options:
- Moscow (Wikipedia), 'moscow'
- Saint Petersburg (Wikipedia), 'spb'
- Nizhny Novgorod (Wikipedia), 'novgorod'
- Novosibirsk (Wikipedia), 'novosib'
- Kiev (Wikipedia), 'kiev'
- Minsk (Wikipedia), 'minsk'
- Omsk, 'omsk' :)


Other stuff
===================
You can rename application title with `RUMETRO_APP_TITLE` in your `settings.py`:

    RUMETRO_APP_TITLE = u'Saint Petersrburg Metro'

I reccomend use it with `django-suit`.
This admin.py adopted for work with SortableStackedInline.


License
===================
MIT probably.
