====
lazy
====
----------------------------------
Lazy attributes for Python objects
----------------------------------

Package Contents
================

@lazy
    A decorator to create lazy attributes.

Overview
========

*Lazy attributes* are computed attributes that are evaluated only
once, the first time they are used.  Subsequent uses return the
results of the first call. They come handy when code should run

- *late*, i.e. just before it is needed, and
- *once*, i.e. not twice, in the lifetime of an object.

You can think of it as *deferred initialization*.
The possibilities are endless.

Examples
========

The class below creates its ``store`` resource lazily::

    from lazy import lazy

    class FileUploadTmpStore(object):

        @lazy
        def store(self):
            location = settings.get('fs.filestore')
            return FileSystemStore(location)

        def put(self, uid, fp):
            self.store.put(uid, fp)
            fp.seek(0)

        def get(self, uid, default=None):
            return self.store.get(uid, default)

Another application area is caching::

    class PersonView(View):

        @lazy
        def person_id(self):
            return self.request.get('person_id', -1)

        @lazy
        def person_data(self):
            return self.session.query(Person).get(self.person_id)

Credits
=======

I first encountered this type of descriptor in the
``zope.cachedescriptors`` package, which is part of the
`Zope Toolkit`_.

.. _`Zope Toolkit`: http://docs.zope.org/zopetoolkit/

