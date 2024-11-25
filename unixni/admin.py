from django.contrib import admin
from django.utils.html import format_html

# ======================= HomePage ===================================
from .models.home.beranda import CompanyValue, ValueDescription, WelcomeCard,TrustedBrand,Testimonial,FAQ

# [1] Card
class WelcomeCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_image')  # Menampilkan kolom judul dan pratinjau gambar
    list_display_links = ('title',)  # Membuat judul menjadi link ke form edit
    search_fields = ('title', 'description')  # Menambahkan fitur pencarian
    readonly_fields = ('preview_image',)  # Menampilkan gambar sebagai field yang hanya bisa dibaca

admin.site.register(WelcomeCard)

# [2] Value
class CompanyValueAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'description')
    list_editable = ('description',)
    search_fields = ('abbreviation', 'description')

admin.site.register(CompanyValue, CompanyValueAdmin)

class ValueDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'title3', 'title4', 'subtitle')
    list_editable = ('subtitle',)

admin.site.register(ValueDescription, ValueDescriptionAdmin)

# [3] Brand
class TrustedBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview') 
    list_display_links = ('name',)  
    list_editable = ()  
    readonly_fields = ('logo_preview',)
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.logo.url)
        return "No Image"
    logo_preview.short_description = 'Logo Preview'

admin.site.register(TrustedBrand, TrustedBrandAdmin)

# [4] Testimoni
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 80px; height: auto;" />', obj.image.url)
        return "Tidak ada gambar"
    image_preview.short_description = "Pratinjau Gambar"

admin.site.register(Testimonial, TestimonialAdmin)

# [5] FAQ
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')

admin.site.register(FAQ, FAQAdmin)





# ========================== Tentang Kami ========================
from .models.home.about import About, Mission, Structur  # Ensure you import the new models

class MissionAdmin(admin.ModelAdmin):
    list_display = ['list']

class StructurAdmin(admin.ModelAdmin):
    list_display = ['list']

admin.site.register(Mission, MissionAdmin)
admin.site.register(Structur, StructurAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'title2', 'title3', 'title4', 'title5', 'title6', 'title7')
    list_editable = ('subtitle',)
    search_fields = ('title', 'description', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7')
    readonly_fields = ('logo_preview', 'diagram_preview',)

    def logo_preview(self, obj):
        return format_html('<img src="{}" style="width: 80px; height: auto;" />', obj.logo.url)

    def diagram_preview(self, obj):
        return format_html('<img src="{}" style="width: 80px; height: auto;" />', obj.diagram.url)

admin.site.register(About, AboutAdmin)


# ================================= Tim ================================
from .models.home.tim import Tim, Value, Pencapaian, Target

class ValueAdmin(admin.ModelAdmin):
    list_display = ['list']

class PencapaianAdmin(admin.ModelAdmin):
    list_display = ['list']
    
class TargetAdmin(admin.ModelAdmin):
    list_display = ['list']

admin.site.register(Value, ValueAdmin)
admin.site.register(Pencapaian, PencapaianAdmin)
admin.site.register(Target, TargetAdmin)

class TimAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'line', 'title2', 'subtitle2', 'subtitle3', 'title3', 'profil_preview')
    list_editable = ('subtitle', 'line', 'title2', 'subtitle2', 'subtitle3', 'title3')
    search_fields = ('title', 'subtitle', 'line', 'title2', 'subtitle2', 'subtitle3')
    readonly_fields = ('profil_preview',)

    def profil_preview(self, obj):
        if obj.profil:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.profil.url)
        return "No Image"

    profil_preview.short_description = "Profil Preview"

admin.site.register(Tim, TimAdmin)



# ============================= Galeri ================================
from django.contrib import admin
from .models.home.galeri import GaleriUtama, Galeri, GaleriItem

# Inline untuk GaleriItem agar bisa dikelola dalam admin Galeri
class GaleriItemInline(admin.TabularInline):
    model = GaleriItem
    extra = 1  # Tambahkan satu baris kosong untuk input baru

# Admin untuk Galeri
class GaleriAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Menampilkan judul dan deskripsi di daftar admin
    search_fields = ('title', 'description')  # Menambahkan fitur pencarian
    inlines = [GaleriItemInline]  # Menampilkan item galeri sebagai inline

# Admin untuk GaleriUtama
class GaleriUtamaAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'line')  # Menampilkan judul, subtitle, dan garis
    search_fields = ('title', 'subtitle', 'line')  # Menambahkan fitur pencarian

# Daftarkan model ke admin
admin.site.register(GaleriUtama, GaleriUtamaAdmin)
admin.site.register(Galeri, GaleriAdmin)


# ==================================== Kontak ===========================
from .models.home.kontak import Kontak, Kerja, Alamat

class KontakAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'subtitle2')
    list_editable = ('subtitle', 'subtitle2')
    search_fields = ('title', 'subtitle', 'subtitle2')

admin.site.register(Kontak, KontakAdmin)
admin.site.register(Kerja)
admin.site.register(Alamat)


# ================================== Blog ==================================
from .models.home.blog import BlogUtama, BlogPost, RelatedPost, Comment, Tag

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'display_tags', 'total_likes', 'view_image','description')
    search_fields = ('title', 'content', 'tags__name')
    list_filter = ('publish_date', 'tags')
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'

    def view_image(self, obj):
        return format_html('<img src="{}" width="100" height="auto" />', obj.image.url if obj.image else '')
    view_image.short_description = "Image Preview"

class RelatedPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_post')
    search_fields = ('title',)
    list_filter = ('blog_post',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_on')
    search_fields = ('user__username', 'content')
    list_filter = ('created_on', 'post')
    ordering = ('-created_on',)

class BlogUtamaAdmin(admin.ModelAdmin):
    list_display = ('title', 'line')
    search_fields = ('title', 'description')
    list_editable = ('line',)

admin.site.register(BlogUtama, BlogUtamaAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(RelatedPost, RelatedPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)