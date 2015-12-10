import FWCore.ParameterSet.Config as cms

flavPlots = 'allbcldusg'

from RecoBTag.ImpactParameter.pfImpactParameterTagInfos_cfi import *
pfImpactParameterTagInfosNoHits = pfImpactParameterTagInfos.clone(
    minimumNumberOfPixelHits = cms.int32(0),
    minimumNumberOfHits = cms.int32(0),
)

# Create new taggers with updated config pfImpactParameterTagInfosNoHits
from RecoBTag.ImpactParameter.pfTrackCountingHighEffBJetTags_cfi import *
pfTrackCountingHighEffBJetTagsNoHits = pfTrackCountingHighEffBJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"))
)
from RecoBTag.ImpactParameter.pfTrackCountingHighPurBJetTags_cfi import *
pfTrackCountingHighPurBJetTagsNoHits = pfTrackCountingHighPurBJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"))
)
from RecoBTag.ImpactParameter.pfJetProbabilityBJetTags_cfi import *
pfJetProbabilityBJetTagsNoHits = pfJetProbabilityBJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"))
)
from RecoBTag.ImpactParameter.pfJetBProbabilityBJetTags_cfi import *
pfJetBProbabilityBJetTagsNoHits = pfJetBProbabilityBJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"))
)
from RecoBTag.SecondaryVertex.pfCombinedSecondaryVertexBJetTags_cfi import *
pfCombinedSecondaryVertexBJetTagsNoHits = pfCombinedSecondaryVertexBJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"), cms.InputTag("pfSecondaryVertexTagInfos"))
)
from RecoBTag.SecondaryVertex.pfCombinedSecondaryVertexV2BJetTags_cfi import *
pfCombinedSecondaryVertexV2BJetTagsNoHits = pfCombinedSecondaryVertexV2BJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"), cms.InputTag("pfSecondaryVertexTagInfos"))
)
from RecoBTag.SecondaryVertex.pfCombinedInclusiveSecondaryVertexV2BJetTags_cfi import *
pfCombinedInclusiveSecondaryVertexV2BJetTagsNoHits = pfCombinedInclusiveSecondaryVertexV2BJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)

# pfBTagging copy with "noHits" update                                                                                                                                                                    
pfBTagging_noHits = cms.Sequence(                                                                                                                                                                         
    (                                                                                                                                                                                                     
      # impact parameters and IP-only algorithms                                                                                                                                                          
      pfImpactParameterTagInfosNoHits *                                                                                                                                                                   
      ( pfTrackCountingHighEffBJetTagsNoHits +                                                                                                                                                            
        pfTrackCountingHighPurBJetTagsNoHits +                                                                                                                                                            
        pfJetProbabilityBJetTagsNoHits +                                                                                                                                                                  
        pfJetBProbabilityBJetTagsNoHits +                                                                                                                                                                 

        # SV tag infos depending on IP tag infos, and SV (+IP) based algos                                                                                                                                
        #pfSecondaryVertexTagInfos *                                                                                                                                                   
        (                                                                                                                                                      
          pfCombinedSecondaryVertexBJetTagsNoHits +                                                                                                                                                      
          pfCombinedSecondaryVertexV2BJetTagsNoHits                                                                                                                                                      
        )                                                                                                                                                                                                 
        + #inclusiveCandidateVertexing *                                                                                                                                                                  
        #pfInclusiveSecondaryVertexFinderTagInfos *                                                                                                                                                       
        pfCombinedInclusiveSecondaryVertexV2BJetTagsNoHits                                                                                                                                
      )                                                                                        
    )                                                                                                                                                                                                  
)

# Adding new tags for default tag list 
from DQMOffline.RecoB.bTagCommon_cff import *
adtionalTags = cms.VPSet(
		cms.PSet(
            bTagTrackCountingAnalysisBlock,
            label = cms.InputTag("pfTrackCountingHighEffBJetTagsNoHits"),
            folder = cms.string("TCHE_noHits")
        ),
        cms.PSet(
            bTagTrackCountingAnalysisBlock,
            label = cms.InputTag("pfTrackCountingHighPurBJetTagsNoHits"),
            folder = cms.string("TCHP_noHits")
        ),
		cms.PSet(
            bTagProbabilityAnalysisBlock,
            label = cms.InputTag("pfJetProbabilityBJetTagsNoHits"),
            folder = cms.string("JP_noHits")
        ),
		cms.PSet(
            bTagBProbabilityAnalysisBlock,
            label = cms.InputTag("pfJetBProbabilityBJetTagsNoHits"),
            folder = cms.string("JBP_noHits")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfCombinedSecondaryVertexBJetTagsNoHits"),
            folder = cms.string("CSV_noHits")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfCombinedSecondaryVertexV2BJetTagsNoHits"),
            folder = cms.string("CSVv2AVR_noHits")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTagsNoHits"),
            folder = cms.string("CSVv2_noHits")
        ),
    ) 
tags = cms.VPSet(bTagCommonBlock.tagConfig + adtionalTags)
