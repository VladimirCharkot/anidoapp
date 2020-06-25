from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from markdown.inlinepatterns import Pattern
import xml.etree.ElementTree as etree
import re

REL_RE = r'\[(\d*?)\]'
REF_RE = r'\((\d*?)\) ?\[(.*?)\]'    # ej (3)[Giroux, tal libro]
INS_RE = r'(__)(.*?)__'
#PAR_RE = re.compile(r'.*?<-(.*?)->.*?', re.DOTALL)
#REF_RE = re.compile(r'(\()(\d*?)\) \[(.*?)\]', re.DOTALL)
cita = '\n>blablablablabla\n>pispispispispis\n> - Fulano de Tal \n'

CIT_RE = r'\n?(>(.+?)\n)+> ?-(.+)\n'
CITL_RE = r'\n?(>(.+?)\n)'

# 'foo[9] bar \n\n(9) [refererefe]'
# 'foo[9] \n|- \nbar\nbaz\n\nbazzinga\n\nend \n-| \n\n(9)[comida]'

class Relacion(Pattern):
    def handleMatch(self, m):
        el = etree.Element('sup')
        el.text = '['+m.group(2)+']'
        el.attrib['class'] = 'rel'
        el.attrib['data-n'] = m.group(2)
        return el

class Referencia(Pattern):
    def handleMatch(self, m):
        el = etree.Element('div')
        el.text = '['+m.group(3)+']'
        el.attrib['class'] = 'ref'
        el.attrib['data-r'] = m.group(2)
        return el

"""class Cita(Pattern):
    def handleMatch(self, m):
        d = etree.Element('div')
        d.attrib['class'] = 'cita'
        partes = re.findall(CITL_RE, m.group())
        for parte in partes[:-1]:
            p = etree.Element('p')
            p.text = parte[1]
            d.append(p)
        p = etree.Element('p')
        p.text = partes[-1][1]
        p.attrib['class'] = 'firma'
        return el"""

#            <div class="cita">
#                <p>{{ elemento.texto }}</p>
#                <p class="firma">— {{ elemento.autor }}</p>
#            </div>

#md.inlinePatterns.deregister('em_strong')

class Parrafo(BlockProcessor):
    RE_ABRIR  = r'\s*\|- *\n'
    RE_CERRAR = r'\n *-\|\s*$'

    def test(self, parent, block):
        return re.match(self.RE_ABRIR, block)

    def run(self, parent, blocks):
        original_block = blocks[0]
        blocks[0] = re.sub(self.RE_ABRIR, '', blocks[0])

        # Buscar tag de cierre
        for block_num, block in enumerate(blocks):
            if re.search(self.RE_CERRAR, block):
                blocks[block_num] = re.sub(self.RE_CERRAR, '', block)
                # Encontrado
                e = etree.SubElement(parent, 'div')
                e.set('class', 'parrafo')
                self.parser.parseBlocks(e, blocks[0:block_num + 1])

                for i in range(0, block_num + 1):
                    blocks.pop(0)
                return True
        blocks[0] = original_block
        return False


class Cita(BlockProcessor):
    RE_ABRIR = '> '
    RE_CERRAR = '> -'

    def test(self, parent, block):
        return re.match(self.RE_ABRIR, block)

    def run(self, parent, blocks):
        original_block = blocks[0]
        blocks[0] = re.sub(self.RE_ABRIR, '', blocks[0])
        print("Bloques recibidos: ", blocks)

        for block_num, block in enumerate(blocks):
            print("Procesando bloque ", block_num, block)
            if not(re.match(self.RE_ABRIR, block)):
                break

            if re.search(self.RE_CERRAR, block):
                re.sub(self.RE_ABRIR, '', blocks[block_num])

                d = etree.Element('div')
                d.attrib['class'] = 'cita'
                partes = blocks[0:block_num-1]

                for parte in partes:
                    p = etree.Element('p')
                    p.text = parte
                    d.append(p)
                p = etree.Element('p')
                p.text = partes[-1]
                p.attrib['class'] = 'firma'
                return el

            re.sub(self.RE_ABRIR, '', blocks[block_num])

        blocks[0] = original_block
        return False

# print(etree.tostring(xml_node, pretty_print=True))

class MDExt(Extension):
   def extendMarkdown(self, md):
       md.inlinePatterns.register(Relacion(REL_RE), 'rel', 175)

       md.inlinePatterns.register(Referencia(REF_RE), 'ref', 170)

       #md.inlinePatterns.register(Cita(CIT_RE), 'cita', 1500)

       md.parser.blockprocessors.register(Parrafo(md.parser), 'parrafo', 175)

       #print(md.parser.blockprocessors._data)
       #md.parser.blockprocessors.deregister('quote')
       #md.parser.blockprocessors.register(Cita(md.parser), 'quote', 1500)

       #ins_tag = SimpleTagPattern(INS_RE, 'ins')
       #md.inlinePatterns.add('ins', ins_tag, '>del')

# puede manejar opciones:
# markdown.markdown(txt, extensions=[MultiExtension(ins_del=True)])