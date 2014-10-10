# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.conf import settings

CMS_VIMEO_LOOP = getattr(settings, "CMS_VIMEO_LOOP", False)
CMS_VIMEO_AUTOPLAY = getattr(settings, "CMS_VIMEO_AUTOPLAY", False)

CMS_VIMEO_BG_COLOR = getattr(settings, "CMS_VIMEO_BG_COLOR", "000000")
CMS_VIMEO_TEXT_COLOR = getattr(settings, "CMS_VIMEO_TEXT_COLOR", "FFFFFF")
CMS_VIMEO_SEEKBAR_COLOR = getattr(
    settings, "CMS_VIMEO_SEEKBAR_COLOR", "13ABEC")

CMS_VIMEO_SEEKBARBG_COLOR = getattr(
    settings, "CMS_VIMEO_SEEKBARBG_COLOR", "333333")

CMS_VIMEO_LOADINGBAR_COLOR = getattr(
    settings, "CMS_VIMEO_LOADINGBAR_COLOR", "828282")

CMS_VIMEO_BUTTON_OUT_COLOR = getattr(
    settings, "CMS_VIMEO_BUTTON_OUT_COLOR", "333333")

CMS_VIMEO_BUTTON_OVER_COLOR = getattr(
    settings, "CMS_VIMEO_BUTTON_OVER_COLOR", "000000")

CMS_VIMEO_BUTTON_HIGHLIGHT_COLOR = getattr(
    settings, "CMS_VIMEO_BUTTON_HIGHLIGHT_COLOR", "FFFFFF")

CMS_VIMEO_PLUGIN_ENABLE_ADVANCED_SETTINGS = getattr(
    settings, "CMS_VIMEO_PLUGIN_ENABLE_ADVANCED_SETTINGS", True)
