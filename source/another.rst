============
Another PyPI
============

I guess it is evident why there is a *new* PyPI, but in case it isn’t, here
are a few more reasons.

* Python 2 and 2020
* `Real authentication <https://glyph.twistedmatrix.com/2017/10/careful-with-that-pypi.html>`__
* `Proper API <https://twitter.com/uranusjr/status/978324513904508928>`__

Are we in agreement now? Excellent.


Python Packaging Authority
==========================

Initialized as PyPA, a working group that maintains many of the relevant
projects in Python packaging.

Initiated in around 2012 by `Nick Coghlan`_ and others (including Donald) to
aggregate packaging-related projects in Python, and try to actively push
forward important but stale development (e.g. virtualenv).

.. _`Nick Coghlan`: http://python-notes.curiousefficiency.org/en/latest/


Warehouse
=========

Started in 2013, and began actual development in 2015. First commit as in Git:

.. code-block:: none

    commit 41358eaf559c1011fc3e94149e716e1dfc79e391
    Author: Donald Stufft <donald@stufft.io>
    Date:   Sat Jan 24 20:31:35 2015 -0500

I start to see a pattern here.

Warehouse is developed with modern technology, including:

* Pyramid
* SQLAlchemy (backed by PostgreSQL)
* Jinja2
* SCSS and JavaScript, bundled with Gulp
* Docker-based develop environment

`Source code hosted on GitHub <https://github.com/pypa/warehouse>`__.
`Documentation hosted on ReadTheDocs <https://warehouse.readthedocs.io/>`__.
Continuous integration powered by Travis CI and Codecov. Security scrutiny with
PyUP_. Everything you can ask for from a Python web application project.

.. _PyUP: https://pyup.io

You can try it right now: https://pypi.org.


Roadmap
=======

See also: https://wiki.python.org/psf/WarehouseRoadmap.

Warehouse has been online for about a year (I think), and reached feature
completeness in **Februrary, 2018**.

Public beta want for a month, and finished on **26 March, 2018**. The new PyPI
has stablized!

The next step is to move all reference from pypi.python.org to the new domain.
The traffic will also be redirected progressively, until all downloads go
through pypi.org. After that the Cheeseshop will be shut down eventually.


Migration
=========

What does this mean to you? Not very much, honestly.

``pip install`` users
---------------------

If all you do is ``pip install`` things, all you need is to upgrade pip
(actually Setuptools) periodically. You should have been doing this anyway.
After you upgrade, all references will be updated as well.

Package authors
---------------

You should start using twine_ to release your packages, instead of running
``python setup.py upload`` manually. You should have been doing this anyway.
This should automatically use the new index, unless you have specifically
set the ``repository`` value in your ``.pypirc`` file. Simply
`remove it <https://packaging.python.org/guides/migrating-to-pypi-org/>`__ and
you’re good.

.. _twine: https://twine.readthedocs.io

Website viewers
---------------

Visit pypi.org instead pypi.python.org. It is much more beautiful and easier
to use! I also found it a little faster, but that might be just an illution.
