from django.db.models import get_model
from regluit.core import cc

    
class BaseFacet(object):
    facet_name = 'all'
    outer_facet = None
    model = get_model('core', 'Work')
    
    def __init__(self, outer_facet):
        if outer_facet:
            self.outer_facet = outer_facet
    
    def _get_query_set(self):
        if self.outer_facet:
            return self.outer_facet.get_query_set()
        else:
            return self.model.objects.filter(editions__ebooks__isnull=False)
           
    def get_query_set(self):
        return self._get_query_set()

    def get_facet_path(self):
        if self.outer_facet:
            return self.outer_facet.get_facet_path() + self.facet_name + '/'
        else:
            return self.facet_name + '/'


class FacetGroup(object):
    pass
    
class NamedFacet(BaseFacet):
    def __init__(self, outer_facet):
        super(NamedFacet, self).__init__( outer_facet )
        self.set_name()
    
class FormatFacetGroup(FacetGroup):
    facets = ['pdf', 'epub', 'mobi']
    def has_facet(self, facet_name):
        return facet_name in self.facets
        
    def get_facet_class(self, facet_name):
        class FormatFacet(NamedFacet):
            def set_name(self):
                self.facet_name=facet_name
            def get_query_set(self):
                return self._get_query_set().filter(editions__ebooks__format=self.facet_name)
        return FormatFacet
        
        
class LicenseFacetGroup(FacetGroup):
    licenses = cc.LICENSE_LIST_ALL
    facets = cc.FACET_LIST    
    def has_facet(self, facet_name):
        return facet_name in self.facets
        
    def get_facet_class(self, facet_name):
        class LicenseFacet(NamedFacet):
            def set_name(self):
                self.facet_name=facet_name
            def get_query_set(self):
                return self._get_query_set().filter(editions__ebooks__rights=cc.licence_value(self.facet_name))
        return LicenseFacet
    
facet_groups = [ FormatFacetGroup() , LicenseFacetGroup() ]

def get_facet(facet_name):
    for facet_group in facet_groups:
        if facet_group.has_facet(facet_name):
            return facet_group.get_facet_class(facet_name)
    return BaseFacet
              
