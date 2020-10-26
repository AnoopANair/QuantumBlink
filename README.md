# QuantumBlink



# **INTRODUCTION**

QunatumBlink is a python module developed by **Anoop A Nair**, under the supervison of **Vishnu E K,Ph.D [@ K.G.T. Labs]**.  It helps in the **analysis of flouresence intermittency data** obtained from the MT-300 single photon detector. The module when provided with the Intensity vs Time trace derives the **ON/OFF event PDFs** and the correlations in data indicating the **memory effect**. 


# **HOW TO INSTALL**

The `Quantum Blink` module depends on the `numpy` module for most of it's functionality.

To Install `numpy` use:


```
pip install numpy
```

To install `QuantumBlink` use: 

```
pip install QuantumBlink
```


To install `QuantumBlink` of a particular version say 1.x use: 

```
pip install QuantumBlink==1.x
```

# **HOW TO USE**

The module can be imported after installation using:

```
import QuantumBlink as qb
```
The csv file should contain two columns the first one being the time and second one being the intesity values.


# **KEYWORDS and METHODS**

 ## > **Data Acquisition**


 ### >> Intensity data

```
IntensityData  =  IntensityDataAcquire(PATH)
```


> 1.**INPUT**
> * PATH = "the path to the csv data file"
> 2.**OUTPUT**
> * IntensityData = array of intesity values



## > **The ON/OFF Events**

### >> ON-OFF durations
```
Positives , Negatives =  Power_dist_one(PATH,Threshold,exptime)
```

> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * Positives = array of ON time durations
> * Negatives = array of OFF time durations

### >> OFF-time distribution

```
Pdf_accept_off,Offtime =  Offtime_pdf(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * Pdf_accept_off = The probability distribution of OFF-time durations
> * Offtime = array of distinct OFF-time durations

### >> ON-time distribution

```
Pdf_accept_on,Ontime =  Ontime_pdf(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * Pdf_accept_on = The probability distribution of ON-time durations
> * Ontime = array of distinct ON-time durations


## > **Event Duration info**

### >> ON time ratio

```
On_ratio =  OnTimeFraction(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * On_ratio = The fraction of ON events.  

### >> OFF time ratio


```
Off_ratio =  OffTimeFraction(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * Off_ratio = The fraction of OFF events.  

### >> ON-OFF ratio


```
ON_OFF_ratio =  OnOffRatio(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * ON_OFF_ratio = The ratio of ON to OFF events.  

### >> OFF-ON ratio


```
OFF_ON_ratio =  OffOnRatio(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * OFF_ON_ratio = The ratio of OFF to ON events.  

### >> TOTAL ONtime


```
TOTAL_ONTIME =  TotalOnTime(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * TOTAL_ONTIME = The total time occupied by ON events.  

### >>  TOTAL OFFtime


```
TOTAL_OFFTIME =  TotalOffTime(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * TOTAL_OFFTIME = The total time occupied by OFF events.  


## >  **Mean, Min, Max intensities**

### >> The min, max and average intesity of tthe data
```
AverageIntensity = AverageIntensity(PATH)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> 2.**OUTPUT**
> * AverageIntensity = The Average intensity calculated from the data.  


```
MaxIntensity = MaxIntensity(PATH)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> 2.**OUTPUT**
> * MaxIntensity = The maximum intensity calculated from the data.  


```
MinIntensity = MinIntensity(PATH)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> 2.**OUTPUT**
> * MinIntensity = The minimum intensity calculated from the data.  

### >> The average intesity between two intensity levels

```
Intensity_average = AverageIntensityBetween(PATH,Threshold1,Threshold2)
```

> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold1 = The upper threshold
> * Threshold2 = The lower threshold
> 2.**OUTPUT**
> * Intensity_average = The average intensity between the upper and lower threshold



## > **Memory Effect**



### >> ON-OFF Correlation

```
XX,YY,R1 =  OnOffCorr(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * XX = array of ON/OFF events .
> * YY = array of ON/OFF events .
> * R1 = The correlation coefficient. 

```
X_x_log,Y_y_log,R1 = OnOffCorrLog(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * X_x_log = array of log value of ON/OFF events .
> * Y_y_log = array of log value of ON/OFF events .
> * R1 = The correlation coefficient. 



### >> ON-ON Correlation

```
XX,YY,R1 OnOnCorr(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * XX = array of ON events .
> * YY = array of ON events .
> * R1 = The correlation coefficient. 

```
X_x_log,Y_y_log,R1 = OnOnCorrLog(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * X_x_log = array of log value of ON events .
> * Y_y_log = array of log value of ON events .
> * R1 = The correlation coefficient. 

### >> OFF-OFF Correlation

```
XX,YY,R1 =  OffOffCorr(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * XX = array of OFF events .
> * YY = array of OFF events .
> * R1 = The correlation coefficient. 

```
X_x_log,Y_y_log,R1 OffOffCorrLog(PATH,Threshold,exptime)
```
> 1.**INPUT**
> * PATH = "the path to the csv data file".
> * Threshold = This specifies the **instensity level** above which events are treated as **positve** and below which events are treated as **negative**.
> * exptime = The time interval between each consecutive event. 
> 2.**OUTPUT**
> * X_x_log = array of log value of OFF events .
> * Y_y_log = array of log value of OFF events .
> * R1 = The correlation coefficient.
"""
