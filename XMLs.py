import xml.etree.ElementTree as ET
import os

class XMLs:
    def __init__(self):
        self.root = None
        self.arq = None
        self.tree = None

    def carregarXML(self, arq):
        if os.path.exists(self.arq):
            self.tree = ET.parse(self.arq)
            self.root = self.tree.getroot()
        else:
            raise FileNotFoundError(f"Arquivo não encontrado: {self.arq}")

    def validarTag(self, tag):
        valor = self.root.find(f".//{tag}")
        if valor is not None:
            return valor.text
        
        else:
            return None
        
        