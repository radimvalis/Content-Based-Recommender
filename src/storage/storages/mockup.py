
from storage import Storage, StorageItem

class MockUpStorage(Storage):

    def get_data(self) -> list[StorageItem] :
        
        keywords_set = [
            ["politics", "parliament", "government"],
            ["politics", "parliament", "government", "prime minister"],
            ["government", "prime minister"],
            ["politics", "parliament", "ministry of justice", "court"],
            ["ministry of justice", "court", "law"],
            ["politics", "president"],
            ["politics", "president", "elections"],
            ["politics", "ministry of agriculture", "agriculture", "animal farming"],
            ["politics", "ministry of environment", "agriculture", "drought"],
            ["ministry of environment", "drought"],
            ["country", "agriculture", "animal farming"],
            ["agriculture", "animal farming"],
            ["country", "agriculture", "drought"],
            ["drought", "weather"],
            ["nature", "mountains", "snow"],
            ["nature", "mountains", "snow", "winter"],
            ["nature", "weather", "snow"],
            ["weather", "snow"],
            ["weather", "summer"],
            ["holiday", "summer"],
            ["weather", "weekend", "holiday"],
            ["weather", "holiday"],
            ["mountains", "avalanche"],
            ["weather", "snow", "mountains"],
            ["weather", "snow", "mountains", "avalanche"],
            ["christmas", "winter", "snow", "weather"],
            ["christmas", "holiday", "snow"],
            ["science", "biology", "cell"],
            ["biology", "cell"],
            ["biology", "oceans"],
            ["oceans", "fish", "biology"],
            ["oceans", "fish"],
            ["oceans", "ministry of environment"],
            ["science", "forests", "drought"],
            ["forests", "weather", "drought", "biology"],
            ["science", "weather", "drought"],
            ["science", "computer science", "computers"],
            ["computer science", "computers", "AI"],
            ["computers", "mathematics"],
            ["AI", "robots", "cybernetics"],
            ["robots", "cybernetics"],
            ["robots", "hardware"],
            ["computers", "hardware"],
            ["computers", "software"],
            ["computers", "software", "AI"],
            ["AI", "robots", "mathematics"],
            ["AI", "law"],
            ["AI", "science"],
        ]

        data = []

        for set in keywords_set:
            title = "-".join(set)
            data.append(StorageItem(title, f"https://www.example.org/{id}", set))

        return data