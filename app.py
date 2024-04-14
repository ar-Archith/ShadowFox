import os
import tensorflow as tf
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Load the ResNet50 model
model = tf.keras.applications.ResNet50(weights='imagenet')

def predict_class(image_path):
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f'Error opening image file: {e}')
        return None

    try:
        img_array = np.array(img.resize((224, 224)))
        img_batch = np.expand_dims(img_array, axis=0)
        img_batch /= 255.
        logits = model.predict(img_batch)
        probabilities = tf.nn.softmax(logits)
        predicted_class = np.argmax(probabilities.numpy())
        return predicted_class, probabilities.numpy()
    except Exception as e:
        print(f'Error predicting class: {e}')
        return None

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        predicted_class, probabilities = predict_class(file_path)
        if predicted_class is not None:
            result_label.config(text=f'Predicted class: {predicted_class}\nProbabilities: {probabilities}')

root = tk.Tk()
root.title('Image Classifier')
root.geometry('400x200')

style = ttk.Style()
style.theme_use('clam')

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky='nsew')

browse_button = ttk.Button(frame, text='Browse file', command=browse_file)
browse_button.grid(row=0, column=0, padx=10, pady=10)

result_label = ttk.Label(frame, text='')
result_label.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()