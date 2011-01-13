from collective.plonetruegallery.browser.util import PTGUtility
from plone.memoize.view import memoize
from Products.CMFCore.utils import getToolByName
import logging

logging.getLogger('collective.collage.plonetruegallery').warn("Monkey patching collective.plonetruegallery.browser.util.PTGUtility's enabled method.")

@memoize
def enabled(self):
    utils = getToolByName(self.context, 'plone_utils')
    try:
        view_name = utils.browserDefault(self.context)[1][0] 
    except:
        return False
    return view_name in ["galleryview","collage_view"]

PTGUtility.enabled = enabled
