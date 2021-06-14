import sys
import json
import argparse
from SPARQLWrapper import SPARQLWrapper, JSON

def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

if __name__ == "__main__":
    endpoint_url = "https://query.wikidata.org/sparql"

    parser = argparse.ArgumentParser()
    parser.add_argument('--index', default=1, type=int, choices=[1, 2, 3], help='index of query')
    parser.add_argument('--path', type=str, help='path to store cached query results')

    args = parser.parse_args()

    """ query items with the attribute """
    if args.index == 1:
        query = """SELECT DISTINCT ?movieLabel ?cost
        WHERE
        {
          ?movie wdt:P31 wd:Q11424 ;
                 wdt:P577 ?publicationDate ;
                 wdt:P2130 ?cost .
          FILTER(YEAR(?publicationDate) = 2020) .
          SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        """
    elif args.index == 2:
        query = """SELECT DISTINCT ?presidentLabel ?electionLabel
        WHERE
        {
          ?election wdt:P31/wdt:P279* wd:Q858439 ;
                    wdt:P585 ?pointInTime ;
                    wdt:P991 ?president .
          FILTER(YEAR(?pointInTime) = 2020) .
          SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }       
        """
    elif args.index == 3:
        query = """SELECT DISTINCT ?universityLabel (YEAR(?inception) AS ?foundingYear)
        WHERE
        {
          ?university wdt:P31/wdt:P279* wd:Q3918 ;
                      wdt:P571 ?inception .
          SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }       
        """
    else:
        raise NotImplementedError

    output = dict()

    results = get_results(endpoint_url, query)

    # caching query results
    # print(results["results"]["bindings"])
    output['items_with_attr'] = results

    """ query items without the attribute """
    if args.index == 1:
        query = """SELECT DISTINCT ?movie ?movieLabel 
        WHERE
        {
          ?movie wdt:P31 wd:Q11424 ;
                 wdt:P577 ?publicationDate ;
          FILTER(YEAR(?publicationDate) = 2020) .
          FILTER NOT EXISTS { ?movie wdt:P2130 ?cost }
          SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        """
    elif args.index == 2:
        query = """SELECT DISTINCT ?election ?presidentLabel ?electionLabel
        WHERE
        {
          ?election wdt:P31/wdt:P279* wd:Q858439 ;
                    wdt:P585 ?pointInTime .
          FILTER(YEAR(?pointInTime) = 2020) .
          FILTER NOT EXISTS { ?election wdt:P991 ?president }
          FILTER NOT EXISTS { ?election wdt:P17 wd:Q30 }
          SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        """
    elif args.index == 3:
        query = """SELECT DISTINCT ?university ?universityLabel (YEAR(?inception) AS ?foundingYear)
        WHERE
        {
          ?university wdt:P31/wdt:P279* wd:Q3918 .
          FILTER NOT EXISTS { ?university wdt:P571 ?inception }
          SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        """
    else:
        raise NotImplementedError

    results = get_results(endpoint_url, query)

    # caching query results
    # print(results["results"]["bindings"])
    output['items_without_attr'] = results

    with open(args.path, 'w+') as f:
        json.dump(output, f, indent=4)

