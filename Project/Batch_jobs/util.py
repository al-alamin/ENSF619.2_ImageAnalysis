# import os
# import zipfile
# import tensorflow as tf
# from tensorflow.keras.optimizers import RMSprop
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras import layers
# from tensorflow.keras import Model
# import matplotlib.pyplot as plt
# import numpy as np
# import tensorflow_datasets as tfds
# import pathlib
# import pandas as pd
# import pickle
# import csv
# import random
# random.seed(10)

# import matplotlib.image as mpimg
# import shutil






# def load_obj(base_dir, name):
#     file_path = os.path.join(base_dir, "pickle", name + ".pkl")
#     with open(file_path, 'rb') as f:
#         return pickle.load(f)

# def save_obj(obj, base_dir, name):
#     dir_path = os.path.join(base_dir, "pickle")
#     create_directory(dir_path)
#     file_path = os.path.join(dir_path, name + ".pkl")
#     with open(file_path, 'wb') as f:
#         pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
#     print("Saved object to a file: %s" % (str(file_path)))


# def save_df(df, file_name, append=False):
#     if append:
#         df.to_csv(file_name, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC, mode="a", header=False)
#     else:
#         df.to_csv(file_name, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

# def save_df(df, base_dir, file_name):
#     file_name = os.path.join(base_dir, file_name)
#     df.to_csv(file_name, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

# def save_df(df, file_name):
#     df.to_csv(file_name, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

# def remove_directory(path):
#     if os.path.exists(path):
#         print("%s path exists and removing it." % path)
#         shutil.rmtree(path)

# def remove_file(file_name):
#     if (os.path.isfile(file_name)):
#         print("Output file %s exists and removing it." % file_name)
#         os.remove(file_name)

# def create_directory(dir):
#     if(not os.path.exists(dir)):
#         print("Creating directory %s." % dir)
#         os.makedirs(dir)
#     else:
#         print("Directory %s already exists and so returning." % dir)

# def remove_and_create_directory(dir):
#     remove_directory(dir)
#     create_directory(dir)

