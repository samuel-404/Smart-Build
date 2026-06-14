import os
import sys

# Add the backend directory to Python path so Vercel can run relative imports
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'backend'))

from app import app
