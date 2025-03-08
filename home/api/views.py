from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
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
            dept = Department.objects.filter(location_id=loc_id)
            
            # page_number = request.GET.get('page',1)
            # paginator = Paginator(loc,2)
            # serializer = DepartmentSerializer(paginator.page(page_number),many=True)
            serializer = DepartmentSerializer(dept,many=True)
            return Response({
                'data': serializer.data,
                'message': 'data fetched successfully'
            },status=status.HTTP_200_OK)
        
        except Exception as e:
                return Response({
                        'data': {},
                        'message': 'something went wrong'
                    },status=status.HTTP_400_BAD_REQUEST)


class cat_by_dept_loc(APIView):
    def get(self,request,loc_id,dep_id):
        try:
            dept = Department.objects.filter(location_id=loc_id)
            # print(dept)
            categories = Category.objects.select_related("department").all()  # 1 Query
            q=[]
            for category in categories:
                if (category.department.id==dep_id):
                    q.append(category) 

            # cat = Category.objects.filter(department_id = dep_id)
            print(q)
            serializer = CategorySerializer(q,many=True)
            return Response({
                'data': serializer.data,
                'message': 'data fetched successfully'
            },status=status.HTTP_200_OK)
        except Exception as e:
                return Response({
                        'data': {},
                        'message': 'something went wrong'
                    },status=status.HTTP_400_BAD_REQUEST)
    
#/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory#

class Scat_cat_dep_loc(APIView):
     def get(self,request,loc_id,dep_id,cat_id):
        try:
            #    print('77777777777777777')
               loc = Location.objects.filter(id=loc_id)
            #    print('till')
               deps = Department.objects.select_related("location").all()
            #    print(deps)
            #    cats = Category.objects.filter(department_id=dep_id)
               c = Category.objects.select_related('department').all()
               
               sub_cat = SubCategory.objects.select_related('category')
               serializer = SubCategorySerializer(sub_cat,many=True)
               return Response({
                    'data': serializer.data,
                    'message': 'data fetched successfully'
                },status=status.HTTP_200_OK)
        except Exception as e:
                    return Response({
                            'data': {},
                            'message': 'something went wrong'
                        },status=status.HTTP_400_BAD_REQUEST)
        
class sub_by_cat_dept_loc(APIView):
    def get(self,request,loc_id,dep_id,cat_id,sub_cat_id):
        try:
            loc = Location.objects.filter(id=loc_id)
    #    print('till')
            deps = Department.objects.select_related("location").all()
    #    print(deps)
    #    cats = Category.objects.filter(department_id=dep_id)
            c = Category.objects.select_related('department').all()
        
            sub_cat = SubCategory.objects.select_related('category')
            sub_cat = sub_cat.filter(id=sub_cat_id)
            serializer = SubCategorySerializer(sub_cat,many=True)
            return Response({
                'data': serializer.data,
                'message': 'data fetched successfully'
            },status=status.HTTP_200_OK)
        except Exception as e:
                    return Response({
                            'data': {},
                            'message': 'something went wrong'
                        },status=status.HTTP_400_BAD_REQUEST)