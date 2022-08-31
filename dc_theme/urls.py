from django import http
from django.conf import settings
from django.conf.urls import url
from django.template import TemplateDoesNotExist, loader
from django.views.decorators.csrf import requires_csrf_token
from django.views.defaults import page_not_found, ERROR_500_TEMPLATE_NAME
from django.views.generic import TemplateView


@requires_csrf_token
def dc_server_error(request, template_name=ERROR_500_TEMPLATE_NAME):
    """
    The same as the Django 500 view but add the site logo.
    """
    context = {
        "site_logo": getattr(
            settings, "SITE_LOGO", "dc_theme/images/logo-with-text.png"
        )
    }
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        if template_name != ERROR_500_TEMPLATE_NAME:
            # Reraise if it's a missing custom template.
            raise
        return http.HttpResponseServerError(
            "<h1>Server Error (500)</h1>", content_type="text/html"
        )
    return http.HttpResponseServerError(template.render(context, request))


urlpatterns = [
    url(
        r"^$",
        TemplateView.as_view(template_name="html_tester/all_elements.html"),
        name="html_tester",
    ),
    url(r"500.html$", dc_server_error),
    url(r"404.html$", page_not_found, {"exception": "Fake problem"}),
]
