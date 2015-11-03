import FWCore.ParameterSet.Config as cms

pfTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)
pfTrackCountingHighPurBJetTagsNoHits = pfTrackCountingHighPurBJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosNoHits"))
)

