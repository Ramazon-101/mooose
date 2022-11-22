from django.forms import ModelForm
from .models import Comment
from contact.models import Contact


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['article', 'user']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"


class Subscribe(ModelForm):
    class Meta:
        model = Contact
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(Subscribe, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"

