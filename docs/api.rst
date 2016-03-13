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


Get Device
==========

* URL: `/api/devices/<pk>/`
* HTTP Method: `GET`

Example response
----------------
.. code::

   {
       "name": "Some Device",
       "slug": "some-device",
       "active": true,
       "model": "AA1",
       "address": "0001",
       "description": "Some description"
   }


Add a Device
============
* URL: `/api/devices/`
* HTTP Method: `POST`

Example Request
---------------
.. code::

   {
       "name": "Some Device",
       "slug": "some-device",
       "active": true,
       "model": "AA1",
       "address": "0001",
       "description": "Some description"
   }

Example Response
----------------
.. code::

   {
       "name": "Some Device",
       "slug": "some-device",
       "active": true,
       "model": "AA1",
       "address": "0001",
       "description": "Some description"
   }

Get Variable
============

* URL: `/api/vars/<pk>/`
* HTTP Method: `GET`

Example response
----------------
.. code::

   {
       "id": 1,
       "name": "Door 1",
       "slug": "door-1",
       "active": true,
       "device": 1,
       "var_type": "binary",
       "units": "",
       "value": 1,
       "description": "Door 1 state: 1=Open, 0=Closed"
   }


Add a Variable
==============
* URL: `/api/vars/`
* HTTP Method: `POST`

Example Request
---------------
.. code::

   {
       "name": "Door 1",
       "slug": "door-1",
       "active": true,
       "device": 1,
       "var_type": "binary",
       "units": "",
       "value": 1,
       "description": "Door 1 state: 1=Open, 0=Closed"
   }

Example Response
----------------
.. code::

   {
       "id": 1,
       "name": "Door 1",
       "slug": "door-1",
       "active": true,
       "device": 1,
       "var_type": "binary",
       "units": "",
       "value": 1,
       "description": "Door 1 state: 1=Open, 0=Closed"
   }

Get Mimic
=========

* URL: `/api/mimic/<pk>/`
* HTTP Method: `GET`

Example response
----------------
.. code::

   {
       "id": 1,
       "name": "Front Door Sensor",
       "vars": [
           {
               "id": 1,
               "name": "Door 1",
               "var_type": "binary",
               "units": "",
               "value": 1,
               "description": "Door 1 state: 1=Open, 0=Closed"
           }
       ],
       "window": 1,
       "x": 0,
       "y": 0
   }

Add a Variable
==============
* URL: `/api/mimics/`
* HTTP Method: `POST`

Example Request
---------------
.. code::

   {
       "name": "Front Door Sensor",
       "vars": [1,2],
       "window": 1,
       "x": 0,
       "y": 0
   }

Example Response
----------------
.. code::

   {
       "id": 1,
       "name": "Front Door Sensor",
       "vars": [
           {
               "id": 1,
               "name": "Door 1",
               "var_type": "binary",
               "units": "",
               "value": 1,
               "description": "Door 1 state: 1=Open, 0=Closed"
           }
       ],
       "window": 1,
       "x": 0,
       "y": 0
   }
