from django import forms

from main.models import Blog


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
                           widget=forms.widgets.Textarea(
                               attrs={
                                   "placeholder": "",
                                   "class": "form-control",
                                   "rows": 5
                               }
                           ),
                           label="Body",
                           )

    class Meta:
        model = Blog
        exclude = ("author", 'slug', 'date')
