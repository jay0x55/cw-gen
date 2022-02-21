from django.shortcuts import render
from django.views.generic import TemplateView
from .cw import xmr_wallet, doge_wallet


class Index(TemplateView):
    template_name = "index.html"


class Wallet(TemplateView):
    def get(self, request, format=None):
        data = {"xmr": xmr_wallet(), "doge": doge_wallet()}
        return render(request, 'wallet.html', context=data, status=200)

