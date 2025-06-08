---
id: Nyquist Sampling Theorem
aliases: []
tags: []
Created: "15-08-2024"
cssclasses:
  - wide-page
---

# Nyquist Sampling Theorem

A signal which is a band limited to $w$_Hz_(the highest frequency component of the signal is $wHz$) can be completely recovered if it's sampled in the sampling interval $1 \over 2w$

$$
f_s = 2 \omega
$$

### Examples

1. Fs = F

![Fs_is_equal_f.png](assets/imgs/Fs_is_equal_f.png)

2. Fs = 1.2F

![Fs_is_1_2_f.png](assets/imgs/Fs_is_1_2_f.png)

3. Fs = 1.5f
   ![Fs_is_1_5f.png](assets/imgs/Fs_is_1_5f.png)

4. Fs = 2f

![Fs_is_2_f.png](assets/imgs/Fs_is_2_f.png)

</br>

---

## Aliasing 
When the sampling rate is less than the bandwidth the original information can no longer recover from the sampled signal and it is forever lost and it is due to aliasing

### Methods used to avoid aliasing
1. Anti aliasing Filters 
2. Oversampling 
3. 