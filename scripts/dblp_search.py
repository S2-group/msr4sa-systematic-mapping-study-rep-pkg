from lxml import etree

DBLP_XML = './dblp-2024-01-01.xml'
YEAR_MIN = 2007
YEAR_MAX = 2023
KEYWORDS = ['ROS']
VENUES = tuple([
    'conf/msr',
    'conf/icsa',
    'conf/ecsa'
])

def iterate_xml(xmlfile):
    doc = etree.iterparse(xmlfile, events=('start', 'end'), load_dtd=True)
    _, root = next(doc)
    start_tag = None
    for event, element in doc:
        if event == 'start' and start_tag is None:
            start_tag = element.tag
        if event == 'end' and element.tag == start_tag:
            yield element
            start_tag = None
            root.clear()

if __name__ == "__main__":
    hits = 0

    # Parse all entries in the DBLP database.
    for dblp_entry in iterate_xml(DBLP_XML):
        key = dblp_entry.get('key')

        # The db key should start with any of the venues we are interested in,
        # as well as be within the desired year range.
        if (key.startswith(VENUES) and
            int(dblp_entry.find('year').text) >= YEAR_MIN and
            int(dblp_entry.find('year').text) <= YEAR_MAX):
            # Remove any potential HTML content (such as <i>) from the title.
            title = ''.join(dblp_entry.find('title').itertext())
            
            # Merge the names of all authors of the work.
            authors = ' & '.join(''.join(author.itertext()) for author in
                dblp_entry.findall('author'))

            # Obtain the source (usually in the form of a DOI link).
            ee = dblp_entry.find('ee')
            if ee is not None:
                ee = ee.text

            # Print the current result to stdout as a csv line.
            print(hits,
                    title.replace(',', ';'),
                    dblp_entry.find('year').text,
                    authors,
                    key,
                    ee,
                    sep=', ')

            hits += 1
