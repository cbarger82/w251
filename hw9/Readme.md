Homework 9 Q&A:

1. How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)

Am training using four V100s. The training is at step 700 out of the 50,000 (7:07pm 7/25) I set in the config file and so far I am averaging about 1.7s per step, so the training should take approximately 23.6 hours. If I include the time it took to do the EVAL steps, I'd say the training will be 24 hours total. 

2. Do you think your model is fully trained? How can you tell?



3. Were you overfitting?



4. Were your GPUs fully utilized?



5. Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?

I monitored network traffic with nmon (quick screen grab in hw9 folder from ~1000th step). The network appears to be a bottle neck since the CPU util never showed them all running at 100% at any point nor were there more than maybe 1/3 of the CPUs running at once at greater than 30% util.

6. Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?



7. How big was your training set (mb)? How many training lines did it contain?



8. What are the files that a TF checkpoint is comprised of?



9. How big is your resulting model checkpoint (mb)?



10. Remember the definition of a "step". How long did an average step take?

An average step took 1.7 seconds.

11. How does that correlate with the observed network utilization between nodes?

