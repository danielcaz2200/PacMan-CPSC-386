class Settings():
    def __init__(self) -> None:
        """Setup the game settings"""
        self.bg = (0, 0, 0)
        self.screenWidth = 780
        self.screenHeight = 900
        self.lives = 3
        self.spriteSize = (28, 28)
        self.fruitScore = 500
        self.pelletScore = None
        self.powerPelletScore = None
        self.initialize_pellet_scores()
        self.initialize_speed_settings()

    def initialize_pellet_scores(self) -> None:
        self.pelletScore = 10
        self.powerPelletScore = 100

    def initialize_speed_settings(self) -> None:
        self.playerSpeed = 3
