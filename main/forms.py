from django import forms
from ckeditor.widgets import CKEditorWidget

from main.models import Blog, Profile


class BlogForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder": "Title",
                                    "class": "form-control",
                                }
                            ),
                            label="Title",
                        )
    body = forms.CharField(required=True,
                           widget=CKEditorWidget(attrs={"class": "form-control"}), label="Body",)

    class Meta:
        model = Blog
        exclude = ("author", 'slug', 'date')


class ProfileForm(forms.ModelForm):
    age = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(
                               attrs={
                                   "class": "form-control",
                                   "type": "number"
                               }
                           ),
                           label="Age", min_value=8)
    avatar = forms.ImageField(required=False, widget=forms.widgets.FileInput(
                               attrs={
                                   "class": "form-control",
                                   "id": "avatar-input"
                               }
                           ),
                           label="Avatar")

    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'age', 'avatar']

        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "firstname": "First Name",
            "lastname": "Last Name",
        }
