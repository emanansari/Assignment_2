import numpy as np
import logging
from multiple_linear_regression_ab import MultipleLinearRegression

# to configure logging before the parameters get updated
logging.basicConfig(filename='ridge_reg.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class RidgeRegression(MultipleLinearRegression):
    def __init__(self, alpha: float = 0.01, iterations: int = 1000,
                 lambda_param: float = 0.1) -> None:
        super().__init__()
        self.alpha = alpha
        self.iterations = iterations
        self.lambda_param = lambda_param

    def _initialize_parameters(self, n_features: int) -> None:
        if self.init_method == 'uniform':
            self.parameters = np.random.uniform(-1, 1, size=(n_features + 1,))
        elif self.init_method == 'normal':
            self.parameters = np.random.randn(n_features + 1)
        else:
            raise ValueError("Invalid initialization method specified.")

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        self._initialize_parameters(X.shape[1])
        for iteration in range(self.iterations):
            pred = self.predict(X)
            loss = self._compute_loss(X, y, pred)
            mean_absolute_error = np.mean(np.abs(y - pred))
            logging.info(f'Iteration {iteration + 1}/{self.iterations}, \
                + Loss: {loss}, MAE: {mean_absolute_error}')
            gradient = self._compute_ridge_gradient(X, y, pred)
            self.parameters -= self.alpha * gradient

    def _compute_loss(self, X: np.ndarray, y: np.ndarray,
                      pred: np.ndarray) -> float:
        error = pred - y
        mean_squared_error = np.mean(error ** 2)
        ridge_penalty = self.lambda_param * np.sum(self.parameters ** 2)
        return mean_squared_error + ridge_penalty

    def _compute_ridge_gradient(self, X: np.ndarray, y: np.ndarray,
                                predictions: np.ndarray) -> np.ndarray:
        error = predictions - y
        gradient = (2 / len(X)) * np.dot(X.T, error) + 2 * \
            + self.lambda_param * self.parameters
        return gradient
