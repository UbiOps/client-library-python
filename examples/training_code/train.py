import json
import os

import tensorflow as tf
import matplotlib.pyplot as plt
import shutil


def train(training_data, parameters, context):
    # Set training parameters
    batch_size = 32
    img_height = 120
    img_width = 120
    nr_epochs = parameters["nr_epochs"]

    # Target directory
    extract_dir = "./"

    # Get the training data
    shutil.unpack_archive(training_data, extract_dir, "zip")

    # Prepare tensorflow image datasets
    data_dir = "./training-data/images"

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
    )

    class_names = train_ds.class_names
    print(f"Found the following class names: {class_names}")

    normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1.0 / 255)
    normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    image_batch, labels_batch = next(iter(normalized_ds))

    # Configure the dataset for performance
    train_ds = train_ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)

    # Train the model
    num_classes = len(class_names)

    data_augmentation = tf.keras.Sequential(
        [
            tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal", input_shape=(img_height, img_width, 3)),
            tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
        ]
    )

    model = tf.keras.Sequential(
        [
            data_augmentation,
            tf.keras.layers.experimental.preprocessing.Rescaling(1.0 / 255),
            tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(num_classes, name="outputs"),
        ]
    )

    model.compile(
        optimizer="adam",
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )

    history = model.fit(train_ds, validation_data=val_ds, epochs=nr_epochs)

    eval_res = model.evaluate(val_ds)

    acc = history.history["accuracy"]
    val_acc = history.history["val_accuracy"]

    loss = history.history["loss"]
    val_loss = history.history["val_loss"]

    epochs_range = range(nr_epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label="Training Accuracy")
    plt.plot(epochs_range, val_acc, label="Validation Accuracy")
    plt.legend(loc="lower right")
    plt.title("Training and Validation Accuracy")

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label="Training Loss")
    plt.plot(epochs_range, val_loss, label="Validation Loss")
    plt.legend(loc="upper right")
    plt.title("Training and Validation Loss")
    plt.savefig("accuracy_and_loss.png")

    # Return the trained model file and metrics
    # joblib.dump(model, 'model.pkl')
    tf.keras.models.save_model(model, "./model.h5", save_format="h5")

    fin_loss = eval_res[0]
    fin_acc = eval_res[1]
    run_id = context["id"]

    return {
        "artifact": {
            "file": "model.h5",
            "bucket": os.environ.get("SYS_DEFAULT_BUCKET", "default"),
            "bucket_file": f"model-1/trained/{run_id}/model.pkl",
        },
        "metrics": json.dumps({"loss": fin_loss, "accuracy": fin_acc}),
        "additional_output_files": [
            {
                "file": "accuracy_and_loss.png",
                "bucket": os.environ.get("SYS_DEFAULT_BUCKET", "default"),
                "bucket_file": f"model-1/trained/{run_id}/accuracy_and_loss.png",
            }
        ],
    }
