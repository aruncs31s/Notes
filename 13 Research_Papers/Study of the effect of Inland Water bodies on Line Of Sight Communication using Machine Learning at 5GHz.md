---
aliases:
  - ansy miss paper
---

# Study of the effect of Inland Water bodies on Line Of Sight Communication using Machine Learning at 5GHz

**Abstract:** This paper studied the the effect of inland water bodies on 5GHz Communication and Modeled a Line Of Sight(LOS) communication channel over inland water bodies using **[[Machine Learning]]**, and shows that the attenuation of signal **during day** and less attenuation during **night**
#summary
- More attenuation during day
- Less attenuation during night
- uses Machine Learning 
- water bodies effect communication 

## Introduction 
The propagation model of wireless communication is characterized by 
- **Path loss**
- **Multipath Fading**[^2]: Happens when the channel between the transmitter and the receiver changes.
- **The dopplar spread**[^1]
Other parameters that are part of antenna modeling 
- Antenna height 
- Antenna beam width 
- Polarization
- Mutual Coupling between multiple antennas

###### Path loss 
The path loss betwen transmitter and receiver determines the attenuation which includes 
- Absorption 
- Diffraction[^3]
- scattering 
- Reflection
- And refraction

At low **SNR** the **BER** performance is increaased. 

## Prediction Model 
Random Forrest 
- The Channel State Information(CSI) of each multipath componet can be estimated from the **Expectation Maximization Algorithm(EM)** 
- Uses the `Supervised Learning` algorithm to train the model using the **CSI** data 
- According to [[Air-to-Air Path Loss Prediction Based on Machine Learning Methods in Urban Environments|This paper]] The best model for channel modeling are **KNN** and **Random Forest**

### Random Forrest 
[Source](https://www.simplilearn.com/tutorials/machine-learning-tutorial/random-forest-algorithm)
It is a subdivision of supervised learning method.
- It is a collection of decision trees 
- The higher the number of trees the better the prediction accuracy.

#working
![](https://www.simplilearn.com/ice9/free_resources_article_thumb/Working_of_RF_1.png)
[Image Source](https://www.simplilearn.com/ice9/free_resources_article_thumb/Working_of_RF_1.png)

#advantages 
- Lees training time 
- Better prediction accuracy 

#### Steps 
- Select random samples from a given data or training 
- This algorithm will construct a decision tree for every training data
- Voting will take place by averaging the decision tree. 
- Select the most voted prediction result as the final prediction result. 

[^1]: Doppler spread refers to **the widening of the spectrum of a narrow-band signal transmitted through a multipath propagation channel**
[^2]: Multipath Fading: **the phenomenon of fluctuations in signal strength formed by incoherent combination of signals coming from different directions through reflection or scattering with the direct signal**.
[^3]: Diffraction: **the bending of waves around obstacles and the spreading of waves by openings**. It happens when the size of the object and the wavelength of the signal are comparable.
```python
def diffreaction(wavelength, size):
    return 1.22 * wavelength / size
```

## Measurement Setup
- used [[Ubiquity Powebeam M5]] for measuring the **CSI**

## References 
14. [[Air-to-Air Path Loss Prediction Based on Machine Learning Methods in Urban Environments]]
15. 