# views.py

from django.shortcuts import render, redirect
from rest_framework import generics, filters
from .models import Cliente
from .serializers import ClienteSerializer
from django.views.generic import ListView
from .models import Cliente
from .forms import ClienteForm
from django.core.paginator import Paginator

class ClienteListCreateAPI(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['dni', 'nombre', 'direccion']

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 3  # Muestra 10 clientes por página

def cliente_create_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente-list')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

def cliente_update_view(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente-list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form})

def cliente_delete_view(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente-list')
    return render(request, 'cliente_confirm_delete.html', {'cliente': cliente})
