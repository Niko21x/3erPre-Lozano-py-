
from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm
from django import forms


def home(request):
    return render(request, 'base.html')

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
           
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        print(request.POST)
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.categoria, created = Categoria.objects.get_or_create(nombre='nombre_de_la_categoria_predeterminada')
            producto.save()
            form.save_m2m()
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form})



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']  # Eliminamos 'categoria'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'descripcion'}),
        }

def buscar(request):
    if request.method == 'POST':
        buscar_texto = request.POST.get('buscar_texto')
        categorias = Categoria.objects.filter(nombre__icontains=buscar_texto)
        productos = Producto.objects.filter(nombre__icontains=buscar_texto)
        clientes = Cliente.objects.filter(nombre__icontains=buscar_texto)
        return render(request, 'buscar_resultados.html', {'categorias': categorias, 'productos': productos, 'clientes': clientes})
    return render(request, 'buscar.html')



