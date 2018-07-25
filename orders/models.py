from django.db import models

class Food(models.Model):
    """
    Model representing a food on the menu (but not a specific copy of a food).
    """
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Foreign Key used because food can only have one price
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the food item')
    # ManyToManyField used because genre can contain many foods. Foods can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


