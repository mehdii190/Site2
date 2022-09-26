from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)
    is_enable = forms.BooleanField()
    publish_date = forms.DateField()
    #created_time = forms.DateTimeField(auto_now_add=True)
    #updated_time = forms.DateTimeField(auto_now=True)