from PIL import Image
from torchvision.models import resnet50, ResNet50_Weights


CATEGORY_MAPPING = {
    1: [], # Food
    2: [], # Landscape
    3: [], # Animal
    4: [], # Portrait
    5: [] # Placeholder
}


class ImageClassifier:
    def __init__(self) -> None:
        # Initialize model with the best available weights
        self.weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=self.weights)
        self.model.eval() # set model to eval mode
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
            # find category
            category_id = 1 # for now, default to 1 Reminder: change to None
            for category, class_list in CATEGORY_MAPPING:
                if class_id in class_list:
                    category_id = category
            # For statistics purpose
            score = prediction[class_id].item()
            category_name = self.weights.meta["categories"][class_id]
            print(f"{category_name}: {100 * score:.1f}%")
            return category_id if category_id else 5
        return 5