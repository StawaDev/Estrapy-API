Estrapy Documentation
======================
**An Easy-to-Use Wrapper Anime Images API with Many Others Features**

.. note::
    This is the official documentation of Estrapy-API, and sometimes it is not stable. Note: This library already supports Python 3+ with async functions, and we prefer the stable version.

Installation
=============

.. caution::
    If you're going to install the stable version, please always check our github repo

+-------------------------------+--------------------------------------------------------------+
| Latest Version                | Stable Version                                               |
+-------------------------------+--------------------------------------------------------------+
| .. code-block:: bash          | .. code-block:: bash                                         |
|    :caption: Console          |    :caption: Console                                         |
|                               |                                                              |
|    $ pip install Estrapy-API  |    $ pip install git+https://github.com/StawaDev/Estrapy-API |
+-------------------------------+--------------------------------------------------------------+

QuickStart
===========

To begin, import ``EstraClient`` as a client object to make it easier.

.. code:: py

   import asyncio
   from Estrapy import EstraClient

   client = EstraClient()

After importing the ``EstraClient``, you can easily call all classes and
functions, for example:

.. code:: py

   import asyncio
   from Estrapy import EstraClient

   client = EstraClient()

   async def sfw_run():
       run = await client.Sfw.run()
       print(run.url)

.. note::
    One more thing I have to say is that every function will return its own property class, for example, “PropertiesManager,” and the rest of it you can check `here </properties/>`__!

.. code:: yaml

   PropertiesManager: Object
       - url: Union[str, list[str]]
       - text: Union[str, list[str]]
       - type: str
       - player: str
       - character_name: str
       - percentage: str
       - total: str
       - with_account: bool
       - original_response: dict
