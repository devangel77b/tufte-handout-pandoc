#!\usr\bin\env python

import panflute as pf
import parse

#import logging
#logging.basicConfig(level=logging.DEBUG)

def latex_sidenote(e, doc):
    if (type(e)==pf.Note) and (doc.format == "latex"):
        if (type(e0 := e.content[0])==pf.Para):
            l = e0.content
            if (l[0]==pf.Str("{-}")):
                l.pop
                l.insert(0,pf.RawInline("\marginnote{",format="latex"))
            elif (l[0]==pf.Str("{.}")):
                l.pop
                l.insert(0,pf.RawInline("\footnote{",format="latex"))
            else:
                l.insert(0,pf.RawInline("\sidenote{",format="latex"))
            l.append(pf.RawInline("}",format="latex"))
            #logging.debug("Returning {0}".format(l.list))
            return(l.list)
            
if __name__ == "__main__":
    pf.run_filter(latex_sidenote)
    
