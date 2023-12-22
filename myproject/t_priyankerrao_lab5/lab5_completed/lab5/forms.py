from django import forms

class FeedbackForm(forms.Form):
    my_message = forms.CharField(label='Feedback Message', widget=forms.Textarea)
    your_name = forms.CharField(max_length=40)
    review_area = forms.MultipleChoiceField(choices=[('food','Food'),('srvc','Service'),('amb','Ambiance')],
        widget=forms.CheckboxSelectMultiple)

    def clean_my_message(self):

        my_message: str = self.cleaned_data.get('my_message')

        if "terrible" in my_message:
            raise forms.ValidationError(f"We don't accept bad reviews. You said '{my_message}'")
        
        return my_message

