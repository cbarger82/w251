Homework 9 Q&A:

1. How long does take to complete the training run? (hint: this session is on distributed training, so it will take a while)

I am training using four V100s. I am averaging about 1.7 seconds per training step and have set the number of steps to complete at 50,000. The total time based on the tensorboard graphs shows that training took 23 hours and 42 minutes. Final training output from nohup file:
***     Validation loss: 1.5905
***     Eval BLUE score: 0.3685
*** Finished training
*** Avg time per step: 1.710s
*** Avg objects per second: 36500.865

2. Do you think your model is fully trained? How can you tell?

I do not believe the model is fully trained. Looking at the graphs for the learning rate, eval_loss, and BLEU_Score, the values appear to be decreasing and increasing respectively. I believe the model would be fully trained if I let it run for more than 50,000 steps, though not 100% sure how many steps to give the model the best output. 

3. Were you overfitting?

I do not believe we are overfitting. Based on the training loss graph, we see a downward sloping curve which then becomes fairly flat. If the data were being overfitted, I would think the values for training loss would be closer to zero. We also trained on a very large dataset; when using a large dataset, we can often better train as the model can pick up on more anomolies. 

4. Were your GPUs fully utilized?

Yes, all four of my GPUs were consistently hitting 100% util. See the file called nvidia_smi_4v100gpus.jpeg for a capture taken during training.

5. Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?

I monitored network traffic with nmon (quick screen grab in hw9 folder from ~1000th step). The network appears to be a bottle neck since the CPU util never showed them all running at 100% at any point nor were there more than maybe 1/3 of the CPUs running at once at greater than 30% util. My port speed was upgraded to 1000Mbps to give best shot for quicker training times. 

6. Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?

Some googling revealed this: https://nvidia.github.io/OpenSeq2Seq/html/_modules/optimizers/lr_policies.html_ which shows that the learning rate uses the transformer policy. Also called the "noam" learning rate decay scheme. Based on the paper by Google Brains (https://arxiv.org/pdf/1706.03762.pdf), the learning rate is determined/varied by this formula:
lrate = d (−0.5 -- model) · min(step_num^−0.5, step_num · warmup_steps^−1.5)
The paper also states that the above formula "corresponds to increasing the learning rate linearly for the first warmup_steps training steps, and decreasing it thereafter proportionally to the inverse square root of the step number.

7. How big was your training set (mb)? How many training lines did it contain?

I did not catch the size before I shut down the vm. Looking through the nohup.out file shows that we are using an english and german dictionary each with 32k words. Also saw that there are 60880896 total trainable parameters, but struggling to find size of training file.  

8. What are the files that a TF checkpoint is comprised of?

A TF checkpoint, which is a way to save a model's parameters, are not files stored on a disk, but prefixes for an index file and one or more data files which contain the variable values. From the tensorflow guide site, the prefixes are grouped together in a single checkpoint file where the CheckpointManager saves its state. (info from here: https://www.tensorflow.org/guide/checkpoint)

9. How big is your resulting model checkpoint (mb)?

Not sure... unable to locate in nohup file. 

10. Remember the definition of a "step". How long did an average step take?

An average step took 1.7 seconds.

11. How does that correlate with the observed network utilization between nodes?

Since the network was set to the 1000Mbps port size and the GPUs were all pegging at 100%, and based on what others reported, I would say that the value correlated well to the values that were set up for the network/v100s.
