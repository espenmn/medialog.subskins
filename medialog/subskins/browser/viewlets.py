from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from plone.portlets.interfaces import IPortletManager
from fractions import Fraction
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


from Products.CMFPlone import PloneMessageFactory as _


from AccessControl import getSecurityManager
from Acquisition import aq_base, aq_inner

from plone.memoize.view import memoize
from zope.component import getMultiAdapter
#from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets.common import GlobalSectionsViewlet as BaseGlobalSectionsViewlet


class SubskinsLoader(ViewletBase):
    render = ViewPageTemplateFile('subskinsloader.pt')

class SubskinsColophon(ViewletBase):
    render = ViewPageTemplateFile('subskinscolophon.pt')
    
class FooterPortlets(ViewletBase):
	name = 'subskins.footerportlets'
	manage_view = '@@manage-footerportlets'
	
class GlobalSectionsViewlet(BaseGlobalSectionsViewlet):
    index = ViewPageTemplateFile('globalnavviewlet.pt')

    def update(self):
    	# stuff for SearchBoxViewlet
        super(BaseGlobalSectionsViewlet, self).update()
        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')

        self.search_input_id = "searchGadget"
        
        folder = context_state.folder()
        self.folder_path = '/'.join(folder.getPhysicalPath())

        # normal GlobalSectionsViewlet stuff
        context = aq_inner(self.context)
        portal_tabs_view = getMultiAdapter((context, self.request),
                                           name='portal_tabs_view')
        self.portal_tabs = portal_tabs_view.topLevelTabs()

        self.selected_tabs = self.selectedTabs(portal_tabs=self.portal_tabs)
        self.selected_portal_tab = self.selected_tabs['portal']