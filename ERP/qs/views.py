from django.shortcuts import render,HttpResponse
# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import JsonResponse
# from .models import HeadOfficeModule, ProjectSpecificModule
# from django.views.decorators.csrf import csrf_exempt
# import json
# # Create your views here.

def vindex(request):
    return HttpResponse("Welcom to Index Page")

# # Home page view
# def home(request):
#     head_office_modules = HeadOfficeModule.objects.all()
#     project_modules = ProjectSpecificModule.objects.all()
#     return render(request, 'home.html')
# # def home(request):
# #     head_office_modules = HeadOfficeModule.objects.all()
# #     project_modules = ProjectSpecificModule.objects.all()
# #     return render(request, 'home.html', {
# #         'head_office_modules': head_office_modules,
# #         'project_modules': project_modules,
# #     })

# # AJAX Add Module

# @csrf_exempt  # Remove this if CSRF protection is required
# def add_module(request):
#     print("GET")
#     if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         print ("POST")
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             category = data.get('category')
#             name = data.get('name')
#             description = data.get('description')
#             module_type = data.get('module_type')
#             sub_items = json.dumps(data.get('sub_items', []))  # Ensure it's stored as JSON

#             if category == 'head_office':
#                 module = HeadOfficeModule.objects.create(
#                     name=name, description=description, module_type=module_type, sub_items=sub_items
#                 )
#             else:
#                 module = ProjectSpecificModule.objects.create(
#                     name=name, description=description, module_type=module_type, sub_items=sub_items
#                 )

#             return JsonResponse({
#                 'id': module.id,
#                 'name': module.name,
#                 'description': module.description,
#                 'module_type': module.module_type,
#                 'sub_items': json.loads(module.sub_items),  # Convert JSON string back to list
#                 'category': category,
#             }, safe=False)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request'}, status=400)

# # AJAX Edit Module
# @csrf_exempt
# def edit_module(request):
#     if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             module_id = data.get('id')
#             category = data.get('category')
#             name = data.get('name')
#             description = data.get('description')
#             sub_items = json.dumps(data.get('sub_items', []))  # Store as JSON
#             module_type = data.get('module_type')

#             if category == 'head_office':
#                 module = get_object_or_404(HeadOfficeModule, id=module_id)
#             else:
#                 module = get_object_or_404(ProjectSpecificModule, id=module_id)

#             module.name = name
#             module.description = description
#             module.sub_items = sub_items
#             module.module_type = module_type
#             module.save()

#             return JsonResponse({
#                 'id': module.id,
#                 'name': module.name,
#                 'description': module.description,
#                 'module_type': module.module_type,
#                 'sub_items': json.loads(module.sub_items),  # Convert back to list
#             }, safe=False)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request'}, status=400)

# # AJAX Delete Module
# @csrf_exempt
# def delete_module(request):
#     if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             module_id = data.get('id')
#             category = data.get('category')

#             if category == 'head_office':
#                 module = get_object_or_404(HeadOfficeModule, id=module_id)
#             else:
#                 module = get_object_or_404(ProjectSpecificModule, id=module_id)

#             module.delete()
#             return JsonResponse({'status': 'success'}, safe=False)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request'}, status=400)