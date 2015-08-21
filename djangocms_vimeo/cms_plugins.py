# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import VimeoVideoForm
from .models import VimeoVideo


class VimeoVideoPlugin(CMSPluginBase):
    model = VimeoVideo
    name = _("Vimeo Video")
    form = VimeoVideoForm

    render_template = "djangocms_vimeo/video.html"

    general_fields = [
        'movie_url',
        ('width', 'height'),
        'auto_play',
        'loop',
    ]

    fieldsets = [
        (None, {
            'fields': general_fields,
        }),
    ]

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(VimeoVideoPlugin)
