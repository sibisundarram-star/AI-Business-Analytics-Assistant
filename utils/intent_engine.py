def detect_intent(question):

    question = question.lower()

    intents = {

        "summary": [
            "summary",
            "summarize",
            "overview",
            "describe",
            "about dataset",
            "dataset"
        ],

        "trend": [
            "trend",
            "increase",
            "decrease",
            "growth",
            "over time"
        ],

        "comparison": [
            "compare",
            "highest",
            "lowest",
            "best",
            "worst",
            "top"
        ],

        "statistics": [
            "average",
            "mean",
            "median",
            "count",
            "rows",
            "columns",
            "missing",
            "duplicate"
        ],

        "prediction": [
            "forecast",
            "predict",
            "future"
        ],

        "correlation": [
            "correlation",
            "relationship"
        ],

        "outlier": [
            "outlier",
            "anomaly",
            "unusual"
        ],

        "machine_learning": [
            "machine learning",
            "classification",
            "regression",
            "clustering"
        ]
    }

    for intent, words in intents.items():

        if any(word in question for word in words):
            return intent

    return "general"