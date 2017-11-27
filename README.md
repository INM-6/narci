# Neural Activity Resource (NAR) Calcium Imaging Ontology (NARCI)

The need for semantic description of data sets as a metadata, 
specially those originating from neuroscience experiments 
are well established due to diversity of experimental
procedures and modalities. `NARCI`, Neural Activity 
Resource (NAR) Calcium Imaging Ontology, provides a 
semantic graph schema for describing Calcium Imaging 
experiments based on the work 
`Montijn et al., 2016, Cell Reports 16, 2486–2498` [doi](http://dx.doi.org/10.1016/j.celrep.2016.07.065). 

This is an RDF schema using OWL languge and should be used 
to express`metadata` from a calcium imaging experiment.

# Programmatic Usage

* For short tutorial on how to use the ontology programmatically
  via `rdflib` see python notebook under `tutorial`.

## Ontology release management

Versions of the persistent URL of the ontology, `narci` should be used in production.
Note that once it is released, schema version move to `dev` of next release
number, first minor in the repository, for development purpose. The schema 
persistent URLs versioning are matching with the released released version.
Documentation and tutorial for each version can be found in the released versions,
either by tagged version or released files.

## Ontology current development URL
* `http://www.purl.org/narci/v0.3dev/schema` 

## Ontology in production URLs
* `http://www.purl.org/narci/v0.2.1/schema`  
   [tutorial](https://github.com/INM-6/narci/blob/v0.2.1/tutorial/narci_tutorial.ipynb) |
   [full graph](https://github.com/INM-6/narci/blob/v0.2.1/ontology/narci.svg) |
   [prov graph](https://github.com/INM-6/narci/blob/v0.2.1/prov/narciprov.svg)

# How to cite

* Neural Activity Resource Calcium Imaging Ontology,
  M.Suezen, G.Meijer, X.Troncoso, J.S.Montijn, C.S.Lansink, 
  A.P.Davison, M.Denker, T.Wachtler, S.Gruen, C.M.A.Pennartz (2017)
  `http://www.purl.org/narci/v0.2.1/schema`

# License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 Generic License</a>.

```
(c) 2017 University of Amsterdam
         Forschungszentrum Juelich GmbH
         The German Neuroinformatics Node (G-Node)
         Le Centre National de la Recherche Scientifique (CRNS)

        
```
# Mailing list

There is a group/mailing list for `narci` called `narci:Calcium Imaging Ontology`, Group: [narci-ontology](https://groups.google.com/forum/#!forum/narci-ontology).

# References

* Population-Level Neural Codes Are Robust to Single-Neuron 
  Variability from a Multidimensional Coding Perspective
  `Montijn et al., 2016, Cell Reports 16, 2486–2498` [doi](http://dx.doi.org/10.1016/j.celrep.2016.07.065). 

# Acknowledgements

`narci` is developed under the auspices of <a href="http://ec.europa.eu/programmes/horizon2020/en/h2020-section/fet-flagships">European Union (EU)</a>
 <a href="http://www.humanbrainproject.eu/en/">Human Brain Project (HBP)</a>. 
Work package SP 5.7.2 named NAR within the Neuroinformatics Platform.
