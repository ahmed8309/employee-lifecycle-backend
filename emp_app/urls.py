# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import DepartmentViewSet, EmployeeViewSet, TaskStatusViewSet, retry_task

# router = DefaultRouter()
# router.register(r'departments', DepartmentViewSet)
# router.register(r'employees', EmployeeViewSet)
# router.register(r'tasks', TaskStatusViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('tasks/<int:task_id>/retry/', retry_task, name='retry-task'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, TaskStatusViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'tasks', TaskStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

