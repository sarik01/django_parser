from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import \
    write_offs, invoice_import, comp_ing_import, without_relations


@csrf_exempt
def create_table_from_excel_view(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        table_name = request.POST.get('table_name', 'default_table_name')

        if file:
            # process_excel_and_create_insert(file, table_name)
            response = comp_ing_import(file)
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse({'error': 'File not provided'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
