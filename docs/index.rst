.. lazy documentation master file, created by
   sphinx-quickstart on Thu May 10 17:11:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===============================================
lazy |version| -- Lazy Attributes
===============================================

.. toctree::
   :maxdepth: 2

.. module:: lazy

The :mod:`lazy` module provides a decorator to create lazy attributes.
A lazy attribute is a computed attribute that is evaluated only once, the
first time it is used. Subsequent uses return the results of the first call.

API Documentation
=================

.. class:: lazy(func)

    lazy descriptor.

    Used as a decorator to create lazy attributes. Lazy attributes are
    evaluated on first use.

.. classmethod:: invalidate(inst, name)

    Invalidate a lazy attribute.

    This obviously violates the :class:`~lazy.lazy` contract. Subclasses
    of :class:`~lazy.lazy` may however have a contract where invalidation
    is appropriate.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

