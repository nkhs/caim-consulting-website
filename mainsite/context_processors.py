from mainsite.models import Advisor, Client, Service


def all_services(request):
    services = Service.objects.all()
    return {"services": services}


def all_advisors(request):
    advisors = Advisor.objects.all()
    return {"advisors": advisors}


def all_clients(request):
    clients = Client.objects.all()
    return {"clients": clients}
