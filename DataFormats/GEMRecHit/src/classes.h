#include "DataFormats/GEMRecHit/interface/GEMRecHit.h"
#include "DataFormats/GEMRecHit/interface/GEMRecHitCollection.h"
#include "DataFormats/GEMRecHit/interface/ME0RecHit.h"
#include "DataFormats/GEMRecHit/interface/ME0RecHitCollection.h"
#include "DataFormats/Common/interface/Wrapper.h"

namespace { 
  struct dictionary {
    std::pair<unsigned int, unsigned int> dummyrpc1;
    std::pair<unsigned long, unsigned long> dummyrpc2;
    std::map<GEMDetId, std::pair<unsigned int, unsigned int> > dummyrpcdetid1;
    std::map<GEMDetId, std::pair<unsigned long, unsigned long> > dummyrpcdetid2;
    std::map<ME0DetId, std::pair<unsigned int, unsigned int> > dummyme0detid1;
    std::map<ME0DetId, std::pair<unsigned long, unsigned long> > dummyme0detid2;

    GEMRecHit rrh;
    std::vector<GEMRecHit> vrh;
    GEMRecHitCollection c;
    edm::Wrapper<GEMRecHitCollection> w;

    ME0RecHit mrh;
    std::vector<ME0RecHit> vmrh;
    ME0RecHitCollection mc;
    edm::Wrapper<ME0RecHitCollection> mw;

  };
}

