from plone.theme.interfaces import IDefaultPloneLayer
from plone.portlets.interfaces import IPortletManager
from zope.viewlet.interfaces import IViewletManager

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IMedialogFooterContent(IPortletManager):
    """we need our own portlet manager below the content area.
    """
    
class IAboveContentViews(IViewletManager):
    """A viewlet manager that sits above the content views
    """