# views.py - Xử lý logic cho từng trang của ứng dụng Home
# Mỗi hàm nhận request từ người dùng, xử lý dữ liệu và trả về template HTML

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *    # Import tất cả models
from .utils import *     # Import các hàm tiện ích (search, pagination)
from .forms import *     # Import các form


def HomePage(request):
    """
    Trang chủ - hiển thị danh sách phim và phim bộ
    - Hỗ trợ tìm kiếm theo từ khóa
    - Phân trang 9 phim mỗi trang
    - Hiển thị phim phổ biến nhất và phim bộ mới nhất
    """
    # Lọc phim theo từ khóa tìm kiếm
    Movies, search_query, serials = searchMovies_Serials(request)
    # Phân trang, 9 phim mỗi trang
    custom_range, Movies = paginateMovies(request, Movies, 9)
    # Lấy tất cả thể loại để hiển thị trên navbar
    Navbar_genre = Genre.objects.all()
    # Lấy phim phổ biến nhất (sắp xếp theo lượt xem giảm dần)
    Most_views_movies = HomePageModel.objects.all().order_by('-page_view')
    # Lấy tất cả phim bộ
    Serials_new = Serial.objects.all()

    context = {
        'movies': Movies,
        'serials': serials,
        'popular': Most_views_movies,
        'genres': Navbar_genre,
        'search_query': search_query,
        'custom_range': custom_range,
        'new_serials': Serials_new
    }
    return render(request, 'Home/home.html', context)


def SingleSerialPage(request, pk):
    """
    Trang chi tiết phim bộ
    - pk: UUID của phim bộ
    - Xử lý POST để lưu bình luận mới
    - Hiển thị phim bộ tương tự cùng thể loại
    """
    # Lấy phim bộ theo ID, báo lỗi 404 nếu không tìm thấy
    serial = Serial.objects.get(id=pk)
    forms = CommentsFormSerial()

    # Xử lý khi người dùng gửi bình luận
    if request.method == 'POST':
        form = CommentsFormSerial(request.POST)
        review = form.save(commit=False)   # Chưa lưu vào DB
        review.serial_page = serial        # Gán phim bộ cho bình luận
        review.save()                      # Lưu vào DB
        return redirect('single-serial', pk=serial.id)

    # Tăng lượt xem
    serial.page_view = serial.page_view + 1
    # Lấy tất cả phim lẻ để hiển thị phần "New Movies"
    Movies = HomePageModel.objects.all()
    # Lấy phim bộ tương tự (cùng thể loại)
    Similar_Serials = Serial.objects.all().distinct().filter(genre__in=serial.genre.all())
    Navbar_genre = Genre.objects.all()
    # Lấy tất cả bình luận của phim bộ này
    comments_all = serial.comments_serial.all()

    context = {
        'serial': serial,
        'similar': Similar_Serials,
        'view': serial.page_view,
        'genres': Navbar_genre,
        'movies': Movies,
        'comments_all': comments_all,
        'forms': forms
    }
    return render(request, 'Home/single-serial.html', context)


def SingleMoviePage(request, pk):
    """
    Trang chi tiết phim lẻ
    - pk: UUID của phim
    - Xử lý POST để lưu bình luận mới
    - Hiển thị phim tương tự cùng thể loại
    """
    # Lấy phim theo ID
    Movie = HomePageModel.objects.get(id=pk)
    forms = CommentsForm()

    # Xử lý khi người dùng gửi bình luận
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        review = form.save(commit=False)
        review.movie_page = Movie          # Gán phim cho bình luận
        review.save()
        return redirect('single-movie', pk=Movie.id)

    # Tăng lượt xem
    Movie.page_view = Movie.page_view + 1
    # Lấy tất cả phim cho phần "New Items"
    Movies = HomePageModel.objects.all()
    # Lấy phim tương tự (cùng thể loại, loại bỏ trùng lặp)
    Similar_Movies = HomePageModel.objects.all().filter(genre__in=Movie.genre.all()).distinct()
    Navbar_genre = Genre.objects.all()
    Serials = Serial.objects.all()
    # Lấy tất cả bình luận của phim này
    comments_all = Movie.comments.all()

    context = {
        'movie': Movie,
        'movies': Movies,
        'similar': Similar_Movies,
        'view': Movie.page_view,
        'genres': Navbar_genre,
        'serials': Serials,
        'forms': forms,
        'comments_all': comments_all
    }
    return render(request, 'Home/single-movie.html', context)


def SingleGenrePage(request, pk):
    """
    Trang danh sách phim theo thể loại
    - pk: UUID của thể loại
    - Hiển thị cả phim lẻ và phim bộ thuộc thể loại đó
    """
    genre = Genre.objects.get(id=pk)
    # Lọc phim lẻ theo thể loại
    Movies_filtered = HomePageModel.objects.all().filter(genre=genre).distinct()
    # Lọc phim bộ theo thể loại
    Serials_filtered = Serial.objects.all().filter(genre=genre).distinct()
    Movies = HomePageModel.objects.all()
    Navbar_genre = Genre.objects.all()
    Serials = Serial.objects.all()

    context = {
        'genre': genre,
        'movies_filtered': Movies_filtered,
        'serials_filtered': Serials_filtered,
        'movies': Movies,
        'genres': Navbar_genre,
        'serials': Serials
    }
    return render(request, 'Home/single-genre.html', context)


def SingleDirectorPage(request, pk):
    """
    Trang danh sách phim theo đạo diễn
    - pk: UUID của đạo diễn
    - Hiển thị cả phim lẻ và phim bộ của đạo diễn đó
    """
    director = Director.objects.get(id=pk)
    # Lọc phim lẻ theo đạo diễn
    Movies_filtered = HomePageModel.objects.all().filter(director=director).distinct()
    # Lọc phim bộ theo đạo diễn
    Serials_filtered = Serial.objects.all().filter(director=director).distinct()
    Movies = HomePageModel.objects.all()
    Navbar_genre = Genre.objects.all()
    Serials = Serial.objects.all()

    context = {
        'director': director,
        'movies_filtered': Movies_filtered,
        'serials_filtered': Serials_filtered,
        'movies': Movies,
        'genres': Navbar_genre,
        'serials': Serials
    }
    return render(request, 'Home/single-director.html', context)


def FeedbackPage(request):
    """
    Trang phản hồi - cho phép người dùng gửi góp ý
    - GET: hiển thị form trống
    - POST: lưu phản hồi và chuyển đến trang thành công
    """
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback-success')  # Chuyển đến trang thành công

    Navbar_genre = Genre.objects.all()
    context = {'form': form, 'genres': Navbar_genre}
    return render(request, 'Home/feedback.html', context)


def FeedbackSuccess(request):
    """Trang thông báo gửi phản hồi thành công"""
    Navbar_genre = Genre.objects.all()
    context = {'genres': Navbar_genre}
    return render(request, 'Home/feedback-success.html', context)


def AboutPage(request):
    """Trang giới thiệu về LuminaPhim"""
    Navbar_genre = Genre.objects.all()
    context = {'genres': Navbar_genre}
    return render(request, 'Home/about.html', context)
