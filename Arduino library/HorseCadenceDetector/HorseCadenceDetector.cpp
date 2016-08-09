#include "Arduino.h"
#include "HorseCadenceDetector.h"

HorseCadenceDetector::HorseCadenceDetector(){}

void HorseCadenceDetector::FeedData (int gforce)
{
    
    if(gforce > _currentMaxValPerSubSample){
        _currentMaxValPerSubSample = gforce;
    }
    
    if((millis() - _timeFrameStart) > _subSampleWindow){
        _sampleSum += _currentMaxValPerSubSample;
        _subSampleCount ++;
        _timeFrameStart = millis();
        _currentMaxValPerSubSample = 0;  
    }

    if(_subSampleCount >= _subSampleToUse){
        int avg = _sampleSum / _subSampleToUse;

        if(avg < _stillThreshold){
            _currentCadence = CADENCE_TYPE_STILL;
        }else if(avg < _walkThreshold){
            _currentCadence = CADENCE_TYPE_WALK;
        }else if(avg < _trotThreshold){
            _currentCadence = CADENCE_TYPE_TROT;
        }else if(avg < _canterThreshold){
            _currentCadence = CADENCE_TYPE_CANTER;
        }
    }
        
}

int HorseCadenceDetector::GetCurrentCadence()
{
	return _currentCadence;
}


