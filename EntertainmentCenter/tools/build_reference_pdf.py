"""Append the supplied design reference without changing Rev E's 12 pages.

Optional document-generation dependencies: reportlab and pypdf.
The browser app does not need these packages.
"""
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'docs/entertainment-center-build-guide-rev-e.pdf'
reference = ROOT / 'assets/design-reference.png'
output = ROOT / 'docs/entertainment-center-build-guide-rev-e-with-reference.pdf'


def main():
    reader = PdfReader(source)
    assert len(reader.pages) == 12, 'Expected the original 12-page Rev E guide'
    width, height = float(reader.pages[0].mediabox.width), float(reader.pages[0].mediabox.height)
    buffer = BytesIO()
    page = canvas.Canvas(buffer, pagesize=(width, height))
    page.setFillColor(HexColor('#263d31'))
    page.setFont('Helvetica-Bold', 10)
    page.drawString(36, height - 30, 'FLOATING ENTERTAINMENT CENTER / REV E + DESIGN REFERENCE')
    page.setFont('Helvetica', 24)
    page.drawString(36, height - 65, 'Design reference')
    image = ImageReader(str(reference))
    iw, ih = image.getSize()
    scale = min((width - 72) / iw, (height - 190) / ih)
    w, h = iw * scale, ih * scale
    page.drawImage(image, (width - w) / 2, 100 + (height - 190 - h) / 2,
                   width=w, height=h, mask='auto')
    page.setFont('Helvetica', 10)
    page.drawString(36, 77, 'Visual reference for the white finish, continuous wood top, and warm interior / underside lighting.')
    page.drawString(36, 61, 'Doors, bay arrangement, shelves and equipment differ from the dimensioned Rev E plan.')
    page.drawString(36, 45, 'Use pages 1-12 for written dimensions. This image does not revise the cut list or mounting details.')
    page.setFont('Helvetica', 9)
    page.drawRightString(width - 36, 22, '13 / 13')
    page.save()
    writer = PdfWriter()
    writer.append(reader)
    writer.append(PdfReader(BytesIO(buffer.getvalue())))
    writer.add_metadata({'/Title': 'Entertainment Center | Rev E with Design Reference',
                         '/Subject': 'Original 12-page Rev E build guide with a visual-reference appendix'})
    with output.open('wb') as stream:
        writer.write(stream)
    print(output)


if __name__ == '__main__':
    main()
