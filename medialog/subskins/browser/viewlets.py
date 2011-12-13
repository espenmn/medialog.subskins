from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class SubskinsLoader(ViewletBase):
    render = ViewPageTemplateFile('subskinsloader.pt')

class SubskinsColophon(ViewletBase):
    render = ViewPageTemplateFile('subskinscolophon.pt')
    def __call__(self, REQUEST):
        css_file = self.request.get('css', '')  
        return css_file
