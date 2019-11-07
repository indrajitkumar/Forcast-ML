from django import forms

from predict.models import Product, SteelProduct


class SteelProductForm(forms.ModelForm):
    class Meta:
        model = SteelProduct
        fields = (
            'X_Minimum',
            'X_Maximum',
            'Y_Minimum',
            'Y_Maximum',
            'Pixels_Areas',
            'X_Perimeter',
            'Y_Perimeter',
            'Sum_of_Luminosity',
            'Minimum_of_Luminosity',
            'Maximum_of_Luminosity',
            'Length_of_Conveyer',
            'TypeOfSteel_A300',
            'TypeOfSteel_A400',
            'Steel_Plate_Thickness',
            'Edges_Index',
            'Empty_Index',
            'Square_Index',
            'Outside_X_Index',
            'Edges_X_Index',
            'Edges_Y_Index',
            'Outside_Global_Index',
            'LogOfAreas',
            'Log_X_Index',
            'Log_Y_Index',
            'Orientation_Index',
            'Luminosity_Index',
            'SigmoidOfAreas'
        )

    def save(self, commit=True):
        product = super(SteelProductForm, self).save(commit=False)
        product.X_Minimum = self.cleaned_data['X_Minimum']
        product.X_Maximum = self.cleaned_data['X_Maximum']
        product.Y_Minimum = self.cleaned_data['Y_Minimum']
        product.Y_Maximum = self.cleaned_data['Y_Maximum']
        product.Pixels_Areas = self.cleaned_data['Pixels_Areas']
        product.X_Perimeter = self.cleaned_data['X_Perimeter']
        product.Y_Perimeter = self.cleaned_data['Y_Perimeter']
        product.Sum_of_Luminosity = self.cleaned_data['Sum_of_Luminosity']
        product.Minimum_of_Luminosity = self.cleaned_data['Minimum_of_Luminosity']
        product.Maximum_of_Luminosity = self.cleaned_data['Maximum_of_Luminosity']
        product.Length_of_Conveyer = self.cleaned_data['Length_of_Conveyer']
        product.TypeOfSteel_A300 = self.cleaned_data['TypeOfSteel_A300']
        product.TypeOfSteel_A400 = self.cleaned_data['TypeOfSteel_A400']
        product.Steel_Plate_Thickness = self.cleaned_data['Steel_Plate_Thickness']
        product.Edges_Index = self.cleaned_data['Edges_Index']
        product.Empty_Index = self.cleaned_data['Empty_Index']
        product.Square_Index = self.cleaned_data['Square_Index']
        product.Outside_X_Index = self.cleaned_data['Outside_X_Index']
        product.Edges_X_Index = self.cleaned_data['Edges_X_Index']
        product.Edges_Y_Index = self.cleaned_data['Edges_Y_Index']
        product.Outside_Global_Index = self.cleaned_data['Outside_Global_Index']
        product.LogOfAreas = self.cleaned_data['LogOfAreas']
        product.Log_X_Index = self.cleaned_data['Log_X_Index']
        product.Log_Y_Index = self.cleaned_data['Log_Y_Index']
        product.Orientation_Index = self.cleaned_data['Orientation_Index']
        product.Luminosity_Index = self.cleaned_data['Luminosity_Index']
        product.SigmoidOfAreas = self.cleaned_data['SigmoidOfAreas']

        if commit:
            product.save()
        return product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'back_camera',
            'front_camera',
            'resolution_1',
            'resolution_2',
            'screen_size',
            'battery',
            'price',
            'pre_release_demand',
            # 'sales',
            # 'quarter',
        )

    def save(self, commit=True):
        product = super(ProductForm, self).save(commit=False)
        product.back_camera = self.cleaned_data['back_camera']
        product.front_camera = self.cleaned_data['front_camera']
        product.resolution_1 = self.cleaned_data['resolution_1']
        product.resolution_2 = self.cleaned_data['resolution_2']
        product.screen_size = self.cleaned_data['screen_size']
        product.battery = self.cleaned_data['battery']
        product.price = self.cleaned_data['price']
        product.pre_release_demand = self.cleaned_data['pre_release_demand']
        # product.sales = self.cleaned_data['sales']
        # product.quarter = self.cleaned_data['quarter']

        if commit:
            product.save()
        return product
