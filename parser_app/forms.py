from django import forms
from . import models, librusec_parser


class BookForm(forms.ModelForm):
    MEDIA_CHOICES = (
        ('librusec', 'librusec'),
        ('mybook', 'mybook'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        model = models.LibrusecParser
        fields = ['media_type']

    def parser_data(self):
        if self.data['media_type'] == 'librusec':
            file_librusec = librusec_parser.parsing()
            for i in file_librusec:
                models.LibrusecParser.objects.create(**i)