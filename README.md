# MSR Approaches for Software Architecture – a Systematic Mapping Study

This is the replication package of the systematic literature review submitted to the IST journal (**under review**). The repository contains all the material required for replicating the study, including a complete list of papers, and all the data analysis phases.

It has been designed, performed, and reported by the following researchers:

```
- Mohamed Soliman - Paderborn University, Paderborn, Germany
- Ivano Malavolta - Vrije Universiteit Amsterdam, S2Group - The Netherlands
- Michel Albonico - Federal University of Technology, Paraná, IntelAgir - Brazil
- Andreas Wortmann - University of Stuttgart, ISW - Germany
```

For any information, interested researchers can contact us by sending an email to any of the investigators listed above.

## Repository Structure
The directory is structured as follows:

```
scripts/dblp_search.py          Script for initial paper crawling.
data/starting_set.csv           Spreadsheet with the first studies.
data/snowballing.csv            Spreadsheet with the papers from snowballing.
data/thematic_analysis.csv      Spreadsheet with the thematic analysis.
data/system_names.csv           Spreadsheet with the list of systems.
data/graph_generation.xlsx      Spreadsheet used for graph generation.
```

The spreadsheet for graph generation is also available [online](https://docs.google.com/spreadsheets/d/1VIQ__Gc9DMExdK1WsOcTba9L-RM6OdnHXr5lc-DzC2Y/edit?usp=sharing).

## Crawling Papers

If you are interested in replicating our papers' crawling, here are a few details that can help you.

You must be in the `scripts` folder:

```bash
$ cd scripts/
```

Then, you must download the last [DBLP snapshot](https://dblp.org/xml/release/) and extract it in the `scripts` folder (it's a big file > 4GB), and download the compatible document type definition (DTD) file - usually the first one after the downloaded XML file.

Now, it is time to set everything (snapshot file, year range, etc.) at the beginning of the `dblp_search.py` file. We plan to use a properties file for this shortly.

Once everything is set, you run the `dblp_search.py` script, and the papers should be selected (it will be a bit long given the file size).

```bash
$ python3 dblp_search.py > papers.csv
```

The snowballing was manually conducted and assisted with the [Zotero](https://www.zotero.org/) tool.

----

This repository is licensed under [MIT license](https://opensource.org/licenses/MIT).
