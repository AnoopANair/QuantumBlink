
import numpy as np

def IntensityDataAcquire(PATH):
    data = np.genfromtxt(PATH,usecols=(0,1),delimiter=",")
    DATA = data[:,1].copy()
    return DATA

def Power_dist_one(PATH,Threshold,exptime):

    DATA      = IntensityDataAcquire(PATH)
    Data      = DATA > Threshold
    
    negatives = np.array([])
    positives = np.array([])
    
    
    counter_neg = 0
    counter_pos = 0
    
    
    
    for i in Data:
    
      if i == False:
          counter_neg += 1 
          positives    = np.append(positives,counter_pos)
          counter_pos  = 0
    
      if i == True:
          negatives    = np.append(negatives,counter_neg)
          counter_neg  = 0
          counter_pos += 1  
    
    if i == False:
      negatives = np.append(negatives,counter_neg)
    
    if i == True:
      positives = np.append(positives,counter_pos)
    
    
    pos_val = positives[positives.nonzero()]
    neg_val = negatives[negatives.nonzero()]

    return pos_val,neg_val

def Power_dist(PATH,Threshold,exptime) :

    pos_val,neg_val = Power_dist_one(PATH,Threshold,exptime)

    max_pos = np.max(pos_val)
    min_pos = np.min(pos_val)
    
    max_neg = np.max(neg_val)
    min_neg = np.min(neg_val)
    
    pos_bin_list = np.arange(min_pos,max_pos+1,1.0)
    neg_bin_list = np.arange(min_neg,max_neg+1,1.0)
    
    pos_bins       = np.array([])
    pos_bin_counts = np.array([])
    
    for bin_val in pos_bin_list:
    
          pos_bin_counts = np.append(pos_bin_counts,np.sum(pos_val == bin_val))
          pos_bins       = np.append(pos_bins,bin_val)
    
    pos_bins       = np.array(pos_bins)
    pos_bin_counts = np.array(pos_bin_counts)
    
    neg_bins       = np.array([])
    neg_bin_counts = np.array([])
    
    for bin_val in neg_bin_list:
    
          neg_bin_counts = np.append(neg_bin_counts,np.sum(neg_val == bin_val))
          neg_bins       = np.append(neg_bins,bin_val)
    
    neg_bins       = np.array(neg_bins)
    neg_bin_counts = np.array(neg_bin_counts)
    
    
    index_neg = neg_bin_counts > 1;
        
    Offtime          = (neg_bins[index_neg])*exptime
    countsoff_accept = neg_bin_counts[index_neg]
    number_offtime   = len(countsoff_accept)
    total_off        = np.sum(countsoff_accept)
    pdf_accept_off   = np.zeros((number_offtime, 1))
    
    
    if number_offtime >= 5:
        for i in  range(0,number_offtime):
            if i == 0:
                delta_off = Offtime[i+1] - Offtime[i];
            elif i == number_offtime-1:
                delta_off = Offtime[i] - Offtime[i-1];
            else:
                A_off = Offtime[i] - Offtime[i-1];
                B_off = Offtime[i+1] - Offtime[i];
                delta_off = (A_off + B_off)/2;
            pdf_accept_off[i] = countsoff_accept[i]/(total_off*delta_off);
    
    
    index_pos = pos_bin_counts > 1;
        
    Ontime          = (pos_bins[index_pos])*exptime
    countson_accept = pos_bin_counts[index_pos]
    number_ontime   = len(countson_accept)
    total_on        = np.sum(countson_accept)
    pdf_accept_on   = np.zeros((number_ontime, 1))
    
    if number_ontime >= 5:
        for i in  range(0,number_ontime):
            if i == 0:
                delta_on = Ontime[i+1] - Ontime[i];
            elif i == number_ontime-1:
                delta_on = Ontime[i] - Ontime[i-1];
            else:
                A_on = Ontime[i] - Ontime[i-1];
                B_on = Ontime[i+1] - Ontime[i];
                delta_on = (A_on + B_on)/2;
            pdf_accept_on[i] = countson_accept[i]/(total_on*delta_on);
    
    return pdf_accept_on,pdf_accept_off,Offtime,Ontime
           

def Offtime_pdf(PATH,Threshold,exptime):
    pdf_accept_on, pdf_accept_off, Offtime, Ontime = Power_dist(PATH,Threshold,exptime)
    return pdf_accept_off,Offtime

def Ontime_pdf(PATH,Threshold,exptime):
    pdf_accept_on, pdf_accept_off, Offtime, Ontime = Power_dist(PATH,Threshold,exptime)
    return pdf_accept_on,Ontime




def On_Off_frac_main(PATH,Threshold,exptime):
      ontime,offtime  = Power_dist_one(PATH,Threshold,exptime)
      TOTAL_OFFTIME   = np.sum(offtime)*exptime
      TOTAL_ONTIME    = np.sum(ontime)*exptime
      TOLAL_TIME      = TOTAL_OFFTIME+TOTAL_ONTIME
      return TOTAL_OFFTIME, TOTAL_ONTIME, TOLAL_TIME


def OnTimeFraction(PATH,Threshold,exptime):
      _, TOTAL_ONTIME, TOLAL_TIME = On_Off_frac_main(PATH,Threshold,exptime)
      On_ratio = TOTAL_ONTIME/TOLAL_TIME
      return On_ratio

def OffTimeFraction(PATH,Threshold,exptime):
      TOTAL_OFFTIME,_, TOLAL_TIME = On_Off_frac_main(PATH,Threshold,exptime)
      Off_ratio = TOTAL_OFFTIME/TOLAL_TIME
      return Off_ratio

def OnOffRatio(PATH,Threshold,exptime):
      TOTAL_OFFTIME,_, TOLAL_TIME = On_Off_frac_main(PATH,Threshold,exptime)
      ON_OFF_ratio  = TOTAL_ONTIME/TOTAL_OFFTIME
      return ON_OFF_ratio

def OffOnRatio(PATH,Threshold,exptime):
      TOTAL_OFFTIME,_, TOLAL_TIME = On_Off_frac_main(PATH,Threshold,exptime)
      OFF_ON_ratio  = TOTAL_OFFTIME/TOTAL_ONTIME
      return OFF_ON_ratio

def TotalOnTime(PATH,Threshold,exptime):
      _, TOTAL_ONTIME,_ = On_Off_frac_main(PATH,Threshold,exptime)
      return TOTAL_ONTIME

def TotalOffTime(PATH,Threshold,exptime):
      TOTAL_OFFTIME,_,_ = On_Off_frac_main(PATH,Threshold,exptime)
      return TOTAL_OFFTIME


def AverageIntensity(PATH):
    DATA = IntensityDataAcquire(PATH)
    return np.mean(DATA)


def MaxIntensity(PATH):
    DATA = IntensityDataAcquire(PATH)
    return np.max(DATA)

def MinIntensity(PATH):
    DATA = IntensityDataAcquire(PATH)
    return np.min(DATA)

def AverageIntensityBetween(PATH,Threshold1,Threshold2):

    DATA = IntensityDataAcquire(PATH)
    counter = 0 
    Intensity_sum = 0

    for i in range(0,len(DATA)):
        if (DATA[i] <= Threshold1) and (DATA[i] >= Threshold2): 
            counter = counter +1;
            Intensity_sum = Intensity_sum + DATA[i];

    Intensity_average = Intensity_sum/counter
    return Intensity_average





def CorrelationCalc(X_x1,Y_y1):

    mean_x1 = np.mean(X_x1)
    mean_y1 = np.mean(Y_y1)

    sum11 = 0
    x_21 = 0
    y_21 = 0

    for i in range(0,len(X_x1)):
        sum11 = sum11 + (X_x1[i]-mean_x1)*(Y_y1[i] - mean_y1)
        x_21 = x_21 + (X_x1[i]-mean_x1)**2
        y_21 = y_21 + (Y_y1[i]-mean_y1)**2

    R1 = sum11/((x_21**(0.5))*(y_21**(0.5)))
    return R1




def OnOff(PATH,Threshold,exptime):

    ontime,offtime = Power_dist_one(PATH,Threshold,exptime)

    if len(ontime) == len(offtime):
        YY = ontime*exptime
        XX = offtime*exptime
    elif len(ontime) < len(offtime):
        YY = ontime*exptime
        XX = offtime[0:len(ontime)]*exptime
    else:
        YY = ontime[0:len(offtime)]*exptime
        XX = offtime*exptime
    return XX,YY

def OnOffCorrLog(PATH,Threshold,exptime):

    XX,YY = OnOff(PATH,Threshold,exptime)
    X_x_log = np.log(XX)
    Y_y_log = np.log(YY)
    R1 = CorrelationCalc(X_x_log,Y_y_log)
    return X_x_log,Y_y_log,R1

def OnOffCorr(PATH,Threshold,exptime):

    XX,YY = OnOff(PATH,Threshold,exptime)
    R1 = CorrelationCalc(XX,YY)
    return XX,YY,R1


def OnOn(PATH,Threshold,exptime):

    ontime,_ = Power_dist_one(PATH,Threshold,exptime)

    on_x = ontime[0:len(ontime):2]
    on_y = ontime[1:len(ontime):2]
    
    if (len(ontime)%2) == 0:
        YY = on_x*exptime
        XX = on_y*exptime
    else :
        YY = on_x[0:(len(on_x)-1)]*exptime
        XX = on_y*exptime
    return XX,YY

def OnOnCorrLog(PATH,Threshold,exptime):

    XX,YY = OnOn(PATH,Threshold,exptime)
    X_x_log = np.log(XX)
    Y_y_log = np.log(YY)
    R1 = CorrelationCalc(X_x_log,Y_y_log)
    return X_x_log,Y_y_log,R1

def OnOnCorr(PATH,Threshold,exptime):

    XX,YY = OnOn(PATH,Threshold,exptime)
    R1 = CorrelationCalc(XX,YY)
    return XX,YY,R1
    
def OffOff(PATH,Threshold,exptime):

    _,offtime = Power_dist_one(PATH,Threshold,exptime)

    off_x = offtime[0:len(offtime):2]
    off_y = offtime[1:len(offtime):2]


    if (len(offtime)%2) == 0:
        YY = off_x*exptime
        XX = off_y*exptime
    else :
        YY = off_x[0:(len(off_x)-1)]*exptime
        XX = off_y*exptime
    return XX,YY

def OffOffCorrLog(PATH,Threshold,exptime):

    XX,YY = OffOff(PATH,Threshold,exptime)
    X_x_log = np.log(XX)
    Y_y_log = np.log(YY)
    R1 = CorrelationCalc(X_x_log,Y_y_log)
    return X_x_log,Y_y_log,R1

def OffOffCorr(PATH,Threshold,exptime):

    XX,YY = OffOff(PATH,Threshold,exptime)
    R1 = CorrelationCalc(XX,YY)
    return XX,YY,R1



