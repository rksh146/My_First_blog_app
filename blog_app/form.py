from django.forms import ModelForm, TextInput, forms, Textarea
from blog_app.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = ['title','body']
        fields = '__all__'
        widgets = {
                'title': TextInput(attrs={'class':'form-control'}),
                'body': Textarea(attrs={'class':'form-control'}),
        }
        # widgets = { 'first_name': TextInput(attrs={'placeholder': 'First Name','size': 10000}),
        #             'last_name': TextInput(attrs={'placeholder': 'Last Name','size': 10}),
        #             'mob_number': TextInput(attrs={'placeholder': 'Your Mobile Name','size': 100}),
        #             'home_phone': TextInput(attrs={'placeholder': 'Home Phone if  any..','size': '100vh'}),
        #             'address': TextInput(attrs={'placeholder': 'Address','size': 1000}),
        #             'comments': TextInput(attrs={'placeholder': 'Comments if any..','size': 9}),
        #             'comments' :Textarea,
        #             # 'address':TextInput(attrs={'size':'200000'})
        #             }
