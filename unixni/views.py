
from django.shortcuts import render, get_object_or_404, redirect
from .models.home.beranda import CompanyValue, ValueDescription, WelcomeCard,TrustedBrand,Testimonial, FAQ
from .models.home.about import About, Mission, Structur
from  .models.home.tim import Tim, Value, Pencapaian, Target
from .models.home.galeri import GaleriUtama, Galeri
from .models.home.kontak import Kontak, Kerja, Alamat
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models.home.blog import BlogUtama, BlogPost, RelatedPost, Comment
from django.contrib.auth.decorators import login_required

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

# Homepage
def homepage(request):
    
    # Welcome Card #
    welcome_cards = WelcomeCard.objects.all()
    
    # Nilai Perusahaan #
    company_values = CompanyValue.objects.all()
    company_profile = ValueDescription.objects.first()
    
    # Terpercaya
    trusted_brands = TrustedBrand.objects.all()
    grouped_brands = list(chunker(trusted_brands, 5))
    
    # Testimoni
    testimonials = Testimonial.objects.all()
    grouped_testimonials = list(chunker(testimonials, 3))
    
    # FAQ
    faqs = FAQ.objects.all()
    
    return render(request, 
                  'homepage.html', 
                  {'welcome_cards': welcome_cards,  
                  'company_values': company_values,
                  'company_profile': company_profile,
                  'trusted_brands': grouped_brands,
                  'grouped_testimonials': grouped_testimonials,
                  'faqs': faqs})
    

def about(request):
    structures = Structur.objects.all()
    mission = Mission.objects.all()
    about_details = About.objects.first()
    return render(request, 'about.html', 
                  {'about_details': about_details,
                   'mission': mission,
                   'structures': structures
                   })
    
def tim(request):
    
    tim_details = Tim.objects.first()
    value = Value.objects.all()
    pencapaian = Pencapaian.objects.all()
    target = Target.objects.all()
    return render(request, 'tim.html', 
                  {'tim_details': tim_details,
                   'value': value,
                   'pencapaian': pencapaian,
                   'target': target,
                   })
    
def galeri(request):
    # Ambil data GaleriUtama pertama (judul dan deskripsi utama galeri)
    galeri_utama = GaleriUtama.objects.first()

    # Ambil semua galeri dan item terkait
    galeri_list = Galeri.objects.prefetch_related('items').all()

    # Group items menjadi batch per galeri
    galeri_data = []
    for galeri in galeri_list:
        if galeri.items.exists():  # Pastikan galeri memiliki item
            grouped_items = list(chunker(galeri.items.all(), 2))  # Kelompokkan item per 3
            galeri_data.append({
                'galeri': galeri,
                'items': grouped_items,
            })

    return render(request, 'galeri.html', {
        'galeri_utama': galeri_utama,
        'galeri_data': galeri_data,
        'galeri_list': galeri_list,
    })
    
def kontak(request):
    kontak_info = Kontak.objects.first()
    working_hours = Kerja.objects.all()
    address_info = Alamat.objects.all()
    if request.method == 'POST':
        from_email = request.POST.get('from')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send an email
        send_mail(
            subject,
            message,
            from_email,
            [settings.EMAIL_HOST_USER],  # Recipient list
            fail_silently=False,
        )
        messages.success(request, 'Email sudah berhasil di kirim')
    return render(request, 'kontak.html', {
        'kontak_info': kontak_info,
        'working_hours': working_hours,
        'address_info': address_info
    })
    

from django.db.models import Q

def blog_list(request):
    posts = BlogPost.objects.all()
    recent_posts = BlogPost.objects.order_by('-publish_date')[:3]
    search_query = request.GET.get('search', '')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        ).distinct()

    context = {
        'posts': posts,
        'recent_posts': recent_posts,
        'blog_main': BlogUtama.objects.first()
    }
    return render(request, 'blog.html', context)

@login_required
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all()
    related_posts = post.related_posts.all()
    if request.method == 'POST' and 'comment' in request.POST:
        comment_content = request.POST.get('comment')
        if comment_content:
            Comment.objects.create(post=post, user=request.user, content=comment_content)
            messages.success(request, "Your comment has been posted.")
            return redirect('blog_detail', pk=post.pk)

    context = {
        'post': post,
        'comments': comments,
        'related_posts': related_posts
    }
    return render(request, 'blog_detail.html', context)

@login_required
def blog_like(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        messages.info(request, "You disliked the post.")
    else:
        post.likes.add(request.user)
        messages.success(request, "You liked the post.")
    return redirect('blog_detail', pk=pk)


# =========================================================================
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm
from .models.home.user import Profile

def user_login(request):
    """
    Fungsi ini menangani proses login pengguna baik melalui form tradisional maupun sosial.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        next_url = request.POST.get('next')  # Mendapatkan 'next' dari form
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Anda berhasil login.')
                    if next_url:
                        return redirect(next_url)
                    else:
                        return redirect('dashboard')
                else:
                    messages.error(request, 'Akun Anda dinonaktifkan.')
            else:
                messages.error(request, 'Username atau password tidak valid.')
    else:
        form = LoginForm()
        next_url = request.GET.get('next')  # Mendapatkan 'next' dari URL

    return render(request, 'account/login.html', {'form': form, 'next': next_url})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Membuat objek user baru tetapi belum menyimpannya
            new_user = user_form.save(commit=False)
            # Menetapkan password yang dipilih
            new_user.set_password(user_form.cleaned_data['password'])
            # Menyimpan objek User
            new_user.save()
            
            # Menggunakan get_or_create untuk menghindari duplikasi
            profile, created = Profile.objects.get_or_create(
                user=new_user,
                defaults={
                    'date_of_birth': None,  # Set default value
                }
            )
            
            # Jika Profile sudah ada dan tidak dibuat baru
            if not created:
                messages.warning(request, 'Profile sudah ada untuk pengguna ini.')
            
            messages.success(request, 'Registrasi berhasil. Silakan login.')
            return redirect('login')
    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/register.html', {'user_form': user_form})


from django.contrib.auth import logout as auth_logout

def keluar(request):
    auth_logout(request)
    return render(request, 'registration/keluar.html')