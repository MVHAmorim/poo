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

    def validarTag(self, tag, node = None) -> str:
        if node:
            valor = node.find(f'{tag}')
        else:
            valor = self.root.find(f'{tag}')

        if valor is not None:
            return valor.text

        else:
            return None        

    def formatarCSTICMS(self, node) -> str:
        origem = node.find(f'imposto/ICMS//Orig')
        cst = node.find(f'imposto/ICMS//CST')
        csosn = node.find(f'imposto/ICMS//CSOSN')
        return f'{origem}{cst}{csosn}'


    def carregarProdutos(self):
        for prod in self.root.findall(f".//det"):
            nitem = self.validarTag('@nItem', prod)
            cprod = self.validarTag('prod/cProd', prod)
            xprod = self.validarTag('prod/xProd', prod)
            qcom = self.validarTag('prod/qCom', prod)
            ucom = self.validarTag('prod/uCom', prod)
            ncm = self.validarTag('prod/NCM', prod)
            cest = self.validarTag('prod/CEST', prod)
            vprod = self.validarTag('prod/vProd', prod)
            vdesc = self.validarTag('prod/vDesc', prod)
            csticms = self.formatarCSTICMS(prod)
            cfop = self.validarTag('prod/CFOP', prod)
            vbcicms = self.validarTag('imposto//ICMS/vBC', prod)
            picms = self.validarTag('imposto//ICMS/pICMS', prod)
            vicms = self.validarTag('imposto//ICMS/vICMS', prod)
            vbcicmsst = self.validarTag('imposto//ICMS/vBCST', prod)
            picmsst = self.validarTag('imposto//ICMS/pICMSST', prod)
            vicmsst = self.validarTag('imposto//ICMS/vICMSST', prod)
            cstipi = self.validarTag('imposto//IPI/CST', prod)
            codenq = self.validarTag('imposto//IPI/codEnq', prod) # <-- Pesquisar tag correta para código de enquadramento
            vbcipi = self.validarTag('imposto//IPI/vBC', prod)
            pipi = self.validarTag('imposto//IPI/pIPI', prod)
            vipi = self.validarTag('imposto//IPI/vIPI', prod)
            cstpis = self.validarTag('imposto//PIS/CST', prod)
            vbcpis = self.validarTag('imposto//PIS/vBC', prod)
            ppis = self.validarTag('imposto//PIS/pPIS', prod)            
            qbcpis = self.validarTag('imposto//PIS/qBCPIS', prod) # <-- Pesquisar tag correta para base de cálculo em reais
            ppisreais = self.validarTag('imposto//PIS/pPISReais', prod) # <-- Pesquisar tag correta para aliquota em reais
            vpis = self.validarTag('imposto//PIS/vPIS', prod)
            cstcofins = self.validarTag('imposto//COFINS/CST', prod)
            vbccofins = self.validarTag('imposto//COFINS/vBC', prod)
            pcofins = self.validarTag('imposto//COFINS/pCOFINS', prod)            
            qbccofins = self.validarTag('imposto//COFINS/qBCCOFINS', prod) # <-- Pesquisar tag correta para base de cálculo em reais
            pcofinsreais = self.validarTag('imposto//COFINS/pCOFINSReais', prod) # <-- Pesquisar tag correta para aliquota em reais
            vcofins = self.validarTag('imposto//COFINS/vCOFINS', prod)
            vabatnt = self.validarTag('imposto//COFINS/vAbatNt', prod) # <-- Pesquisar tag correta para valor de abatimento

            [nitem, cprod, xprod, qcom, ucom, ncm, cest, vprod, vdesc, csticms, cfop]