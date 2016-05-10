import urltools
from hashlib import md5 as _md5
import dateutil as _dateutil
import datetime as _datetime

def find_domain(url_str):
    "Extract domain from URL"
    return urltools.parse(url_str).domain

def find_path(url_str):
    "Extract path component from URL"
    return urltools.parse(url_str).path

def find_query(url_str):
    "Extract query component from URL"
    return urltools.parse(url_str).query

def find_fragment(url_str):
    "Extract fragment component from URL"
    return urltools.parse(url_str).fragment

def md5_hash(input_str):
    "Compuate MD5 hash"
    return _md5(input_str.encode()).hexdigest()

def normalize(url, strip=True):
    "RFC3986 normalize URL & Optionally removing url-query/fragment string (default)"
    p = urltools.parse(url)
    if strip:
        url = p.scheme + '://' + p.subdomain + p.domain + p.path
    return urltools.normalize(url)

def extract_date(url_path, url=None):
    "Extract date from URL page if exists."
    if url_path is None and url:
        url_path = get_path(url)
    url_path_parts = _clean_split(url_path, sep='/', case='lower')
    date_parts = []
    for part in url_path_parts:
        try:
            _dateutil.parser.parse(part) # is part date-like?
            date_parts.append(part)
        except:
            next
    date_str = '/'.join(date_parts)
    if len(date_str) < 4: # require  >=4 digits
        return
    url_date = _dateutil.parser.parse(date_str)
    if url_date <= (_datetime.datetime.utcnow() + _datetime.timedelta(weeks=1)):
        return url_date.strftime('%Y-%m-%d')

def _clean_split(div_str, sep=', ', case=None):
    sl = []
    for div in div_str.split(sep):
        div = div.strip()
        if case == 'upper':
            div = div.upper()
        elif case == 'lower':
            div = div.lower()
        if div != '':
            sl.append(div)
    return sl
