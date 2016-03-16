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
       "id": 1,
       "title": "Some Windows",
       "slug": "some-window",
       "description": "The first window",
       "mimics": [
            "http://server/api/mimics/1/",
            "http://server/api/mimics/2/"
       ],
       "links": {
           "self": "http://server/api/windows/1/"
       }
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
       "id": 1,
       "title": "Some Windows 2",
       "slug": "some-window-2",
       "description": "The second window",
       "mimics": [
            "http://server/api/mimics/1/",
            "http://server/api/mimics/2/"
       ],
       "links": {
           "self": "http://server/api/windows/1/"
       }
   }


Get Device
==========

* URL: `/api/devices/<pk>/`
* HTTP Method: `GET`

Example response
----------------
.. code::

   {
       "id": 1,
       "name": "Some Device",
       "slug": "some-device",
       "active": true,
       "model": "AA1",
       "address": "0001",
       "description": "Some description",
       "vars": [
           "http://server/api/vars/1/",
           "http://server/api/vars/2/"
       ],
       "links": {
           "self": "http://server/api/devices/1/"
       }
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
       "id": 1,
       "name": "Some Device",
       "slug": "some-device",
       "active": true,
       "model": "AA1",
       "address": "0001",
       "description": "Some description",,
       "vars": [
           "http://server/api/vars/1/",
           "http://server/api/vars/2/"
       ],
       "links": {
           "self": "http://server/api/devices/1/"
       }
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
       "var_type_display": "Digital",
       "units": "",
       "value": 1,
       "description": "Door 1 state: 1=Open, 0=Closed",
       "links": {
           "self": "http://server/api/vars/1/",
           "device": "http://server/api/device/1/"
       }
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
       "var_type_display": "Digital",
       "units": "",
       "value": 1,
       "description": "Door 1 state: 1=Open, 0=Closed",
       "links": {
           "self": "http://server/api/vars/1/",
           "device": "http://server/api/devices/1/"
       }
   }

Get Mimic
=========

* URL: `/api/mimics/<pk>/`
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
               "description": "Door 1 state: 1=Open, 0=Closed",
               "links": {
                   "self": "http://server/api/vars/1/"
               }
           }
       ],
       "window": 1,
       "x": 0,
       "y": 0,
       "links": {
           "self": "http://server/api/mimics/1/",
           "window": "http://server/api/windows/1/"
       }
   }

Add a Mimic
===========
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
               "description": "Door 1 state: 1=Open, 0=Closed",
               "links": {
                   "self": "http://server/api/vars/1/"
               }
           }
       ],
       "window": 1,
       "x": 0,
       "y": 0,
       "links": {
           "self": "http://server/api/mimics/1/",
           "window": "http://server/api/windows/1/"
       }
   }

Get User
========

* URL: `/api/users/<username>/`
* HTTP Method: `GET`

Example response
----------------
.. code::

   {
       "id": 1,
       "username": "marti"
       "full_name": "Jose Marti",
       "is_active": true
       "groups": [
           "operator"
       ],
       "links": {
           "self": "http://server/api/users/1/"
       }
   }

Add a User
==========
* URL: `/api/users/`
* HTTP Method: `POST`

Example Request
---------------
.. code::

   {
       "id": 1,
       "username": "ernesto"
       "full_name": "Ernesto Guevara",
       "is_active": true
   }

Example Response
----------------
.. code::

   {
       "id": 1,
       "username": "ernesto"
       "full_name": "Ernesto Guevara",
       "is_active": true
       "groups": [],
       "links": {
           "self": "http://server/api/devices/1/"
       }
   }

.. todo:: Add groups, operations to manage user's groups, permissions