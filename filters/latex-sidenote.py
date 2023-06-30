#!/usr/bin/env python3

import panflute as pf
import parse

#import logging
#logging.basicConfig(level=logging.DEBUG)

def latex_sidenote(e, doc):
    if (type(e)==pf.Note) and (doc.format == "latex"):
        if (type(e0 := e.content[0])==pf.Para):
            l = e0.content
            #logging.debug(l)
            if (l[0]==pf.Str("{-}")):
                l.insert(0,pf.RawInline("\marginnote{",format="latex"))
                l.pop(1)
            elif (l[0]==pf.Str("{.}")):
                l.insert(0,pf.RawInline("\footnote{",format="latex"))
                l.pop(1)
            else:
                l.insert(0,pf.RawInline("\sidenote{",format="latex"))
            l.append(pf.RawInline("}",format="latex"))
            #logging.debug("Returning {0}".format(l.list))
            return(l.list)
            
if __name__ == "__main__":
    #logging.debug("here")
    pf.run_filter(latex_sidenote)
    
