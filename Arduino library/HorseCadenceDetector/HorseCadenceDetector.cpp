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
        _sampleAvg  = _sampleSum / _subSampleToUse;

        if(_sampleAvg < _stillThreshold){
            _currentCadence = CADENCE_TYPE_STILL;
        }else if(_sampleAvg < _walkThreshold){
            _currentCadence = CADENCE_TYPE_WALK;
        }else if(_sampleAvg < _trotThreshold){
            _currentCadence = CADENCE_TYPE_TROT;
        }else if(_sampleAvg < _canterThreshold){
            _currentCadence = CADENCE_TYPE_CANTER;
        }

        _sampleSum = 0;
        _subSampleCount = 0;
    }

}

int HorseCadenceDetector::GetCurrentCadence()
{
	return _currentCadence;
}


