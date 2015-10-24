import FWCore.ParameterSet.Config as cms

pfTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)
noHitsPfTrackCountingHighEffBJetTags = pfTrackCountingHighEffBJetTags.clone(
tagInfos = cms.VInputTag(cms.InputTag("noHitsPfImpactParameterTagInfos"))
)


