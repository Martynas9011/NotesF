from django.shortcuts import render, redirect
from .models import Category, Document


# Create your views here.

def index(request):
    return render(request, 'index.html')


# def show_category(request):
#     category = Category.objects.values(all)
#
#     context = {
#         'category': category
#     }
#
#     return render(request, 'show_category.html', context)

#
# def show_orders(request):
#     orders = Order.objects.filter(vehicle__model__brand__startswith='Brand').all()
#     return render(request, 'show_orders.html', context={'orders': orders})

# def show_note(request):
#     docid = int(request.GET.get('docid', 0))
#     document = Document.objects.all()
#
#     if request.method == 'POST':
#         docid = int(request.POST.get('docid', 0))
#         title = request.POST.get('title')
#         content = request.POST.get('content', '')
#
#         if docid > 0:
#             document = Document.objects.get(pk=docid)
#             document.title = title
#             document.content = content
#             document.save()
#
#             return redirect('/?docid=%i' % docid)
#         else:
#             document = Document.objects.create(title=title, content=content)
#
#             return redirect('/?docid=%i' % document.id)
#
#     if docid > 0:
#         document = Document.objects.get(pk=docid)
#     else:
#         document = ''
#
#     context = {
#         'docid': docid,
#         'documents': documents
#         'document': document
#     }
#
#     return render(request, 'index.html', context)

def show_note(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.save()

            return redirect('/?docid=%i' % docid)
        else:
            document = Document.objects.create(title=title, content=content)

            return redirect('/?docid=%i' % document.id)

    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document': document
    }

    return render(request, 'index.html', context)

def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect('/?docid=0')