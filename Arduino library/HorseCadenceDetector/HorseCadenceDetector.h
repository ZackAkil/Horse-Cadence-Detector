#ifndef HorseCadenceDetector_h
#define HorseCadenceDetector_h


class HorseCadenceDetector
{
	public: 

	const char CADENCE_TYPE_CANTER = 2;
	const char CADENCE_TYPE_TROT = 1;
	const char CADENCE_TYPE_OTHER = 0;

	HorseCadenceDetector();
	int GetCurrentCadence();
	void FeedData (int gforce, long currentTime);

	private:

	long _timeFrameStart = 0;
	int _validTrotPeaks = 0;
	int _validCantPeaks = 0;
	int _currentCadence = 0;


	bool _inTrotPeakFlag = false;
	bool _inCantPeakFlag = false;

	const int _peakCantThreshold = 10178;
	const int _peakTrotThreshold = 879;
	const int _peakCantFrequencyThreshold = 3;
	const int _peakTrotFrequencyThreshold = 3;
	const int _sampleWindow = 2900;
};

#endif





