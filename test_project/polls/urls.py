from django.urls import path
from .views import (
    index, 
    detail, 
    results, 
    vote, 
    get_popular_choices, 
    PollIndex, 
    assign_can_view_results_permission,
    BooksListView,
    UploadUserDocuments
)

urlpatterns = [
    path('poll-index/', index, name='index'),
    path('poll-index_class/', PollIndex.as_view(), name='cb_index'),
    path('detail/<int:question_id>/', detail, name='detail'),
    path('results/', results, name='results'),
    path('question/vote/<int:choice_id>/', vote, name='vote'),
    path('get-popular-choices/', get_popular_choices, name='get_popular_choices'),
    path(
        'assign-view-results-permission', 
        assign_can_view_results_permission, 
        name='assingn_permission'
    ),
    path('books-list/', BooksListView.as_view(), name='books_list'),
    path('upload-docs/', UploadUserDocuments.as_view(), name='upload_documents'),
]