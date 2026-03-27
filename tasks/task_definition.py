TASKS = {

    "easy": {
        "code": """
            def divide(a, b):
                return a / b
            """,
        "expected": {
            "issues": ["division by zero"],
            "severity": "medium",
            "fix_keywords": ["check", "zero", "if"],
            "concepts": ["runtime error"]
        }
    },

    "medium": {
        "code": """
            def get_user(id):
                query = "SELECT * FROM users WHERE id = " + id
                return query
            """,
        "expected": {
            "issues": ["sql injection"],
            "severity": "high",
            "fix_keywords": ["parameterized", "prepared"],
            "concepts": ["security", "injection"]
        }
    },

    "hard": {
        "code": """
            def process(data):
                result = []
                for i in range(len(data)):
                    result.append(data[i] * 2)
                print("Processing done")
                return result
            """,
        "expected": {
            "issues": ["inefficient loop", "debug print","iteration"],
            "severity": "medium",
            "fix_keywords": ["list comprehension", "remove print"],
            "concepts": ["performance", "clean code"]
        }
    }
}