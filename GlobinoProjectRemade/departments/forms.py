from departments.models import Departments
from django.forms import ModelForm
# ,TextField,CharField,IntegerField
class DepartmentsForm(ModelForm):
    class Meta:
        model = Departments
        fields = ['title','description',
                  'min_t','max_t','default_value_t',
                  'min_h','max_h','default_value_h',
                  'min_a','max_a','default_value_a']

        # widgets = {
        #
        #     'title':CharField(attrs = {
        #
        #         'placeholder':'Department name'
        #     }),
        #     'description': TextField(attrs={
        #         'placeholder': 'description'
        #     }),
        #
        #
        #
        #     'min_t':IntegerField(attrs = {
        #         'placeholder': 'min_temperature'
        #     }),
        #     'max_t': IntegerField(attrs={
        #         'placeholder': 'max_temperature'
        #     }),
        #     'default_value_t': IntegerField(attrs={
        #         'placeholder': 'default_value_temperature'
        #     }),
        #
        #
        #
        #     'min_h': IntegerField(attrs={
        #         'placeholder': 'min_humidity'
        #     }),
        #     'max_h': IntegerField(attrs={
        #         'placeholder': 'max_humidity'
        #     }),
        #     'default_value_h': IntegerField(attrs={
        #         'placeholder': 'default_value_humidity'
        #     }),
        #
        #
        #
        #     'min_a': IntegerField(attrs={
        #         'placeholder': 'min_air'
        #     }),
        #     'max_a': IntegerField(attrs={
        #         'placeholder': 'max_air'
        #     }),
        #     'default_value_a': IntegerField(attrs={
        #         'placeholder': 'default_value_air'
        #     }),
        #
        # }