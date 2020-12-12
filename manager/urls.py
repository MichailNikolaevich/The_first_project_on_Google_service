from django.urls import path

from manager.views import hello, bui, MyPage, AddLikeComment, DelComment, DelBook, AddRate2Book, BookDetail

urlpatterns =[
    path("hello/<int:digit>/", hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
    path('goodbye/', bui),
    path('add_like_comment/<int:id>/', AddLikeComment.as_view(), name="add-like-comment"),
    path('del_book/<int:id>/', DelBook.as_view(), name="del-book"),
    path('del_comment/<int:id>/', DelComment.as_view(), name="del-comment"),
    path('add_rate_to_book/<int:id>/<int:rate>/', AddRate2Book.as_view(), name='add-rate'),
    path('add_rate_to_book/<int:id>/<int:rate>/<str:location>', AddRate2Book.as_view(), name='add-rate-location'),
    path('book_view_detail/<int:id>/', BookDetail.as_view(), name="book-detail"),
    path('', MyPage.as_view(), name='the-main-page')


]

