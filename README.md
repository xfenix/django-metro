django-russian-metro
===================

Russian metro models for django, plus the parser that fills models with actual data from various data providers (primary - Wikipedia).

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
        
        RUMETRO_CITY = 'moscow'

1. Finally, fill models with data:
        
        ./manage.py load_metro
   
   Or:

        from russian_metro.parser import provider
        provider.download_all()


Current available data providers
===================
- Moscow (Wikipedia), `RUMETRO_CITY = 'moscow'`
- Saint Petersburg (Wikipedia), `RUMETRO_CITY = 'spb'`


License
===================
Who cares? Use it whatever you want.
