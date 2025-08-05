from django import forms
from .models import NewsAndEvents, GoogleMeetLink, Semester, SEMESTER


# news and events
class NewsAndEventsForm(forms.ModelForm):
    class Meta:
        model = NewsAndEvents
        fields = (
            "title",
            "summary",
            "posted_as",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["summary"].widget.attrs.update({"class": "form-control"})
        self.fields["posted_as"].widget.attrs.update({"class": "form-control"})


class SessionForm(forms.ModelForm):
    next_session_begins = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                "type": "time",
            }
        ),
        required=False,
    )

    class Meta:
        model = GoogleMeetLink
        fields = ["course", "meet_link"]


# class SemesterForm(forms.ModelForm):
#     semester = forms.CharField(
#         widget=forms.Select(
#             choices=SEMESTER,
#             attrs={
#                 "class": "browser-default custom-select",
#             },
#         ),
#         label="semester",
#     )
#     is_current_semester = forms.CharField(
#         widget=forms.Select(
#             choices=((True, "Yes"), (False, "No")),
#             attrs={
#                 "class": "browser-default custom-select",
#             },
#         ),
#         label="is current semester ?",
#     )
#     session = forms.ModelChoiceField(
#         queryset=GoogleMeetLink.objects.all(),
#         widget=forms.Select(
#             attrs={
#                 "class": "browser-default custom-select",
#             }
#         ),
#         required=True,
#     )

#     next_semester_begins = forms.DateTimeField(
#         widget=forms.TextInput(
#             attrs={
#                 "type": "date",
#                 "class": "form-control",
#             }
#         ),
#         required=True,
#     )

#     class Meta:
#         model = Semester
#         fields = ["semester", "is_current_semester", "session", "next_semester_begins"]
