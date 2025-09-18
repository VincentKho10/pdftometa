import os
import pymupdf
import re
import locale

locale.setlocale(locale.LC_ALL, 'en_ID.UTF-8')

res={}
def main():
    pattern = r"ORDER NO\n:\n(.*)|GRAND TOTAL\n:\nIDR\n(.*)\n"
    lsof = [ "input/{f}".format(f=v) for v in os.listdir("input")]
    for v in lsof:
        if (v.endswith('.pdf')):
            doc = pymupdf.open(v)
            convert(doc, pattern)
    total = 0
    for k in res:
        grandtot = res[k]
        ngt = grandtot[:-3]
        total += int(ngt.replace(",",""))
    total = locale.currency(total, grouping=True)
    # print("Grand Total: {total}".format(total=total))
    
    with open("output.txt", "w") as f:
        for v in res:
            print("{poval} = {gtval}".format(poval=v, gtval=res[v]),file=f)
        print("", file=f)
        print("Grand Total = {total}".format(total=total), file=f)
            # print(v,file=f)
    return

def convert(doc, pattern):
    text=""
    for page_number in range(doc.page_count):
        # Get the page object for the current page number.
        page = doc.load_page(page_number)
        
        # Extract the text from the page.
        temp = page.get_text()
        text+=temp
    matches = re.finditer(pattern, text, re.MULTILINE)
    dict={}
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            matchValue = match.group(groupNum)
            labels = ["poid", "gt"]
            if(matchValue!=None):
                dict[labels[groupNum-1]] = matchValue
    
    res[dict["poid"]] = dict["gt"]
    return

if __name__ == "__main__":
    main()