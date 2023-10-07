from ui.app import Titan3023
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    app = Titan3023()
    app.run()
