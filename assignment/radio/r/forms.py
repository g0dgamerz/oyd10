from django import forms

first_CHOICES= [
    ('a', 'A'),
    ('b', 'B'),
    ('c', 'C'),
    ]
second_CHOICES= [
    ('d', 'D'),
    ('e', 'E'),
    ('f', 'F'),
    ]
third_CHOICES= [
    ('g', 'G'),
    ('h', 'H'),
    ('i', 'I'),
    ]


class UserForm(forms.Form):

    first= forms.CharField(label='List1', widget=forms.RadioSelect(choices=first_CHOICES))
    second= forms.CharField(label='List1', widget=forms.RadioSelect(choices=second_CHOICES))
    third= forms.CharField(label='List1', widget=forms.RadioSelect(choices=third_CHOICES))