from django.forms import ModelForm
from .models import  Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['owner','vote_tottal', 'vote_ratio']
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'input'})
        #  self.fields['title'].widget.attrs.update({'class': 'input'})
        #  the above line puts the class of the bootstrap in the field but it will add to one  field only

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
    
    labels = {
        'value' : 'Place your vote',
        'body' : 'Add comment with your vote'
    }
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'input'})