#!/usr/bin/env python3

import panflute as pf

import logging
logging.basicConfig(level=logging.DEBUG)

def to_latex(e,doc):
    if (doc.format == "latex"):
        if (isinstance(e,pf.BlockQuote)):
            l = e.content.list
            l.insert(0,pf.RawBlock("\\begin{quote}",format="latex"))
            l.append(pf.RawBlock("\\end{quote}",format="latex"))
            logging.debug("BlockQuote replaced by {0}".format(l))
            return(l)
        elif (e==pf.RawBlock("<footer>",format="html")):
            logging.debug("<footer>")
            return(pf.RawBlock("\\begin{blockquotefooter}",format="latex"))
        elif (e==pf.RawBlock("</footer>",format="html")):
            logging.debug("</footer>")
            return(pf.RawBlock("\\end{blockquotefooter}",format="latex"))

            

def main(doc=None):
    return pf.run_filter(to_latex,doc)

if __name__ == "__main__":
    main()

"""
BlockQuote -> quote environment
RawBlock "<footer>" -> latex \begin{blockquotefooter}
RawBlock "<\footer>" -> latex \end{blockquotefooter}
"""
