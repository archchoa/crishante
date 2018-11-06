from .models import Section


def links(request):
    sections = Section.objects.all()
    return {'gallery_links': sections}
