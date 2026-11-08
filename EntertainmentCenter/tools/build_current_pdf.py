"""Build Rev F from preserved Rev E with explicit current-design replacements.
Requires PyMuPDF (fitz), reportlab. Run from any working directory.
"""
from io import BytesIO
from pathlib import Path
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'docs/entertainment-center-build-guide-rev-f.pdf'

def replace(page, prefix, text, size=10):
    blocks=[b for b in page.get_text('blocks') if b[4].startswith(prefix)]
    assert len(blocks)==1, (page.number+1,prefix,len(blocks))
    b=blocks[0];rect=fitz.Rect(b[:4]); rect.x1=756
    page.add_redact_annot(rect,fill=(1,1,1))
    page.apply_redactions(images=0,graphics=0)
    # Place the new text in exactly the original block's vertical space.
    box=fitz.Rect(rect.x0,rect.y0,756,rect.y1+1)
    result=page.insert_textbox(box,text,fontsize=size,fontname='helv',color=(.08,.17,.22),lineheight=1.15)
    assert result>=0,(page.number+1,prefix,result)

def main():
    doc=fitz.open(ROOT/'docs/entertainment-center-build-guide-rev-e.pdf')
    for i,p in enumerate(doc):
        for target,text,rect in [('REV E','REV F',fitz.Rect(730,6,765,22)),(f'{i+1} / 12',f'{i+1} / 14',fitz.Rect(706,581,756,598))]:
            matches=p.search_for(target);assert len(matches)==1
            p.add_redact_annot(matches[0],fill=(1,1,1));p.apply_redactions(images=0,graphics=0)
            assert p.insert_textbox(rect,text,fontsize=9,fontname='helv',color=(.08,.17,.22))>=0
    replace(doc[0],'Four separate plywood boxes','Four separate plywood boxes | 93 wide x 16 high x 20 deep before trim and joined white top',10)
    replace(doc[0],'3 sheets of 4 ft', '3 sheets of nominal 3/4" cabinet plywood cover the original boxes, shelves, surround and one door blank.\nReserve additional stock for the joined white top and remaining three doors; finalize material and thickness first.\nDo not buy the former 10 ft butcher-block blank. Finished top target: 112" x about 20 1/4", field-fit.\nTrim: two straight 8 ft poplar strips for long rails, plus matching stock for five short strips.',10)
    replace(doc[2],'112 assembly /','112 assembly / joined painted-white top',9)
    replace(doc[2],'1 1/2" nominal wood','White top: thickness TBD',9)
    replace(doc[2],'Box bottom 8 1/2','Box bottom 8 1/2". Box top 24 1/2". Finished height = 24 1/2" + selected top thickness.',10)
    replace(doc[2],'Door layout follows','Current direction: four inset doors, one per floating bay; subwoofer stays open. See pages 13-14.',9)
    # Visually distinguish the four closed fronts and a white cap in the elevation.
    p=doc[2]; k=5.35; x=58+(6.625+19)*k; base=290-0 # original drawing uses bottom-left coordinates
    for w in [26,26,20,21]:
        # Original reportlab front: y=335.475, height=85.6; PDF top-left y=190.925.
        p.draw_rect(fitz.Rect(x+4,195,x+w*k-4,272),color=(.65,.69,.64),width=.6,overlay=False)
        x+=w*k
    # Change cap fill while preserving dimension labels above it.
    p.draw_rect(fitz.Rect(58+6.625*k,182.9,58+118.625*k,190.9),fill=(.96,.96,.93),color=(.6,.64,.59),width=.5)
    replace(doc[3],'02   Shelves and inset door','02   Shelves and four inset doors',11)
    replace(doc[3],'Fit one flat inset door','Fit one inset door per bay (four total). Subtract 1/4" from each measured opening for 1/8" reveals.',10)
    replace(doc[3],'03   Stainable butcher','03   Joined painted-white top',11)
    replace(doc[3],'One continuous cap spans','Join shorter panels into one finished white top spanning all 112". Place the seam over solid support.',10)
    replace(doc[3],'Target 112" wide','Target 112" x about 20 1/4"; material and thickness TBD. Finished height = 24 1/2" + top thickness.',10)
    replace(doc[3],'Account for the slab weight','Retain all box tops. Stabilize the seam mechanically before filling, sanding, priming and painting. See p. 14.',10)
    replace(doc[8],'Fit the shelves, trim and inset door','Fit shelves, trim and four inset doors',25)
    replace(doc[8],'03  Build and hang','03  Build and hang four inset doors',11)
    replace(doc[8],'Cut a flat 3/4" paint-grade','Fit four inset doors to the installed trim openings; Shaker styling is shown in the current reference.\nMaterial, thickness and hardware remain to be selected before door cutting and hinge drilling.\nFor 1/8" reveals, subtract 1/4" from each opening dimension; confirm against hinge specifications.\nTest on scrap. Provide room-air intake and exhaust for enclosed equipment; see page 14.',10)
    replace(doc[8],'Align boxes, fit shelves and trim','Align boxes, fit shelves and trim, measure all four doors, then finish. Keep doors removable for adjustment.',10)
    replace(doc[9],'One 112-inch butcher','One joined painted-white top | Current finish and top details on pages 13-14',11)
    replace(doc[9],'02  Fit and fasten','02  Join and finish the white top',11)
    replace(doc[9],'Start with the 10 ft blank','Field-fit the 112" length and approximately 20 1/4" depth after the boxes and surround are aligned.\nLocate the panel seam over a supported cabinet area. Stabilize the joint with substrate-appropriate joinery\nand backing where needed, then fill, sand, prime and paint. Filler is cosmetic, not the joint connection.\nRetain the plywood box tops. Finalize stock, thickness, joinery and fastening before cutting; see page 14.',10)
    replace(doc[9],'Dry-fit the warm LED','Retain the warm underside lighting; interior lights are optional behind opaque doors. Test wiring first.\nProvide a low room-air intake and a separate exhaust back to the room; inter-bay holes alone do not cool.\nKeep drivers, fans, controllers and cables accessible and clear of hinges, fasteners and hot equipment.',10)
    replace(doc[9],'Wood Welded butcher','Current joined-top and ventilation details: page 14 (replaces butcher-block guidance).',8)
    for link in doc[9].get_links(): doc[9].delete_link(link)
    replace(doc[11],'One 4 ft x 8 ft sheet','Original Sheet 3 layout: surround and ONE door blank only. Extra door/top stock required.',10)
    replace(doc[11],'If any fitted dimension','Reserve extra stock for three more doors and the joined top; this layout is not the full revised shopping list.',9)
    buf=BytesIO();c=canvas.Canvas(buf,pagesize=(792,612));ink=HexColor('#263d31')
    def header(title,n):
        c.setFillColor(ink);c.setFont('Helvetica-Bold',10);c.drawString(36,582,'ENTERTAINMENT CENTER / REV F')
        c.setFont('Helvetica',25);c.drawString(36,549,title)
        c.setFont('Helvetica',9);c.drawRightString(756,20,f'{n} / 14')
    header('Current design: four doors and a white top',13)
    image=ImageReader(str(ROOT/'assets/design-white-top.png'));iw,ih=image.getSize();scale=min(720/iw,435/ih)
    c.drawImage(image,(792-iw*scale)/2,94,width=iw*scale,height=ih*scale)
    c.setFont('Helvetica',10)
    c.drawString(36,70,'Four floating bays: Xbox 26", Denon 26", Switch 20", storage 21". Separate 19" open subwoofer alcove.')
    c.drawString(36,54,'The image shows the selected finish and door arrangement. Top thickness is illustrative; dimensions govern cuts.')
    c.drawString(36,38,'Rev F replaces the butcher-block purchase and one-door finish plan. Box panel dimensions are unchanged.')
    c.showPage();header('Joined white top: decisions and assembly',14)
    y=513
    sections=[
      ('01  Confirm the substrate and finished height',[
       'Target one finished 112" x approximately 20 1/4" top, made from shorter joined panels.',
       'Material and thickness are not selected. Paint-grade plywood or MDF need different edge and joint treatment.',
       'Keep all existing box tops and the surround top. Finished elevation = 24 1/2" + chosen top thickness.',
       'The previous 26" height applies only to a 1 1/2" top. Reserve additional top and door stock before buying.']),
      ('02  Support and stabilize the seam before filling',[
       'Dry-fit after mounting, leveling and joining the boxes. Place the seam over solid support, away from a box joint.',
       'Use joinery suitable for the substrate and backing where needed; keep both panel faces coplanar.',
       'Biscuits or splines can help alignment; filler alone cannot connect the panels or prevent movement cracks.',
       'Check fastener depth and access from below. Do not cut mounting strips, cleats or box joints for seam hardware.']),
      ('03  Fill, sand, prime and paint',[
       'Follow the selected adhesive cure time. Fill the stable seam with a compatible paint-grade filler and sand flush.',
       'Seal exposed edges, prime and sand as the coating system requires, then paint the top uniformly white.',
       'Finish exposed faces and underside as appropriate for the substrate. Let coatings cure before placing speakers.',
       'A filled seam can telegraph later if the panels move; plan the joint and support before committing to a finish.']),
      ('04  Four doors and enclosed-equipment cooling',[
       'Current visual direction: one inset Shaker-style white door on each floating bay; subwoofer stays open.',
       'Fit doors after face trim. Three additional doors and top stock are not included in the original three-sheet layout.',
       'Select door material, hinges and opening method; do not drill from the rendering. Verify hardware on scrap.',
       'Provide low intake air from the room and exhaust back into the room, with fans if required for the heat load.',
       'Inter-bay openings only connect the airflow path. Confirm equipment clearances and test temperatures closed.',
       'Vent routes, fan sizes and structural mounting details remain to be finalized before drilling or loading.'])]
    for title,lines in sections:
        c.setFont('Helvetica-Bold',11);c.drawString(36,y,title);y-=20
        c.setFont('Helvetica',10)
        for line in lines:c.drawString(36,y,line);y-=15
        y-=15
    c.showPage();c.save()
    appendix=fitz.open(stream=buf.getvalue(),filetype='pdf');doc.insert_pdf(appendix)
    doc.set_metadata({'title':'Entertainment Center Build Guide - Rev F','subject':'Four doors and joined painted-white top; material and thickness pending'})
    doc.save(OUTPUT,garbage=4,deflate=True)
    print(OUTPUT)
if __name__=='__main__':main()
