from django.db.models import Q
from rest_framework import generics, status, mixins, permissions, authentication, viewsets
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .serializers import ProductSerializer
from django.http import JsonResponse
from .models import Product


# CBV -- > class Based View

# GET

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# POST
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content' or None)
        if content is None:
            content = title
        serializer.save(content=content)


# GET - POST
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content' or None)
        if content is None:
            content = title
        serializer.save(content=content)

    def get_queryset(self):
        qs = super().get_queryset()
        # q = self.request.GET.get('q')
        q = self.request.query_params.get('q')
        c = self.request.query_params.get('c')

        q_condition = Q()
        if q:
            # qs = qs.filter(title__icontains=q)
            q_condition = Q(title__icontains=q)
        c_condition = Q()
        if c:
            # qs = qs.filter(content__icontains=c)
            c_condition = Q(content__icontains=c)
        return qs.filter(q_condition, c_condition)


# GET (retrieve)
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'


# PUT
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# GET - PUT
class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# DELETE
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# GET - DELETE
class ProductRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Object was deleted'}, status=status.HTTP_204_NO_CONTENT)


# GET - PUT - DELETE -- > RUD
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Object was deleted'}, status=status.HTTP_204_NO_CONTENT)


# mixins
class MyListMixin(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


# view-sets
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
