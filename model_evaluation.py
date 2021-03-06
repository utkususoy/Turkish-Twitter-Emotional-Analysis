# -*- coding: utf-8 -*-
"""model_evaluation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vv1jhjUBZH182Xt6cWa6E-MLg2dESNyt
"""

#Model Evaluation
import string
import re
from keras.models import load_model

# load the model
model = load_model('/content/modelv9.h5')
# evaluate model on training dataset
_, acc = model.evaluate(Xtrain, ytrain, verbose=0)
print('Train Accuracy: %.2f' % (acc*100))
# evaluate model on test dataset

_, acc = model.evaluate(Xtest, ytest, verbose=0)
print('Test Accuracy: %.2f' % (acc*100))