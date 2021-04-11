from django.forms import ModelForm, Textarea
from .models import Review


class PartialReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "description"]
        widgets = {
            "description": Textarea(attrs={"cols": 60, "rows": 10}),
        }
