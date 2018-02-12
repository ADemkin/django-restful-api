from django import forms


class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=50,
                           widget=forms.TextInput(
                                   attrs={
                                       'class'      :'form-control col-sm-3 ml-3',
                                       'placeholder':'Enter word',
                                   }
                           ))
    
    def search(self):
        return self.cleaned_data['word']
