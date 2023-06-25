#!/usr/bin/env python3
import panflute as pf
import re


def latex(s):
    return pf.RawInline(s, format="latex")

marginnote_pattern = re.compile("\s*{-}")
footnote_pattern = re.compile("\s*{.}")

# get string
# check if it fits patterns and handle appropriately
def latex_sidenote(e, doc):
    if type(e)==pf.Note and doc.format=="latex":
        s = pf.stringify(e)
        if (rv := marginnote_pattern.match(s)):
            return latex("\\marginnote{"+s[rv.end():]+"}")
        elif (rv := footnote_pattern.match(s)):
            return latex("\\footnote{"+s[rv.end():]+"}")
        else:
            return latex("\\sidenote{"+s+"}")

if __name__ == "__main__":
    pf.run_filter(latex_sidenote)

