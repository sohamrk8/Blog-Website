from django import forms
from .models import Postmodel,Comment


class PostmodelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':'2','col':'1'}))
    class Meta:
        model = Postmodel
        fields=('title','content')



class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Postmodel
        fields=('title','content')


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='' ,widget=forms.TextInput(attrs={'placeholder':'Add comment here..'}))
    class Meta:
        model = Comment
        fields = ('content',)