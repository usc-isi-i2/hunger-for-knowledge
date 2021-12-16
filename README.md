# Enriching Wikidata with Linked Open Data
This is the official repository for paper "Enriching Wikidata with Linked Open Data".

## Data
All the data we used can be downloaded from this [google drive folder](https://drive.google.com/drive/folders/13UjvUKcc7YUiYSQjxba4R8UmTTGVWNft?usp=sharing).
The usage and information of each data file can be found in each notebook's environment path step.
```
.
|__ input  // original data files for Wikidata, DBpedia and Getty
|   |
|   |__ wikidata
|   |   |__ claims.tsv.gz
|   |   |__ labels.en.tsv.gz
|   |   |__ derived.P31.tsv.gz
|   |   |__ derived.P279star.tsv.gz
|   |   |__ value_type_constraint.json
|   |
|   |__ dbpedia
|   |   |__ infobox_properties_wkd_uris_en.ttl.bz2
|   |   |__ wikidata-20181210.sitelinks.zip
|   |
|   |__ getty
|       |__ AAT_explicit.zip
|       |__ ULAN_explicit.zip
|       |__ TGN_explicit.zip
|
|__ intermediate  // graphs after importing by kgtk
|   |
|   |__ dbpedia
|   |   |__ wikidata_infobox.tsv
|   |
|   |__ getty
|       |__ ULAN
|       |   |__ explicit.zip
|       |   |__ subgraphs.zip
|       |   |__ wiki.align.tsv
|       |__ TGN
|           |__ explicit.zip
|           |__ wiki.align.tsv
|
|__ output  // output results, mainly the validated novel and disagreement
    |
    |__ dbpedia
    |   |__ novel.zip
    |   |__ disagree.zip
    |
    |__ getty
        |__ novel.zip
        |__ disagree.zip
```
There are two ways to use the above data and run our examples:
1. Run from scratch by using data in `./input` folder and run our notebooks in `./import`,
   it will generate the same data in `./intermediate` which are graphs imported by `kgtk`.
2. Skip the import step, directly use data in `./intermediate` folder and run the examples.

**Note:** 

In each notebook in examples, there are cells after the import cell that one can adjust the path to the files. 
The users can match the file path according to the specific file names.

## Requirements
We use [Knowledge Graph Toolkit](https://github.com/usc-isi-i2/kgtk) dev branch to implement our procedures.

## Notebooks
The following file tree shows the structure of our code, the comment notes the simple objetive of each notebook:
```
.
|__ import  // import external graphs
|   |__ build_wikidata_infobox.ipynb  // import DBpedia
|   |__ import_getty_vocab.ipynb  // import Getty
|
|__ examples  // enrichment notebooks
    |
    |__ dbpedia 
    |   |__ batch_query_procedure.ipynb  // batch enrichment
    |   |__ founding_year_of_university.ipynb  // on-demand enrichment for P571
    |   |__ industry_of_company.ipynb  // on-demand enrichment for P452
    |   |__ movies_with_cost.ipynb  // on-demand enrichment for P2130
    |   |__ spouse_of_politicians.ipynb  // on-demand enrichment for P26
    |
    |__ getty
        |__ getty_birthdate_query.ipynb  // on-demand enrichment for P569
        |__ getty_birthplace_query.ipynb  // on-demand enrichment for P19
        |__ getty_deathdate_query.ipynb  // on-demand enrichment for P570
        |__ getty_deathplace_query.ipynb  // on-demand enrichment for P20
        |__ getty_gender_query.ipynb  // on-demand enrichment for P21
        |__ getty_nationality_query.ipynb  // on-demand enrichment for P27
        |__ getty_query_procedure.ipynb  // example of enrichment for a subgraph of Wikidata (not included in our paper)
```