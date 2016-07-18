#include "HorseCadenceDetector.h"

HorseCadenceDetector::HorseCadenceDetector(){}

void HorseCadenceDetector::FeedData (int gforce)
{
        _time ++;

        if ((gforce > _peakTrotThreshold) && (!_inTrotPeakFlag)){
            _inTrotPeakFlag = true;
        }else if((gforce < _peakTrotThreshold) && _inTrotPeakFlag){
            _inTrotPeakFlag = false;
            _validTrotPeaks ++;
        }
            
        if((gforce > _peakCantThreshold) && (!_inCantPeakFlag)){
            _inCantPeakFlag = true;
        }else if((gforce < _peakCantThreshold) && _inCantPeakFlag){
            _inCantPeakFlag = false;
            _validCantPeaks ++;
        }
        
        if(_time > _sampleWindow){
            
            if(_validCantPeaks > _peakCantFrequencyThreshold){
                _currentCadence = CADENCE_TYPE_CANTER;
            }
            else if(_validTrotPeaks > _peakTrotFrequencyThreshold){
                _currentCadence = CADENCE_TYPE_TROT;
            }else{
            	_currentCadence = CADENCE_TYPE_OTHER;
            }
            _validTrotPeaks = 0;
            _validCantPeaks = 0;
            _time = 0;
        }
}

int HorseCadenceDetector::GetCurrentCadence()
{
	return _currentCadence;
}


