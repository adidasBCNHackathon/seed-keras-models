import os
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard, Callback
from tensorflow.python.lib.io import file_io

import modelname.model as model


CHECKPOINT_PATH = "checkpoint.{epoch:02d}-{val_loss:.2f}.hdf5"
MODEL = "model.hdf5"


class ContinuousEval(Callback):
    """
    Continuous eval callback to evaluate the checkpoint once
    every so many epochs.
    """

    pass


def dispatch(train_files,
             eval_files,
             job_dir,
             batch_size,
             num_epochs,
             checkpoint_epochs):
    fst_model = model.build_model()

    try:
        os.makedirs(job_dir)
    except:
        pass
