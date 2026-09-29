"""Build bibliography from the verified literature register and author metadata."""
from pathlib import Path
import re, json

ROOT = Path(__file__).resolve().parent
# Complete author lists from primary-source metadata; source IDs match papers.md.
AUTHORS = {
'S01':'Junjie Wang;Yuchao Huang;Chunyang Chen;Zhe Liu;Song Wang;Qing Wang',
'S02':'Quanjun Zhang;Chunrong Fang;Siqi Gu;Ye Shang;Zhenyu Chen;Liang Xiao',
'S03':'Bei Chu;Yang Feng;Kui Liu;Zhaoqiang Guo;Yichi Zhang;Hange Shi;Zifan Nan;Baowen Xu',
'S04':'Cristian Augusto;Antonia Bertolino;Guglielmo De Angelis;Francesca Lonetti;Jesús Morán',
'S05':'Zhenzhen Yang;Rubing Huang;Chenhui Cui;Nan Niu;Dave Towey',
'S06':'Orimoloye Folorunsho;Hassan Reza',
'S07':'Murat Tasarsu;Ahmet Vedat Tokmak;Cagatay Catal',
'U01':'Max Schäfer;Sarah Nadi;Aryaz Eghbali;Frank Tip',
'U02':'Yinghao Chen;Zehao Hu;Chen Zhi;Junxiao Han;Shuiguang Deng;Jianwei Yin',
'U03':'Gabriel Ryan;Siddhartha Jain;Mingyue Shang;Shiqi Wang;Xiaofei Ma;Murali Krishna Ramanathan;Baishakhi Ray',
'U04':'Caroline Lemieux;Jeevana Priya Inala;Shuvendu K. Lahiri;Siddhartha Sen',
'U05':'Juan Altmayer Pizzorno;Emery D. Berger',
'U06':'Arghavan Moradi Dakhel;Amin Nikanjam;Vahid Majdinasab;Foutse Khomh;Michel C. Desmarais',
'U07':'Nadia Alshahwan;Jubin Chheda;Anastasia Finegenova;Beliz Gokkaya;Mark Harman;Inna Harper;Alexandru Marginean;Shubho Sengupta;Eddy Wang',
'U08':'Yuwei Zhang;Qingyuan Lu;Kai Liu;Wensheng Dou;Jiaxin Zhu;Li Qian;Chunxi Zhang;Zheng Lin;Jun Wei',
'U09':'Quanjun Zhang;Ye Shang;Siqi Gu;Jianyi Zhou;Chunrong Fang;Zhenyu Chen;Liang Xiao',
'U10':'Pengyu Chang;Yixiong Fang;Silin Chen;Yuling Shi;Beijun Shen;Xiaodong Gu',
'U11':'Michele Tufano;Dawn Drain;Alexey Svyatkovskiy;Shao Kun Deng;Neel Sundaresan',
'R01':'Chetan Arora;Tomas Herda;Verena Homm',
'R02':'Dragan Milchevski;Gordon Frank;Anna Hätty;Bingqing Wang;Xiaowei Zhou;Zhe Feng',
'R03':'Margarida Ferreira;Luis Viegas;Joao Pascoal Faria;Bruno Lima',
'R04':'André Pereira;Bruno Lima;João Pascoal Faria',
'O01':'Madeline Endres;Sarah Fakhoury;Saikat Chakraborty;Shuvendu K. Lahiri',
'O02':'Seung Yeob Shin;Fabrizio Pastore;Domenico Bianculli;Alexandra Baicoianu',
'O03':'Dong Huang;Mingzhe Du;Jie M. Zhang;Zheng Lin;Meng Luo;Qianru Zhang;See-Kiong Ng',
'O04':'Elizabeth Dinella;Gabriel Ryan;Todd Mytkowicz;Shuvendu K. Lahiri',
'O05':'Soneya Binta Hossain;Antonio Filieri;Matthew B. Dwyer;Sebastian Elbaum;Willem Visser',
'O06':'Qinghua Xu;Guancheng Wang;Lionel Briand;Kui Liu',
'A01':'Tyler Stennett;Myeongsoo Kim;Saurabh Sinha;Alessandro Orso',
'A02':'Rangeet Pan;Raju Pavuluri;Ruikai Huang;Rahul Krishna;Tyler Stennett;Alessandro Orso;Saurabh Sinha',
'A03':'Juyeon Yoon;Robert Feldt;Shin Yoo',
'A04':'Zhe Liu;Chunyang Chen;Junjie Wang;Mengzhuo Chen;Boyu Wu;Xing Che;Dandan Wang;Qing Wang',
'F01':'Yinlin Deng;Chunqiu Steven Xia;Haoran Peng;Chenyuan Yang;Lingming Zhang',
'F02':'Yinlin Deng;Chunqiu Steven Xia;Chenyuan Yang;Shizhuo Dylan Zhang;Shujing Yang;Lingming Zhang',
'F03':'Chunqiu Steven Xia;Matteo Paltenghi;Jia Le Tian;Michael Pradel;Lingming Zhang',
'F04':'Ruijie Meng;Martin Mirchev;Marcel Böhme;Abhik Roychoudhury',
'F05':'Yunlong Lyu;Yuxuan Xie;Peng Chen;Hao Chen',
'F06':'Chuyang Chen;Brendan Dolan-Gavitt;Zhiqiang Lin',
'F07':'Yiyi Wang;Dongsong Yu;Ruiqi Dong;Yiyang Chen;Xiaogang Zhu;Chao Zhang',
'T01':'Wannita Takerngsaksiri;Rujikorn Charakorn;Chakkrit Tantithamthavorn;Yuan-Fang Li',
'T02':'Dongjun Lee;Changho Hwang;Kimin Lee',
'T03':'Qingyao Li;Xinyi Dai;Weiwen Liu;Xiangyang Li;Yasheng Wang;Ruiming Tang;Yong Yu;Weinan Zhang',
'T04':'Zi Lin;Sheng Shen;Ilia Kulikov;Jingbo Shang;Jason Weston;Yixin Nie',
'T05':'Archiki Prasad;Elias Stengel-Eskin;Justin Chih-Yao Chen;Zaid Khan;Mohit Bansal',
'T06':'Zeyao Ma;Xiaokang Zhang;Jing Zhang;Jifan Yu;Sijia Luo;Jie Tang',
'T07':'Jiacheng Xu;Wentao Zhang;Zhiyi Lyu;Fuxiang Zhang;Chaojie Wang;Yang Liu;Bo An',
'T08':'{Aditi};Hyunwoo Park;Sicheol Sung;Yo-Sub Han;Sang-Ki Ko',
'T09':'Sicheol Sung;{Aditi};Dogyu Kim;Yo-Sub Han;Sang-Ki Ko',
'T10':'Bei Chen;Fengji Zhang;Anh Nguyen;Daoguang Zan;Zeqi Lin;Jian-Guang Lou;Weizhu Chen',
'T11':'Sarah Fakhoury;Aaditya Naik;Georgios Sakkas;Saikat Chakraborty;Shuvendu K. Lahiri',
'T12':'Benjamin Steenhoek;Michele Tufano;Neel Sundaresan;Alexey Svyatkovskiy',
'B01':'Kush Jain;Gabriel Synnaeve;Baptiste Rozière',
'B02':'Wenhan Wang;Chenyuan Yang;Zhijie Wang;Yuheng Huang;Zhaoyang Chu;Da Song;Lingming Zhang;An Ran Chen;Lei Ma',
'B03':'Niels Mündler;Mark Niklas Müller;Jingxuan He;Martin Vechev',
'B04':'Dong Huang;Jie M. Zhang;Mark Harman;Qianru Zhang;Mingzhe Du;See-Kiong Ng',
'B05':'Leon Kogler;Stefan Hangler;Maximilian Ehrhart;Benedikt Dornauer;Roland Wuersching;Peter Schrammel',
'E01':'Phouvadeth Vathana;Prapti Bhatt;Rishi Patel;Nasir U. Eisty',
'E02':'Sabaat Haroon;Mohammad Taha Khan;Muhammad Ali Gulzar',
'E03':'Alexander Berndt;Thomas Bach;Rainer Gemulla;Marcus Kessel;Sebastian Baltes',
'G01':'Sungmin Kang;Juyeon Yoon;Shin Yoo',
}
# Explicitly verified proceedings / journal metadata. Other entries cite the
# accessible arXiv version without claiming an unverified publication venue.
FORMAL = {
'S07':('article',2026,'Cluster Computing','10.1007/s10586-026-06021-z'),
'U04':('inproceedings',2023,'Proceedings of the International Conference on Software Engineering (ICSE)',''),
'U05':('article',2025,'Proceedings of the ACM on Software Engineering','10.1145/3729398'),
'R01':('inproceedings',2024,'IEEE International Requirements Engineering Conference (RE)','10.1109/RE59067.2024.00031'),
'R02':('inproceedings',2025,'Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Industry Track)','10.18653/v1/2025.acl-industry.11'),
'R03':('inproceedings',2025,'IEEE/ACM International Conference on Automation of Software Test (AST)','10.1109/AST66626.2025.00007'),
'O04':('inproceedings',2022,'Proceedings of the International Conference on Software Engineering (ICSE)','10.1145/3510003.3510141'),
'F04':('inproceedings',2024,'Network and Distributed System Security Symposium (NDSS)','10.14722/ndss.2024.24556'),
'F05':('inproceedings',2024,'ACM SIGSAC Conference on Computer and Communications Security (CCS)','10.1145/3658644.3670396'),
'F06':('inproceedings',2025,'34th USENIX Security Symposium',''),
'F07':('inproceedings',2026,'35th USENIX Security Symposium',''),
'T01':('article',2025,'Journal of Systems and Software','10.1016/j.jss.2025.112381'),
'T02':('inproceedings',2026,'International Conference on Learning Representations (ICLR)',''),
'T03':('inproceedings',2026,'International Conference on Learning Representations (ICLR)',''),
'T06':('inproceedings',2025,'Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)','10.18653/v1/2025.acl-long.343'),
'T09':('inproceedings',2025,'Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI)','10.24963/ijcai.2025/861'),
'B02':('inproceedings',2025,'Findings of the Association for Computational Linguistics: NAACL 2025','10.18653/v1/2025.findings-naacl.197'),
}
def escape(s):
    s=s.replace('&',r'\&').replace('_',r'\_')
    for a,b in {'ä':r'{\"a}','ö':r'{\"o}','ü':r'{\"u}','é':r"{\'e}",'è':r"{\`e}",'í':r"{\'i}",'ú':r"{\'u}",'á':r"{\'a}",'ã':r'{\~a}'}.items(): s=s.replace(a,b)
    return s
metadata_path=ROOT/'source-metadata.json'
metadata=json.loads(metadata_path.read_text(encoding='utf-8')) if metadata_path.exists() else {}
entries=[]
for line in (ROOT.parent/'papers.md').read_text(encoding='utf-8').splitlines():
    m=re.match(r'\| ([A-Z]\d\d) \| \[(.*?)\]\((.*?)\) \| ([^|]+)',line)
    if not m: continue
    key,title,url,state=m.groups()
    title=title.split(' — ')[0]
    year=int(re.search(r'20\d\d',state).group())
    fields={'author':escape(' and '.join(AUTHORS[key].split(';'))),'title':'{'+escape(title)+'}','year':str(year)}
    typ='misc'
    if key in FORMAL:
        typ,year,venue,doi=FORMAL[key]
        fields['year']=str(year); fields['journal' if typ=='article' else 'booktitle']=venue
        if doi: fields['doi']=doi
        else: fields['url']=url
    else:
        arxiv=re.search(r'/abs/(\d+\.\d+)',url)
        if arxiv: fields['howpublished']='arXiv:'+arxiv.group(1)
        fields['url']=url
    md=metadata.get(key,{})
    if 'container' in md:
        for a,b in [('volume','volume'),('issue','number'),('pages','pages'),('article_number','articleno'),('publisher','publisher')]:
            if md.get(a): fields[b]=escape(md[a]).replace('-','--') if b=='pages' else escape(md[a])
        if md.get('container'): fields['journal' if typ=='article' else 'booktitle']=escape(md['container'][0])
    if key=='T01': fields.update(volume='224',pages='112381')
    if key=='F06': fields.update(pages='6279--6298',publisher='USENIX Association',address='Seattle, WA')
    if key=='F07': fields.update(pages='4089--4108',publisher='USENIX Association',address='Baltimore, MD')
    if key=='T09': fields.update(pages='7742--7750')
    if key=='T06': fields.update(address='Vienna, Austria')
    source_authors=md.get('metadata',{}).get('citation_author')
    if source_authors: fields['author']=escape(' and '.join(source_authors))
    entries.append('@'+typ+'{'+key+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}\n')
(ROOT/'references.bib').write_text('\n'.join(entries),encoding='utf-8')
if __name__=='__main__': print(f'Wrote {len(entries)} bibliography entries')
