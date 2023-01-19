from django.shortcuts import render, redirect
from .models import Category, Document


# Create your views here.

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

def notes(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        catid = request.POST.get('catid', '')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.catid = Category.objects.get(pk=catid)
            document.save()

            return redirect('/?docid=%i' % docid)
        else:
            document = Document.objects.create(title=title, content=content, catid=Category.objects.get(pk=catid))

            return redirect('/?docid=%i' % document.id)

    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document': document,
        'categories': categories
    }

    return render(request, 'index.html', context)

def categories(request):
    catid = int(request.GET.get('catid', 0))
    categories = Category.objects.all()
    documents = Document.objects.all()

    if request.method == 'POST':
        catid = int(request.POST.get('catid', 0))
        name = request.POST.get('name')

        if catid > 0:
            category = Category.objects.get(pk=catid)
            category.name = name
            category.save()

            return redirect('/categories/?catid=%i' % catid)
        else:
            category = Category.objects.create(name=name)

            return redirect('/categories/?catid=%i' % category.id)

    if catid > 0:
        category = Category.objects.get(pk=catid)
    else:
        category = ''

    context = {
        'catid': catid,
        'categories': categories,
        'documents': documents,
        'category': category,
    }

    return render(request, 'categories.html', context)


def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect('/?docid=0')

def delete_category(request, catid):
    document = Category.objects.get(pk=catid)
    document.delete()

    return redirect('/?catid=0')