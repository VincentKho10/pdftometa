import pymupdf
import re

def main():
    doc = pymupdf.open("build/input/test.pdf")
    out = open("input/25500252-OF_1_5_2025.pdf", "wb")
    pattern = r"ORDER NO\n:\n(.*)|GRAND TOTAL\n:\nIDR\n(.*)\n|^[0-9]$\n(.*\n.*\n.*\n.*\n.*)"
    dict = {}
    for page in doc:
        text = page.get_text()
        matches = re.finditer(pattern, text, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
        # ponum = [v for v in matched[0] if v!=""][0]
        # grand_total = [v for v in matched[1] if v!=""][0]
        # items = [v for v in matched[2] if v!=""][0]
        # dict["ponum"] = ponum
        # dict["grand_total"] = grand_total
        # dict["items"] = items
            #  print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            print(type(match.group()))
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                # print(match.group(groupNum))
                # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    out.close()
    return

if __name__ == "__main__":
    main()