from django.urls import path 
from .views import CocuyListView, BlogCreateView

urlpatterns = [
    
    path("",CocuyListView.as_view(), name="home"),# si no le pones la coma el de abjao no funciona debido a que es un array y los array se separan por coma
    path("post/new/",BlogCreateView.as_view(), name="post_new"),


]
