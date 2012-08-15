from plone.theme.interfaces import IDefaultPloneLayer
from plone.portlets.interfaces import IPortletManager

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IMedialogFooterContent(IPortletManager):
    """we need our own portlet manager below the content area.
    """
