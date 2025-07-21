import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Generate synthetic data
def generate_data(n_samples=100):
    np.random.seed(42)
    X = 2 * np.random.rand(n_samples, 1)
    y = 4 + 3 * X[:, 0] + np.random.randn(n_samples)
    return pd.DataFrame({'X': X[:, 0], 'y': y})

def main():
    data = generate_data()
    X = data[['X']]
    y = data['y']
    model = LinearRegression()
    model.fit(X, y)
    print(f"Intercept: {model.intercept_}")
    print(f"Coefficient: {model.coef_[0]}")
    joblib.dump(model, 'linear_regression_model.joblib')
    print("Model saved as linear_regression_model.joblib")

if __name__ == "__main__":
    main() 