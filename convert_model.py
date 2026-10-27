import tensorflow as tf
import os

# Chargement du modèle sur votre machine
model = tf.keras.models.load_model("model/model.keras")

# Sauvegarde au format 
model.save("model/model.h5")
print("Modèle converti avec succès en model.h5 !")