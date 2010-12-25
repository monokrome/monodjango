### This middleware will set a variable, request.site
### to reference the current Site for the given request.

from django.contrib.sites.models import Site, SiteManager
from django.conf import settings
import re

ignore_www_zone = getattr(settings, 'IGNORE_WWW_ZONE', True)
ignore_server_port = getattr(settings, 'IGNORE_SERVER_PORT', True)

# New get_current override, which can take a request into account. This is some
# nasty monkey patching, but it does what we want it to.
SiteManager.get_current_legacy = SiteManager.get_current

def get_current(self, request=None):
    if request is None:
        return Site.objects.get_current_legacy()

    hostname = request.get_host()

    # Remove the www from our domain unless requested otherwise
    if ignore_www_zone:
        hostname = re.sub(r'^w{2,3}\d*\.', '', hostname)

    if ignore_server_port:
        hostname = re.sub(r':\d*$', '', hostname)

    try:
        # Attempt to get a site based on the current domain
        return Site.objects.get(domain=hostname)

    except Site.DoesNotExist:
        # If this site doesn't exist, revert to our SITE_ID
        return Site.objects.get_current()

SiteManager.get_current = get_current

class SiteProviderMiddleware(object):
    def process_request(self, request):
        # Prevent future version collisions
        if hasattr(request, 'site'):
            return

        request.site = Site.objects.get_current(request)

