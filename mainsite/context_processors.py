from mainsite.models import Service, Advisor


def all_services(request):
    services = Service.objects.all()
    return {"services": services}


def all_advisors(request):
    advisors = Advisor.objects.all()
    return {"advisors": advisors}
