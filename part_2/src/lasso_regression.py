import numpy as np
import logging
from multiple_linear_regression_ab import MultipleLinearRegression

# to configure logging before the parameters get updated
logging.basicConfig(filename='lasso_regression.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class LassoRegression(MultipleLinearRegression):
    def __init__(self, alpha: float = 0.01, iterations: int = 1000,
                 lambda_param: float = 0.1,
                 init_method: str = 'normal') -> None:
        super().__init__()
        self.alpha = alpha
        self.iterations = iterations
        self.lambda_param = lambda_param
        self.init_method = init_method

    def _initialize_parameters(self, n_features: int) -> None:
        if self.init_method == 'uniform dist':
            self.parameters = np.random.uniform(-1, 1, size=n_features + 1)
        elif self.init_method == 'normal dist':
            self.parameters = np.random.randn(n_features + 1)
        else:
            raise ValueError("This strategy is invalid.")

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        self._initialize_parameters(X.shape[1])
        for iteration in range(self.iterations):
            pred = self.predict(X)
            loss = self._compute_loss(X, y, pred)
            mean_absolute_error = np.mean(np.abs(y - pred))
            logging.info(f'Iteration {iteration + 1}/{self.iterations}, \
                        + Loss: {loss}, Mean abs error: {mean_absolute_error}')
            gradient = self._compute_lasso_gradient(X, y, pred)
            self.parameters -= self.alpha * gradient

    def _compute_loss(self, X: np.ndarray, y: np.ndarray,
                      pred: np.ndarray) -> float:
        error = pred - y
        mean_square_error = np.mean(error ** 2)
        lasso_penalty = self.lambda_param * np.sum(np.abs(self.parameters))
        return mean_square_error + lasso_penalty

    def _compute_lasso_gradient(self, X: np.ndarray, y: np.ndarray,
                                pred: np.ndarray) -> np.ndarray:
        error = pred - y
        gradient = (2 / len(X)) * np.dot(X.T, error) + \
            + self.lambda_param * np.sign(self.parameters)
        return gradient
