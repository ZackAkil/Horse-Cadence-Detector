#ifndef HorseCadenceDetector_h
#define HorseCadenceDetector_h


class HorseCadenceDetector
{
	public: 

	const char CADENCE_TYPE_CANTER = 3;
	const char CADENCE_TYPE_TROT = 2;
    const char CADENCE_TYPE_WALK = 1;
	const char CADENCE_TYPE_STILL = 0;

	HorseCadenceDetector();
	int GetCurrentCadence();
	void FeedData (int gforce);

	private:

	long _timeFrameStart = 0;
    int _currentMaxValPerSubSample = 0;
    int _subSampleCount = 0;
    int _sampleSum = 0;
    
	int _currentCadence = 0;


	const int _canterThreshold = 20000;
	const int _trotThreshold = 11500;
    const int _walkThreshold = 7000;
    const int _stillThreshold = 4500;

    
	const int _subSampleWindow = 725;
    const int _subSampleToUse = 4;
};

#endif





