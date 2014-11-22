============
django-russian-metro
============

Russian metro models for django (only for 1.7+), plus the parser that fills models with actual data from various data providers (primary - Wikipedia).

Parser downloads the following data:
- MetroLine: number, color and title
- Metro: line binding, title

Also you can run django command sometimes to get always actual data.


============
Installing
============

1. For install django-russian-metro, run on terminal:
.. code-block:: bash
    $ pip install django-russian-metro

2. Then add this app to ``INSTALLED_APPS``:

.. code-block:: python
    INSTALLED_APPS = (
        ...
        'russian_metro',
        ...
    )

3. Apply migrations:
  
.. code-block:: bash
    ./manage.py migrate

4. Choose and specify data provider in ``settings.py``:

.. code-block:: python        
    RUMETRO_PROVIDER = 'moscow'

5. Finally, fill models with data:

.. code-block:: python
    ./manage.py load_metro
   
   Or:

.. code-block:: python
    from russian_metro.parser import provider
    provider.download_all()


============
Current available data providers
============
**(list updated)**

Assign ``RUMETRO_PROVIDER`` (in settings.py) one of the values below:

- ``'moscow'`` -- Moscow (Wiki)
- ``'spb'`` -- Saint Petersburg (Wiki)
- ``'novgorod'`` -- Nizhny Novgorod (Wiki)
- ``'novosib'`` -- Novosibirsk (Wiki)
- ``'ekat'`` -- Yekaterinburg (Wiki/self)
- ``'kazan'`` -- Kazan (Wiki)
- ``'samara'`` -- Samara (Wiki)
- ``'kiev'`` -- Kiev (Wiki)
- ``'minsk'`` -- Minsk (Wiki)
- ``'omsk'`` -- Omsk (self) :)


============
Other stuff
============
You can rename application title with `RUMETRO_APP_TITLE` in your ``settings.py``:

.. code-block:: python
    RUMETRO_APP_TITLE = u'Saint Petersrburg Metro'

I reccomend use it with ``django-suit``.
This admin.py adopted for SortableStackedInline.


============
License
============
MIT probably.
