from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    info = models.TextField

    def __str__(self):
        return self.artist_name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    album_info = models.TextField

    def __str__(self):
        return "%s | %s" % (self.album_name , self.artist)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    song_name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    link = models.CharField(max_length=300)

    def __str__(self):
        return "%s | %s" % (self.song_name, self.album)