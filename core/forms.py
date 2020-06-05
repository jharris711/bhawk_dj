from django import forms


class BookingForm(forms.Form):
    full_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Full Name"
        })
    )
    email = forms.EmailField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Email Address"
        })
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "What's on your mind?"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "What's up?"
        })
    )


class SubscribeForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control border-secondary text-white bg-transparent",
            "placeholder": "Enter your email..."
        })
    )
