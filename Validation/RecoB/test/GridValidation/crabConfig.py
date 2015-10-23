from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'Track_optimization_test_2'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'ANALYSIS'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'validation_FirstStepOnGrid.py'

config.section_("Data")
config.Data.inputDataset = '/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/AODSIM'

#config.Data.splitting = 'FileBased'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 3
config.Data.totalUnits = -1
config.Data.outLFNDirBase = "/store/user/baskakov/bTag/runIIspring_QCDinc_25ns_BTAG74X_v1_03/"
config.Data.publication = False
# This string is used to construct the output dataset name
config.Data.publishDataName = ''


config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite='T2_RU_JINR'
config.Site.whitelist=['T2_RU_JINR','T2_IT_Pisa', 'T2_US_Caltech', 'T2_DE_DESY', 'T1_US_FNAL']

