from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class CookView(BrowserView):
    """
    cook portal_css and portal_javascript
    """
    
    def __call__(self,):
        cssregistry=getToolByName(self, 'portal_css')        
        javascriptregistry=getToolByName(self, 'portal_javascripts')        
        cssregistry.cookResources()
        javascriptregistry.cookResources()