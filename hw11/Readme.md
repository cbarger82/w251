### Homework 11 Q&A

1. What parameters did you change?

Gamma, Learning Rate, Density First and Second Layer, Num_Epochs, epsilon_min

2. What values did you try?

Run 1 - Changed number of epochs from 1 to 3 AND lowered gamma from 0.99 to 0.75 \n
Run 2 - Lowered gamma to 0.50, density 1st layer to 8, density second layer to 4, num_epochs to 5, epsilon_min to 0.05, and learning rate to 0.0001 \n
Run 3 - Game to 0.25, num_epochs at 5, epsilon_min to 0.10, and learning rate to 0.005

3. Did you try any other changes that made things better or worse?



4. Did they improve or degrade the model? Did you have a test run with 100% of the scores above 200?



5. Based on what you observed, what conclusions can you draw about the different parameters and their values?

Between watching the model and studying the parameters, I came up with this list:
- density_first_layer = 16
- density_second_layer = 8
- num_epochs = 1
- batch_size = 64
- epsilon_min = 0.01
- gamma = The closer this value is to 1 means immediate rewards are worth more than future rewards. Inversely, the closer the value is to 0 means future rewards are worth more.
- learning_rate = The closer this value is to 1, the faster the model learns, but the slower it converges. The closer to 0, the slower it will learn, but it will steadily converge
- epsilon = 

6. What is the purpose of the epsilon value?



7. Describe "Q-Learning".

