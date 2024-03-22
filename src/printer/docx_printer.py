from docxtpl import DocxTemplate


class DOCXPrinter:
    @staticmethod
    def print(template, data, filepath):
        doc = DocxTemplate(template)
        doc.render(data)
        doc.save(filepath)
