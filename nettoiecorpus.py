#!/usr/bin/python3
#programme de nettoyage des balises / scories dans le text
#modif 2 test
import re
    
def NettoieCorpus(corpus):
    corpus=open(corpus, "r")
    corpus=corpus.read()
    
    corpus=re.sub(r'</?(font|em|br|p|b|i|li|P|FONT|P|BR|EM|Br|strong|Strong|STRONG|STrong|I|LI|ul|sub|font\s{0,3}size=\s{0,2}"-?\d{1,2}"|sup|inf)/?>|&#8804|<br/?'," ",corpus)
    corpus=corpus.replace("<. ","<.")
    corpus=re.sub(r"(<)=?\s{0,2}\.?\d+","&lt;",corpus)
    corpus=re.sub(r"</=","&lt;=",corpus)
    corpus=re.sub(r"<\?","&lt;",corpus)
    corpus=re.sub(r"< or"," &lt;or",corpus)
    corpus=re.sub(r"(>)=?\s{0,2}\d+","&gt;",corpus)
    corpus=re.sub(r"<<|>>","'",corpus)
    

    corpus=corpus.replace("&plusmn;","+-")
    corpus=corpus.replace(" & "," and ")
    corpus=corpus.replace("&"," and ")
    corpus=corpus.replace("e-&"," e-and ")
    corpus=corpus.replace("&sup","&gt;")
    corpus=corpus.replace("< >"," ")
    corpus=corpus.replace("< (","&lt;")
    corpus=corpus.replace("< )","&lt;")
    corpus=corpus.replace("< A","&lt; A")
    corpus=corpus.replace("F&V","FandV")
    
   
    return corpus
    


corpusnett=NettoieCorpus("/home/laetitia/Documents/these/sibil/corpus/corp.txt")
print(corpusnett)
#corpusnett=corpusnett.split("</abstract>")
#print(len(corpusnett))

