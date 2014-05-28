from django.db import models

class Profiles(models.Model):

    user_name = models.Charfield(
            max_length=255,
            )
    user_city = models.Charfield(
            max_length=255,
            )
    user_state = models.Charfield(
            max_length=255,
            )
    email = models.EmailField()

    def __str__(self):
        return ' '.join([self.user_name, self.user_city, self.user_state,])


