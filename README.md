🐳 Dockerized Regression Model


A simple yet powerful machine learning project that demonstrates how to train a regression model and serve it via a REST API using Flask and Docker. This project showcases a complete ML pipeline from training to deployment in a containerized environment.

📌 Features
📊 Trains a regression model using scikit-learn

🧪 Saves and loads model using joblib

🌐 Provides a simple REST API with Flask for inference

🐳 Fully containerized with Docker

🔁 Easy to reproduce and deploy anywhere

🗂️ Project Structure
bash
Copy
Edit
dockerized-regression-model/
├── app/
│   ├── model.pkl            # Saved regression model
│   ├── app.py               # Flask API
│   └── utils.py             # Helper functions
├── data/
│   └── dataset.csv          # Input data (optional)
├── model/
│   └── train_model.py       # Script to train and export model
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
