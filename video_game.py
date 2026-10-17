class VideoGame:
    def __init__(self, name, release_year, developer, platform):
        self.name = name
        self.release_year = release_year
        self.developer = developer
        self.platform = platform
        self.finished = False
        self.rating = None

    def __str__(self):
        if self.rating is None:
            rating_text = "Not rated"
        else:
            rating_text = f"{self.rating}/10"

        if self.finished:
            status_text = "Finished"
        else:
            status_text = "Unfinished"    

        return f"{self.name} ({self.release_year}) | {self.platform} | {self.developer} | Rating: {rating_text} | {status_text}"

    def mark_finished(self):
        if self.finished:
            return False

        self.finished = True
        return True

    def rate_game(self, rating):
        if rating < 1 or rating > 10:
            return False
        
        self.rating = rating
        return True
