=============================
PyPI Is Dead. Long Live PyPI.
=============================

A short talk for Taipei.py.

.. raw:: html

    <p><a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nd/3.0/88x31.png" /></a></p>
    <p>This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/">Creative Commons Attribution-NoDerivs 3.0 Unported License</a>.</p>


Build
=====

This is a Sphinx document intended to be read in HTML form. Install
dependencies, build the HTML, and open ``build/html/index.html`` to view.


Step by Step
============

If the previous section is too succinct for you.

Requirements
------------

* Python 3.6
* Pipenv_

.. _Pipenv: https://docs.pipenv.org

Setup
-----

::

    $ pipenv install --dev

Run live
--------

::

    $ pipenv run watch --open-browser

This should automatically build the HTML files, start an HTTP server to serve
them, and open a browser window for you to view.

Build without live server
-------------------------

::

    $ pipenv run build

This builds HTML files into ``build/html``.
