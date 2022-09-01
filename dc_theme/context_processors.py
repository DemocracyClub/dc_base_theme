from django.conf import settings


def setting(key, default):
    return getattr(settings, key, default)


def dc_theme_context(request):
    return {
        "site_title": setting("SITE_TITLE", "Democracy Club"),
        "site_og_image": setting("SITE_OG_IMAGE", "dc_theme/icons/og-image.jpg"),
        "site_logo": setting("SITE_LOGO", "dc_theme/images/logo-with-text.png"),
        "site_logo_width": setting("SITE_LOGO_WIDTH", 300),
    }
