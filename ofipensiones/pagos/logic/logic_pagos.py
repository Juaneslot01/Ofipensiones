from ..models import Pagos


def get_pagos():
    pagos = Pagos.objects.all()
    return pagos

def get_pago(pago_pk):
    pago = Pagos.objects.get(pk=pago_pk)
    return pago