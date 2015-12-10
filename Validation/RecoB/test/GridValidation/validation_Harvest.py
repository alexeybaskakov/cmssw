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
from Validation.RecoB.trackOptimisation_cfi import tags, flavPlots
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
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_71.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_3.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_89.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_67.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_38.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_10.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_87.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_63.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_11.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_44.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_77.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_42.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_171.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_126.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_21.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_33.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_45.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_125.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_65.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_110.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_84.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_123.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_70.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_131.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_88.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_124.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_6.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_157.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_43.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_144.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_72.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_66.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_9.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_1.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_8.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_145.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_170.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_128.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_58.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_90.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_122.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_13.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_31.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_129.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_39.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_118.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_32.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_167.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_51.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_172.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_40.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_161.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_76.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_60.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_103.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_50.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_28.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_105.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_48.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_46.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_102.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_165.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_169.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_12.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_24.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_174.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_162.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_52.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_54.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_101.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_59.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_35.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_120.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_49.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_16.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_158.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_148.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_34.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_138.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_7.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_121.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_56.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_53.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_98.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_108.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_47.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_134.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_27.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_92.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_173.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_159.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_107.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_133.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_25.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_68.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_104.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_150.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_147.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_23.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_18.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_26.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_36.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_136.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_4.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_94.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_15.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_30.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_140.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_119.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_137.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_91.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_95.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_127.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_109.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_82.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_142.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_139.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_61.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_153.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_22.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_29.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_20.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_149.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_163.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_62.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_5.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_112.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_166.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_135.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_37.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_97.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_113.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_55.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_2.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_154.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_175.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_151.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_116.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_96.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_115.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_64.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_156.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_114.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_83.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_168.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_117.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_93.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_41.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_130.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_75.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_164.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_160.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_19.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_74.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_152.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_111.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_69.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_57.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_14.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_132.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_85.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_155.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_100.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_146.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_17.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_80.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_79.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_99.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_141.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_81.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_86.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_73.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_106.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_78.root',
'file:/afs/cern.ch/work/b/baskakov/public/b-tagging/TrackSelection/CMSSW_7_4_11/src/Validation/RecoB/test/GridValidation/crab_QCD_Pt_300to470_2015-12-06_1449409867845/results/MEtoEDMConverter_143.root',
]

