from __future__ import unicode_literals

from django.shortcuts import render


def view_category_board(request):
    return render(request, 'category/category_base.html', {
        'evidence_list': [
            {
                'time_elapsed': str(i) + ' hrs ago',
                'tags': ['tag #' + str(n) for n in [1, 2, 3]]
            } for i in [1, 2, 3, 4, 5]
        ],
        'contributors': [
            {'name': 'Jane Doe', 'role': 'practitioner'},
            {'name': 'Miley Jennifer', 'role': 'researcher'},
            {'name': 'Elaine Lwane', 'role': 'chairman'}
        ]
    })