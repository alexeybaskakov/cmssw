# The following comments couldn't be translated into the new config version:

#! /bin/env cmsRun

import FWCore.ParameterSet.Config as cms

runOnMC = True

process = cms.Process("harvest")
process.load("DQMServices.Components.DQMEnvironment_cfi")

#keep the logging output to a nice level
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring()
)

process.load("Validation.RecoB.bTagAnalysis_harvesting_cfi")

#loading configuration from  trackOptimisation_cfi.py file
from Validation.RecoB.trackOptimisation_cfi import *
process.bTagValidationHarvest.tagConfig = tags
process.bTagValidationHarvest.flavPlots = flavPlots

if runOnMC:
	process.dqmSeq = cms.Sequence(process.bTagValidationHarvest * process.dqmSaver)
else:
	process.dqmSeq = cms.Sequence(process.bTagValidationHarvestData * process.dqmSaver)

process.plots = cms.Path(process.dqmSeq)

process.dqmEnv.subSystemFolder = 'BTAG'
process.dqmSaver.producer = 'DQM'
process.dqmSaver.workflow = '/POG/BTAG/BJET'
process.dqmSaver.convention = 'Offline'
process.dqmSaver.saveByRun = cms.untracked.int32(-1)
process.dqmSaver.saveAtJobEnd =cms.untracked.bool(True) 
process.dqmSaver.forceRunNumber = cms.untracked.int32(1)

process.DQMRootSource.fileNames = [
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_Track_optimization_noHits_test_19/results/MEtoEDMConverter_1.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_Track_optimization_noHits_test_19/results/MEtoEDMConverter_2.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_Track_optimization_noHits_test_19/results/MEtoEDMConverter_3.root'
]

