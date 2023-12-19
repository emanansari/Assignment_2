import pandas as pd
from src.multiple_linear_regression_ab import MultipleLinearRegression
from src.ridge_regression import RidgeRegression
from src.lasso_regression import LassoRegression
from src.model_saver import ModelSaver
from src.regression_plotter import RegressionPlotter
import argparse


def main():
    parser = argparse.ArgumentParser(description='Run regression models.')
    parser.add_argument('model', choices=['mlr', 'ridge', 'lasso'])
    args = parser.parse_args()

    df = pd.read_csv('petrol_consumption.csv')
    X = df[['Paved_Highways', 'Petrol_tax']].values
    y = df['Target'].values

    if args.model == 'mlr':
        model = MultipleLinearRegression()
    elif args.model == 'ridge':
        model = RidgeRegression(alpha=0.01, iterations=1000, lambda_param=0.1)
    elif args.model == 'lasso':
        model = LassoRegression(alpha=0.01, iterations=1000, lambda_param=0.1)

    model.train(X, y)
    predictions = model.predict(X)
    for true, pred in zip(y, predictions):
        print(f"True: {true}, Predicted: {pred}")

    saver = ModelSaver()
    filename = f'{args.model}_model_params.json'
    saver.save(model, filename)

    plotter = RegressionPlotter(model)
    plotter.plot(X, y)

    new_model = type(model)()
    saver.load(new_model, filename)


if __name__ == "__main__":
    main()
