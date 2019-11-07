from rest_framework_xml.parsers import XMLParser


class DoXMLParser(XMLParser):

    tags = [
        'element',
        'list-item',
    ]

    def _xml_convert(self, element):

        children = list(element)

        if len(children) == 0:
            return self._type_convert(element.text)
        else:
            if children[0].tag in self.tags:
                datatag = []
                for child in children:
                    datatag.append(self._xml_convert(child))
            else:
                datatag = {}
                for child in children:
                    datatag[child.tag] = self._xml_convert(child)
            return datatag
