from django.urls import path, include

from apps.dashboard.tables.csv_tables import ImageAjaxDatatableView
from apps.dashboard.tables.user_tables import UserAjaxDatatableView
from apps.dashboard.views import DashboardIndexView, DashboardEmptyView, DashboardLoginView

urlpatterns = [
    # ...
    path('', DashboardIndexView.as_view(), name='dashboard_index'),
    path('empty/', DashboardEmptyView.as_view(), name='dashboard_empty'),

    # ...

    # image builder
    path('image_builder/', include('apps.image_builder.urls')),


    # LOGIN
    path('login/', DashboardLoginView.as_view(), name='dashboard_login'),

    # TABLES
    path('table/users/', UserAjaxDatatableView.as_view(), name='dashboard_user_table'),
    path('table/csv/', ImageAjaxDatatableView.as_view(), name='dashboard_csv_table'),
    # ...

]
