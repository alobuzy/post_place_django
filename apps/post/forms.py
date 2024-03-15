from django import forms

from apps.post.models import Post

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class PostSearchForm(forms.Form):
    post_id = forms.CharField(max_length=32, label="Post ID")

class CommentForm(forms.Form):
    text = forms.CharField(max_length=1024, widget=forms.Textarea, label="Comment text")