import FWCore.ParameterSet.Config as cms

flavPlots = 'allbcldusg'

from RecoBTag.ImpactParameter.pfImpactParameterTagInfos_cfi import *
pfImpactParameterTagInfosNoHits = pfImpactParameterTagInfos.clone(
    minimumNumberOfPixelHits = cms.int32(0),
    minimumNumberOfHits = cms.int32(0),
)

# Taggers noHits setting implementation Start
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
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"))
)

from RecoBTag.SecondaryVertex.pfCombinedInclusiveSecondaryVertexV2BJetTags_cfi import *
pfCombinedInclusiveSecondaryVertexV2BJetTagsNoHits = pfCombinedInclusiveSecondaryVertexV2BJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"))
)
# Taggers noHits setting implementation Finish

# Tags list
from DQMOffline.RecoB.bTagCommon_cff import *
tags = cms.VPSet(
        cms.PSet(
            bTagTrackIPAnalysisBlock,
            type = cms.string('CandIP'),
            label = cms.InputTag("pfImpactParameterTagInfos"),
            folder = cms.string("IPTag")
        ),
        cms.PSet(
            bTagCombinedSVAnalysisBlock,
            ipTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
            type = cms.string('GenericMVA'),
            svTagInfos = cms.InputTag("pfSecondaryVertexTagInfos"),
            label = cms.InputTag("candidateCombinedSecondaryVertexComputer"),
            folder = cms.string("CSVTag")

        ),
        cms.PSet(
            bTagTrackCountingAnalysisBlock,
            label = cms.InputTag("pfTrackCountingHighEffBJetTags"),
            folder = cms.string("TCHE")
        ),
        cms.PSet(
            bTagTrackCountingAnalysisBlock,
            label = cms.InputTag("pfTrackCountingHighPurBJetTags"),
            folder = cms.string("TCHP")
        ),
        cms.PSet(
            bTagProbabilityAnalysisBlock,
            label = cms.InputTag("pfJetProbabilityBJetTags"),
            folder = cms.string("JP")
        ),
        cms.PSet(
            bTagBProbabilityAnalysisBlock,
            label = cms.InputTag("pfJetBProbabilityBJetTags"),
            folder = cms.string("JBP")
        ),
        cms.PSet(
            bTagSimpleSVAnalysisBlock,
            label = cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"),
            folder = cms.string("SSVHE")
        ),
        cms.PSet(
            bTagSimpleSVAnalysisBlock,
            label = cms.InputTag("pfSimpleSecondaryVertexHighPurBJetTags"),
            folder = cms.string("SSVHP")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("combinedSecondaryVertexBJetTags"),
            folder = cms.string("CSV_tkOnly")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfCombinedSecondaryVertexBJetTags"),
            folder = cms.string("CSV")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
            folder = cms.string("CSVv2")
        ),
        cms.PSet(
            bTagSoftLeptonAnalysisBlock,
            label = cms.InputTag("softPFMuonBJetTags"),
            folder = cms.string("SMT")
        ),
        cms.PSet(
            bTagSoftLeptonAnalysisBlock,
            label = cms.InputTag("softPFElectronBJetTags"),
            folder = cms.string("SET")
        ),
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
            label = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTagsNoHits"),
            folder = cms.string("CSVv2_noHits")
        ),
    ) 
	
# pfBTagging copy with "noHits" update
#from RecoBTag.Configuration.RecoBTag_cff import *
