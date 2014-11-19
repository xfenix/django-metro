django-moscow-metro
===========

Base metro structure for django.
Includes Metro and MetroLine models, and parser, that download and fill this models with current data.

Parser downloads the following data:
- MetroLine: number, color and title
- Metro: line binding, title

Also you can run django command sometimes to get always actual data.


Installing
==========

For install django-moscow-metro, run on terminal: ::

    $ pip install django-moscow-metro

Then add this app to ``INSTALLED_APPS``:

    INSTALLED_APPS = (
        ...
        'moscow_metro',
        ...
    )

And, finally, apply migrations:
  
    ./manage.py migrate


Data downloading
===================

Load current metro lines and stations:

    ./manage.py load_metro

Or:

    from moscow_metro.models import load as load_metro_data()
    
    load_metro_data()


Tests
===================
Soon


License
===================
Who cares? Use it whatever you want.
