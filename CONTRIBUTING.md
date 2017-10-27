# Guide to contribution

Use a plain text editor to edit `narci` file in 
turtle syntax. Protoge or other GUI editors will 
mess the syntax on `narci`, so correct the style 
accordingly if you use a GUI. 

## New class

* A new `rdfs:Class` name should start with a 
  capital letter.

## New metadata entry

A new metadata entry should be defined via 
`rdfs:Property` and have the following values.

* `rdfs:isDefinedBy` should point to
  `narci` persistent URL <http://www.purl.org/narci/schema#>.
* `rdfs:label` usually the same as item name.
* `rdfs:domain` the class name where this metadata entry should be used. 
* `rdfs:range` type of literal values this metadata could take, use `xsd` data types.
* `rdf:type` must be `owl:DatatypeProperty`.
* If there are related terms `narci:relatedTo`.
* Use `skos:definition` for detailed description of the metadata.
* Relevant references should be provides via `narci:reference`.
* Reference to external ontology should be given `narci:onto`.
* Synonymous terms should be defined via `owl:sameAs`.
* Units should be given via `narci:unit`.

