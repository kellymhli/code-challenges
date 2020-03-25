def subdomainVisits(cpdomains):
    d = {}
    for i in cpdomains:
        visits, domain = i.split()
        subdomains_lst = domain.split(".")
        subdom = ""
        for dom in subdomains_lst[::-1]:
            if subdom == "":
                subdom = dom
            else:
                subdom = dom + "." + subdom
            d[subdom] = d.get(subdom, 0) + int(visits)

    res = [str(v) + " " + k for k, v in d.items()]

    return res

print(subdomainVisits(["9001 discuss.leetcode.com"]))
print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))