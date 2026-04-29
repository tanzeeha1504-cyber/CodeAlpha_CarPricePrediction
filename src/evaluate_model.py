from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)

    print("MAE:", mean_absolute_error(y_test, predictions))
    print("MSE:", mean_squared_error(y_test, predictions))
    print("R2 Score:", r2_score(y_test, predictions))

    # Plot
    plt.scatter(y_test, predictions)
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs Predicted")
    plt.savefig("outputs/plots/prediction_plot.png")
    plt.show()
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red')