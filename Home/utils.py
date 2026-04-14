# utils.py - Các hàm tiện ích dùng chung trong ứng dụng Home
# Bao gồm: phân trang và tìm kiếm phim

from .models import *
from django.db.models import Q                                        # Q object cho phép tìm kiếm phức tạp (OR, AND)
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # Công cụ phân trang của Django


def paginateMovies(request, movies, results):
    """
    Hàm phân trang danh sách phim
    
    Tham số:
        request: HTTP request (để lấy số trang từ query string ?page=)
        movies: QuerySet danh sách phim cần phân trang
        results: Số phim hiển thị mỗi trang
    
    Trả về:
        custom_range: Dải số trang để hiển thị nút phân trang (vd: 1,2,3,4,5)
        movies: QuerySet phim của trang hiện tại
    """
    page = request.GET.get('page')  # Lấy số trang từ URL (?page=2)
    paginator = Paginator(movies, results)  # Tạo paginator với số phim mỗi trang

    try:
        movies = paginator.page(page)  # Lấy phim của trang được yêu cầu

    except PageNotAnInteger:
        # Nếu page không phải số (vd: ?page=abc) -> về trang 1
        page = 1
        movies = paginator.page(page)

    except EmptyPage:
        # Nếu page vượt quá số trang tối đa -> về trang cuối
        page = paginator.num_pages
        movies = paginator.page(page)

    # Tính dải số trang hiển thị (tối đa 9 trang xung quanh trang hiện tại)
    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1  # Không cho nhỏ hơn trang 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1  # Không cho vượt quá trang cuối

    custom_range = range(leftIndex, rightIndex)  # Dải số trang để render nút bấm

    return custom_range, movies


def searchMovies_Serials(request):
    """
    Hàm tìm kiếm phim và phim bộ theo từ khóa
    
    Tìm kiếm trong các trường:
        - Tên phim/phim bộ
        - Giới thiệu ngắn
        - Tóm tắt nội dung
        - Tên đạo diễn
        - Tên thể loại
    
    Trả về:
        movies: QuerySet phim lẻ phù hợp
        search_query: Từ khóa tìm kiếm (chuỗi rỗng nếu không có)
        serials: QuerySet phim bộ phù hợp
    """
    search_query = ''  # Mặc định không có từ khóa -> trả về tất cả

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')  # Lấy từ khóa từ URL (?search_query=...)

    # Tìm kiếm phim lẻ - dùng Q object để tìm trong nhiều trường cùng lúc (OR)
    # icontains: tìm kiếm không phân biệt hoa thường
    movies = HomePageModel.objects.distinct().filter(
        Q(title__icontains=search_query) |           # Tìm theo tên phim
        Q(short_intro__icontains=search_query) |     # Tìm theo giới thiệu ngắn
        Q(summary__icontains=search_query) |         # Tìm theo tóm tắt
        Q(director__name__icontains=search_query) |  # Tìm theo tên đạo diễn
        Q(genre__name__icontains=search_query)       # Tìm theo thể loại
    )

    # Tìm kiếm phim bộ tương tự
    serials = Serial.objects.distinct().filter(
        Q(Serial_name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(summary__icontains=search_query) |
        Q(director__name__icontains=search_query) |
        Q(genre__name__icontains=search_query)
    )

    return movies, search_query, serials
