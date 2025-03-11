from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import SubCategorySerializer, SkuSerializer, CategorySerializer, LocationSerializer,DepartmentSerializer
from metadata.models import Sku,SubCategory,Category,Location,Department
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

                    

class SkuIndex(APIView):
    def get(self,request):
        try:
            sku = Sku.objects.all()
                  
            page_number = request.GET.get('page',1)
            paginator = Paginator(sku,2)
            serializer = SkuSerializer(paginator.page(page_number),many=True)
            return Response({
                'data': serializer.data,
                'message': 'data fetched successfully'
            },status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                    'data': {},
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
        

# /api/v1/location/{location_id}/department    # 

class dept_by_loc(APIView):
    def get(self,request,loc_id):
        try:
            location = get_object_or_404(Location, id=loc_id)

            # Get Departments under the given Location
            departments = Department.objects.filter(location=location)
            serializer = DepartmentSerializer(departments, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({
                        'data': {},
                        'message': 'something went wrong'
                    },status=status.HTTP_400_BAD_REQUEST)


class cat_by_dept_loc(APIView):
    def get(self,request,loc_id,dep_id):
        try:
            location = get_object_or_404(Location, id=loc_id)
            department = get_object_or_404(Department, id=dep_id, location=location)
            categories = Category.objects.filter(department=department)
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
                return Response({
                        'data': {},
                        'message': 'something went wrong'
                    },status=status.HTTP_400_BAD_REQUEST)
    
#/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory#

class Scat_cat_dep_loc(APIView):
     def get(self,request,loc_id,dep_id,cat_id):
        try:
            location = get_object_or_404(Location, id=loc_id)

        # Validate Department under Location
            department = get_object_or_404(Department, id=dep_id, location=location)

            # Validate Category under Department
            category = get_object_or_404(Category, id=cat_id, department=department)

            # Get Subcategories under the given Category
            subcategories = SubCategory.objects.filter(category=category)
            serializer = SubCategorySerializer(subcategories, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
                    return Response({
                            'data': {},
                            'message': 'something went wrong'
                        },status=status.HTTP_400_BAD_REQUEST)
        
class sub_by_cat_dept_loc(APIView):
    def get(self,request,loc_id,dep_id,cat_id,sub_cat_id):
        try:
            location = get_object_or_404(Location, id=loc_id)

            department = get_object_or_404(Department, id=dep_id, location=location)

            category = get_object_or_404(Category, id=cat_id, department=department)

            # Validate SubCategory under Category
            subcategory = get_object_or_404(SubCategory, id=sub_cat_id, category=category)

            serializer = SubCategorySerializer(subcategory)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
                    return Response({
                            'data': {},
                            'message': 'something went wrong'
                        },status=status.HTTP_400_BAD_REQUEST)