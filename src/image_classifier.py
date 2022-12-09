from PIL import Image
from torchvision.models import resnet50, ResNet50_Weights
import os

CATEGORY_MAPPING = {
    1: [],  # Food
    2: [979],  # Landscape
    3: [208],  # Animal
    4: [],  # Portrait
    5: []  # Placeholder
}


class ImageClassifier:
    def __init__(self) -> None:
        # Initialize model with the best available weights
        self.weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=self.weights)
        self.model.eval()  # set model to eval mode
        # Initialize the inference transforms
        self.preprocess = self.weights.transforms()

    def classify_image(self, path=None):
        # Reads a file using pillow
        if path:
            img = Image.open(path)
            # Apply inference preprocessing transforms
            batch = self.preprocess(img).unsqueeze(0)
            # Use the model and print the predicted category
            prediction = self.model(batch).squeeze(0).softmax(0)
            class_id = prediction.argmax().item()
            # print(class_id)
            # find category
            category_id = None
            for category, class_list in CATEGORY_MAPPING.items():
                if class_id in class_list:
                    category_id = category
            # For statistics purpose
            score = prediction[class_id].item()
            category_name = self.weights.meta["categories"][class_id]
            print(f"{category_name}: {100 * score:.1f}%")
            return category_id if category_id else 5
        return 5


if __name__ == "__main__":
    app_dir = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(app_dir, 'static/uploaded/')
    file = 'landscape.jpg'
    location = target + file

    print(location)

    image_classifier = ImageClassifier()
    category_id = image_classifier.classify_image(path=location)
    print(category_id)
