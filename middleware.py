### This middleware will set a variable, request.site
### to reference the current Site for the given request.

from django.contrib.sites.models import Site
from django.conf import settings

ignore_www_zone = getattr(settings, 'IGNORE_WWW_ZONE', True)

class SiteProviderMiddleware(object):
    def process_request(self, request:

        # Prevent future version collisions
        if hasattr(request, 'site'):
            return

        hostname = request.get_host()

        # Remove the www from our domain unless requested otherwise
        if ignore_www_zone and hostname[:4] == 'www.':
            hostname = hostname[4:]

        try:
            # Attempt to get a site based on the current domain
            request.site = Site.objects.get(domain=hostname)
        except Site.DoesNotExist:
            # If this site doesn't exist, revert to our SITE_ID
            request.site = Site.objects.get_current()

