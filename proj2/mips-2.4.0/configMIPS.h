//Here we put all variables and MACROS that control processor configuration

//Cache trace config
string programName = "Hello";
bool generateTraces = true;//generate traces for later use in DineroIV

//Data hazard config
#define USING_FOWARDING	false

//Superscalar config
#define IS_SUPERESCALAR	false

//Control Hazard config
bool isPredictorActive = true;

//Pipeline Size
int pipeLineSize = 5;
