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
|   |   |__ infobox-properties_lang=en_2021_12_01.ttl.bz2
|   |   |__ sitelink.20211027.tsv.gz
|   |
|   |__ getty
|       |__ AAT_explicit.zip
|       |__ ULAN_explicit.zip
|       |__ TGN_explicit.zip
|
|__ intermediate files  // graphs after importing by kgtk
|   |
|   |__ dbpedia
|   |   |__ wikidata_infobox.zip
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
|__ output  // output results, mainly the validated novel and statistics
    |
    |__ dbpedia
    |   |__ novel.zip                           // validated enriched statements 
    |   |__ property_mapping.json               // property mapping results
    |   |__ property_mapping_ground_truth.json  // ground truth property mappings
    |   |__ statement.statistics.json           // stats count in statement
    |   |__ entity.statistics.json              // stats count in entity
    |   |__ annotation.tsv                      // annotation and prediction
    |
    |__ getty
    |   |__ novel.zip                           // validated enriched statements
    |   |__ statement.statistics.json           // stats count in statement
    |   |__ entity.statistics.json              // stats count in entity
    |   |__ annotation.tsv                      // annotation and prediction
    |
    |__ agree                                   // overlapping entity-property values
    |   |__ wikidata.getty.P19.tsv              // place of birth
    |   |__ wikidata.getty.P20.tsv              // place of death
    |   
    |__ literals                                // literals enrichment
        |__ new.results.P569.tsv                // date of birth
        |__ new.results.P570.tsv                // date of death
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
The following file tree shows the structure of our code, which includes import notebooks and enrichment notebooks, for our two external graphs: DBpedia and Getty.
```
.
|__ import  // import external graphs
|   |__ build_wikidata_infobox.ipynb  // import DBpedia
|   |__ import_getty_vocab.ipynb      // import Getty
|
|__ examples  // enrichment notebooks
    |
    |__ dbpedia 
    |   |__ batch_query_procedure.ipynb  // enrichment for all properties with value-type constraint
    |   |__ founding_year_of_university.ipynb  
    |   |__ industry_of_company.ipynb  
    |   |__ movies_with_cost.ipynb  
    |   |__ spouse_of_politicians.ipynb  
    |
    |__ getty
        |__ getty_birthdate_query.ipynb    // enrichment for P569
        |__ getty_birthplace_query.ipynb   // enrichment for P19
        |__ getty_deathdate_query.ipynb    // enrichment for P570
        |__ getty_deathplace_query.ipynb   // enrichment for P20
        |__ getty_gender_query.ipynb       // enrichment for P21
        |__ getty_nationality_query.ipynb  // enrichment for P27
        |__ getty_query_procedure.ipynb    // example of enrichment for a subset of Wikidata (not included in our paper)
```
