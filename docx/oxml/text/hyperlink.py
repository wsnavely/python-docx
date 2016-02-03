# encoding: utf-8

"""
Custom element classes related to hyperlinks (CT_Hyperlink).
"""

from ..ns import qn
from ..simpletypes import ST_RelationshipId
from ..xmlchemy import (
    BaseOxmlElement, OptionalAttribute, RequiredAttribute, ZeroOrMore
)

class CT_Hyperlink(BaseOxmlElement):
    """
    ``<w:hyperlink>`` element, containing the properties and text for a hyperlink.

    The ``<w:hyperlink>`` contains a ``<w:r>`` element which holds all the
    visible content. The ``<w:hyperlink>`` has an attribute ``r:id`` which
    holds an ID relating a URL in the document's relationships.
    """
    r = ZeroOrMore('w:r')
    rid = OptionalAttribute('r:id', ST_RelationshipId)
    anchor = OptionalAttribute('r:anchor', ST_RelationshipId)

    @property
    def anchor(self):
        val = self.get(qn('r:anchor'))
        return val

    @anchor.setter
    def anchor(self, anchor):
        self.set(qn('w:anchor'), anchor)
        self.set(qn('w:history'), '1')

    @property
    def relationship(self):
        """
        String contained in ``r:id`` attribute of <w:hyperlink>. It should
        point to a URL in the document's relationships.
        """
        val = self.get(qn('r:id'))
        return val

    @relationship.setter
    def relationship(self, rId):
        self.set(qn('r:id'), rId)
        self.set(qn('w:history'), '1')

    def clear_content(self):
        """
        Remove all child r elements
        """
        r_to_rm = []
        for child in self[:]:
            if child.tag == qn('w:r'):
                r_to_rm.append(child)
        for r in r_to_rm:
            self.remove(r)
