
## <center>TD1 Bilan de puissance en 2G

### 1. Niveau de reception GSM-DCS

1) FL(622)=1710.2 + 0.2 * (622-512) =  1732.2 Mhz  MS -> BTS  
FU(622)=1732.2 + 95 = 1827.2 BTS -> MS

2)  $P_2= 31.6 pW$ \
$P_r=10 ^ {\frac{-75}{10}}mW$\
$3.13\times 10^{-8}mW$

3) $P=U\times i= \frac{U²}{R}$ 0\
$U=\sqrt{P \times R}$ \
$=\sqrt{31.6\times 10{-8} \times100}$\
$\equiv 56.2  \mu V$

4) BTS classe M1
colone DCS


5) $P_R=P_E+G_E+G_R-(Pertes affaiblissments)$ \
$A= 32 + 17 + 0 - (-75)=124 dB$

6) ![](./img/IMG_0558.jpg)

$A = 40 \log d - 20 \log(20 * 1.7) + 20 + \frac{1827.2}{40} + 0.18 * \frac{1827.2}{40} + 0.18 * \frac{80}{100} - 0.34(20 - 1.7)$  \
$40 \log d = 124 - 28.972$  \
$d =10^\frac{95.028}{40}=237.5 m$

7) $d_2=837.5m$ \
$P_{R_2}=32+17+0-(40\log (d_2+28.972)$
$P_{R_2}= -96.89 dBm$

8) -96 > -102 => ok

9) ![alt text](img/reponse-question-9.jpg)