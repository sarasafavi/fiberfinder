
WTF?
####
Shamelessly scrape Google's "`Austin Apartments With Fiber
<https://fiber.google.com/cities/austin/apartments/neighborhoods/?neighborhood=all>`_"
map to build a more different map.

But why?
########
Because there are a ton of apartments in Austin where Google Fiber is Coming
Real Soon Now, and only a relative few with Fiber *actually* available. It's
impossible to search Google's Fiber map for only potential places to live that
are relevant to my fiber-desiring interests, and that's not cool.

Can I use this?
###############
The publically-available location data is Google's, so if you need it for
non-personal use talk to them. But if this dinky little tool is relevant to
your own interests... Knock yourself out. It'll maybe/probably work with the
meta-urls for other (non-Austin) `Google
<https://fiber.google.com/cities/kansascity/apartments/neighborhoods/?neighborhood=all>`_
`Fiber
<https://fiber.google.com/cities/provo/apartments/neighborhoods/?neighborhood=all>`_
cities too, but I haven't checked.

How?
####
::

    $ pip install -r requirements.txt
    $ ./makemap

*See also:* ::

    $ ./makemap --help

Wait this isn't a map, this is a JSON file...
##############################################
Throw the output file in a `gist <https://gist.github.com>`_ or open it at
`geojson.io <http://geojson.io/>`_.  *MAGIC.*

Ain't nobody got time for that, just give me the map please
#############################################################

`See this repo's map in action here. <https://github.com/sarasafavi/fiberfinder/blob/master/atx_fiber_05-26-16.geojson>`_
