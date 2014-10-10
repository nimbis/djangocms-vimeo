# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.utils.compat.dj import python_2_unicode_compatible
from cms.models import CMSPlugin

from . import settings


@python_2_unicode_compatible
class VimeoVideo(CMSPlugin):
    """
    Vimeo video player (size, video url) and
    plugin (background color) settings.
    """

    # player settings
    movie_url = models.CharField(
        _('movie url'), max_length=255,
        help_text=_('Vimeo video url. '
                    'Example: https://vimeo.com/50516814'),
        blank=True, null=True)

    width = models.PositiveSmallIntegerField(_('width'))

    height = models.PositiveSmallIntegerField(_('height'))

    auto_play = models.BooleanField(
        _('auto play'), default=settings.CMS_VIMEO_AUTOPLAY)

    loop = models.BooleanField(_('loop'), default=settings.CMS_VIMEO_LOOP)

    def __str__(self):
        name = self.movie_url
        return u"%s" % os.path.basename(name)

    def get_height(self):
        """
        Return the height of the movie in pixels.
        """

        return "%s" % self.height

    def get_width(self):
        """
        Return the width of the movie in pixels.
        """
        return "%s" % self.width

    def get_movie(self):
        """
        Return the url of this movie.
        """

        return self.movie_url
