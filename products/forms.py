from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["by_user", "product", "description", "rating"]
        widgets = {
            "description": Textarea(attrs={"cols": 60, "rows": 10}),
        }
