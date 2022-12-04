FILTER_NAMES = {
    1: "Vivid",
    2: "Monochrome",
    3: "Dramatic",
    4: "Vignette"
}

CATEGORIES = {
    1: "Food",
    2: "Landscape",
    3: "Animal",
    4: "Portrait",
    5: "Placeholder"
}

FILTER_CONFIGS = {
    1: [(1,1,3,4,5), (1,2,3,4,5), (1,3,3,4,5), (1,4,3,4,5)],
    2: [(2,1,3,4,5), (2,2,3,4,5), (2,3,3,4,5), (1,4,3,4,5)],
    3: [(3,1,3,4,5), (3,2,3,4,5), (3,3,3,4,5), (1,4,3,4,5)],
    4: [(4,1,3,4,5), (4,2,3,4,5), (4,3,3,4,5), (1,4,3,4,5)]
}

_FILTERS = {
    1: [
        {
            "brightness": 0.0,
            "exposure": 0.5,
            "contrast": -0.1,
            "warmth": 0.0,
            "saturation": 0.5,
            "vibrance": 0.2,
            "hue": 0.0,
            "gamma": 1.3,
        },
        {
            "brightness": 0.0,
            "exposure": 0.5,
            "contrast": 0.1,
            "warmth": 0.0,
            "saturation": 0.3,
            "vibrance": 0.6,
            "hue": 0.0,
            "gamma": 1.3,
        },
        {
            "brightness": 0.0,
            "exposure": 0.2,
            "contrast": -0.1,
            "warmth": 0.6,
            "saturation": 0.3,
            "vibrance": 0.5,
            "hue": 0.0,
            "gamma": 1.3,
        }
    ],
    2: [
        {
            "brightness": 0.0,
            "exposure": 0.0,
            "contrast": -0.2,
            "warmth": 0.0,
            "saturation": -1.0,
            "vibrance": 0.0,
            "hue": 0.0,
            "gamma": 1.3,
        },
        {
            "brightness": 0.0,
            "exposure": 0.0,
            "contrast": 0.1,
            "warmth": 0.0,
            "saturation": -1.0,
            "vibrance": 0.0,
            "hue": 0.0,
            "gamma": 1.3,
        },
        {
            "brightness": -0.1,
            "exposure": 0.9,
            "contrast": 0.0,
            "warmth": 0.0,
            "saturation": -1.0,
            "vibrance": -0.5,
            "hue": 0.0,
            "gamma": 1.3,
        }
    ],
    3: [

        {
            "brightness": -0.1,
            "exposure": 0.0,
            "contrast": 0.0,
            "warmth": 0.6,
            "saturation": -0.4,
            "vibrance": -0.5,
            "hue": 0.0,
            "gamma": 1.3,
        },
        {
            "brightness": -0.1,
            "exposure": 0.4,
            "contrast": 0.2,
            "warmth": 0.4,
            "saturation": -0.4,
            "vibrance": -0.5,
            "hue": 0.03,
            "gamma": 1.3,
        },
        {
            "brightness": -0.1,
            "exposure": 0.4,
            "contrast": 0.1,
            "warmth": 0.6,
            "saturation": -0.2,
            "vibrance": -0.8,
            "hue": 0.02,
            "gamma": 1.3,
        }
    ],
    4: [
        {"size": 150, "brightness": 0.1, "contrast": 0.2},
        {"size": 200, "brightness": 0.2, "contrast": 0.4},
        {"size": 300, "brightness": 0.4, "contrast": 0.8}
    ]
}
