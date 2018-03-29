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

.. code-block:: text

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


Future
======

Problems
--------

* `PyPI uses plain password to authenticate users <https://glyph.twistedmatrix.com/2017/10/careful-with-that-pypi.html>`__
* `The “simple API” does not offer metadata extraction <https://wiki.python.org/moin/PyPISimple>`__

Solutions
---------

* A better, *real* authentication system. Something similar to modern VCSs
  (e.g. Git, Mercurial) offer.
* Implement JSON API in Warehouse.
* Move pip to use the JSON API.
* Kill the XML/RPC API.
* Phase out the “simple” API.

Comparison
----------

Take Pillow as an example.


Simple
......

See https://pypi.org/simple/pillow/.

.. code-block:: html

    <a data-requires-python="&gt;=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*" href="../../packages/1a/bf/36f7308b053d847113df07c35fc22039c9326f30b36c2c24551f4c21e845/Pillow-5.0.0-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl#md5=27b2829bf90ffa523749be7e8470f1a6" rel="internal">Pillow-5.0.0-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl</a><br/>
    <a data-requires-python="&gt;=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*" href="../../packages/80/90/6a734a63375234ebba6fabd9f1f57a912875181e46d3bc7501ec4ad59b79/Pillow-5.0.0-cp34-cp34m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl#md5=81b58fd7de0a685cf6789e09408e86e2" rel="internal">Pillow-5.0.0-cp34-cp34m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl</a><br/>
    <a data-requires-python="&gt;=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*" href="../../packages/08/d4/b12ff5cfe0e1a85380ee931f6784020ff5f7066a91993653a8e9efc0fa60/Pillow-5.0.0-cp35-cp35m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl#md5=f02958eec20a0609ee901484b3fb1b73" rel="internal">Pillow-5.0.0-cp35-cp35m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl</a><br/>
    <a data-requires-python="&gt;=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*" href="../../packages/f6/02/9d98b5bc4535ad4e03aeda9e529e7d925a569ad4e47883ee093364b6e086/Pillow-5.0.0-cp35-cp35m-win_amd64.whl#md5=0ca9d0b9b35bc6c05c48b3efb56b7bc4" rel="internal">Pillow-5.0.0-cp35-cp35m-win_amd64.whl</a><br/>
    <a data-requires-python="&gt;=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*" href="../../packages/e1/d2/a4f993e3079a9b8898c6bd6f6fc3c19d7f0a95e0cca285019def3c16869b/Pillow-5.0.0-pp259-pypy_41-win32.whl#md5=cdcc14fa5f4176b76436f9ffc328adf4" rel="internal">Pillow-5.0.0-pp259-pypy_41-win32.whl</a><br/>
    <a data-requires-python="&gt;=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*" href="../../packages/af/45/9baa3dfd099d39e8ce63d8a36e40cb4791b85b7044706bb45f749f88d9af/Pillow-5.0.0.win32-py3.6.exe#md5=5becccb88b9523c0868f0c1ac71c8102" rel="internal">Pillow-5.0.0.win32-py3.6.exe</a><br/>

JSON
....

See https://pypi.python.org/pypi/Pillow/json/. It is not available yet in
Warehouse (I think).

.. code-block:: json

    {
        "info": {
            "maintainer": "",
            "docs_url": null,
            "requires_python": ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
            "maintainer_email": "",
            "cheesecake_code_kwalitee_id": null,
            "keywords": "Imaging",
            "package_url": "http://pypi.python.org/pypi/Pillow",
            "author": "Alex Clark (Fork Author)",
            "author_email": "aclark@aclark.net",
            "download_url": "",
            "platform": "",
            "version": "5.0.0",
            "cheesecake_documentation_id": null,
            "_pypi_hidden": false,
            "description": "...",
            "release_url": "http://pypi.python.org/pypi/Pillow/5.0.0",
            "downloads": {
                "last_month": 0,
                "last_week": 0,
                "last_day": 0
            },
            "_pypi_ordering": 57,
            "classifiers": [
                "Development Status :: 6 - Mature",
                "License :: Other/Proprietary License",
                "Programming Language :: Python :: 2",
                "Programming Language :: Python :: 2.7",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.4",
                "Programming Language :: Python :: 3.5",
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: Implementation :: CPython",
                "Programming Language :: Python :: Implementation :: PyPy",
                "Topic :: Multimedia :: Graphics",
                "Topic :: Multimedia :: Graphics :: Capture :: Digital Camera",
                "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
                "Topic :: Multimedia :: Graphics :: Graphics Conversion",
                "Topic :: Multimedia :: Graphics :: Viewers"
            ],
            "name": "Pillow",
            "bugtrack_url": "",
            "license": "Standard PIL License",
            "summary": "Python Imaging Library (Fork)",
            "home_page": "https://python-pillow.org",
            "cheesecake_installability_id": null
        },
        "more data..."
    }
