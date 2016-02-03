from ns import qn
from simpletypes import ST_String, ST_DecimalNumber
from xmlchemy import (
    BaseOxmlElement, RequiredAttribute
)

class CT_BookmarkStart(BaseOxmlElement):
    wid = RequiredAttribute('w:id', ST_DecimalNumber)
    wname = RequiredAttribute('w:name', ST_String)

    @property
    def id(self):
        val = self.get(qn('w:id'))
        return val

    @id.setter
    def id(self, bid):
        self.set(qn('w:id'), bid)

    @property
    def name(self):
        val = self.get(qn('w:name'))
        return val

    @name.setter
    def name(self, bname):
        self.set(qn('w:name'), bname)

class CT_BookmarkEnd(BaseOxmlElement):
    wid = RequiredAttribute('w:id', ST_DecimalNumber)

    @property
    def id(self):
        val = self.get(qn('w:id'))
        return val

    @id.setter
    def id(self, bid):
        self.set(qn('w:id'), bid)
