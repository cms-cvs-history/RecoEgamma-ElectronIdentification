import FWCore.ParameterSet.Config as cms

from RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi import *

import RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi
eidRobustLoose = RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi.eidCutBasedExt.clone()

import RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi
eidRobustTight = RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi.eidCutBasedExt.clone()
eidRobustTight.robustEleIDCuts.barrel = [0.015, 0.0092, 0.020, 0.0025]
eidRobustTight.robustEleIDCuts.endcap = [0.018, 0.025, 0.020, 0.0040]

import RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi
eidRobustHighEnergy = RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi.eidCutBasedExt.clone()
eidRobustHighEnergy.robustEleIDCuts.barrel = [0.050, 0.011, 0.090, 0.005]
eidRobustHighEnergy.robustEleIDCuts.endcap = [0.100, 0.0275, 0.090, 0.007]

import RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi
eidLoose = RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi.eidCutBasedExt.clone()
eidLoose.electronQuality = 'loose'

import RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi
eidTight = RecoEgamma.ElectronIdentification.electronIdCutBasedExt_cfi.eidCutBasedExt.clone()
eidTight.electronQuality = 'tight'

eIdSequence = cms.Sequence(eidRobustLoose+eidRobustTight+eidRobustHighEnergy+eidLoose+eidTight)
