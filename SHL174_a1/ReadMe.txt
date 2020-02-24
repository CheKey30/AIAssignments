ReadMe
Shuche Liu(shl174@pitt.edu)

How to run this project:
please put the "assign1_sentences.txt" into the "data" folder then run the "Assignment1Main.py"

Environment:
I use python 3.6 to do this project

**************************running result with lambda=0.7**********************************
The probability of "Water" appearing after "<s>" is 0.0004
The probability of "<s>" appearing after "Water" is 0.0
The probability of "economy" appearing after "planned" is 0.046511627906976744
The probability of "</s>" appearing after "." is 1.0
-1.4254510763210846	<s> The
-1.6863989535702288	<s> Israel and Jordan signed the peace process
-2.4119032839544814	<s> It is expected
-0.8774680645546007	<s> The
-0.39336646514354306	<s> Israel and Jordan signed the peace process
-0.8488428781582585	<s> It is expected to

***********************running result with lambda=3**************************************
The probability of "Water" appearing after "<s>" is 0.0004
The probability of "<s>" appearing after "Water" is 0.0
The probability of "economy" appearing after "planned" is 0.046511627906976744
The probability of "</s>" appearing after "." is 1.0
-1.4254510763210846	<s> The
-1.6863989535702288	<s> Israel and Jordan signed the peace process
-2.4119032839544814	<s> It is expected
-0.00422703191998465	<s> He said that he said that he said that he said that he said that he added . </s>
-0.002954910279033736	<s> Israel and Jordan signed the peace process . </s>
-0.00679857221971202	<s> It is expected to the past few years , the two countries . </s>


************************running result with lambda=4**************************************
The probability of "Water" appearing after "<s>" is 0.0004
The probability of "<s>" appearing after "Water" is 0.0
The probability of "economy" appearing after "planned" is 0.046511627906976744
The probability of "</s>" appearing after "." is 1.0
-1.4254510763210846	<s> The
-1.6863989535702288	<s> Israel and Jordan signed the peace process
-2.4119032839544814	<s> It is expected
-0.00023437515382367747	<s> Secretary General Tun Kyi said that the United States , he said that he said that he said that
-0.0002954910279033736	<s> Israel and Jordan signed the peace process . </s>
-0.0004604502726738305	<s> It is expected to the past five years , the two countries . </s>


*************************running result with lambda=5*********************************
The probability of "Water" appearing after "<s>" is 0.0004
The probability of "<s>" appearing after "Water" is 0.0
The probability of "economy" appearing after "planned" is 0.046511627906976744
The probability of "</s>" appearing after "." is 1.0
-1.4254510763210846	<s> The
-1.6863989535702288	<s> Israel and Jordan signed the peace process
-2.4119032839544814	<s> It is expected
-1.0694558713771062e-05	<s> Secretary of State Warren Christopher came as well as well as well as well as well as well as
-6.152634909416356e-07	<s> Israel and Jordan signed the peace process of the United States , the United States , he said that the United States , he said that the United States , the United States , the United States . </s>
-3.1048268053714884e-05	<s> It is expected to the past few years ago , the country . </s>


*****************************running result with lambda = 10*****************************
The probability of "Water" appearing after "<s>" is 0.0004
The probability of "<s>" appearing after "Water" is 0.0
The probability of "economy" appearing after "planned" is 0.046511627906976744
The probability of "</s>" appearing after "." is 1.0
-1.4254510763210846	<s> The
-1.6863989535702288	<s> Israel and Jordan signed the peace process
-2.4119032839544814	<s> It is expected
-3.342049598053457e-12	<s> Secretary of State Warren Christopher came as well as well as well as well as well as well as
-4.340667955161982e-15	<s> Israel and Jordan signed the peace process as well as well as well as well as well as well as well as well as well as well as well as well as well as well as well . </s>
-4.218826172859362e-11	<s> It is expected to the past few years ago , which is expected to

discussion of the running result:
Based on the score function, we can tell that, with a really small or zero lambda, the score of a short sentence would be higher than the score of long sentence. 
That is why with lambda =0, the best sentences just add one word after the pre-word. 
With the increase of lambda, the long sentence would get a higher score than the short one. That is why the best sentences are getting longer and longer In my tests.
However, if lambda is too large, the best sentence would repeate several words again and again. 
So, lambda is imporant to generate a sutible sentence. According my experience, 3 is a good value in this case.
