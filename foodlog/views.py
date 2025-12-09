from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Food
from .forms import FoodForm

def food_list_create(request):
    if request.method == 'POST' and 'add_food' in request.POST:
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food:list')
    else:
        form = FoodForm()

    foods = Food.objects.order_by('-created')
    total = foods.aggregate(total_calories=Sum('calories'))['total_calories'] or 0

    return render(request, 'foodlog/list.html', {'form': form, 'foods': foods, 'total_calories': total})

def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('food:list')
    return render(request, 'foodlog/confirm_delete.html', {'food': food})
