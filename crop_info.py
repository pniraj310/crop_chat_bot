crop_details= {
    "Rice": {
        "season": "Kharif (June–October)",
        "states": "West Bengal, Uttar Pradesh, Punjab, Andhra Pradesh, Tamil Nadu"
    },
    "Maize": {
        "season": "Kharif",
        "states": "Karnataka, Andhra Pradesh, Madhya Pradesh"
    },
    "Millets": {
        "season": "Kharif",
        "states": "Rajasthan, Maharashtra, Karnataka"
    },
    "Cotton": {
        "season": "Kharif",
        "states": "Gujarat, Maharashtra, Andhra Pradesh, Telangana, Haryana"
    },
    "Sugarcane": {
        "season": "Kharif",
        "states": "Maharashtra, Karnataka, Tamil Nadu, Andhra Pradesh, Gujarat, Bihar, Haryana, Punjab"
    },
    "Pulses": {
        "season": "Kharif",
        "states": "Madhya Pradesh, Maharashtra"
    },
    "Wheat": {
        "season": "Rabi (October–April)",
        "states": "Uttar Pradesh, Punjab, Haryana, Madhya Pradesh, Rajasthan, Bihar, Gujarat"
    },
    "Barley": {
        "season": "Rabi",
        "states": "Rajasthan, Uttar Pradesh, Madhya Pradesh"
    },
    "Mustard": {
        "season": "Rabi",
        "states": "Rajasthan, Uttar Pradesh, Haryana"
    },
    "Gram (Chana)": {
        "season": "Rabi",
        "states": "Madhya Pradesh, Maharashtra, Rajasthan"
    },
    "Watermelon": {
        "season": "Zaid (March–June)",
        "states": "Various states during summer"
    },
    "Muskmelon": {
        "season": "Zaid",
        "states": "Various states"
    },
    "Cucumber": {
        "season": "Zaid",
        "states": "Regions with summer conditions"
    },
    "Tea": {
        "season": "Cash Crop",
        "states": "Assam, West Bengal, Tamil Nadu, Kerala"
    },
    "Coffee": {
        "season": "Cash Crop",
        "states": "Karnataka, Kerala, Tamil Nadu"
    },
    "Jute": {
        "season": "Cash Crop",
        "states": "West Bengal, Assam, Bihar"
    },
    "Oilseeds": {
        "season": "Cash Crop",
        "states": "Gujarat, Maharashtra, Madhya Pradesh"
    },
    "Potato": {
        "season": "Horticultural Crop",
        "states": "Uttar Pradesh, West Bengal"
    },
    "Onion": {
        "season": "Horticultural Crop",
        "states": "Maharashtra, Karnataka"
    },
    "Tomato": {
        "season": "Horticultural Crop",
        "states": "Andhra Pradesh, Madhya Pradesh"
    },
}
state_based_crops = {
    "West Bengal": ["Rice", "Jute", "Potato"],
    "Uttar Pradesh": ["Wheat", "Sugarcane", "Rice"],
    "Maharashtra": ["Cotton", "Sugarcane", "Onion"],
    "Madhya Pradesh": ["Wheat", "Soybean", "Pulses"],
    "Punjab": ["Rice", "Wheat", "Sugarcane"],
    "Haryana": ["Wheat", "Cotton", "Mustard"],
    "Rajasthan": ["Wheat", "Barley", "Mustard"],
    "Karnataka": ["Maize", "Coffee", "Soybean"],
    "Gujarat": ["Cotton", "Groundnut", "Sugarcane"],
    "Tamil Nadu": ["Rice", "Sugarcane", "Cotton"],
    # Add more states as needed
}
season_based_crops = {
    "Kharif": {
        "Rice": "West Bengal, Uttar Pradesh, Punjab, Andhra Pradesh, Tamil Nadu",
        "Maize": "Karnataka, Andhra Pradesh, Madhya Pradesh",
        "Millets (Bajra, Jowar, Ragi)": "Rajasthan, Maharashtra, Karnataka",
        "Cotton": "Gujarat, Maharashtra, Andhra Pradesh, Telangana, Haryana",
        "Sugarcane": "Maharashtra, Karnataka, Tamil Nadu, Andhra Pradesh, Gujarat, Bihar, Haryana, Punjab",
        "Pulses (Moong, Urad)": "Madhya Pradesh, Maharashtra"
    },
    "Rabi": {
        "Wheat": "Uttar Pradesh, Punjab, Haryana, Madhya Pradesh, Rajasthan, Bihar, Gujarat",
        "Barley": "Rajasthan, Uttar Pradesh, Madhya Pradesh",
        "Mustard": "Rajasthan, Uttar Pradesh, Haryana",
        "Gram (Chana)": "Madhya Pradesh, Maharashtra, Rajasthan"
    },
    "Zaid": {
        "Watermelon": "Various states during summer",
        "Muskmelon": "Various states during summer",
        "Cucumber": "Regions with summer conditions",
        "Vegetables": "Quick-growing veggies planted in summer"
    },
    "Cash Crops": {
        "Tea": "Assam, West Bengal, Tamil Nadu, Kerala",
        "Coffee": "Karnataka, Kerala, Tamil Nadu",
        "Jute": "West Bengal, Assam, Bihar",
        "Oilseeds (Groundnut, Soybean, Sunflower)": "Gujarat, Maharashtra, Madhya Pradesh"
    }
}
state_season_crop_map = {
    "Maharashtra": {
        "Kharif": ["Millets (Bajra, Jowar, Ragi)", "Cotton", "Sugarcane", "Pulses (Moong, Urad)"],
        "Rabi": ["Gram (Chana)"],
        "Zaid": ["Watermelon", "Muskmelon", "Vegetables"],
        "Cash Crops": ["Oilseeds (Groundnut, Soybean, Sunflower)"]
    },
    "Uttar Pradesh": {
        "Kharif": ["Rice"],
        "Rabi": ["Wheat", "Barley", "Mustard"],
        "Zaid": ["Vegetables"],
        "Cash Crops": []
    },
    "Madhya Pradesh": {
        "Kharif": ["Maize"],
        "Rabi": ["Wheat", "Barley", "Gram (Chana)"],
        "Zaid": ["Vegetables"],
        "Cash Crops": ["Oilseeds (Soybean)"]
    },
    "Punjab": {
        "Kharif": ["Rice", "Cotton"],
        "Rabi": ["Wheat"],
        "Zaid": [],
        "Cash Crops": []
    },
    "Haryana": {
        "Kharif": ["Cotton", "Rice", "Sugarcane"],
        "Rabi": ["Wheat", "Mustard"],
        "Zaid": [],
        "Cash Crops": []
    },
    "Rajasthan": {
        "Kharif": ["Millets", "Cotton"],
        "Rabi": ["Barley", "Mustard", "Gram (Chana)"],
        "Zaid": [],
        "Cash Crops": []
    },
    "Andhra Pradesh": {
        "Kharif": ["Rice", "Maize", "Cotton", "Sugarcane"],
        "Rabi": [],
        "Zaid": ["Vegetables"],
        "Cash Crops": ["Oilseeds"]
    },
    "Karnataka": {
        "Kharif": ["Maize", "Millets", "Sugarcane"],
        "Rabi": [],
        "Zaid": ["Vegetables"],
        "Cash Crops": ["Coffee", "Oilseeds"]
    },
    "Tamil Nadu": {
        "Kharif": ["Rice", "Sugarcane"],
        "Rabi": [],
        "Zaid": ["Watermelon", "Vegetables"],
        "Cash Crops": ["Tea", "Coffee"]
    },
    "Gujarat": {
        "Kharif": ["Cotton", "Groundnut"],
        "Rabi": [],
        "Zaid": [],
        "Cash Crops": ["Oilseeds", "Sugarcane"]
    },
    "West Bengal": {
        "Kharif": ["Rice", "Jute"],
        "Rabi": [],
        "Zaid": ["Vegetables"],
        "Cash Crops": []
    },
    "Bihar": {
        "Kharif": ["Sugarcane"],
        "Rabi": ["Wheat"],
        "Zaid": ["Vegetables"],
        "Cash Crops": []
    },
    "Assam": {
        "Kharif": ["Rice", "Jute"],
        "Rabi": [],
        "Zaid": [],
        "Cash Crops": ["Tea"]
    },
    "Kerala": {
        "Kharif": [],
        "Rabi": [],
        "Zaid": [],
        "Cash Crops": ["Tea", "Coffee"]
    },
    "Himachal Pradesh": {
        "Kharif": [],
        "Rabi": [],
        "Zaid": [],
        "Cash Crops": ["Apple"]
    },
    "Jammu & Kashmir": {
        "Kharif": [],
        "Rabi": [],
        "Zaid": [],
        "Cash Crops": ["Apple"]
    }
}
# yield_ranges.py

crop_yield_ranges = {
    "Rice": {"good": 3.5, "average": 2.0},     # tons/acre
    "Wheat": {"good": 3.2, "average": 1.8},
    "Maize": {"good": 3.0, "average": 1.7},
    "Cotton": {"good": 1.8, "average": 1.0},
    "Sugarcane": {"good": 40.0, "average": 25.0},
    "Soybean": {"good": 2.5, "average": 1.2},
    "Barley": {"good": 2.8, "average": 1.5},
    "Mustard": {"good": 1.8, "average": 1.0},
    "Gram": {"good": 1.6, "average": 0.8},
    # Add more crops as needed
}



