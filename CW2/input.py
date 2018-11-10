import json
import pandas as pd
import matplotlib.pyplot as plt


cntry_to_cont = {
  'AF': 'AS',
  'AX': 'EU',
  'AL': 'EU',
  'DZ': 'AF',
  'AS': 'OC',
  'AD': 'EU',
  'AO': 'AF',
  'AI': 'NA',
  'AQ': 'AN',
  'AG': 'NA',
  'AR': 'SA',
  'AM': 'AS',
  'AW': 'NA',
  'AU': 'OC',
  'AT': 'EU',
  'AZ': 'AS',
  'BS': 'NA',
  'BH': 'AS',
  'BD': 'AS',
  'BB': 'NA',
  'BY': 'EU',
  'BE': 'EU',
  'BZ': 'NA',
  'BJ': 'AF',
  'BM': 'NA',
  'BT': 'AS',
  'BO': 'SA',
  'BQ': 'NA',
  'BA': 'EU',
  'BW': 'AF',
  'BV': 'AN',
  'BR': 'SA',
  'IO': 'AS',
  'VG': 'NA',
  'BN': 'AS',
  'BG': 'EU',
  'BF': 'AF',
  'BI': 'AF',
  'KH': 'AS',
  'CM': 'AF',
  'CA': 'NA',
  'CV': 'AF',
  'KY': 'NA',
  'CF': 'AF',
  'TD': 'AF',
  'CL': 'SA',
  'CN': 'AS',
  'CX': 'AS',
  'CC': 'AS',
  'CO': 'SA',
  'KM': 'AF',
  'CD': 'AF',
  'CG': 'AF',
  'CK': 'OC',
  'CR': 'NA',
  'CI': 'AF',
  'HR': 'EU',
  'CU': 'NA',
  'CW': 'NA',
  'CY': 'AS',
  'CZ': 'EU',
  'DK': 'EU',
  'DJ': 'AF',
  'DM': 'NA',
  'DO': 'NA',
  'EC': 'SA',
  'EG': 'AF',
  'SV': 'NA',
  'GQ': 'AF',
  'ER': 'AF',
  'EE': 'EU',
  'ET': 'AF',
  'FO': 'EU',
  'FK': 'SA',
  'FJ': 'OC',
  'FI': 'EU',
  'FR': 'EU',
  'GF': 'SA',
  'PF': 'OC',
  'TF': 'AN',
  'GA': 'AF',
  'GM': 'AF',
  'GE': 'AS',
  'DE': 'EU',
  'GH': 'AF',
  'GI': 'EU',
  'GR': 'EU',
  'GL': 'NA',
  'GD': 'NA',
  'GP': 'NA',
  'GU': 'OC',
  'GT': 'NA',
  'GG': 'EU',
  'GN': 'AF',
  'GW': 'AF',
  'GY': 'SA',
  'HT': 'NA',
  'HM': 'AN',
  'VA': 'EU',
  'HN': 'NA',
  'HK': 'AS',
  'HU': 'EU',
  'IS': 'EU',
  'IN': 'AS',
  'ID': 'AS',
  'IR': 'AS',
  'IQ': 'AS',
  'IE': 'EU',
  'IM': 'EU',
  'IL': 'AS',
  'IT': 'EU',
  'JM': 'NA',
  'JP': 'AS',
  'JE': 'EU',
  'JO': 'AS',
  'KZ': 'AS',
  'KE': 'AF',
  'KI': 'OC',
  'KP': 'AS',
  'KR': 'AS',
  'KW': 'AS',
  'KG': 'AS',
  'LA': 'AS',
  'LV': 'EU',
  'LB': 'AS',
  'LS': 'AF',
  'LR': 'AF',
  'LY': 'AF',
  'LI': 'EU',
  'LT': 'EU',
  'LU': 'EU',
  'MO': 'AS',
  'MK': 'EU',
  'MG': 'AF',
  'MW': 'AF',
  'MY': 'AS',
  'MV': 'AS',
  'ML': 'AF',
  'MT': 'EU',
  'MH': 'OC',
  'MQ': 'NA',
  'MR': 'AF',
  'MU': 'AF',
  'YT': 'AF',
  'MX': 'NA',
  'FM': 'OC',
  'MD': 'EU',
  'MC': 'EU',
  'MN': 'AS',
  'ME': 'EU',
  'MS': 'NA',
  'MA': 'AF',
  'MZ': 'AF',
  'MM': 'AS',
  'NA': 'AF',
  'NR': 'OC',
  'NP': 'AS',
  'NL': 'EU',
  'NC': 'OC',
  'NZ': 'OC',
  'NI': 'NA',
  'NE': 'AF',
  'NG': 'AF',
  'NU': 'OC',
  'NF': 'OC',
  'MP': 'OC',
  'NO': 'EU',
  'OM': 'AS',
  'PK': 'AS',
  'PW': 'OC',
  'PS': 'AS',
  'PA': 'NA',
  'PG': 'OC',
  'PY': 'SA',
  'PE': 'SA',
  'PH': 'AS',
  'PN': 'OC',
  'PL': 'EU',
  'PT': 'EU',
  'PR': 'NA',
  'QA': 'AS',
  'RE': 'AF',
  'RO': 'EU',
  'RU': 'EU',
  'RW': 'AF',
  'BL': 'NA',
  'SH': 'AF',
  'KN': 'NA',
  'LC': 'NA',
  'MF': 'NA',
  'PM': 'NA',
  'VC': 'NA',
  'WS': 'OC',
  'SM': 'EU',
  'ST': 'AF',
  'SA': 'AS',
  'SN': 'AF',
  'RS': 'EU',
  'SC': 'AF',
  'SL': 'AF',
  'SG': 'AS',
  'SX': 'NA',
  'SK': 'EU',
  'SI': 'EU',
  'SB': 'OC',
  'SO': 'AF',
  'ZA': 'AF',
  'GS': 'AN',
  'SS': 'AF',
  'ES': 'EU',
  'LK': 'AS',
  'SD': 'AF',
  'SR': 'SA',
  'SJ': 'EU',
  'SZ': 'AF',
  'SE': 'EU',
  'CH': 'EU',
  'SY': 'AS',
  'TW': 'AS',
  'TJ': 'AS',
  'TZ': 'AF',
  'TH': 'AS',
  'TL': 'AS',
  'TG': 'AF',
  'TK': 'OC',
  'TO': 'OC',
  'TT': 'NA',
  'TN': 'AF',
  'TR': 'AS',
  'TM': 'AS',
  'TC': 'NA',
  'TV': 'OC',
  'UG': 'AF',
  'UA': 'EU',
  'AE': 'AS',
  'GB': 'EU',
  'US': 'NA',
  'UM': 'OC',
  'VI': 'NA',
  'UY': 'SA',
  'UZ': 'AS',
  'VU': 'OC',
  'VE': 'SA',
  'VN': 'AS',
  'WF': 'OC',
  'EH': 'AF',
  'YE': 'AS',
  'ZM': 'AF',
  'ZW': 'AF'
}



continents = {
  'AF': 0,
  'AS': 0,
  'EU': 0,
  'NA': 0,
  'SA': 0,
  'OC': 0,
  'AN': 0
}

def input_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            current_line = process_line(json.loads(line))
            data.append(current_line)
    return data


def process_line(line):
    desired_fields = ["visitor_uuid", "visitor_country", "visitor_useragent", "env_doc_id"]
    d = {}
    for field in desired_fields:
        if field in line:
            d[field] = line[field]
    return d


print("\nExtracted relevant info")
data = input_file("issuu_cw2.json")


table = pd.DataFrame.from_dict(data)
table.rename(columns={'env_doc_id': 'doc_id', 'visitor_uuid': 'user_id', 'visitor_country': 'country', 'visitor_useragent': 'browser' }, inplace=True)

print(table[:10])


x = table['country'].value_counts()
print(x)

# change to get frequency count of countries, then iterate over frequency counts adding those to continent

country_iterator = table['country'].__iter__()

for country in country_iterator:
    if country in cntry_to_cont:
        continents[cntry_to_cont[country]] += 1

print(continents)



def show_histo(dict, orient="horiz", label="counts", title="title"):
    """Take a dictionary of counts and show it as a histogram."""
    if orient == "horiz":
        bar_fun = plt.barh  # NB: this assigns a function to bar_fun!
        bar_ticks = plt.yticks
        bar_label = plt.xlabel
    elif orient == "vert":
        bar_fun = plt.bar
        bar_ticks = plt.xticks
        bar_label = plt.ylabel
    else:
        raise Exception("show_histo: Unknown orientation: %s ".format % orient)

    n = len(dict)
    bar_fun(range(n), list(dict.values()), align='center', alpha=0.4)
    bar_ticks(range(n), list(dict.keys()))  # NB: uses a higher-order function
    bar_label(label)
    plt.title(title)
    plt.show()

show_histo(continents, 'vert', 'Continents', 'Views by continent')

print('test')