#!/usr/bin/env python3

import panflute as pf

import logging
#logging.basicConfig(level=logging.DEBUG)

def to_latex(e,doc):
    if (doc.format=="latex"):
        if (isinstance(e,pf.Code)):
            logging.debug("Code")
            logging.debug(e.classes)
            if (len(e.classes)==0):
                logging.debug("use backtick")
                logging.debug(e.text)
                return([pf.Str("`"),pf.Str(e.text),pf.Str("`")])
            else:
                logging.debug("use mintedinline")
                logging.debug(e.text)
                s = "\\mintedinline{"+e.classes[0]+"}{"+e.text+"}"
                logging.debug(s)
                return([pf.RawInline(s,format="latex")])
        elif (isinstance(e,pf.CodeBlock)):
            logging.debug("CodeBlock")
            logging.debug(e.classes)
            if (len(e.classes)==0):
                logging.debug("use verbatim")
                logging.debug(e.text)
                s = ("""\\begin{verbatim}\n""" +
                     e.text + """\n\\end{verbatim}""")
                return([pf.RawBlock(s,format="latex")])
            else:
                logging.debug("use minted")
                logging.debug(e.text)
                s = ("""\\begin{minted}{""" + 
                     e.classes[0]+"""}\n""" + 
                     e.text+"""\n\\end{minted}""")
                return([pf.RawBlock(s,format="latex")])
    pass

def main(doc=None):
    return pf.run_filter(to_latex,doc)

if __name__ == "__main__":
    main()

"""

when going to LaTeX:
Code -> \texttt{}
Code(type given) -> mintinline{}
CodeBlock --> verbatim environment
CodeBlock(type given) -> mint

Since we are trying to write stuff using plain markdown vice markup,
not going to do these till later... as convenience for if i write stuff
in latex when i shouldnt
when not going to latex: (LATER)
RawInline tex \texttt{} -> Code
RawInline tex mintinline{} -> Code
Inline verbatim environment -> CodeBlock
Inline minted environment -> CodeBlock
"""


