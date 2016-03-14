====================
Fotuto Install Guide
====================

Quick Install Development Environment
=====================================

1. Install SO dependences::

     sudo apt-get install python-pip virtualenv

2. Create environment and install packages::

     cd PROJECT_ROOT
     virtualenv env
     source env/bin/activate
     pip install -r requirments.txt

   .. note:: If use PostgreSQL, maybe is requrie to install::

        sudo apt-get install libpq-dev python-dev
        pip install psycopg2

      Then create the database, and change database settings by rename `fotuto/settings_local.py.example` to
      `fotuto/settings_local.py` and change the values.

3. Create Database::

     python migrate

4. Create superuser::

     python manage.py createsuperuser

5. Add static resources::

     sudo apt-get install npm
     sudo npm install -g bower
     sudo ln -s /usr/bin/nodejs /usr/bin/node
     cd PROJECT_ROOT
     bower install

6. Start development server::

     python manage.py runserver

Run Tests
=========

.. note:: Before continue, be sure to activate the virtual environment created on step 2.

.. code::

   pip install -r requirments_test.txt
   python manage.py test
