Initialization:
- initialize the RL model
- Initialize the data store - create dictionary with all image categories and filter configs, score values 0
- Run simulation
- Update datastore with scores for each filter config per category

Simulator:
- Uniform probabilities for each category
- For the selected category, define different probabilities for each filter based on our understanding
- For the selected filter, simulate probabilities of picking a configuration

"Live" flow (after the simulation step):
- Input image fed to the image classifier that returns the parent category of the classified objects, ie if there are multiple objects in the image it returns one of the 5 predefined categories - [food, animals, portrait/human, landscapes, buildings] 
- Feed the category to the ranking model
- Return random selection of filters
- Update the data store for every user response (intial responses ~5000 will be simulated)
- 


Changing predictions based on trends:
- Periodically normalize the counts for each filter, essentially resetting the training process.

Crowdsource view vs Live view:
- [Crowd sourcing view] Cold start screen (shown to the crowd workers) has the ability to rank filters for each image - so we get more responses for each image category. The crowd worker ranks the top 4 filters, and clicks next to get to the next image.
- [Live View] The end user selects the filter they like the best, and get a download button. Every download click gives us the reward for that filter config, so that the end users also contribute to the model training.

- Think of including service design, how backend developers can use this app

Create filter bank that has:
- Filter ID
- Kernel
- Configs

Control flow sequence:
[Screen 1]
- User uploads an image - we generate a unique file path for the image
- File path fed to the classifier -> return category
- ImageFilter model takes in the file path and calls the filter bank and applies all filters to the image and saves each image -> returns a list of file paths of images with filters applied, and the filter_id, config_id
# WIP
{
    "Vivid": [
        {
            "config_id_1": "image_path.jpg",
            "config_id_2": "image_path.jpg",
            "config_id_3": "image_path.jpg",
        }
    ]
}

- Category -> RankingModel -> Ranked sequence of all filters and configs
- Rankings for filters/configs + image paths of filtered images -> Controller -> returns ranked list of filtered images
[Screen 2]
- Required to display the screen:

{
    "filePath": "original_image_path.jpg", 
    "filters": [
        {"Vivid": [
            {"config_id": "modified_image_path.jpg"},
            {"config_id": "modified_image_path.jpg"},
            {"config_id": "modified_image_path.jpg"}
        ]},
        {"Monochrome": [
            {"config_id": "modified_image_path.jpg"},
            {"config_id": "modified_image_path.jpg"},
            {"config_id": "modified_image_path.jpg"}
        ]}
        ]
}

- User clicks on an image -> Open overaly with the expanded image and a download button
- User clicks download -> API call to the controller {category, filter_id, config_id}
- Controller passes this to the model -> Update the datastore
[Screen 3]
- Option to upload another image

Data Schema:

{
    'picture_category_1': {
        "Vivid": [{"config_1": score}, {"config_2": score}],
        "filter_2": [{"config_1": score}, {"config_2": score}]
    },
    'picture_category_2': {
        "filter_1": [{"config_1": score}, {"config_2": score}],
        "filter_2": [{"config_1": score}, {"config_2": score}]
    }
}
