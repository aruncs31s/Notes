---
aliases: 
Date: 03-03-25
---
# Modulations

## QPSK

### Tut


> [!multi-column]
>
>> [!blank]+ Block
>> ![](https://wiki.gnuradio.org/images/b/bd/Qpsk_rrc_rolloff_fg.png)
>
>> [!blank]+ output
>> ![](https://wiki.gnuradio.org/images/a/ad/Qpsk_rrc_rolloff_output.png)
- The excess bandwidth is taken as 0.35

#### Matched Filters and ISI

```mermaid
graph LR
rand_source --> Const_mod --> out 
```
- This introduces the `ISI` 
-  But when we convolve two ==RRC filters together, we get a raised cosine filter== (which is a form of a Nyquist filter).
> [!multi-column]
>
>> [!blank]+ Block
>> ![](https://wiki.gnuradio.org/images/8/89/Qpsk_stage1_fg.png)
>
>> [!blank]+ output
>> ![](https://wiki.gnuradio.org/images/5/5d/Qpsk_stage1_out.png)

#### Channel Impairments


> [!multi-column]
>
>> [!blank]+ Block
>> ![](https://wiki.gnuradio.org/images/4/40/Qpsk_stage2_fg.png)
>
>> [!blank]+ output
>> ![](https://wiki.gnuradio.org/images/f/fe/Qpsk_stage2_out.png)




### Polyphase Clock Sync
1.  performs the clock recovery.
2.  it provides the receiver matched filter to remove the ISI
3. down-samples the signal (reduces the samples per symbol)

> [!multi-column]
>
>> [!blank]+ Block
>> ![](https://wiki.gnuradio.org/images/thumb/7/70/Qpsk_stage3_fg.png/1200px-Qpsk_stage3_fg.png)
>
>> [!blank]+ output
>> ![](https://wiki.gnuradio.org/images/thumb/9/99/Qpsk_stage3_out.png/1200px-Qpsk_stage3_out.png)




#### Phase and Frequency Correction
- reduced using costas loop


## BPSK


![](https://wiki.gnuradio.org/images/thumb/2/2f/Bpsk_stage6_fg.png/1200px-Bpsk_stage6_fg.png)

![](https://wiki.gnuradio.org/images/thumb/7/72/Qpsk_stage6_ss_fg.png/1200px-Qpsk_stage6_ss_fg.png)