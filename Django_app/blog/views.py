from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


# ListView 로 html 페이지에 데이터 전달
class PostList(ListView):
    model = Post

    # 포스트 생성 날짜 순으로 정렬
    def get_queryset(self):
        return Post.objects.order_by('-date')

# def index(request):
#
#     posts = Post.objects.all()
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts
#         }
#     )
