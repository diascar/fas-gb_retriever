#!/usr/bin/python
import requests
import xml.etree.ElementTree as ET

# defining the base URL for eutils
baseURL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def get_baseSearch(database, query):
    '''
    using esearch tool to query in a specific ncbi database 
    '''
    if len(query) == 1:
        baseSearch = "esearch.fcgi?db={}&term={}&usehistory=y".format(database, query[0])
    else:
        new_query =  '+AND+'.join(query)
        baseSearch = "esearch.fcgi?db={}&term={}&usehistory=y".format(database, new_query)
    return baseSearch

def get_name(query):
    '''
    defining the base name for the output file
    '''
    if len(query) == 1:
        name = query[0]
    elif len(query) > 1:
        name = query[0]+ "_" + '_'.join(query[1:])
    return name

def url_to_xml(database, query):
    global baseURL
    bs = get_baseSearch(database, query)
    open_url = requests.get(baseURL+bs)
    string_xml = open_url.content.decode('utf-8')
    xml_instance = ET.fromstring(string_xml)
    return xml_instance

def get_webenv(database, query):
    '''
    Function obtains webEnv and queryKey from esearch in order to fetch data from database
    '''
    xmlfile = url_to_xml(database, query)
    for child in xmlfile:
        if child.tag == "WebEnv":
            webEnv = child.text
        elif child.tag == "QueryKey":
            queryKey = child.text
        else:
            continue
    return webEnv, queryKey


def get_baseFetch(database, query, retTypeVar, retModeVar):
    
    webEnv = get_webenv(database, query)[0]
    queryKey = get_webenv(database, query)[1]
    baseFetch = "efetch.fcgi?db={}&query_key={}&WebEnv={}&rettype={}&retmode={}".format(database, queryKey, webEnv, retTypeVar, retModeVar)
    return baseFetch

def get_data(database, query, retTypeVar, retModeVar):
    global baseURL
    file_name = get_name(query)
    
    if retModeVar == "text":
        if retTypeVar == "fasta":
            file_type = ".fas"
        elif retTypeVar == "gb":
            file_type = ".gb"
        else:
            file_type = ".txt"
    else:
        file_type = ".xml"

    bf = get_baseFetch(database, query, retTypeVar, retModeVar)
    open_fetch = requests.get(baseURL+bf)
    text = open_fetch.content.decode('utf-8')
    
    with open(str(file_name) + file_type, "w") as out:
        for line in text:
                out.write(line)
