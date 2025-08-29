# Automated Mapping of Wikipedia Templates to DBpedia

The process of mapping Wikipedia templates into DBpedia is often repetitive and labor-intensive. Each template, along with its attributes, needs to be identified, documented, and transformed into a structured mapping format. As the number of templates grows, manually repeating these steps becomes inefficient, time-consuming, and prone to inconsistencies. Automation is therefore essential to accelerate the mapping workflow, ensure consistency across templates, and support large-scale extraction efforts.

## 1. Why Automation?

The process of creating Wikipedia templates and their corresponding DBpedia mappings is often repetitive, time-consuming, and error-prone if done manually. Each template contains multiple attributes (properties), which must be identified, mapped to DBpedia ontology, and kept consistent across different languages. Automating this process helps to:

- Save time and effort by avoiding repetitive manual mapping.
- Ensure consistency in attribute translation and ontology alignment.
- Reduce errors when dealing with large numbers of templates.
- Scale efficiently to support new templates, properties, and languages.
- Enable reproducibility so that other contributors can repeat the process with the same steps.

## 2. Objectives of Automation

The main objectives of automation in the Amharic DBpedia extraction are:

- Automatically extract attributes (properties) from Wikipedia infobox templates.
- Translate these attributes into Amharic using machine translation (e.g., NLLB or Gemini API).
- Generate DBpedia-compliant mapping files with minimal manual intervention.
- Build a pipeline that can be reused for future templates and extended to other Ethiopian languages.

## 3. Prerequisites

Before running the automated extraction pipeline, the following are required:

### Technical Setup
- Python environment with required libraries (`requests`, `json`, `re`, `transformers` if using NLLB).
- Access to a translation API (e.g., Google Gemini, NLLB, or another free LLM).
- DBpedia Extraction Framework installed and configured.

### Knowledge Requirements
- Familiarity with Wikipedia template syntax.
- Understanding of DBpedia ontology classes and properties.
- Basic knowledge of RDF and SPARQL.

## 4. Steps Followed

The automation process can be summarized in the following steps:

### 4.1 Template Retrieval
- Fetch Wikipedia templates (e.g., `Infobox company`, `Infobox book`) using the Wikipedia API.
### 4.2 Attribute Extraction
- Parse the raw wikitext and extract attribute names.
### 4.3 Automatic Translation
- Send extracted attributes to a translation model (e.g., NLLB or Gemini) for English → Amharic translation.
### 4.4 Mapping Generation
- Use translated attributes to generate DBpedia mapping files (mapping_am.xml).
- Align translated attributes with DBpedia ontology properties.
### 4.5 Testing & Validation
- Run DBpedia extraction with the new mappings.
- Query extracted RDF data via SPARQL to ensure correctness.
