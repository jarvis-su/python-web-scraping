

FILEDS = ('are',
          'population',
          'iso',
          'country',
          'capital',
          'continent','tld','currency_code','currency_name',
          'phone','postal_code_format','postal_code_regex','languages',
          'neighbours'
          )

import re
def re_scraper(html):
    results = {}
    for filed in FILEDS:
        results[filed] = re.search()