from mftool import Mftool



code_list = [122639, 129220, 119807, 120505, 125354, 120594, 135800, 120465, 120152, 118778, 130503, 118803, 112323, 118955, 119528, 125497, 119556, 120348, 118834, 120468, 119775, 147778]
print(code_list)


#Code to convert each element of list into list
def extractDigits(lst):
    res = []
    for el in lst:
        sub = str(el).split(', ')
        res.append(sub)

    return (res)

code_list_e= extractDigits(code_list)
print(code_list_e)
mf = Mftool()

for index, code in enumerate(code_list):
    scheme_quotes=mf.get_scheme_quote(code)
    print(scheme_quotes['scheme_name']+" "+scheme_quotes['last_updated']+" "+scheme_quotes['nav'])


