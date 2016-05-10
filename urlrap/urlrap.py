import urltools
from hashlib import md5
import dateutil
import datetime

def get_domain(url_str):
    "Extract domain from URL"
    return urltools.parse(url_str).domain

def get_path(url_str):
    "Extract path component from URL"
    return urltools.parse(url_str).path

def _parse(url):
    "Parse URL with urltools"
    return urltools.parse(url)

def md5_hash(input_str):
    "Compuate MD5 hash"
    return md5(input_str.encode()).hexdigest()

def normalize(url, strip=True):
    "Optionally removing query string & RFC3986 normalize URL"
    p = urltools.parse(url)
    if strip:
        url = p.scheme + '://' + p.subdomain + p.domain + p.path
    return urltools.normalize(url)

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

def find_path_date(url_path):
    "Extract date from URL page if exists."
    url_path_parts = _clean_split(url_path, sep='/', case='lower')
    match = []
    for part in url_path_parts:
        try:
            dateutil.parser.parse(part) # is part is date-like?
            match.append(part)
        except:
            next
    date_str = '/'.join(match)
    if len(date_str) < 4: # need at least 4 digits
        return None
    try:
        url_date = dateutil.parser.parse(date_str)
        if url_date >= dateutil.parser.parse('1982-06-01') and url_date <= (datetime.datetime.utcnow() + datetime.timedelta(weeks=3)):
            return url_date.strftime('%Y-%m-%d')
    except:
        return None

def url_path_features(url=None, url_path=None):
    "Extract features from URL"
    d = {}
    if url_path:
        d['path'] = url_path 
    else:
        d['path'] = get_path(url)
    d['path_parts'] = _clean_split(d['path'], sep='/', case='lower')
    url_date = find_path_date(d['path'])
    if url_date != None:
        d['url_date'] = url_date
    path_part_lengths = list(map(len, d['path_parts']))
    d['max_part_size'] = max(path_part_lengths)
    d['path_title'] = d['path_parts'][path_part_lengths.index(d['max_part_size'])]
    d['path_title_words'] = len(d['path_title'].split('-'))
    return d
