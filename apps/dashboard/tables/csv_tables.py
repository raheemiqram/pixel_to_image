from ajax_datatable.views import AjaxDatatableView

from apps.image_builder.models import OriginalImage


class ImageAjaxDatatableView(AjaxDatatableView):
    model = OriginalImage
    title = 'Images'
    initial_order = [["created", "desc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'csv_file', 'visible': True, },
        {'name': 'original_image', 'visible': True, },
        {'name': 'original_size', 'title': 'Original Size', 'placeholder': True, 'searchable': False,
         'orderable': False, },
        {'name': 'resize', 'title': 'Resize', 'placeholder': True, 'searchable': False, 'orderable': False, },
        {'name': 'resize_image', 'title': 'Resize', 'placeholder': True, 'searchable': False, 'orderable': False, },
        {'name': 'created', 'visible': True, },
        {'name': 'actions', 'title': 'Actions', 'placeholder': True, 'searchable': False, 'orderable': False, },
    ]

    def customize_row(self, row, obj):
        row['actions'] = f'<a href="/dashboard/image_builder/build/{obj.id}" class="btn btn-info">Build </a>'
        row['original_size'] = f'{obj.original_width} X {obj.original_height}'
        row['resize'] = f'{obj.resized_width} X {obj.resized_height}'
        if obj.original_width:
            row[
                'original_image'] = f'<a href="{obj.original_image.url}"><img width=20 height=100 src="{obj.original_image.url}"/> </a>'
        else:
            row['original_image'] = "N/A"

        if obj.resized_image:
            row[
                'resize_image'] = f'<a href="{obj.resized_image.url}"><img width=20 height=100 src="{obj.resized_image.url}"/> </a>'
        else:
            row['resize_image'] = "N/A"
