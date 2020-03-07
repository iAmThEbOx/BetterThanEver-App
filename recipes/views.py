from django.shortcuts import render

from .models import Recipe

def fruit(request, *args, **kwargs):
    context = {
        'title': 'Fruit-Focused Recipes',
        'description': "Fruit has been recognized as a good source of vitamins and minerals, and for their role in preventing vitamin C and vitamin A deficiencies. People who eat fruit as part of an overall healthy diet generally have a reduced risk of chronic diseases. USDA's MyPlate encourages making half your plate fruits and vegetables for healthy eating. Our easy-to-make fruit recipes will bring you all these benefits in the form of a delicious meal to making eating healthy easier than ever!",
        'recipes': Recipe.objects.filter(category='FR'),
    }
    return render(request, template_name='recipes/landing.html', context=context)

def veg(request, *args, **kwargs):
    context = {
        'title': 'Vegetable-Focused Recipes',
        'description': "Eating vegetables provides health benefits – people who eat more vegetables and fruits as part of an overall healthy diet are likely to have a reduced risk of some chronic diseases. Vegetables provide nutrients vital for health and maintenance of your body. USDA's MyPlate encourages making half your plate fruits and vegetables for healthy eating. Our easy-to-make vegetable recipes will bring you all these benefits in the form of a delicious meal to making eating healthy easier than ever!",
        'recipes': Recipe.objects.filter(category='VE'),
    }
    return render(request, template_name='recipes/landing.html', context=context)

def meat(request, *args, **kwargs):
    context = {
        'title': 'Meat-Focused Recipes',
        'description': "Meat and poultry contain protein, which is important for growth and development, and other nutrients your body needs, such as iodine, iron, zinc and vitamin B12. Despite health controversies around various types of meat, avoiding processed meats to minimise your intake of salt and saturated fat, and choosing lean cuts of meat and poultry, will make it a greatly beneficial and filling part of your diet. Our easy-to-make meat recipes will bring you all these benefits, without most of the disadvantages, in the form of a delicious meal to making eating healthy easier than ever!",
        'recipes': Recipe.objects.filter(category='ME'),
    }
    return render(request, template_name='recipes/landing.html', context=context)

def grains(request, *args, **kwargs):
    context = {
        'title': 'Grain-Focused Recipes',
        'description': "People who eat whole grains as part of a healthy diet have a reduced risk of some chronic diseases. Grains are important sources of many nutrients, including fiber, B vitamins (thiamin, riboflavin, niacin and folate) and minerals (iron, magnesium and selenium), helping reduce blood cholesterol levels, lowering risk of heart disease, and redicung constipation. USDA's MyPlate recommends making half of your daily grain choices whole grain for healthy eating. Our easy-to-make grain-based recipes will bring you all these benefits in the form of a delicious meal to making eating healthy easier than ever!",
        'recipes': Recipe.objects.filter(category='GR'),
    }
    return render(request, template_name='recipes/landing.html', context=context)

def carbs(request, *args, **kwargs):
    context = {
        'title': 'Carb-Focused Recipes',
        'description': "Aside from being the main energy source for the body, carbohydrates play a role in glucose and insulin metabolism, as well as cholesterol and triglyceride metabolism and fermentation. When carbohydrates are digested, they are broken down into glucose to be either used as energy or stored in the liver and muscles for future use. Our easy-to-make carb-based recipes will bring you all these benefits in the form of a delicious meal to making eating healthy easier than ever!",
        'recipes': Recipe.objects.filter(category='CA'),
    }
    return render(request, template_name='recipes/landing.html', context=context)

def dessert(request, *args, **kwargs):
    context = {
        'title': 'Healthy Dessert Recipes',
        'description': "A delicious dessert doesn't have to be a high-calorie, high-fat disaster, either: they just have to integrate smart choices and substitutions in the cooking process, such as steering clear of fatty ingredients like creamy whipped topping or butter, and sticking with fresh fruit and low-fat choices.  Our easy-to-make healthy dessert recipes will satisfy your sweet tooth without compromising your wellbeing through substitutions and creative ingredients that will make your desserts both tastier AND healthier than ever!",
        'recipes': Recipe.objects.filter(category='DE'),
    }
    return render(request, template_name='recipes/landing.html', context=context)

def catalog(request, *args, **kwargs):
    return render(request, template_name='recipes/catalog.html')
