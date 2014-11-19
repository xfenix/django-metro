django-moscow-metro
===========

Moscow metro structure for django.
Includes Metro and MetroLine models, and parsers. With this parsers you can download all current metro stations, metro lines with numbers and colors.


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


Using
===================

Load current metro lines and stations:

    ./manage.py load_metro

Or:

    from moscow_metro.models import load as load_all_metro()
    
    load_all_metro()

Then you can use some of this methods sometimes (for updating). It's just append all new lines and stations (or removed by you).


Tests
===================
Soon


License
===================
Who cares? Use it whatever you want.
