===================
The history of PyPI
===================

Before we talk about PyPI, let’s start from a more fundamental question: **How
does Python know where to find a module when you import?**

.. code:: pycon

    >>> import sys
    >>> for p in sys.path:
    ...    print(repr(p))
    ...
    ''
    '/Users/uranusjr/Library/PythonUp/versions/3.6/lib/python36.zip'
    '/Users/uranusjr/Library/PythonUp/versions/3.6/lib/python3.6'
    '/Users/uranusjr/Library/PythonUp/versions/3.6/lib/python3.6/lib-dynload'
    '/Users/uranusjr/Library/PythonUp/versions/3.6/lib/python3.6/site-packages'

Each entry in ``sys.path`` is a directory (or archive). Python looks for your
module in them in order until a match is found, and use it as the result.

When you install something into Python, generally they go into the
``site-packages`` directory. Like ``tar xzvf`` or something.


Python packages
===============

The `PEP 241`_, proposed by A.M. Kuchling, introduced ``distutils`` that
standardized what a Python package is, and what it should contain. This is the
origin of ``setup.py``, in case you wonder.

.. _`PEP 241`: https://www.python.org/dev/peps/pep-0241/

``distutils`` allows developers to automate the *packaging* process of a Python
package, from a local filesystem tree to a transferrable blob (mostly a tar.gz
archive, bundled with the ``sdist`` subcommand).

A recipient, upon receiving one of these blobs, knows immediately what to do::

    $ python setup.py install


Python Package Index
====================

A central place to upload, exchange, download, and view Python packages. First
implemented by `Richard Jones`_ in 2002 with inspiration from CPAN_, with early
contributions from Martin v. Löwis and `Michael (Mick) Twomey`_.

.. _CPAN: https://www.cpan.org
.. _`Richard Jones`: http://mechanicalcat.net/richard
.. _`Michael (Mick) Twomey`: https://www.twoistoomany.com

The first PyPI is very intersting in various regards. It was online after
the initial development of less a month, by one single person (Richard). Also
comparing when it was developed to common technologies in a timeline fashion:

* 2000: Apache mod_python
* **2002: PyPI**
* 2003: Wordpress
* 2004: PEP 333 (WSGI 1.0)
* 2005: Django

you know how ancient and poor the code base is.


Donald Stufft
=============

.. image:: _static/dstufft.jpg
    :alt: Donald Stufft
    :width: 240px
    :align: center

You might notice you know no-one in the PyPI credit list. That is absolutely
normal because they don’t really involve now. They are still visible figures in
the Python community (especially Richard), but they don’t do the actual
programming anymore.

The responsibility now falls on `Donald Stufft`_. With PyPI going through
multiple changes during the years to update the techonology behind it (it now
runs on WSGI with `mod_wsgi` on Apache), even its original creaters might not
be able to understand it anymore. Only Donald.

.. _`Donald Stufft`: https://caremad.io

    By "dev team" you mean me, because there is no dev team, It's just me.
    Coincidentally there's no real ops team either, there's me and when he has
    time Ernest. In addition, I'm not so much "actively avoiding" the issue as
    I am just seriously overloaded. Not only am I the primary/only person
    keeping PyPI going, I'm also one of the main driving forces behind pip
    (though thankfully that has additional folks working on it too! Not with as
    much "available" time to dedicate to it though) and one of the main driving
    forces behind working through a variety of PEPs to try and improve
    packaging as a whole and the primary developer of a PyPI 2.0 that will
    hopefully replace this decade old rotted code base that we call PyPI.

    -- `Donald Stufft, on Reddit <https://www.reddit.com/r/Python/comments/4jaaib/pypi_download_stats_have_stopped_working_again/d355dt6/>`__

By Ernest he meant `Ernest W. Durbin III`_, by the way.

.. _`Ernest W. Durbin III`: https://ernest.ly
