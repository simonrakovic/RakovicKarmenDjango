from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

class StaticSitemap(Sitemap):
   
    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home', 'povprasevanje', 'novice', 'kontakti']

    def location(self, item):
        return reverse(item)
        