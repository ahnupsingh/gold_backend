from math import ceil
from typing import Tuple


def get_pagination_values(page: int, offset: int, page_size: int) -> Tuple[int, int, int]:
    if page < 1:
        page = 1

    if page_size > 50:
        page_size = 50

    if offset < 0:
        offset = 0

    return page, offset, page_size


def get_page(queryset, page: int, offset: int, page_size: int, is_already_serialized=False):
    page, offset, page_size = get_pagination_values(page, offset, page_size)
    paginated_queryset = queryset[(page - 1) * page_size + offset:page * page_size + offset]
    total_count = 0
    if queryset:
        if is_already_serialized:
            total_count = len(queryset)
        else:
            total_count = queryset.count()
    total_pages = ceil(total_count / page_size)

    return paginated_queryset, {
        'page': page, 'offset': offset, 'page_size': page_size,
        'pages': total_pages, 'total_count': total_count
    }


def get_page_request_fields(request) -> Tuple[int, int, int]:
    page = int(request.GET.get('page', 1))
    offset = int(request.GET.get('offset', 0))
    page_size = int(request.GET.get('page_size', 50))

    return page, offset, page_size


def get_page_post_request_fields(request) -> Tuple[int, int, int]:
    page = int(request.data.get('page', 1))
    offset = int(request.data.get('offset', 0))
    page_size = int(request.data.get('page_size', 50))

    return page, offset, page_size
