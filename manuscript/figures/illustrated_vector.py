"""Native vector reconstruction of the user-selected illustrated reference.

Original geometry and native text; no raster embedding or automatic tracing.
The source sketch is illustrative, and sorting assertions are a partial oracle.
"""
from math import hypot, cos, sin, pi
from reportlab.lib.colors import toColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from html import escape
from draw_figures import Figure

from font_config import font_path
pdfmetrics.registerFont(TTFont('CodeCustom',font_path('mono')))
N='#253E60'; T='#207E88'; V='#75619C'; R='#A45232'
B='#EDF4FB'; G='#EDF7F8'; L='#F3EFF9'; O='#FCF1EB'

def render():
    f=Figure('construction-overview-illustrated',1000,625)
    c=f.c
    def text(x,y,s,size=11,bold=False,col=N,anchor='start'):
        # Enlarge body labels without altering the 1000 x 625 canvas.
        size *= 1.22 if size < 10 else (1.12 if size < 17 else 1.04)
        f.text(x,y,s,size,bold,col,anchor)
    def code(x,y,rows,size=8.8,col=N,step=13):
        size *= 1.18
        for j,s in enumerate(rows):
            yy=y+j*step
            c.setFont('CodeCustom',size);c.setFillColor(toColor(col));c.drawString(x,625-yy,s)
            f.svg.append(f'<text x="{x}" y="{yy}" font-family="Consolas,monospace" font-size="{size}" fill="{col}">{escape(s)}</text>')
    def box(x,y,w,h,col=N,fill='white',r=3,dash=False):
        c.setStrokeColor(toColor(col));c.setFillColor(toColor(fill));c.setLineWidth(.85);c.setDash([4,3] if dash else [])
        c.roundRect(x,625-y-h,w,h,r,fill=1,stroke=1);c.setDash([])
        f.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{col}" stroke-width=".85"'+(' stroke-dasharray="4 3"' if dash else '')+'/>')
    def line(pts,col=N,arrow=False,dash=False): f.path(pts,col,dash,arrow)
    def circle(x,y,r,col=N,fill='white',dash=False):
        c.setStrokeColor(toColor(col));c.setFillColor(toColor(fill));c.setLineWidth(.9);c.setDash([3,2] if dash else [])
        c.circle(x,625-y,r,fill=1,stroke=1);c.setDash([])
        f.svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{col}" stroke-width=".9"'+(' stroke-dasharray="3 2"' if dash else '')+'/>')
    def edge(a,b,ra=6,rb=6,col=N,dash=False):
        dx,dy=b[0]-a[0],b[1]-a[1];d=hypot(dx,dy)
        line([(a[0]+dx*ra/d,a[1]+dy*ra/d),(b[0]-dx*(rb+1)/d,b[1]-dy*(rb+1)/d)],col,True,dash)
    def curve(points,col=N,dash=False,arrow=True):
        x,y,a,b,d,e,u,v=points
        c.setStrokeColor(toColor(col));c.setLineWidth(.95);c.setDash([4,3] if dash else [])
        p=c.beginPath();p.moveTo(x,625-y);p.curveTo(a,625-b,d,625-e,u,625-v);c.drawPath(p);c.setDash([])
        f.svg.append(f'<path d="M{x},{y} C{a},{b} {d},{e} {u},{v}" fill="none" stroke="{col}" stroke-width=".95"'+(' stroke-dasharray="4 3"' if dash else '')+'/>')
        if arrow: line([(u+(d-u)*.08,v+(e-v)*.08),(u,v)],col,True)
    def document(x,y,w,h,col=N,fill=B):
        # One folded sheet, never duplicated backing borders.
        pts=[(x,y),(x+w-9,y),(x+w,y+9),(x+w,y+h),(x,y+h),(x,y)]
        c.setFillColor(toColor(fill));c.setStrokeColor(toColor(col));c.setLineWidth(.85)
        p=c.beginPath();p.moveTo(x,625-y)
        for xx,yy in pts[1:]:p.lineTo(xx,625-yy)
        c.drawPath(p,fill=1,stroke=1)
        f.svg.append(f'<polygon points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="{fill}" stroke="{col}" stroke-width=".85"/>')
        line([(x+w-9,y),(x+w-9,y+9),(x+w,y+9)],col)
    def model_icon(x,y):
        # Paired model chips replace the abstract letter-only continuation ports.
        box(x-6,y-6,12,12,V,L,2)
        for d in [-3,3]:
            line([(x+d,y-9),(x+d,y-6)],V)
            line([(x+d,y+6),(x+d,y+9)],V)
            line([(x-9,y+d),(x-6,y+d)],V)
            line([(x+6,y+d),(x+9,y+d)],V)
        # A small neural graph makes the glyph a learned model rather than a CPU.
        for a,b in [((-3,-3),(2,0)),((-3,3),(2,0)),((2,0),(3,3))]:
            line([(x+a[0],y+a[1]),(x+b[0],y+b[1])],V)
        for dx,dy in [(-3,-3),(-3,3),(2,0),(3,3)]:
            circle(x+dx,y+dy,1,V,V)

    # Stable reference layout, solid fills, and a pure white outer background.
    box(8,12,224,487,N,'white',5)
    box(242,12,477,487,T,'white',5)
    box(736,12,256,487,R,'white',5)
    text(18,35,'Information sources',21,True)
    text(252,35,'Test construction',21,True,T)
    text(746,35,'Quality evidence',21,True,R)

    # Exactly three independent sources; no decorative stacked sheets.
    for y,label,fill in [(49,'Requirements',B),(84,'Contracts',O),(119,'Human judgments',O)]:
        box(46,y,149,27,N,fill,2);text(120.5,y+18,label,12,False,N,'middle')
    nodes=[(80,174),(34,201),(78,210),(123,202),(39,244),(121,245)]
    for i,j in [(0,1),(0,2),(0,3),(1,2),(3,2),(2,4),(2,5)]:
        edge(nodes[i],nodes[j],8 if i!=2 else 10,10 if j==2 else 8)
    for j,(x,y) in enumerate(nodes):circle(x,y,10 if j==2 else 8,N,'#74BDC5' if j==2 else '#D9E6F2')
    for x,y,s in [(80,162,'utils.py'),(35,222,'core.py'),(79,232,'model.py'),(124,222,'data.py'),(38,262,'render.py'),(124,264,'test_utils.py')]:text(x,y,s,9,False,N,'middle')
    document(147,157,72,92,N,B)
    code(154,179,['def','process(x):','  ...','','  ...'],8.5)
    text(120,278,'Code / dependencies',12,False,N,'middle')
    document(22,292,102,74,N,B)
    code(29,310,['def test_sort():','  ...','def test_edge():','  ...'],8.1)
    box(137,293,84,70,N,'white',0,True)
    code(144,308,['> test_sort','> ...','> x = [3,1,2]','> y = [1,2,3]','> assert ...'],7.8,step=11)
    text(22,383,'Existing tests / traces',11.5)
    text(156,383,'trace.log',10.5)
    box(17,395,206,89,N,'white',3,True)
    for x,label,col,fill in [(22,'Reference',T,B),(131,'Candidate',R,O)]:
        box(x,401,86,60,col,'white',0)
        box(x,401,86,20,col,fill,0)
        text(x+43,415,label,11,False,col,'middle')
        rows=['def sort(x):','  return (','    sorted(x))'] if label=='Reference' else ['def sort(x):','  ...']
        code(x+6,433,rows,7.3,step=11)
    text(120,477,'Reference agreement is conditional',9.8,False,N,'middle')

    # Alternative mechanisms and a shared operation graph.
    text(480,54,'Method families (alternative or combinable)',12,False,N,'middle')
    line([(256,70),(256,61),(705,61),(705,70)],T)
    for x,w,label,col,fill in [(264,133,'Prompting + retrieval',N,B),(413,147,'Program analysis + search',T,G),(575,123,'Agent orchestration',V,L)]:
        box(x,73,w,28,col,fill,4);text(x+w/2,92,label,11.4,False,N,'middle')
    curve((319,101,319,120,339,126,350,142),N)
    curve((486,101,486,120,467,126,465,142),T)
    curve((641,101,641,124,614,132,595,149),V)
    # Connector endpoints terminate outside nodes.
    for x,label,col,fill in [(366,'Plan',N,B),(469,'Generate',T,G),(572,'Check',V,L)]:
        circle(x,176,32,col,fill);text(x,194,label,12,True,col,'middle')
    # Native plan sheet, cog, and magnifier icons.
    document(358,158,16,20,N,B)
    for y in [164,168,172]:line([(361,y),(371,y)],N)
    gear=[]
    for j in range(32):
        a=2*pi*j/32;r=10 if j%4 in [0,3] else 12
        gear.append((469+r*cos(a),168+r*sin(a)))
    line(gear+[gear[0]],T);circle(469,168,5,T,'white')
    circle(569,166,8,V,L);line([(575,172),(582,179)],V)
    line([(398,176),(436,176)],N,True)
    line([(501,176),(539,176)],N,True)
    curve((554,147,532,122,491,125,481,143),V,True)
    text(528,122,'Execution feedback',10,False,V,'middle')
    line([(604,176),(664,176),(664,222)],N,True)
    text(618,169,'Retain',11)

    # Constructed test and exact live code text.
    box(257,225,447,94,N,'white',3)
    text(270,241,'Constructed test',12,True)
    text(390,241,'(illustrative)',10)
    for x,w,label,col,fill in [(265,144,'Setup',N,B),(409,139,'Inputs / actions',T,G),(548,148,'Oracle',R,O)]:
        box(x,247,w,21,col,fill,0);text(x+w/2,262,label,11.5,True,col,'middle')
        box(x,268,w,43,col,'white',0)
    code(279,285,['before = copy(x)'],10)
    code(447,285,['y = sort(x)'],10)
    code(561,285,['assert ordered(y)','assert x == before'],9.3)
    line([(468,319),(468,349)],N,True)
    curve((468,319,425,330,355,325,333,351),N)
    curve((468,319,515,329,589,327,604,351),N)
    # One clean outer boundary per artifact; code strips are intentional modules.
    document(249,360,122,122,T,G)
    text(258,382,'Scenarios',13,True)
    code(258,409,['# reverse order','x = [3, 2, 1]','...'],8.2)
    box(387,360,138,122,V,L,3)
    text(456,380,'Executable tests',12.4,True,V,'middle')
    for y,h,rows in [(391,22,['setup: before = copy(x)']),(424,22,['run: y = sort(x)']),(457,24,['assert: ordered(y)','assert: x == before'])]:
        box(392,y,128,h,V,'white',1);code(397,y+12,rows,7.7,step=10)
    line([(456,414),(456,423)],V,True);line([(456,447),(456,456)],V,True)
    document(538,360,166,122,R,O)
    text(621,381,'Generators / mutators',12,True,R,'middle')
    box(603,389,43,17,R,'white',3);text(624,401,'<list>',9,False,R,'middle')
    for x,label in [(565,'<size>'),(616,'<elements>'),(674,'<pattern>')]:
        edge((624,407),(x,423),0,0,R)
        w=48 if label=='<elements>' else 42
        box(x-w/2,423,w,16,R,'white',2);text(x,434,label,8.2,False,R,'middle')
    for x,labels in [(565,['0','1','...']),(616,['int','str','...']),(674,['sorted','random'])]:
        for j,label in enumerate(labels):
            xx=x+(j-1)*15 if x!=674 else [659,690][j]
            edge((x,440),(xx,455),0,0,R)
            text(xx,468,label,7,False,N,'middle')
    text(674,478,'...',7,False,N,'middle')

    # Quality evidence: path illustration and independent behavioral checks.
    box(742,50,244,190,T,'white',4)
    text(751,72,'Operational evidence',17,True,T)
    box(750,88,128,145,N,B,0)
    code(758,104,['def sort(x):','  ...'],8.5)
    pts=[(801,119),(800,142),(781,168),(826,168),(770,197),(795,196),(840,196),(796,224),(827,223),(827,142)]
    for i,j in [(0,1),(1,2),(1,3),(2,4),(2,5),(3,6),(3,8),(5,7),(5,8),(6,8),(1,9),(9,3)]:
        edge(pts[i],pts[j],6,6,N,j in [4,7,9])
    for j,(x,y) in enumerate(pts):circle(x,y,6,N,'#74BDC5' if j in [0,1,3,5,8] else 'white',j in [4,7,9])
    line([(896,90),(896,169)],T)
    for y,s in [(107,'Execution'),(135,'Coverage'),(161,'Stability / cost')]:text(909,y,s,11)
    for y,fill,label in [(197,'#74BDC5','Executed path'),(219,'white','Uncovered path')]:
        circle(896,y,6,T,fill);text(906,y+4,label,10.5)
    box(742,247,244,247,R,'white',4)
    text(751,268,'Behavioral evidence',17,True,R)
    document(755,296,81,101,N,B)
    text(763,314,'Specification',11,True)
    line([(762,321),(828,321)],N)
    code(760,337,['Preconditions:','  ...','Postconditions:','  ...','Invariants:','  ...'],7.6,step=10)
    for y,labels,col,fill in [(287,['Valid programs','(legal behavior)'],T,G),(368,['Faulty programs','(incorrect behavior)'],R,O)]:
        text(925,y,labels[0],10,False,N,'middle');text(925,y+12,labels[1],9.5,False,N,'middle')
        document(892,y+22,77,43,col,fill)
        code(899,y+39,['def sort(x):','  ...'],8)
    curve((836,346,860,341,858,319,888,319),N)
    curve((836,356,860,363,856,398,888,398),N)
    line([(711,455),(830,455)],T,True)
    text(753,449,'Independent',10,True)
    text(753,466,'evaluation',10,True)
    line([(860,442),(860,484)],R)
    for y,s in [(450,'Oracle validity'),(465,'Accept legal behavior'),(480,'Detect faulty behavior')]:text(866,y,s,9.4)

    # Paired model icons continue the update without crossing evaluation.
    box(9,512,982,66,V,L,4,True)
    text(19,542,'Learning across tasks',19,True,V)
    text(19,560,'Training-time information',11)
    for x,w,title,rows in [(248,177,'Training data',['Code, tests, specifications,','human feedback, ...']),(468,200,'SFT / RL / self-play',['Learn generation policy','across tasks']),(713,178,'Updated generator',['Better priors for','test generation'])]:
        box(x,523,w,48,V,'white',4);text(x+w/2,538,title,11.5,True,N,'middle')
        for j,s in enumerate(rows):text(x+w/2,552+j*12,s,10,False,N,'middle')
    line([(425,547),(467,547)],V,True);line([(668,547),(712,547)],V,True)
    model_icon(912,546);line([(891,546),(902,546)],V,True)
    model_icon(512,213)
    line([(502,213),(494,213),(483,205)],V,True)
    text(527,217,'model update',8.5,False,V)
    line([(10,592),(990,592)],N)
    text(500,612,'Unit / regression   ·   Requirements / acceptance   ·   API / GUI   ·   Fuzzing   ·   Bug reproduction',12,True,N,'middle')
    f.save()

if __name__=='__main__':render()
