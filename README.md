djangocms-vimeo
===============

A [video.js](https://github.com/videojs/video.js) Vimeo video plugin for django CMS.
Loosely based on the [djangocms-video](https://github.com/divio/djangocms-video) plugin.
Uses the [videojs-vimeo](https://github.com/eXon/videojs-vimeo) plugin.


Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install djangocms-vimeo``.
* Add ``'djangocms_vimeo'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_vimeo``.


History
-------

* v0.1.5: Made fixes to videojs-vimeo to correctly detect HTTPS.
* v0.1.4: Added missing static directory to MANIFEST.
* v0.1.0: Inital release
