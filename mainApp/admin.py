from django.contrib import admin
from .models import Artist, Album, Song

# Register your models here.

class SongInLine(admin.TabularInline):
    model = Song
    extra = 5

class AlbumsInLine(admin.TabularInline):
    model = Album

class ArtistAdmin(admin.ModelAdmin):
    list_filter = ['artist_name']
    search_fields = ['artist_name']
    fieldsets = [
        ('Artist name',     {'fields':['artist_name']}),
    ]
    inlines = [AlbumsInLine]

class AlbumAdmin(admin.ModelAdmin):
    list_filter = ['album_name']
    search_fields = ['album_name']
    fieldsets = [
        ('Album name',      {'fields':['album_name']}),
    ]
    inlines = [SongInLine]

class SongAdmin(admin.ModelAdmin):
    list_filter = ['album']
    search_fields = ['song_name']
    fieldsets = [
        ('Song name',        {'fields':['song_name']}),
        ('№ in album',      {'fields':['number']}),
        ('Duration',        {'fields':['duration']}),
        ('Link for tabs', {'fields':['link']}),
    ]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)