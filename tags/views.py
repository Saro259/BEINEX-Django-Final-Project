from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from tags.serializer import WriteTagSerializer, ReadTagSerializer
from tags.models import Tags
from django.utils.text import slugify
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from products.filters import SimplePaginationClass
# Create your views here.

class CreateTagView(APIView):

    def post(self, request):
        """Creates a new tag based on provided data, ensuring unique slug generation."""
        serializer = WriteTagSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            tag_object = Tags.objects.create(name=name, slug=slugify(name))
            response_data = ReadTagSerializer(instance=tag_object).data 
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagDetailViewV1(APIView):
    def get(self, request, slug):
        """Retrieves and returns the details of a specific tag based on its slug, handling potential tag existence errors."""
        try:
            tag_object = Tags.objects.get(slug=slug)
            response_data = ReadTagSerializer(instance=tag_object).data
            return Response(response_data, status=status.HTTP_200_OK)

        except(Tags.DoesNotExist, Tags.MultipleObjectsReturned):
            return Response({"message":"Tag not found!"}, status=status.HTTP_400_BAD_REQUEST)

class TagDetailViewV2(RetrieveAPIView):
        """Retrieves and returns the details of a specific tag using a generic view approach, leveraging lookup by slug."""
        queryset = Tags.objects.all()
        serializer_class = ReadTagSerializer
        lookup_field = 'slug'



class DeleteTagView1(APIView):
    def delete(self, request, slug):
        """Deletes a specific tag based on its slug, handling potential tag existence errors and returning confirmation of deletion or error messages."""
        try:
            tag_object = Tags.objects.get(slug=slug)
            tag_object.delete()
            return Response({"message": "Tag Deleted"}, status=status.HTTP_200_OK)
        except(Tags.DoesNotExist, Tags.MultipleObjectsReturned):
            return Response({"message":"Tag not found!"}, status=status.HTTP_400_BAD_REQUEST)

class DeleteTagView2(DestroyAPIView):
    """Deletes a specific tag based on its slug using a generic destruction view, with built-in error handling for invalid slugs."""
    queryset = Tags.objects.all()
    lookup_field = 'slug'


class TagListView1(APIView):
    """Retrieves a list of serialized tags available"""
    def get(self, request):
        queryset = Tags.objects.all()
        response_data = ReadTagSerializer(instance=queryset, many=True).data
        return Response(response_data, status=status.HTTP_200_OK)

class TagListView2(ListAPIView):
    """Retreives and returns a paginated list of tags using generic list view approach"""
    queryset = Tags.objects.all()
    serializer_class = ReadTagSerializer
    pagination_class = SimplePaginationClass





