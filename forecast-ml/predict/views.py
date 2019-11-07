from django.shortcuts import render

from ml_code.ml_process import server_predictor
from predict.forms import ProductForm
from predict.forms import SteelProductForm


def operate_function(product_detail):
    back_camera = product_detail.back_camera
    front_camera = product_detail.front_camera
    resolution_1 = product_detail.resolution_1
    resolution_2 = product_detail.resolution_2
    screen_size = product_detail.screen_size
    battery = product_detail.battery
    price = product_detail.price
    pre_release_demand = product_detail.pre_release_demand
    # sales = product_detail.sales
    # quarter = product_detail.quarter
    cluster_assigned, predicted_sales = server_predictor.get_prediction(back_camera, front_camera,
                                                                        resolution_1,
                                                                        resolution_2, screen_size,
                                                                        battery, price,
                                                                        pre_release_demand)
    return cluster_assigned[0], int(predicted_sales[0])


def operate_function_for_steel(product_detail1):
    X_Minimum = 4#product_detail1.X_Minimum
    X_Maximum = 6#product_detail1.X_Maximum
    Y_Minimum = 5#product_detail1.Y_Minimum
    Y_Maximum = 8#product_detail1.Y_Maximum
    Pixels_Areas = product_detail1.Pixels_Areas
    X_Perimeter = product_detail1.X_Perimeter
    Y_Perimeter = product_detail1.Y_Perimeter
    Sum_of_Luminosity = product_detail1.Sum_of_Luminosity
    Minimum_of_Luminosity = product_detail1.Minimum_of_Luminosity
    Maximum_of_Luminosity = product_detail1.Maximum_of_Luminosity
    Length_of_Conveyer = product_detail1.Length_of_Conveyer

    TypeOfSteel_A300 = product_detail1.TypeOfSteel_A300
    TypeOfSteel_A400 = product_detail1.TypeOfSteel_A400
    Steel_Plate_Thickness = product_detail1.Steel_Plate_Thickness
    Edges_Index = product_detail1.Edges_Index
    Empty_Index = product_detail1.Empty_Index
    Square_Index = product_detail1.Square_Index
    Outside_X_Index = product_detail1.Outside_X_Index
    Edges_X_Index = product_detail1.Edges_X_Index
    Edges_Y_Index = product_detail1.Edges_Y_Index
    Outside_Global_Index = product_detail1.Outside_Global_Index

    LogOfAreas = product_detail1.LogOfAreas
    Log_X_Index = product_detail1.Log_X_Index
    Log_Y_Index = product_detail1.Log_Y_Index
    Orientation_Index = product_detail1.Orientation_Index
    Luminosity_Index = product_detail1.Luminosity_Index
    SigmoidOfAreas = product_detail1.SigmoidOfAreas

    steelpredictor = server_predictor.get_steel_prediction(X_Minimum, X_Maximum, Y_Minimum, Y_Maximum, Pixels_Areas,
                                                           X_Perimeter, Y_Perimeter, Sum_of_Luminosity,
                                                           Minimum_of_Luminosity, Maximum_of_Luminosity,
                                                           Length_of_Conveyer, TypeOfSteel_A300, TypeOfSteel_A400,
                                                           Steel_Plate_Thickness, Edges_Index, Empty_Index,
                                                           Square_Index, Outside_X_Index, Edges_X_Index, Edges_Y_Index,
                                                           Outside_Global_Index, LogOfAreas, Log_X_Index, Log_Y_Index,
                                                           Orientation_Index, Luminosity_Index,
                                                           SigmoidOfAreas)
    return steelpredictor[0]


def product_describe_view(request):
    """
    View to take the data from the user and process year
    """
    product_added = False
    cluster_assigned = 0
    predicted_sales = 0
    steel_predicteds = 0
    if request.method == 'POST':
        product_form = ProductForm(data=request.POST)
        product_form1 = SteelProductForm(data=request.POST)
        if product_form.is_valid():
            product_detail = product_form.save()
            product_added = True
            print(product_detail)
            cluster_assigned, predicted_sales = operate_function(product_detail)
            print("Cluster Assigned : {}".format(cluster_assigned))
            product_detail.save()
        else:
            if product_form1.is_valid():
                product_detail1 = product_form1.save()
                product_added = True
                print(product_detail1)
                steel_predicteds = operate_function_for_steel(product_detail1)
                print("Steel Cluster Assigned : {}".format(steel_predicteds))
                product_detail1.save()
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        product_form = ProductForm()
        product_form1 = SteelProductForm()
    return render(request, 'predict/add_product.html',
                  {'product_form': product_form, 'product_form1': product_form1, 'product_added': product_added,
                   'cluster_assigned': cluster_assigned, 'predicted_sales': predicted_sales,
                   'steel_predicteds': steel_predicteds})
