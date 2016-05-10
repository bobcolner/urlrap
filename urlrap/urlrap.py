import urltools as _urltools
import datetime as _datetime
from dateutil.parser import parse as _dateparse

def normalize(url, strip=False):
    "RFC3986 normalize URL & Optionally removing url-query/fragment string"
    if strip:
        p = _urltools.parse(url)
        url = p.scheme + '://' + p.subdomain + p.domain + p.path
    return _urltools.normalize(url)

def find_date(url):
    "Extract date from URL page if exists."
    def _clean_split(div_str):
        sl = []
        for div in div_str.split('/'):
            div = div.strip().lower()
            if div != '':
                sl.append(div)
        return sl
        
    url_path = find_path(url)
    url_path_parts = _clean_split(url_path)
    date_parts = []
    for part in url_path_parts:
        try:
            _dateparse(part) # is part date-like?
            date_parts.append(part)
        except ValueError:
            continue
    if len(date_parts) == 0:
        return
    date_str = '/'.join(date_parts)
    return _dateparse(date_str)# .strftime('%Y-%m-%d')

def find_domain(url_str):
    "Extract domain from URL"
    return _urltools.parse(url_str).domain

def find_path(url_str):
    "Extract path component from URL"
    return _urltools.parse(url_str).path

def find_query(url_str):
    "Extract query component from URL"
    return _urltools.parse(url_str).query

def find_fragment(url_str):
    "Extract fragment component from URL"
    return _urltools.parse(url_str).fragment

def parse(url_str):
    "Parse URL into component parts"
    return _urltools.parse(url_str)
