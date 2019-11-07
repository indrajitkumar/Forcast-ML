import pickle

from sklearn.externals import joblib

classifier_model = joblib.load('ml_code/clustering_model.pkl')
logistic_regression_model = joblib.load('ml_code/logistic_regression_model.pkl')
linear_regression_model = joblib.load('ml_code/linear_regression_model.pkl')
predictivereg = pickle.load(open("ml_code/final_prediction.pkl", "rb"))
# predictivereg = pickle.loads(predictive_model)
clf = pickle.loads(classifier_model)
logreg = pickle.loads(logistic_regression_model)
lreg = pickle.loads(linear_regression_model)


def get_prediction(back_camera, front_camera, resolution_1, resolution_2, screen_size, battery, price,
                   pre_release_demand
                   ):
    y_pred = logreg.predict([[back_camera, front_camera, resolution_1, resolution_2, screen_size, battery,
                              price, pre_release_demand]])
    predicted_sales = lreg.predict([[back_camera, front_camera, resolution_1, resolution_2, screen_size, battery,
                                     price, pre_release_demand]])

    return y_pred, predicted_sales


def get_steel_prediction(X_Minimum, X_Maximum, Y_Minimum, Y_Maximum, Pixels_Areas, X_Perimeter, Y_Perimeter,
                         Sum_of_Luminosity, Minimum_of_Luminosity, Maximum_of_Luminosity, Length_of_Conveyer,
                         TypeOfSteel_A300, TypeOfSteel_A400, Steel_Plate_Thickness, Edges_Index, Empty_Index,
                         Square_Index, Outside_X_Index, Edges_X_Index, Edges_Y_Index, Outside_Global_Index, LogOfAreas,
                         Log_X_Index, Log_Y_Index, Orientation_Index, Luminosity_Index, SigmoidOfAreas):
    y_prediction = predictivereg.predict(
        [[X_Minimum, X_Maximum, Y_Minimum, Y_Maximum, Pixels_Areas, X_Perimeter, Y_Perimeter,
          Sum_of_Luminosity, Minimum_of_Luminosity, Maximum_of_Luminosity, Length_of_Conveyer,
          TypeOfSteel_A300, TypeOfSteel_A400, Steel_Plate_Thickness, Edges_Index, Empty_Index,
          Square_Index, Outside_X_Index, Edges_X_Index, Edges_Y_Index, Outside_Global_Index, LogOfAreas,
          Log_X_Index, Log_Y_Index, Orientation_Index, Luminosity_Index, SigmoidOfAreas]])

    return y_prediction
