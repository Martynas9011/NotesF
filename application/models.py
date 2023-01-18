from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    # customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL('', '', '', ''))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'
