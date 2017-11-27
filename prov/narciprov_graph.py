#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:45:33 2017

@author: Mehmet Suzen
"""

import prov.model as prov

document = prov.ProvDocument()

#
# narciprov ontology
#
document.add_namespace('narciprov', 'http://www.purl.org/narci/prov#')
#
# Activities
#
document.activity('narciprov:CraniotomyProcedure')
document.activity('narciprov:TwoPhotonImaging')
document.activity('narciprov:VisualStimulation')
document.activity('narciprov:RegionClassification')
document.activity('narciprov:TimeSeriesExtract')
#
# Entities
#
document.entity('narciprov:Subject')
document.entity('narciprov:CraniotomyProtocol')
document.entity('narciprov:Craniotomy')
document.entity('narciprov:AnaesthesiaProtocol')
document.entity('narciprov:TwoImagingSystem')
document.entity('narciprov:VisualStimulus')
document.entity('narciprov:VisualStimulusPresentation')
document.entity('narciprov:ImageSequence')
document.entity('narciprov:RegionOfInterest')
document.entity('narciprov:CellFromRegionOfInterest')
document.entity('narciprov:FluorescenceActivity')
#
# used
#
document.used('narciprov:CraniotomyProcedure', 'narciprov:Subject')
document.used('narciprov:TwoPhotonImaging', 'narciprov:Craniotomy')
document.used('narciprov:TwoPhotonImaging', 'narciprov:TwoImagingSystem')
document.used('narciprov:TwoPhotonImaging', 'narciprov:AnaesthesiaProtocol')
document.used('narciprov:CraniotomyProcedure', 'narciprov:CraniotomyProtocol')
document.used('narciprov:VisualStimulation', 'narciprov:VisualStimulus')
document.used('narciprov:TimeSeriesExtract', 'narciprov:CellFromRegionOfInterest')
document.used('narciprov:RegionClassification', 'narciprov:RegionOfInterest')
document.used('narciprov:VisualStimulation', 'narciprov:VisualStimulusPresentation')
#
#  wasGeneratedBy
#
document.wasGeneratedBy('narciprov:Craniotomy', 'narciprov:CraniotomyProcedure')
document.wasGeneratedBy('narciprov:ImageSequence', 'narciprov:TwoPhotonImaging')
document.wasGeneratedBy('narciprov:CellFromRegionOfInterest', 'narciprov:RegionClassification')
document.wasGeneratedBy('narciprov:FluorescenceActivity', 'narciprov:TimeSeriesExtract')

#
# wasInformedBy
#
document.wasInformedBy('narciprov:VisualStimulation', 'narciprov:TwoPhotonImaging')

#
# wasDerivedFrom
#
document.wasDerivedFrom('narciprov:RegionOfInterest', 'narciprov:ImageSequence')

#
# Visualize the graph
#
from prov.dot import prov_to_dot
dot = prov_to_dot(document)
dot.write_svg("narciprov.svg") # graphviz should be installed

             
             
