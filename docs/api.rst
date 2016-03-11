===
API
===

Get Windows
===========

* URL: `/api/windows/<pk>/`
* HTTP Method: `GET`

Example response
----------------
.. code::

   {
        "title": "Some Windows",
        "slug": "some-window",
        "description": "The first window"
   }


Add a Window
============
* URL: `/api/windows/`
* HTTP Method: `POST`

Example Request
---------------
.. code::

   {
        "title": "Some Windows 2",
        "slug": "some-window-2",
        "description": "The second window"
   }

Example Response
----------------
.. code::

   {
        "title": "Some Windows 2",
        "slug": "some-window-2",
        "description": "The second window"
   }
