from django.db import models


# Create your models here.

class Product(models.Model):
    back_camera = models.DecimalField(decimal_places=2, max_digits=10)
    front_camera = models.DecimalField(decimal_places=2, max_digits=10)
    resolution_1 = models.DecimalField(decimal_places=2, max_digits=10)
    resolution_2 = models.DecimalField(decimal_places=2, max_digits=10)
    screen_size = models.DecimalField(decimal_places=2, max_digits=10)
    battery = models.DecimalField(decimal_places=2, max_digits=10)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    pre_release_demand = models.DecimalField(decimal_places=2, max_digits=10)
    # sales = models.DecimalField(decimal_places=2, max_digits=10)
    # quarter = models.DecimalField(decimal_places=2, max_digits=10)


class SteelProduct(models.Model):
    X_Minimum = models.DecimalField(decimal_places=2, max_digits=10)
    X_Maximum = models.DecimalField(decimal_places=2, max_digits=10)
    Y_Minimum = models.DecimalField(decimal_places=2, max_digits=10)
    Y_Maximum = models.DecimalField(decimal_places=2, max_digits=10)
    Pixels_Areas = models.DecimalField(decimal_places=2, max_digits=10)
    X_Perimeter = models.DecimalField(decimal_places=2, max_digits=10)
    Y_Perimeter = models.DecimalField(decimal_places=2, max_digits=10)
    Sum_of_Luminosity = models.DecimalField(decimal_places=2, max_digits=10)
    Minimum_of_Luminosity = models.DecimalField(decimal_places=2, max_digits=10)
    Maximum_of_Luminosity = models.DecimalField(decimal_places=2, max_digits=10)

    Length_of_Conveyer = models.DecimalField(decimal_places=2, max_digits=10)
    TypeOfSteel_A300 = models.DecimalField(decimal_places=2, max_digits=10)
    TypeOfSteel_A400 = models.DecimalField(decimal_places=2, max_digits=10)
    Steel_Plate_Thickness = models.DecimalField(decimal_places=2, max_digits=10)
    Edges_Index = models.DecimalField(decimal_places=2, max_digits=10)
    Empty_Index = models.DecimalField(decimal_places=2, max_digits=10)
    Square_Index = models.DecimalField(decimal_places=2, max_digits=10)
    Outside_X_Index = models.DecimalField(decimal_places=2, max_digits=10)
    Edges_X_Index = models.DecimalField(decimal_places=2, max_digits=10)
    Edges_Y_Index = models.DecimalField(decimal_places=2, max_digits=10)

    Outside_Global_Index = models.DecimalField(decimal_places=2, max_digits=10)
    LogOfAreas = models.DecimalField(decimal_places=2, max_digits=10)
    Log_X_Index = models.DecimalField(decimal_places=2, max_digits=10)
    Log_Y_Index = models.DecimalField(decimal_places=2, max_digits=10)
    Orientation_Index = models.DecimalField(decimal_places=2, max_digits=10)
    Luminosity_Index = models.DecimalField(decimal_places=2, max_digits=10)
    SigmoidOfAreas = models.DecimalField(decimal_places=2, max_digits=10)
