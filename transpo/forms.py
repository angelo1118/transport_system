from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile  # Import the Profile model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)  # Add the profile picture field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Save the profile picture to the Profile model
            Profile.objects.create(
                user=user,
                profile_picture=self.cleaned_data.get('profile_picture', 'default.jpg')
            )
        return user
    
class SearchForm(forms.Form):
    model = forms.ChoiceField(choices=[('', 'Select Model'), ('model_1', 'Model 1'), ('model_2', 'Model 2')], required=False)
    brand = forms.ChoiceField(choices=[('', 'Select Brand'), ('brand_1', 'Brand 1'), ('brand_2', 'Brand 2')], required=False)
    year = forms.ChoiceField(choices=[('', 'Year Model'), ('2019', '2019'), ('2018', '2018')], required=False)
    price_limit = forms.ChoiceField(choices=[('', 'Price Limit'), ('$50', '$50'), ('$100', '$100')], required=False)