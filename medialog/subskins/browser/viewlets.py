from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class SubskinsLoader(ViewletBase):
    render = ViewPageTemplateFile('subskinsloader.pt')

class SubskinsColophon(ViewletBase):
    render = ViewPageTemplateFile('subskinscolophon.pt')

