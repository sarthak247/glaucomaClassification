# Import Libraries
from PIL import Image
import numpy as np
from keras.models import load_model
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # Shut Up Tensorflow!!!
# tf.logging.set_verbosity(tf.logging.ERROR)
model = load_model('models/model.h5') # Replace model.h5 with saved model and it's weights


# Predict Glaucoma Function
def predictGlaucoma(imagePath):
    image = Image.open(imagePath) # Load Image
    image = image.resize((224, 224)) # Resize according to model input dimensions
    image = np.array(image) # Convert to NP Array
    image = image/255.0 # Normalize Image
    prediction = np.round(model.predict(np.array([image]))) # Predciton
    return 'Normal' if prediction == 0 else 'Glaucoma' # Return output to driver function
