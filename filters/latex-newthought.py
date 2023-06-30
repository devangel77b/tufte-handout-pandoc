#!/usr/bin/env python3

import panflute as pf
import parse

import logging
logging.basicConfig(level=logging.DEBUG)

def latex_newthought(e, doc):
    if (isinstance(e,pf.Span)) and (doc.format == "latex"):
        if ('newthought' in e.classes):
            l = e.content # get content
            l.insert(0,pf.RawInline("\\newthought{",format="latex"))
            l.append(pf.RawInline("}",format="latex"))
            logging.debug(l)
            return(l.list)

def main(doc=None):
    return pf.run_filter(latex_newthought,doc=doc)
            
if __name__ == "__main__":
    main()
