from django.db import models

# Create your models here.
# Create a BLOG models/
# title , publication date , body , image
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')
# ADD blog app to setting
# migration
#add to admin
    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.publication_date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
