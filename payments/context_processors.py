from .models import BankDetail

def payment_info(request):
    return {
        'bank_info': BankDetail.objects.filter(is_active=True).first()
    }