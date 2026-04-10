from django.db import models
from .models import comments, comments_serial, Feedback
from django.forms import ModelForm, widgets

# comments class
class CommentsForm(ModelForm):
    class Meta:
        model = comments
        fields = ['name', 'body']

        label = {
            'name' : 'Your Name',
            'body' : 'Add a comment'
        }
    
    # set the class (css/style) for fields
    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'form_title'})


# comments class for serial page
class CommentsFormSerial(ModelForm):
    class Meta:
        model = comments_serial
        fields = ['name', 'body']

        label = {
            'name' : 'Your Name',
            'body' : 'Add a comment'
        }
    
    # set the class (css/style) for fields
    def __init__(self, *args, **kwargs):
        super(CommentsFormSerial, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'form_title'})


# Feedback Form / Form Phản hồi
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

        label = {
            'name': 'Họ và Tên',
            'email': 'Email',
            'message': 'Nội dung phản hồi'
        }
    
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form_title'})
