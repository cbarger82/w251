### Homework 11 Q&A

1. What parameters did you change?

Gamma, Learning Rate, Density First and Second Layer, Num_Epochs, epsilon_min

2. What values did you try?

- Run 1 - Changed number of epochs from 1 to 3 AND lowered gamma from 0.99 to 0.75  
- Run 2 - Lowered gamma to 0.50, density 1st layer to 8, density second layer to 4, num_epochs to 5, epsilon_min to 0.05, and learning rate to 0.0001
- Run 3 - Game to 0.25, num_epochs at 5, epsilon_min to 0.10, and learning rate to 0.005

3. Did you try any other changes that made things better or worse?

Only changed what I mentioned above. The second run seemed to do the best. There was one initial run where I changed the batch size to 128, but the results were no better than any of the other changes that I made. Since Run 2 did the best (though it still wasn't great), I would think perhaps either the learning rate or the density layer changes had the most positive impact. All the other changes that I made in that and during the other two runs seemed to make things worse and I ended up killing the model during the other iterations.

4. Did they improve or degrade the model? Did you have a test run with 100% of the scores above 200?

The only run that hit the 200 score was Run 2 and it took 890 trials I believe to hit the 200 score. None of my runs were excellent 100% of the time. 

5. Based on what you observed, what conclusions can you draw about the different parameters and their values?

Between watching the model and studying the parameters, I came up with this list:
- gamma = The closer this value is to 1 means value is added to future rewards. Inversely, the closer the value is to 0 means immediate rewards are givem a higher value. 
- learning_rate = The closer this value is to 1, the faster the model learns, but the slower it converges. The closer to 0, the slower it will learn, but it will steadily converge
- epsilon = this value, which was always set to 1, represents the maximum reward that is attainable in the state following the current one.
- epsilon_min = I believe that this is similar to the epsilon value. If we have this set to 0.1, then it would mean that the minimum reward attainable would be 10%.

6. What is the purpose of the epsilon value?

As stated above, the epsilon value represents the amximum reward that is attainable in the state following the current one.

7. Describe "Q-Learning".

Q-learning is a type of reinforcement learning that "learns as we take each action but instead searches through the possible subsequent actions to learn faster". (source: https://towardsdatascience.com/reinforcement-learning-from-scratch-simple-application-and-evaluating-parameters-in-detail-2dcee3de008c)
