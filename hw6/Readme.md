Had issues with CUDA runtime errors and also with the transformers class - when I load the model per the hugging instructions:

Let's load our model
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

And then look at the data, I only show 1 tensor, not the expected 12. 
