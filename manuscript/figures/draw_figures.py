"""Deterministic vector figures for the survey; no measured study counts.

Sources: sections 02, 04, and 07 and the accompanying papers.md register.
PDF is the manuscript format; SVG preserves editable text and geometry.
Coordinates use a top-left origin. Font sizes are in points at final width.
"""
from pathlib import Path
from html import escape
import math
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import toColor as HexColor

ROOT=Path(__file__).resolve().parent
from font_config import font_path
pdfmetrics.registerFont(TTFont('TimesCustom',font_path('serif')))
pdfmetrics.registerFont(TTFont('TimesCustomBold',font_path('serif_bold')))
INK='#243442'; BLUE='#245779'; TEAL='#286C60'; RUST='#925036'; LINE='#BEC9CF'
class Figure:
    def __init__(self,name,w,h):
        self.name,self.w,self.h=name,w,h
        self.c=canvas.Canvas(str(ROOT/(name+'.pdf')),pagesize=(w,h))
        self.c.setTitle(name.replace('-',' ').title())
        self.svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}pt" height="{h}pt" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/>']
    def rect(self,x,y,w,h,fill='white',stroke=LINE):
        self.c.setFillColor(HexColor(fill)); self.c.setStrokeColor(HexColor(stroke)); self.c.setLineWidth(.65)
        self.c.rect(x,self.h-y-h,w,h,fill=1,stroke=1)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width=".65"/>')
    def text(self,x,y,s,size=9,bold=False,color=INK,anchor='start'):
        font='TimesCustomBold' if bold else 'TimesCustom'
        self.c.setFont(font,size); self.c.setFillColor(HexColor(color))
        fn={'start':self.c.drawString,'middle':self.c.drawCentredString,'end':self.c.drawRightString}[anchor]
        fn(x,self.h-y,s)
        self.svg.append(f'<text x="{x}" y="{y}" font-family="Times New Roman,serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="{color}" text-anchor="{anchor}">{escape(s)}</text>')
    def lines(self,x,y,lines,**kw):
        for i,s in enumerate(lines): self.text(x,y+i*11,s,**kw)
    def path(self,pts,color=BLUE,dashed=False,arrow=False):
        self.c.setStrokeColor(HexColor(color)); self.c.setLineWidth(.85); self.c.setDash([3,2] if dashed else [])
        p=self.c.beginPath(); p.moveTo(pts[0][0],self.h-pts[0][1])
        for x,y in pts[1:]: p.lineTo(x,self.h-y)
        self.c.drawPath(p); self.c.setDash([])
        self.svg.append(f'<polyline points="{" ".join(str(x)+","+str(y) for x,y in pts)}" fill="none" stroke="{color}" stroke-width=".85"'+(' stroke-dasharray="3 2"' if dashed else '')+'/>')
        if arrow:
            (x0,y0),(x,y)=pts[-2:]; a=math.atan2(y-y0,x-x0)
            ends=[(x-4*math.cos(a+t),y-4*math.sin(a+t)) for t in [-.45,.45]]
            self.path([ends[0],(x,y),ends[1]],color)
    def save(self):
        self.c.save(); (ROOT/(self.name+'.svg')).write_text('\n'.join(self.svg+['</svg>']),encoding='utf-8')

def overview():
    from illustrated_vector import render
    render()


def landscape():
    f=Figure('literature-map',420,229)
    x=[3,83,162,245,328,417]
    heads=[['Testing setting'],['Scenarios /','obligations'],['Inputs /','actions'],['Tests /','oracles'],['Generators /','mutators']]
    for i,ls in enumerate(heads): f.lines(x[i]+5,12,ls,size=9,bold=True,color=BLUE)
    rows=[
      ('Unit / regression',{3:['TestPilot [P,F]','CoverUp [P,F]']}),
      ('Requirements',{1:['RAGTAG [P,R]'],3:['Test Flow [P]']}),
      ('Oracle synthesis',{3:['nl2postcond [P]','Nexus [P,F]']}),
      ('API / GUI',{2:['DroidAgent [P,F]'],3:['SAINT [P,A]']}),
      ('Fuzzing',{2:['TitanFuzz [P]'],4:['PromptFuzz [P,F]','ELFuzz [P,S]']}),
      ('Code-task testing',{3:['PyTester [L]','UTRL [L]'],4:['SAGE [L]']})]
    for r,(name,cells) in enumerate(rows):
        y=32+r*27
        f.rect(3,y,414,27,'#F4F7F9' if r%2==0 else 'white',LINE)
        f.text(8,y+16,name,8.6,True)
        for col,labels in cells.items():
            f.lines(x[col]+4,y+(11 if len(labels)>1 else 16),labels,size=8.5,color=TEAL)
    f.lines(4,207,['Mechanisms: P prompting; A analysis; R retrieval; F execution feedback;',
                    'L parameter learning; S search. Blank cells are unlisted, not absent.'],size=8.7)
    f.save()

def evidence():
    f=Figure('quality-evidence',420,190)
    f.text(3,11,'WHAT IS OBSERVED',9,True,BLUE)
    f.text(183,11,'WHAT THIS SUPPORTS',9,True,TEAL)
    entries=[
      ('Build and run in the target environment','Executability in that environment'),
      ('Reach a line, branch, or path','Structural coverage'),
      ('Pass an executed reference program','Reference consistency'),
      ('Reject independent faulty programs','Fault detection on the chosen pool'),
      ('Accept alternative legal implementations','Non-rejection on the chosen pool')]
    for i,(a,b) in enumerate(entries):
        y=23+i*24
        f.rect(3,y,163,20,'#F1F6FA'); f.text(8,y+13,a,8.7)
        f.path([(166,y+10),(181,y+10)],arrow=True)
        f.rect(183,y,234,20,'#F3F7F5'); f.text(189,y+13,b,9)
    f.path([(3,153),(417,153)],LINE)
    f.text(5,168,'Oracle semantics: judge the assertion against the intended behavior.',9.5,True,RUST)
    f.text(5,182,'Combine complementary evidence; the rows are not a ranking or an implication chain.',9)
    f.save()

if __name__=='__main__':
    overview(); landscape(); evidence()
    print('Created three vector PDF/SVG figure pairs.')
