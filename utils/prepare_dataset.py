import os
import subprocess


def prepare_dataset(dir: str) -> None:
    for img_fn in sorted(os.listdir(dir)):
        fn, extension = img_fn.split(".")
        if fn == "farfetchd":
            new_fn = "Farfetch'd"
        elif fn == "flabebe":
            new_fn = "Flabébé"
        elif fn == "mime-jr":
            new_fn = "Mime Jr"
        elif fn == "mr-mime":
            new_fn = "Mr. Mime"
        elif fn == "nidoran-f":
            new_fn = "Nidoran♀"
        elif fn == "nidoran-m":
            new_fn = "Nidoran♂"
        elif fn in ["kommo-o", "hakamo-o", "jangmo-o", "ho-oh"]:
            new_fn = fn.capitalize()
        elif fn.startswith("tapu") or fn == "type-null":
            new_fn = " ".join([token.capitalize() for token in fn.split("-")])
        else:
            new_fn = fn.split("-")[0].capitalize()

        os.rename(
            os.path.join(dir, img_fn),
            os.path.join(dir, f"{new_fn}.{extension}"),
        )


if __name__ == "__main__":
    DATASET_DIR = "./datasets"
    TEST_DIR = os.path.join(DATASET_DIR, "test", "images")

    prepare_dataset(dir=TEST_DIR)
