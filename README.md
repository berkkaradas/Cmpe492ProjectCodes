🎵 Facify – Emotion-Aware Music Recommendation System

Facify is a research-based web application that uses facial mood recognition powered by deep learning to recommend personalized music. The project combines artificial intelligence, web development, and human-computer interaction to create an innovative user experience.

🏆 Awarded Top 3 Research Project of the Year (2021/2022) under the supervision of Assoc. Prof. Dr. Savaş Yıldırım.

📸 Overview

Facify captures facial expressions via webcam, analyzes the emotional state in real time, and suggests songs that match or complement the user’s mood.

Key features:

🎥 Real-time facial emotion recognition

🤖 Pre-trained deep learning models (VGGFace, ResNet-50, InceptionV3, MobileNet)

🎶 AI-based music classification and recommendation

🌐 Developed with Django (Python) for backend and web integration

🗄️ Structured database design for scalable song management

📊 Trained with AffectNet dataset (10,000+ images)

🚀 Technologies Used

Programming Language: Python

Framework: Django

Deep Learning Libraries: TensorFlow, Keras, PyTorch

Pre-trained Models:

VGGFace

ResNet-50

InceptionV3

MobileNet

Machine Learning Algorithms for Song Classification:

Support Vector Machines (SVM)

Random Forests

k-Nearest Neighbors (k-NN)

🔧 Installation

Clone the repository:

git clone https://github.com/username/facify.git
cd facify


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows


Install dependencies:

pip install -r requirements.txt


Run the server:

python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

📂 Project Structure
facify/
│── dataset/             # Training data (AffectNet samples)
│── models/              # Pre-trained DL models
│── music_classifier/    # ML algorithms for songs
│── facify_app/          # Django application
│   ├── templates/       # HTML templates
│   ├── static/          # CSS, JS, images
│   └── views.py         # Main logic
│── requirements.txt     # Dependencies
│── manage.py            # Django manager
└── README.md

🖼️ Screenshots 

Home Page – Webapp landing page

Camera Input – Real-time face capture

Emotion Detection – Showing recognized emotion

Music Recommendation – Suggested playlist

📊 Research Contributions

Designed a full-stack system combining AI and traditional computer science fundamentals

Implemented real-time data processing pipelines

Explored human-computer interaction by mapping emotions to personalized content

Produced an 80-page research thesis with theoretical + practical analysis

✨ Future Work

Extend dataset for more diverse emotions

Improve accuracy with transformer-based models (e.g., Vision Transformers, CLIP)

Add integration with Spotify API for dynamic playlists

Enhance UI/UX for mobile responsiveness

👤 Author

Ömer Berk Karadaş

📜 License

This project is licensed under the MIT License – feel free to use, modify, and share.
