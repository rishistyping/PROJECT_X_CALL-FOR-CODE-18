from django.views.generic import TemplateView

class AddBoardView(TemplateView):
    template_name = "board/add_board.html"